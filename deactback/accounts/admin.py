from django.contrib import admin
from siwe_auth.admin import WalletBaseAdmin
from .models import UserModel


class UserModelAdmin(WalletBaseAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('ethereum_address',)
    list_filter = ('email', 'account_type', 'ethereum_address')
    fieldsets = (
        ('Credentials', {'fields': ('ethereum_address', 'email')}),
        ('Full Name', {'fields': ('name',)}),
        ('Account Type', {'fields': ('account_type',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
            (
                None, {
                    'classes': ('wide',),
                    'fields': ('email', 'name', 'ethereum_address')}
            ),
        )
    search_fields = ('email', 'account_type', 'name')
    ordering = ('email',)
    filter_horizontal = ()

    class Meta:
        model = UserModel


admin.site.register(UserModel, UserModelAdmin)
