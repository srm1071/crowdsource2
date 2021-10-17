from django.contrib import admin
from home.models import Register
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Register)

class usrdet(ImportExportModelAdmin):
    pass