from django.contrib import admin
from .models import ExpenseCategory, Expense, Budget

admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(Budget)