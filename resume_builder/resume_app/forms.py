# from django import forms
# from .models import Resume
# from .models import Resume, Resource, BlogPost
# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = [
#             'name', 'email', 'phone', 'address', 'linkedin', 'github', 'portfolio',
#             'job_title', 'summary', 'experience', 'education', 'skills',
#             'certifications', 'languages', 'hobbies_interests', 'template_id'
#         ]
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'john.doe@example.com'}),
#             'phone': forms.TextInput(attrs={'placeholder': '+1234567890'}),
#             'address': forms.TextInput(attrs={'placeholder': '123 Main St, City, Country'}),
#             'linkedin': forms.URLInput(attrs={'placeholder': 'https://linkedin.com/in/yourprofile'}),
#             'github': forms.URLInput(attrs={'placeholder': 'https://github.com/yourusername'}),
#             'portfolio': forms.URLInput(attrs={'placeholder': 'https://yourportfolio.com'}),
#             'job_title': forms.TextInput(attrs={'placeholder': 'Software Engineer'}),
#             'summary': forms.Textarea(attrs={'placeholder': 'A passionate software engineer with 5+ years of experience...'}),
#             'experience': forms.Textarea(attrs={'placeholder': 'Worked as a Software Engineer at XYZ Company from 2020-2023...'}),
#             'education': forms.Textarea(attrs={'placeholder': 'Bachelor of Science in Computer Science, University of ABC, 2019'}),
#             'skills': forms.Textarea(attrs={'placeholder': 'Python, Django, JavaScript, React, SQL'}),
#             'certifications': forms.Textarea(attrs={'placeholder': 'AWS Certified Solutions Architect, PMP Certified'}),
#             'languages': forms.Textarea(attrs={'placeholder': 'English (Fluent), Spanish (Intermediate)'}),
#             'hobbies_interests': forms.Textarea(attrs={'placeholder': 'Reading, Traveling, Photography, Chess'}),
#             'template_id': forms.HiddenInput(),  # Hidden field for template ID
#         }
        
        
# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'slug', 'content', 'image']
        
# from django import forms
# from .models import Resource

# class ResourceForm(forms.ModelForm):
#     class Meta:
#         model = Resource
#         fields = ['title', 'slug', 'content']  # add 'category' if you define it








from django import forms
from .models import Resume, Resource, BlogPost
from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'user',
            'name', 'email', 'phone', 'address',
            'linkedin', 'github', 'portfolio',
            'job_title', 'summary', 'experience', 'skills',
            'certifications', 'languages', 'hobbies_interests',
            'template_id', 'template_name',
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
            'summary': forms.Textarea(attrs={'placeholder': 'Brief overview...'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Detail your professional experience...'}),
            'skills': forms.Textarea(attrs={'placeholder': 'List your technical or soft skills...'}),
            'certifications': forms.Textarea(attrs={'placeholder': 'Certifications (e.g. AWS, PMP)...'}),
            'languages': forms.Textarea(attrs={'placeholder': 'List languages (English, Spanish, etc.)'}),
            'hobbies_interests': forms.Textarea(attrs={'placeholder': 'Hobbies, interests, volunteering...'}),
            'template_id': forms.HiddenInput(),
            'template_name': forms.TextInput(attrs={'placeholder': 'Corporate Pro'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'institution', 'degree', 'field_of_study',
            'start_year', 'end_year', 'description'
        ]
        widgets = {
            'institution': forms.TextInput(attrs={'placeholder': 'Harvard University'}),
            'degree': forms.TextInput(attrs={'placeholder': 'Bachelor of Science'}),
            'field_of_study': forms.TextInput(attrs={'placeholder': 'Computer Science'}),
            'start_year': forms.TextInput(attrs={'placeholder': '2020'}),
            'end_year': forms.TextInput(attrs={'placeholder': '2024'}),
            'description': forms.Textarea(attrs={'placeholder': 'Notable achievements, coursework...'}),
        }

# Inline formset to manage multiple education entries for a single Resume
EducationFormSet = inlineformset_factory(
    Resume,
    Education,
    form=EducationForm,
    extra=1,      # number of blank forms initially
    can_delete=True
)

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'slug', 'content', 'category']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'image', 'is_published']
        
        



# myapp/forms.py
from django import forms
from .models import CoverLetter

class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = [
            'full_name', 'job_title', 'phone', 'city_state', 'email', 'linkedin',
            'employer_name', 'employer_title', 'employer_company', 'employer_email', 'employer_location',
            'greeting', 'body', 'closing'
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'closing': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
