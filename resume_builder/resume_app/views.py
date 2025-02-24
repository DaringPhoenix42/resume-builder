# from django.shortcuts import render, redirect
# from .forms import ResumeForm  # Import the ResumeForm
# from .models import Resume
# from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from docx import Document
# from io import BytesIO
# from .models import Resume
# from django.shortcuts import render, get_object_or_404
# from .models import Resume
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, logout
# from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.models import User
# from .models import Resource, BlogPost
# from .forms import ResumeForm, ResourceForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .forms import ResumeForm, ResourceForm  # <-- import both
# from .models import Resume, Resource



# @staff_member_required
# def create_resource(request):
#     if request.method == 'POST':
#         # Save new Resource object
#         ...
#     return render(request, 'create_resource.html')

# def index(request):
#     return render(request, 'index.html')

# def resume_form(request):
#     template_id = request.GET.get('template_id', 1)  # Default to template 1 if no ID is provided
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.template_id = template_id  # Save the selected template ID
#             resume.save()
#             return redirect('resume_preview', id=resume.id)
#     else:
#         form = ResumeForm(initial={'template_id': template_id})  # Pass template_id to the form
#     return render(request, 'resume_form.html', {'form': form, 'template_id': template_id})

# def resume_preview(request, id):
#     resume = get_object_or_404(Resume, id=id)
#     return render(request, 'resume_preview.html', {'resume': resume})

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def templates(request):
#     return render(request, 'templates.html')

# def faq(request):
#     return render(request, 'faq.html')

# # New pages
# def pricing(request):
#     return render(request, 'pricing.html')

# def resources(request):
#     return render(request, 'resources.html')

# @login_required
# def dashboard(request):
#     # Only logged-in users can see this page.
#     user_resumes = Resume.objects.filter(user=request.user)
#     return render(request, 'dashboard.html', {'resumes': user_resumes})


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')  # or request.POST['username'] if you're sure it's there
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             # handle invalid credentials
#             # e.g., show an error message or redirect
#             ...
#     return render(request, 'login.html')


# def logout_user(request):
#     logout(request)
#     return redirect('index')

# def testimonials(request):
#     return render(request, 'testimonials.html')

# def examples(request):
#     return render(request, 'examples.html')

# def blog(request):
#     return render(request, 'blog.html')

# def cover_letter(request):
#     return render(request, 'cover_letter.html')

# # views.py
# def create_resource(request):
#     if request.method == 'POST':
#         form = ResourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('resources')  # or wherever
#     else:
#         form = ResourceForm()
#     return render(request, 'create_resource.html', {'form': form})


# def download_resume(request, id, format):
#     resume = Resume.objects.get(id=id)
    
#     if format == 'pdf':
#         buffer = BytesIO()
#         p = canvas.Canvas(buffer, pagesize=letter)
#         p.drawString(100, 750, f"Name: {resume.name}")
#         p.drawString(100, 730, f"Email: {resume.email}")
#         p.drawString(100, 710, f"Phone: {resume.phone}")
#         p.drawString(100, 690, f"Summary: {resume.summary}")
#         p.drawString(100, 670, f"Skills: {resume.skills}")
#         p.drawString(100, 650, f"Experience: {resume.experience}")
#         p.drawString(100, 630, f"Education: {resume.education}")
#         p.showPage()
#         p.save()
        
#         buffer.seek(0)
#         response = HttpResponse(buffer, content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.pdf"'
#         return response
    
#     elif format == 'word':
#         document = Document()
#         document.add_heading(f"Resume: {resume.name}", 0)
#         document.add_paragraph(f"Email: {resume.email}")
#         document.add_paragraph(f"Phone: {resume.phone}")
#         document.add_paragraph(f"Summary: {resume.summary}")
#         document.add_paragraph(f"Skills: {resume.skills}")
#         document.add_paragraph(f"Experience: {resume.experience}")
#         document.add_paragraph(f"Education: {resume.education}")
        
