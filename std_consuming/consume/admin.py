from django.contrib import admin
from .models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name','student_email']

admin.site.register(StudentModel,StudentAdmin)
