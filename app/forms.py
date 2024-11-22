from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Booking, Hotel, Review, Room, User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = (
            "name",
            "email",
            "address",
            "city",
            "country",
            "description",
            "phone_number",
        )


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = (
            "hotel",
            "room_number",
            "price_per_day",
            "description",
            "is_available",
            "max_allowed",
        )


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = (
            "user",
            "room",
            "check_in",
            "check_out",
            "num_guests",
            "total_price",
            "status",
        )


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("user", "hotel", "comment")


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "email": "Email",
        }