#         buffer = BytesIO()
#         document.save(buffer)
#         buffer.seek(0)
        
#         response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.docx"'
#         return response
    
#     else:
#         return HttpResponse("Invalid format", status=400)





















# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .forms import ResumeForm
# from .models import Resume
# import subprocess
# import os
# from io import BytesIO

# def generate_latex(resume):
#     # Escape special LaTeX characters
#     def escape_latex(text):
#         if text is None:
#             return ""
#         return str(text).replace("&", "\\&").replace("%", "\\%").replace("$", "\\$")

#     # LaTeX template with placeholders
#     latex_template = r"""
# \documentclass[11pt, a4paper]{article}
# \usepackage{geometry}
# \geometry{a4paper, margin=1in}

# \title{Resume}
# \author{%s}
# \date{}

# \begin{document}

# \maketitle

# \section*{Personal Information}
# \begin{itemize}
#     \item Name: %s
#     \item Email: %s
#     \item Phone: %s
#     \item Address: %s
#     \item LinkedIn: %s
#     \item GitHub: %s
#     \item Portfolio: %s
# \end{itemize}

# \section*{Professional Summary}
# %s

# \section*{Skills}
# %s

# \section*{Experience}
# %s

# \section*{Education}
# %s

# \section*{Certifications}
# %s

# \section*{Languages}
# %s

# \section*{Hobbies and Interests}
# %s

# \end{document}
#     """ % (
#         escape_latex(resume.name), escape_latex(resume.name), escape_latex(resume.email),
#         escape_latex(resume.phone), escape_latex(resume.address), escape_latex(resume.linkedin),
#         escape_latex(resume.github), escape_latex(resume.portfolio), escape_latex(resume.summary),
#         escape_latex(resume.skills), escape_latex(resume.experience), escape_latex(resume.education),
#         escape_latex(resume.certifications), escape_latex(resume.languages), escape_latex(resume.hobbies_interests)
#     )
#     return latex_template

# def resume_form(request):
#     template_id = request.GET.get('template_id', 1)  # Default to template 1 if no ID is provided
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.template_id = template_id  # Save the selected template ID
#             resume.save()
#             return redirect('resume_preview', id=resume.id)
#     else:
#         form = ResumeForm(initial={'template_id': template_id})  # Pass template_id to the form
#     return render(request, 'resume_form.html', {'form': form, 'template_id': template_id})

# def resume_preview(request, id):
#     resume = get_object_or_404(Resume, id=id)
#     return render(request, 'resume_preview.html', {'resume': resume})

# def download_resume(request, id, format):
#     resume = get_object_or_404(Resume, id=id)
    
#     if format == 'pdf':
#         # Generate the LaTeX file
#         latex_content = generate_latex(resume)

#         # Save the LaTeX content to a file
#         with open("resume.tex", "w") as file:
#             file.write(latex_content)

#         # Compile the LaTeX file to PDF
#         try:
#             subprocess.run(["pdflatex", "resume.tex"], check=True)
#         except subprocess.CalledProcessError:
#             return HttpResponse("Failed to generate PDF. Please check the LaTeX content.", status=500)

#         # Serve the PDF file for download
#         with open("resume.pdf", "rb") as file:
#             response = HttpResponse(file.read(), content_type="application/pdf")
#             response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.pdf"'

#         # Clean up temporary files
#         for ext in [".tex", ".pdf", ".log", ".aux"]:
#             try:
#                 os.remove(f"resume{ext}")
#             except FileNotFoundError:
#                 pass

#         return response
    
#     elif format == 'word':
#         # Generate a Word document
#         from docx import Document
#         document = Document()
#         document.add_heading(f"Resume: {resume.name}", 0)
#         document.add_paragraph(f"Email: {resume.email}")
#         document.add_paragraph(f"Phone: {resume.phone}")
#         document.add_paragraph(f"Summary: {resume.summary}")
#         document.add_paragraph(f"Skills: {resume.skills}")
#         document.add_paragraph(f"Experience: {resume.experience}")
#         document.add_paragraph(f"Education: {resume.education}")
        
