from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': (
            "رمز عبور اشتباه است"
        ),
        'inactive': ("حساب کاربری غیرفعال است"),
        'password_mismatch': (
            'رمز عبور یکسان نیست'
        ),
        'password_too_similar': (
            'رمز عبور با نام کاربری مشابه است'
        ),
    }

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].label = ''