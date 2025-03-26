from django.shortcuts import render, redirect
from .models import Trade, Enter_Trade, Exit_Trade
from .forms import CreateTrade, CreateEntry, CreateExit
from django.http import HttpResponse
from datetime import date

def home(request):
    return render(request, 'main/home.html', {})

def dates(request, date_str):  # Rename date to date_str initially
    user = request.user
    trades = user.trade_set.all()
    filtered_trades = trades.filter(date=date_str)
    return render(request, 'main/dates.html', {"filtered_trades": filtered_trades})

def profile(request):
    unique_dates = Trade.objects.values_list('date', flat=True).distinct().order_by('date')
    return render(request, 'main/profile.html', {'unique_dates': unique_dates})

def trade(request):
    if request.method == 'POST':
        form = CreateTrade(request.POST, user=request.user)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user  # Assign the user before saving
            trade.save()
            form.save_m2m()  # Save many-to-many fields if any
            return redirect('trade')  # Redirect to a success page
    else:
        form = CreateTrade(user=request.user)

    return render(request, 'main/trade.html', {'form': form})


def entry(request):
    user = request.user
    print(user)
    if request.method == "POST":
        form = CreateEntry(request.POST)
        if form.is_valid():
            r = form.cleaned_data['reason']
            exit = Enter_Trade(reason = r, user = user)
            exit.save()
    else:
        form = CreateEntry()

    return render(request, 'main/entry.html', {"form": form})

def exit(request):
    user = request.user
    if request.method == "POST":
        form = CreateExit(request.POST)
        if form.is_valid():
            r = form.cleaned_data['reason']
            exit = Exit_Trade(reason = r, user = user)
            exit.save()
    else:
        form = CreateEntry()

    return render(request, 'main/exit.html', {"form": form})