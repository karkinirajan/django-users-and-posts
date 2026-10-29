
# Blogging Web App  

## Overview  

**Blogging Web App** is a multi-functional project combining frontend and backend capabilities to manage users and posts efficiently. Built using Django and modern web technologies, this application provides a responsive user interface and a robust backend for various operations.  

---

## ✨ Features  

- **User Management**:  
  - Create, update, and delete user profiles.  
  - Secure authentication and authorization.  

- **Post Management**:  
  - Add, edit, and delete posts with ease.  
  - Dynamic content display with JavaScript interactivity.  

- **Responsive Frontend**:  
  - Built with modern CSS and JavaScript for a seamless user experience.  
  - Fully responsive design for desktop and mobile devices.  

- **Django Backend**:  
  - Secure and scalable backend powered by Django.  
  - RESTful APIs for integration with other services.  

---

## 🛠️ Technology Stack  

- **Frontend**: CSS, JavaScript, HTML  
- **Backend**: Django (Python)  
- **Database**: SQLite or PostgreSQL (configurable)  

---

## 🚀 Getting Started  

### Prerequisites  

Ensure the following are installed:  
- Python 3.8 or higher  
- pip (Python package manager)  

### Configuration

Set a unique Django secret key before starting the application. For local development:

```bash
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_DEBUG=true
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Production deployments should set `DJANGO_DEBUG=false`, list their real hostnames in
`DJANGO_ALLOWED_HOSTS`, and provide SMTP settings through `DJANGO_EMAIL_HOST`,
`DJANGO_EMAIL_PORT`, `DJANGO_EMAIL_HOST_USER`, `DJANGO_EMAIL_HOST_PASSWORD`, and
`DJANGO_EMAIL_USE_TLS`. Email uses Django's console backend by default for local work.
Never commit secrets or `.env` files.

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/kneeraazon404/django-users-and-posts.git  
   cd django-users-and-posts  
   ```  

2. Create and activate a virtual environment:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Apply database migrations:  
   ```bash  
   python manage.py migrate  
   ```  

5. Create a superuser for admin access:  
   ```bash  
   python manage.py createsuperuser  
   ```  

6. Run the development server:  
   ```bash  
   python manage.py runserver  
   ```  

7. Access the application at `http://127.0.0.1:8000`.  

---

## 🔧 Usage  

- **Admin Panel**: Manage users and posts through the Django admin interface at `/admin`.  
- **Frontend Interface**: Interact with posts and users via the responsive web interface.  

---

## 📜 License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

## 🤝 Contributions  

Contributions are welcome! To contribute:  

1. Fork the repository.  
2. Create a feature branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature-name"  
   ```  
4. Push to your fork:  
   ```bash  
   git push origin feature-name  
   ```  
