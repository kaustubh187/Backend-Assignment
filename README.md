# Gas Utility Service Backend

This repository contains the backend of a Gas Utility Service web application. It is built using Django and provides features such as customer service request tracking, support representative management, and more.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)


## Description

The project is designed to manage customer service requests for a gas utility company. It enables customers to submit service requests, track their requests, and interact with support representatives who can manage and resolve the requests.

## Features

- Customer registration and login.
- Service request creation, tracking, and updating.
- Support representative dashboard to manage service requests.
- Ability to upload and download attachments related to service requests.
- User authentication using Django's built-in system.
  
## Installation

Follow the steps below to set up the project on your local machine.

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Backend-Assignment.git

2. Navigate to Directory
   ```bash
    cd Backend-Assignment

4. Install the required dependencies:
   ```bash
     pip install -r requirements.txt

6. Apply migrations to set up the database:
   ```bash
     python manage.py migrate
5. Create a superuser (for Django admin access):
   ```bash
      python manage.py createsuperuser
7. Run the development server:
   ```bash
    python manage.py runserver


Usage
Once the server is running, you can access the following endpoints:

- /login/ - Customer or support representative login.
- /signup/ - Customer registration page.
- /create/ - Create a new service request (customer).
- /track/ - Track all service requests (customer).
- /manage/ - View and manage service requests (support representative).
- /update/{request_id}/ - Update the status of a service request (support representative).
- Admin Panel: Go to /admin/ to log into the Django admin panel. You can manage users, service requests, and other backend data.



## Screenshots

![image](https://github.com/user-attachments/assets/1f342075-d399-41a3-9f43-069979610432)
Login Page


![image](https://github.com/user-attachments/assets/d83c5268-86ed-4429-9e9e-f93db7ed93ca)
Dashboard for Users


![image](https://github.com/user-attachments/assets/b9f5e288-1921-45e4-ae91-a32cc76c70c6)
Creating a service request


![image](https://github.com/user-attachments/assets/58aef4bc-ce80-4267-bc73-53c1911f83be)
Service Representative Manage Requests



![image](https://github.com/user-attachments/assets/4519b565-c5a0-48fb-98dc-8bde624df763)
Updating Status of request on the customer service representative side

![image](https://github.com/user-attachments/assets/50c568bc-1eb0-499a-aad4-049d7e9afc4d)
Tracking Service Requests

