from django.contrib import admin
from .models import Train, Seat,Shedule,Review

admin.site.register(Seat)
admin.site.register(Train)
admin.site.register(Shedule)
admin.site.register(Review)
