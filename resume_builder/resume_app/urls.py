# resume_app/urls.py
from django.urls import path
from . import views
from .forms import CoverLetterForm


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.resume_form, name='resume_form'),
    path('preview/<int:id>/', views.resume_preview, name='resume_preview'),
    path('download/<int:id>/<str:format>/', views.download_resume, name='download_resume'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('templates/', views.templates, name='templates'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing'),
    path('resources/', views.resources, name='resources'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('examples/', views.examples, name='examples'),
    path('blog/', views.blog, name='blog'),
    path('cover-letter/', views.cover_letter, name='cover_letter'),
    path('signup/', views.signup, name='signup'),

    path('create-resource/', views.create_resource, name='create_resource'),
    path('cover-letter/', views.cover_letter, name='cover_letter'),
    path('cover-letter/<int:id>/preview/', 
         views.cover_letter_preview, 
         name='cover_letter_preview'),
    path('cover-letter/<int:id>/download/<str:format>/', 
         views.download_cover_letter, 
         name='download_cover_letter'),
   path('resume/<int:id>/<str:format>/', views.download_resume, name='download_resume'),

]
