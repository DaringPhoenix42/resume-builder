# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document


class Resume(models.Model):
    """Stores user resume data."""
    # Link to the user (if you want each resume tied to a specific user)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Basic fields
    name = models.CharField(max_length=255, help_text="Your full name")
    email = models.EmailField(help_text="Your email address")
    phone = models.CharField(max_length=20, help_text="Your phone number")
    address = models.CharField(max_length=255, blank=True, null=True, help_text="Your address")
    linkedin = models.URLField(blank=True, null=True, help_text="Your LinkedIn profile URL")
    github = models.URLField(blank=True, null=True, help_text="Your GitHub profile URL")
    portfolio = models.URLField(blank=True, null=True, help_text="Your portfolio website URL")

    # Professional Information
    job_title = models.CharField(max_length=255, blank=True, null=True, help_text="Your current or desired job title")
    summary = models.TextField(help_text="A brief summary of your professional experience")

    # Work Experience
    experience = models.TextField(help_text="Describe your work experience")
    education = models.TextField(help_text="List your educational background")
    skills = models.TextField(help_text="List your skills (e.g., Python, Django, JavaScript)")
    certifications = models.TextField(blank=True, null=True, help_text="List your certifications (e.g., AWS Certified, PMP)")
    languages = models.TextField(blank=True, null=True, help_text="List languages you speak (e.g., English, Spanish)")
    hobbies_interests = models.TextField(blank=True, null=True, help_text="List your hobbies and interests")

    # Template Info
    template_id = models.IntegerField(default=1, help_text="The selected template ID")
    template_name = models.CharField(max_length=100, blank=True, null=True)

    # Created_at with default for existing rows
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Template {self.template_id})"


class Resource(models.Model):
    """Represents a career resource or article."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=[
            ('resume', 'Resume Writing'),
            ('interview', 'Interview Prep'),
            ('networking', 'Networking'),
            ('career', 'Career Advice'),
        ],
        default='career'
    )

    # Add defaults to avoid prompts if existing rows
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Represents a blog post entry."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # auto_now_add with default
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Stores user testimonials."""
    user_name = models.CharField(max_length=100)
    content = models.TextField()

    # auto_now_add with default
    created_at = models.DateTimeField(auto_now_add=True)

    template_used = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user_name} - {self.created_at.date()}"


class CoverLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    greeting = models.CharField(max_length=200, blank=True)
    introduction = models.TextField(blank=True)
    body = models.TextField(blank=True)
    closing = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cover Letter - {self.user.username}"


from django import forms
from .models import CoverLetter

class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = ['greeting', 'introduction', 'body', 'closing']
        widgets = {
            'greeting': forms.TextInput(attrs={
                'placeholder': 'Dear Hiring Manager',
                'class': 'form-control'
            }),
            'introduction': forms.Textarea(attrs={
                'placeholder': "Introduce yourself and the position you're applying for...",
                'rows': 3,
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Highlight relevant experience, skills, and achievements...',
                'rows': 6,
                'class': 'form-control'
            }),
            'closing': forms.Textarea(attrs={
                'placeholder': 'Thank the employer, express enthusiasm...',
                'rows': 2,
                'class': 'form-control'
            })
        }
        
from django.db import models
from django.contrib.auth.models import User

class CoverLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    greeting = models.CharField(max_length=200)
    introduction = models.TextField()
    body = models.TextField()
    closing = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cover Letter - {self.user.username}"