#         buffer = BytesIO()
#         document.save(buffer)
#         buffer.seek(0)
        
#         response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.docx"'
#         return response
    
#     else:
#         return HttpResponse("Invalid format", status=400)
    
    
# from django.shortcuts import render, redirect
# from .forms import ResumeForm  # Import the ResumeForm
# from .models import Resume
# from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from docx import Document
# from io import BytesIO
# from .models import Resume
# from django.shortcuts import render, get_object_or_404
# from .models import Resume

# def index(request):
#     return render(request, 'index.html')

# def resume_form(request):
#     template_id = request.GET.get('template_id', 1)  # Default to template 1 if no ID is provided
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.template_id = template_id  # Save the selected template ID
#             resume.save()
#             return redirect('resume_preview', id=resume.id)
#     else:
#         form = ResumeForm(initial={'template_id': template_id})  # Pass template_id to the form
#     return render(request, 'resume_form.html', {'form': form, 'template_id': template_id})

# def resume_preview(request, id):
#     resume = get_object_or_404(Resume, id=id)
#     return render(request, 'resume_preview.html', {'resume': resume})

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def templates(request):
#     return render(request, 'templates.html')

# def faq(request):
#     return render(request, 'faq.html')


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document




from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from io import BytesIO

from .models import Resume, Resource
from .forms import ResumeForm, ResourceForm

def index(request):
    return render(request, 'index.html')

def resume_form(request):
    template_id = request.GET.get('template_id', 1)  # Default to template 1 if none provided
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.template_id = template_id
            # Optionally set resume.user = request.user if you want
            resume.save()
            return redirect('resume_preview', id=resume.id)
    else:
        form = ResumeForm(initial={'template_id': template_id})
    return render(request, 'resume_form.html', {'form': form, 'template_id': template_id})

def resume_preview(request, id):
    resume = get_object_or_404(Resume, id=id)
    return render(request, 'resume_preview.html', {'resume': resume})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def templates(request):
    return render(request, 'templates.html')

def faq(request):
    return render(request, 'faq.html')

def pricing(request):
    return render(request, 'pricing.html')

def resources(request):
    return render(request, 'resources.html')

@login_required
def dashboard(request):
    user_resumes = Resume.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'resumes': user_resumes})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def testimonials(request):
    return render(request, 'testimonials.html')

def examples(request):
    return render(request, 'examples.html')

def blog(request):
    return render(request, 'blog.html')

def cover_letter(request):
    return render(request, 'cover_letter.html')

@staff_member_required
def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')  # or any other desired page
    else:
        form = ResourceForm()
    return render(request, 'create_resource.html', {'form': form})

# views.py

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required

import pdfkit
from io import BytesIO
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

from .models import Resume


@staff_member_required
def create_resource(request):
    # Your existing create_resource logic here (if any)
    pass


