from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer, ServiceRequest, SupportRepresentative
from .forms import ServiceRequestForm  
from django.http import HttpResponse,FileResponse,JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserSignupForm,UpdateServiceRequestForm
import os


@login_required
def create_service_request(request):
    customer = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            return redirect('track_requests')  
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_service_request.html', {'form': form})



@login_required
def track_requests(request):
    customer = get_object_or_404(Customer, user=request.user)
    requests = ServiceRequest.objects.filter(customer=customer).order_by('-created_at')
    return render(request, 'service_requests/track_requests.html', {'requests': requests})

@login_required
def manage_requests(request):
    if not hasattr(request.user, 'supportrepresentative'):
        return HttpResponse("You are not authorized to access this page.", status=403)
    
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service_requests/manage_requests.html', {'requests': requests})


@login_required
def update_request_status(request, request_id):
    if not hasattr(request.user, 'supportrepresentative'):
        return HttpResponse("You are not authorized to access this page.", status=403)

    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = UpdateServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('manage_requests')
    else:
        form = UpdateServiceRequestForm(instance=service_request)
    
    return render(request, 'service_requests/update_request_status.html', {'form': form})

def download_file(request, file_id):
 
    file = get_object_or_404(ServiceRequest, id=file_id)


    file_path = file.attachment.path

    file_handle = open(file_path, 'rb')


    response = FileResponse(file_handle, as_attachment=True, filename=os.path.basename(file_path))
    return response

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            

            if hasattr(user, 'customer'):
                return redirect('customer_dashboard')
            
            elif hasattr(user, 'supportrepresentative'):
                return redirect('support_dashboard')
            
            else:
                return redirect('default_home') 
        
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid credentials'})
    
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def customer_dashboard(request):
    
    return render(request, 'dashboard/customer_dashboard.html')

@login_required
def support_dashboard(request):

    return render(request, 'dashboard/support_dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            
            user_type = form.cleaned_data['user_type']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            
            if user_type == 'customer':
                Customer.objects.create(
                    user=user,
                    phone_number=phone_number,
                    address=address
                )
            elif user_type == 'support_rep':
                SupportRepresentative.objects.create(user=user)

            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})



def redirect_dashboard(request):
    
    if request.user.is_authenticated:

        if hasattr(request.user, 'customer'):
            return redirect('customer_dashboard')
        
        elif hasattr(request.user, 'supportrepresentative'):
           return redirect('support_dashboard')
        
        else:
           return redirect('login')
    else:
        return redirect('login')


def get_request_details(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    data = {
        'description': service_request.description,
        'created_at': service_request.created_at,
        'status': service_request.status,
        'updated_at': service_request.updated_at,
        'resolved_at': service_request.resolved_at,
        'attachment_url': service_request.attachment.url if service_request.attachment else None,
    }
    return JsonResponse(data)