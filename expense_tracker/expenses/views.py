from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *



def home(request):

    return redirect('login')



def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('expense_list')

    else:

        form = RegisterForm()

    return render(request, 'expenses/register.html', {
        'form': form
    })


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('expense_list')

    else:

        form = AuthenticationForm()

    return render(request, 'expenses/login.html', {
        'form': form
    })


def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def expense_list(request):

    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses
    })

@login_required
def add_expense(request):

    if request.method == 'POST':

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = request.user

            expense.save()

            return redirect('expense_list')

    else:

        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {
        'form': form
    })

@login_required
def update_expense(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    if request.method == 'POST':

        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():

            form.save()

            return redirect('expense_list')

    else:

        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/update_expense.html', {
        'form': form
    })



@login_required
def delete_expense(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    if request.method == 'POST':

        expense.delete()

        return redirect('expense_list')

    return render(request, 'expenses/delete_expense.html', {
        'expense': expense
    })
