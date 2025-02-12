# Register your models here.
from django.contrib import admin
from .models import GuestName, DateTime, MyModel, Table, Reservation

class TableAdmin(admin.ModelAdmin):
    list_display =['TableNumber', 'quantity', 'place'] #co tutaj dac[]

class ReservationAdmin(admin.ModelAdmin):
    list_display = [] #co tutaj dac

# Register your models here.
admin.site.register(GuestName)
admin.site.register(DateTime)
admin.site.register(MyModel)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)