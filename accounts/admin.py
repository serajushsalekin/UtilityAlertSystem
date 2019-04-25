from django.contrib import admin
# from .models import UserProfile
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth import get_user_model

UserProfile = get_user_model()


class UserProfileAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_pic', 'address', 'phone', 'postal_code',)}),
        ('Permissions', {'fields': ('admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(Group)
# admin.site.register(UserProfile)
