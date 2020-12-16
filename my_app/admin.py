from django.contrib import admin
from .models import Client
from .models import Premises
from .models import rentContract

admin.site.register(Premises)
admin.site.register(rentContract)
admin.site.register(Client)
# Register your models here.
