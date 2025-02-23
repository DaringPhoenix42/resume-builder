#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#   path('form/', views.resume_form, name='resume_form'),
#    path('download/<int:id>/<str:format>/', views.download_resume, name='download_resume'),
#    path('about/', views.about, name='about'),
#    path('preview/<int:id>/', views.resume_preview, name='resume_preview'),
#    path('contact/', views.contact, name='contact'),
#    path('templates/', views.templates, name='templates'),
#    path('faq/', views.faq, name='faq'),
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.resume_form, name='resume_form'),
    path('preview/<int:id>/', views.resume_preview, name='resume_preview'),
    path('download/<int:id>/<str:format>/', views.download_resume, name='download_resume'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('templates/', views.templates, name='templates'),
    path('faq/', views.faq, name='faq'),
]