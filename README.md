# 🚗 Vehicle Management System  

A simple **CRUD-based web application** built with **Django**.  
The project allows users with different roles (Superuser, Staff, Normal User) to manage vehicle records.  

---

## 📌 Features  
- User Roles with Permissions:  
  - **Superuser** → full access (create, view, edit, delete, manage staff/users).  
  - **Staff User** → can add, view, and edit vehicle details.  
  - **Normal User** → can only view vehicle details.  

- Add new vehicle details (number, description, model, etc.)  
- View a list of vehicles  
- Edit vehicle information  
- Delete vehicles (if allowed)  
- Authentication & Authorization  
- **Django ORM** used for database operations  
- **Custom Middleware** implemented  

---

## 🛠️ Tech Stack  
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default), MySQL (optional)  

---

## ⚙️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/vehicle-management-system.git
cd vehicle-management-system

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # for Windows
# or
source venv/bin/activate   # for Mac/Linux

3. Install Requirements
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create a Superuser (Admin)
python manage.py createsuperuser

6. Run the Development Server
python manage.py runserver


Now open your browser at:
👉 http://127.0.0.1:8000/

🧪 Usage Example

Login as Superuser → full admin panel access.

Login as Staff → can add, view, and edit vehicle details.

Login as Normal User → can only view vehicles.

Example:
Add vehicle: Enter vehicle number, description, and model in the form.

Saved in database using Django ORM:
Vehicle.objects.create(vehicle_no="MH12AB1234", description="Sedan", model="Honda City")

Data shown in list page.

--- 

