from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name', 'email', 'phone', 'address', 'linkedin', 'github', 'portfolio',
            'job_title', 'summary', 'experience', 'education', 'skills',
            'certifications', 'languages', 'hobbies_interests', 'template_id'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'placeholder': 'john.doe@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+1234567890'}),
            'address': forms.TextInput(attrs={'placeholder': '123 Main St, City, Country'}),
            'linkedin': forms.URLInput(attrs={'placeholder': 'https://linkedin.com/in/yourprofile'}),
            'github': forms.URLInput(attrs={'placeholder': 'https://github.com/yourusername'}),
            'portfolio': forms.URLInput(attrs={'placeholder': 'https://yourportfolio.com'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Software Engineer'}),
            'summary': forms.Textarea(attrs={'placeholder': 'A passionate software engineer with 5+ years of experience...'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Worked as a Software Engineer at XYZ Company from 2020-2023...'}),
            'education': forms.Textarea(attrs={'placeholder': 'Bachelor of Science in Computer Science, University of ABC, 2019'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Python, Django, JavaScript, React, SQL'}),
            'certifications': forms.Textarea(attrs={'placeholder': 'AWS Certified Solutions Architect, PMP Certified'}),
            'languages': forms.Textarea(attrs={'placeholder': 'English (Fluent), Spanish (Intermediate)'}),
            'hobbies_interests': forms.Textarea(attrs={'placeholder': 'Reading, Traveling, Photography, Chess'}),
            'template_id': forms.HiddenInput(),  # Hidden field for template ID
        }