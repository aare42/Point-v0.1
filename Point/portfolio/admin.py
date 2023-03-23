from django.contrib import admin
from .models import StudentLeaf, StudentLeafStatus, Student

# Register your models here.

admin.site.register(StudentLeaf)
admin.site.register(StudentLeafStatus)
admin.site.register(Student)