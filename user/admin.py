from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    change_form_template = "admin/custom_changeform.html"

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            User.objects.create_reftoken(obj)
            self.message_user(request, "New referral code has been added successfully!")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    list_display = ["username", "email", "phone", "first_name", "last_name", "is_staff"]