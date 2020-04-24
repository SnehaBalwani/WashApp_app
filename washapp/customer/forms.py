from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from customer.models import (Customer, User)

#
# class TeacherSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_teacher = True
#         if commit:
#             user.save()
#         return user


class CustomerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        self.cleaned_data.get('name')
        return user

