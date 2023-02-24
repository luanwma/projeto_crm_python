from django.contrib import admin

# Register your models here.
from .models import Customer

#abaixo é um decorator
# abaixo é descrito como a classe que está sendo registrada pelo decorator
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name", "email"]