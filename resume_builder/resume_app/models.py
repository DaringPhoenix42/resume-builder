from django.db import models

class Resume(models.Model):
    # Personal Information
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

    # Hobbies and Interests
    hobbies_interests = models.TextField(blank=True, null=True, help_text="List your hobbies and interests")

    # Template ID (if needed)
    template_id = models.IntegerField(default=1, help_text="The selected template ID")

    def __str__(self):
        return self.name