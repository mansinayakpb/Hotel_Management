from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Booking, Hotel, Review, Room, User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm  
    add_form = CustomUserCreationForm  

    list_display = (
        "id",
        "email",
        "email_verified",
        "verification_code",
        "is_approved",
        "address",
        "city",
        "country",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_type",
                    "email_verified",
                    "verification_code",
                    "token_created_at",
                    "is_approved",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_type",
                    "password1",
                    "password2",
                    "is_approved",
                ),
            },
        ),
    )

    filter_horizontal = ("user_permissions", "groups")
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
        "city",
        "country",
        "description",
        "phone_number",
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hotel",
        "room_number",
        "price_per_day",
        "description",
        "is_available",
        "max_allowed",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "room",
        "check_in",
        "check_out",
        "num_guests",
        "total_price",
        "status",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "hotel",
        "comment",
    )