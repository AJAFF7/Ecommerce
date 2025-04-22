from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your basic models
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)

# Profile info inline with User
class ProfileInline(admin.StackedInline):  # Corrected class name
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):  # Inherit from BaseUserAdmin
    inlines = (ProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    list_select_related = ('profile',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# Unregister the original User admin
admin.site.unregister(User)

# Register the new User admin
admin.site.register(User, UserAdmin)

