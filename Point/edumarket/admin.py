from django.contrib import admin
from .models import Educator, Course, Contract, ContractStatus, ContractStatusChange

# Register your models here.

admin.site.register(Educator)
admin.site.register(Course)
admin.site.register(Contract)
admin.site.register(ContractStatus)
admin.site.register(ContractStatusChange)