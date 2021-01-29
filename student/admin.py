from django.contrib import admin

# Register your models here.
from student import models

admin.site.register(models.Student)
admin.site.register(models.Grade)
admin.site.register(models.Paper)
admin.site.register(models.Teacher)
admin.site.register(models.Question)
