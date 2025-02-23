# from django.contrib import admin
# from .models import Resource, BlogPost, Testimonial, Resume
# from django.contrib import admin
# from .models import Resource

# @admin.register(Resource)
# class ResourceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'created_at')
#     prepopulated_fields = {"slug": ("title",)}



# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug')
# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'created_at')

# @admin.register(Resume)
# class ResumeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'template_name', 'created_at')
    
# from django.contrib import admin
# from .models import Resource, BlogPost, Testimonial, Resume






from django.contrib import admin
from .models import Resource, BlogPost, Testimonial, Resume

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created_at')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'created_at')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'template_name', 'created_at')
    # You can add search_fields, list_filter, etc. as needed.
