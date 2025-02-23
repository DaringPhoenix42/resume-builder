from django.shortcuts import render, redirect
from .forms import ResumeForm  # Import the ResumeForm
from .models import Resume
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from io import BytesIO
from .models import Resume
from django.shortcuts import render, get_object_or_404
from .models import Resume

def index(request):
    return render(request, 'index.html')

def resume_form(request):
    template_id = request.GET.get('template_id', 1)  # Default to template 1 if no ID is provided
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.template_id = template_id  # Save the selected template ID
            resume.save()
            return redirect('resume_preview', id=resume.id)
    else:
        form = ResumeForm(initial={'template_id': template_id})  # Pass template_id to the form
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

# New pages
def pricing(request):
    return render(request, 'pricing.html')

def resources(request):
    return render(request, 'resources.html')

def dashboard(request):
    # In a real app, you'd check if the user is authenticated, fetch user resumes, etc.
    return render(request, 'dashboard.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def examples(request):
    return render(request, 'examples.html')

def blog(request):
    return render(request, 'blog.html')

def cover_letter(request):
    return render(request, 'cover_letter.html')

def download_resume(request, id, format):
    resume = Resume.objects.get(id=id)
    
    if format == 'pdf':
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, f"Name: {resume.name}")
        p.drawString(100, 730, f"Email: {resume.email}")
        p.drawString(100, 710, f"Phone: {resume.phone}")
        p.drawString(100, 690, f"Summary: {resume.summary}")
        p.drawString(100, 670, f"Skills: {resume.skills}")
        p.drawString(100, 650, f"Experience: {resume.experience}")
        p.drawString(100, 630, f"Education: {resume.education}")
        p.showPage()
        p.save()
        
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.pdf"'
        return response
    
    elif format == 'word':
        document = Document()
        document.add_heading(f"Resume: {resume.name}", 0)
        document.add_paragraph(f"Email: {resume.email}")
        document.add_paragraph(f"Phone: {resume.phone}")
        document.add_paragraph(f"Summary: {resume.summary}")
        document.add_paragraph(f"Skills: {resume.skills}")
        document.add_paragraph(f"Experience: {resume.experience}")
        document.add_paragraph(f"Education: {resume.education}")
        
        buffer = BytesIO()
        document.save(buffer)
        buffer.seek(0)
        
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.docx"'
        return response
    
    else:
        return HttpResponse("Invalid format", status=400)





















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