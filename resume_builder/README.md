# Space AstroResume

A modern, web-based resume and cover letter builder with blog, resources, testimonials, and more. Built with Django.

---

## Features
- Create, preview, and download resumes
- Cover letter builder
- User authentication (sign up, login, dashboard)
- Blog, resources, testimonials, FAQ, and contact pages
- Multiple templates and examples
- Responsive, space-themed UI
- Admin interface for managing content

---

## Folder Structure

```
resume-builder/
│
├── LICENSE
├── README.md                # This file
├── requirements.txt         # Python dependencies
│
├── resume_builder/          # Main Django project folder
│   ├── db.sqlite3           # SQLite database
│   ├── global_requirements.txt
│   ├── manage.py            # Django management script
│   ├── readme               # (Legacy/readme file)
│   ├── resume.tex           # LaTeX resume template
│   ├── test_pdfkit.py       # PDF generation test script
│   ├── test.pdf             # Example PDF output
│   ├── venv/                # Python virtual environment
│   │
│   ├── resume_builder/      # Django project settings & config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── resume_app/          # Main Django app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── migrations/
│       ├── models.py
│       ├── static/
│       │   ├── css/
│       │   ├── images/
│       │   └── js/
│       ├── templates/
│       ├── tests.py
│       ├── urls.py
│       └── views.py
```

---

## Key Files & Folders

- **manage.py**: Run Django commands (server, migrations, etc)
- **settings.py**: Project settings (database, apps, etc)
- **urls.py**: URL routing for the project and app
- **models.py**: Database models (resume, cover letter, blog, etc)
- **views.py**: Logic for handling web requests
- **forms.py**: Django forms for user input
- **admin.py**: Register models for Django admin
- **templates/**: HTML templates for all pages
- **static/**: CSS, JS, and images
- **migrations/**: Database schema changes
- **test_pdfkit.py**: Script to test PDF generation
- **resume.tex**: LaTeX template for resumes

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd resume-builder/resume_builder
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Usage
- Register or log in to create and manage resumes and cover letters.
- Explore templates, examples, and resources.
- Download resumes as PDF.
- Admins can manage all content via the admin panel.

---

## Notes
- Static files are in `resume_app/static/`.
- HTML templates are in `resume_app/templates/`.
- The project uses SQLite by default (see `db.sqlite3`).
- For PDF/LaTeX features, ensure you have a LaTeX distribution installed if using advanced export.

---

## License
See [LICENSE](LICENSE). 