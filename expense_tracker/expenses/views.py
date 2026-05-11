from django.shortcuts import render, redirect
from .models import *
from .forms import *


def expense_list(request):

    expenses = Expense.objects.all()

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses
    })


def add_expense(request):

    if request.method == 'POST':

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = User.objects.first()

            expense.save()

            return redirect('expense_list')

    else:

        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {
        'form': form
    })