def download_resume(request, id, format):
    """
    Generates a PDF or Word resume for the given Resume object.
    :param id: The Resume object ID.
    :param format: 'pdf' or 'word'.
    """
    resume = get_object_or_404(Resume, id=id)

    if format == 'pdf':
        # 1) Render your HTML template with the resume data
        html_string = render_to_string('resume_pdf_template.html', {'resume': resume})

        # 2) Convert the HTML to PDF using pdfkit
        #    If wkhtmltopdf is not on your PATH, specify its location via configuration:
        #    config = pdfkit.configuration(wkhtmltopdf=r"C:\path\to\wkhtmltopdf.exe")
        #    pdf_file = pdfkit.from_string(html_string, False, configuration=config)
        pdf_file = pdfkit.from_string(html_string, False)  # returns PDF bytes

        # 3) Return as a downloadable PDF
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.pdf"'
        return response

    elif format == 'word':
        # 1) Create a Word document with python-docx
        document = Document()

        # 2) Optional: Adjust default font & size
        styles = document.styles
        normal_style = styles['Normal']
        if normal_style and normal_style.type == WD_STYLE_TYPE.PARAGRAPH:
            normal_style.font.name = 'Arial'
            normal_style.font.size = Pt(11)

        # 3) Name & Job Title
        document.add_heading(resume.name or "Your Name", 0)
        if resume.job_title:
            job_title_paragraph = document.add_paragraph(resume.job_title)
            job_title_paragraph.style = document.styles['Normal']

        # 4) Contact Info
        contact_info = []
        if resume.address:
            contact_info.append(f"Address: {resume.address}")
        if resume.phone:
            contact_info.append(f"Phone: {resume.phone}")
        if resume.email:
            contact_info.append(f"Email: {resume.email}")
        if resume.github:
            contact_info.append(f"GitHub: {resume.github}")
        if resume.linkedin:
            contact_info.append(f"LinkedIn: {resume.linkedin}")
        if resume.portfolio:
            contact_info.append(f"Portfolio: {resume.portfolio}")

        if contact_info:
            document.add_paragraph("\n".join(contact_info))

        # 5) Summary
        if resume.summary:
            document.add_heading("Summary", level=1)
            document.add_paragraph(resume.summary)

        # 6) Technical Skills (example: bullet points)
        if resume.skills:
            document.add_heading("Technical Skills", level=1)
            skill_lines = [line.strip() for line in resume.skills.split('\n') if line.strip()]
            for line in skill_lines:
                document.add_paragraph(line, style='List Bullet')

        # 7) Professional Experience
        if resume.experience:
            document.add_heading("Professional Experience", level=1)
            exp_lines = [line.strip() for line in resume.experience.split('\n') if line.strip()]
            for line in exp_lines:
                document.add_paragraph(line, style='List Bullet')

        # 8) Education
        if resume.education:
            document.add_heading("Education", level=1)
            document.add_paragraph(resume.education)

        # 9) Certifications
        if resume.certifications:
            document.add_heading("Certifications", level=1)
            document.add_paragraph(resume.certifications)

        # 10) Languages
        if resume.languages:
            document.add_heading("Languages", level=1)
            document.add_paragraph(resume.languages)

        # 11) Hobbies & Interests
        if resume.hobbies_interests:
            document.add_heading("Hobbies & Interests", level=1)
            document.add_paragraph(resume.hobbies_interests)

        # 12) Save to an in-memory buffer
        buffer = BytesIO()
        document.save(buffer)
        buffer.seek(0)

        # 13) Return as a downloadable Word file
        response = HttpResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.docx"'
        return response

    else:
        return HttpResponse("Invalid format", status=400)




from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in right away
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document
from io import BytesIO

from .models import CoverLetter
from .forms import CoverLetterForm
from django.shortcuts import render, redirect

@login_required
def cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            cover_letter = form.save(commit=False)
            cover_letter.user = request.user
            cover_letter.save()
            return redirect('cover_letter_preview', id=cover_letter.id)
    else:
        form = CoverLetterForm()
    return render(request, 'cover_letter.html', {'form': form})


@login_required
def cover_letter_preview(request, id):
    cover_letter = get_object_or_404(CoverLetter, id=id, user=request.user)
    return render(request, 'cover_letter_preview.html', {'cover_letter': cover_letter})

@login_required
def download_cover_letter(request, id, format):
    cover_letter = get_object_or_404(CoverLetter, id=id, user=request.user)
    
    content = f"""
    {cover_letter.greeting}

    {cover_letter.introduction}

    {cover_letter.body}

    {cover_letter.closing}
    """
    
    if format == 'pdf':
        # Generate PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="cover_letter.pdf"'
        
        # Use reportlab to create PDF
        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(100, 750, content)
        p.showPage()
        p.save()
        
        return response
        
    elif format == 'docx':
        # Generate Word document
        document = Document()
        document.add_paragraph(content)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="cover_letter.docx"'
        
        document.save(response)
        
        return response
    
    else:
        return HttpResponse("Invalid format", status=400)

