from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Event, Eventparticipant


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display        = ('title', 'slug' , 'creator', 'date', 'created', 'updated', 'status')
    list_filter         = ('status', 'created', 'date', 'updated', 'creator')
    search_fields       = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields       = ('creator',)
    data_hierarchy      = ('date')
    ordering            = ('date', 'status')  

@admin.register(Eventparticipant)
class Eventparticipant(admin.ModelAdmin):
    list_display   = ('user_id', 'event_id')
    list_filter    = ('user_id', 'event_id')
    search_fields  = ('user_id', 'event_id')
    data_hierarchy = ('created')
    