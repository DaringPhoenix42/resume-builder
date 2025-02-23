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

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'user',  # Optional if you want to assign user from the form
            'name', 'email', 'phone', 'address', 'linkedin', 'github', 'portfolio',
            'job_title', 'summary', 'experience', 'education', 'skills',
            'certifications', 'languages', 'hobbies_interests', 'template_id',
            'template_name',
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
            'summary': forms.Textarea(attrs={'placeholder': 'A passionate software engineer...'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Worked as a Software Engineer...'}),
            'education': forms.Textarea(attrs={'placeholder': 'Bachelor of Science in Computer Science...'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Python, Django, JavaScript, React, SQL'}),
            'certifications': forms.Textarea(attrs={'placeholder': 'AWS Certified Solutions Architect...'}),
            'languages': forms.Textarea(attrs={'placeholder': 'English (Fluent), Spanish (Intermediate)'}),
            'hobbies_interests': forms.Textarea(attrs={'placeholder': 'Reading, Traveling, Photography...'}),
            'template_id': forms.HiddenInput(),
            'template_name': forms.TextInput(attrs={'placeholder': 'Corporate Pro'}),
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'slug', 'content', 'category']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'image', 'is_published']


