from django.contrib import admin
from .models import Contact, Employee, Market, Product, ProductMarket
# Register your models here.


class MarketEmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1
    fields = ('first_name', 'last_name')


class MarketAdmin(admin.ModelAdmin):
    inlines = [MarketEmployeeInline]
    list_display = ('name',)
    exclude = ('user',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', )
    list_filter = ('type','is_homemade', )


admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Contact)
admin.site.register(ProductMarket)