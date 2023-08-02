from django.contrib import admin
from .models import Cloths,Category,Cart

# Register your models here.

admin.site.register(Cloths)
admin.site.register(Category)
admin.site.register(Cart)