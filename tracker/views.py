from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, InvestmentForm
from .models import Investment


def landing_page(request):
    return render(request, 'tracker/landing_page.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


@login_required
def dashboard(request):
    investments = Investment.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'investments': investments})


def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            return redirect('dashboard')
    else:
        form = InvestmentForm()
    return render(request, 'tracker/add_investment.html', {'form': form})


def list_investments(request):
    investments = Investment.objects.filter(user=request.user)
    return render(request, 'tracker/list_investments.html', {'investments': investments})


def edit_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        # Update the investment with form data
        investment.name = request.POST.get('name')
        investment.amount_invested = request.POST.get('amount_invested')
        investment.active = request.POST.get('active') == 'on'
        investment.url = request.POST.get('url')
        investment.save()
        return redirect('list_investments')
    return render(request, 'tracker/edit_investment.html', {'investment': investment})

def delete_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        investment.delete()
        return redirect('list_investments')
    return render(request, 'tracker/confirm_delete.html', {'investment': investment})
