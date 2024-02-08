from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from expensetracker.models import expensive
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        ex = expensive.objects.create(description=description, amount=amount)
        ex.save()
    e = expensive.objects.all()
    total_income = sum(expense.amount for expense in e if expense.amount > 0)
    total_expenses = abs(sum(expense.amount for expense in e if expense.amount < 0))

    # Calculate balance
    balance = total_income - total_expenses
    return render(request, 'home.html',
                  {'e': e, 'total_income': total_income, 'total_expenses': total_expenses, 'balance': balance})


def deleteexpensive(request, id):
    ex = expensive.objects.get(id=id)
    ex.delete()
    messages.success(request, 'Expense deleted successfully')

    # Redirect to a specific page after deletion
    return redirect('home')


def updateexpensive(request, id):
    expense = get_object_or_404(expensive, id=id)

    if request.method == 'POST':
        # Assuming you have form fields named 'description' and 'amount'
        description = request.POST.get('description', '')
        amount = request.POST.get('amount', 0)

        expense.description = description
        expense.amount = amount
        expense.save()
        messages.success(request, 'Expense update successfully')
        return redirect('home')
    return render(request, 'update_expense.html', {'expense': expense})
