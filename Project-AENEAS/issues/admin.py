from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    #  https://docs.djangoproject.com/en/1.8/intro/tutorial02/
    exclude = ('submitted_date', 'modified_date',)
    list_display = ('submitter', 'description', 'submitted_date')


admin.site.register(Ticket, TicketAdmin)
