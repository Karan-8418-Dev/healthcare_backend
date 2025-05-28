# 🏥 Healthcare Backend API

This is a RESTful backend system for a healthcare application built using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**. It supports user registration/login, and management of patients, doctors, and their mappings. API documentation is powered by **drf-spectacular** (Swagger & ReDoc).

---

## 🚀 Features

- ✅ JWT Authentication (Access & Refresh Tokens)
- ✅ Register/Login Users
- ✅ CRUD for Patients & Doctors
- ✅ Assign Doctors to Patients
- ✅ PostgreSQL Database
- ✅ Environment Variable Management with `python-decouple`
- ✅ CORS Support
- ✅ Auto-generated API docs using drf-spectacular

---

## 🧱 Technology Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Documentation:** drf-spectacular (Swagger UI, ReDoc)
- **Database:** PostgreSQL
- **Environment Config:** python-decouple

---

## 📁 Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend
2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root with content like:

ini
Copy
Edit
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
4. Run Migrations
python manage.py makemigrations authentication
python manage.py makemigrations patients
python manage.py makemigrations doctors
python manage.py makemigrations mappings
python manage.py migrate
5. Create a Superuser
python manage.py createsuperuser
6. Run the Server
python manage.py runserver
🔐 Authentication APIs
1. Register User
POST /api/auth/register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "strongpassword123",
  "password_confirm": "strongpassword123"
}
2. Login User
POST /api/auth/login/


{
  "email": "john@example.com",
  "password": "strongpassword123"
}
🧑‍⚕️ Patient APIs
Requires JWT Token

3. Create Patient
POST /api/patients/
Header: Authorization: Bearer <your_jwt_token>


{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "1234567890",
  "date_of_birth": "1990-01-15",
  "gender": "F",
  "address": "123 Main St, City",
  "medical_history": "No known allergies"
}
Other endpoints:

GET /api/patients/

GET /api/patients/<id>/

PUT /api/patients/<id>/

DELETE /api/patients/<id>/

👨‍⚕️ Doctor APIs
Requires JWT Token

4. Create Doctor
POST /api/doctors/
Header: Authorization: Bearer <your_jwt_token>


{
  "name": "Dr. Smith",
  "email": "dr.smith@hospital.com",
  "phone": "9876543210",
  "specialization": "CARDIOLOGY",
  "license_number": "LIC123456",
  "years_of_experience": 10,
  "hospital_affiliation": "City Hospital",
  "consultation_fee": "500.00",
  "available_from": "09:00:00",
  "available_to": "17:00:00"
}
Other endpoints:

GET /api/doctors/

GET /api/doctors/<id>/

PUT /api/doctors/<id>/

DELETE /api/doctors/<id>/

🔁 Patient-Doctor Mapping APIs
Requires JWT Token

5. Create Mapping
POST /api/mappings/
Header: Authorization: Bearer <your_jwt_token>

{
  "patient": 1,
  "doctor": 1,
  "notes": "Regular checkup assigned"
}
Other endpoints:

GET /api/mappings/

GET /api/mappings/<patient_id>/

DELETE /api/mappings/<id>/

📑 API Documentation
After running the server, access the API documentation at:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

Admin Panel: http://127.0.0.1:8000/admin/

✅ Key Features Implemented
JWT Authentication with refresh tokens

ViewSets for all CRUD operations

Proper serializers with field validation

User-specific patient access

Swagger docs using drf-spectacular

PostgreSQL integration

CORS enabled for frontend access

Environment variable configuration using .env

🔐 Security Highlights
JWT-based secure authentication

Authorization: Only authenticated users can manage resources

Secure password hashing and validation

Input validation and sanitization

CORS headers to control frontend access

Sensitive config managed via environment variables

🧪 Testing

You can use Postman, cURL, or Swagger UI to test all API endpoints.

- Use the `/api/auth/login/` endpoint to get a JWT token.
- Include the token in the Authorization header as `Bearer <your_token>` for protected routes.

### Swagger UI
For an interactive API documentation and testing interface, open:

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

This UI allows you to explore all endpoints, see request/response schemas, and execute requests directly from your browser

📬 Contact
For any questions or suggestions, feel free to connect with the developer.