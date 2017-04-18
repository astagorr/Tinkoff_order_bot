from django.contrib import admin

# Register your models here.
from tinkoff_order_bot.orders.models import Order

def update_status(status, queryset):
    queryset.update(status=status)


def make_confirmed(modeladmin, request, queryset):
    update_status(Order.CONFIRMED, queryset)
make_confirmed.short_description = "Mark selected orders as confirmed"


def make_rejected(modeladmin, request, queryset):
    update_status(Order.REJECTED, queryset)
make_rejected.short_description = "Mark selected orders as rejected"


def make_nonconfirmed(modeladmin, request, queryset):
    update_status(Order.NON_CONFIRMED, queryset)
make_nonconfirmed.short_description = "Mark selected orders as non-confirmed"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['number', 'status']
    ordering = ['number']
    actions = [make_confirmed, make_rejected, make_nonconfirmed]

admin.site.register(Order, OrderAdmin)
