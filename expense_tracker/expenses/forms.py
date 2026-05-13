from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Budget


class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = ['category', 'amount', 'description']



class BudgetForm(forms.ModelForm):

    class Meta:
        
        model = Budget
        fields = ['monthly_budget']