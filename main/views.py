from django.shortcuts import render, redirect
from .models import Trade, Enter_Trade, Exit_Trade
from .forms import CreateTrade, CreateEntry, CreateExit
from django.http import HttpResponse
from datetime import date
from decimal import Decimal

def home(request):
    user = request.user
    trades = user.trade_set.all()
    return render(request, 'main/home.html', {})

def dates(request, date_str):  # Rename date to date_str initially
    user = request.user
    trades = user.trade_set.all()
    filtered_trades = trades.filter(date=date_str)
    return render(request, 'main/dates.html', {"filtered_trades": filtered_trades})


def profile(request):
    user = request.user
    unique_dates = Trade.objects.values_list('date', flat=True).distinct().order_by('date')
    strategies = Enter_Trade.objects.filter(user = user)
    trades = user.trade_set.all()
    entry_reasons_profit = {strat: strat.profit for strat in strategies}
    wins = 0
    total_win = Decimal(0.00)
    losses = 0
    total_loss = Decimal(0.00)

    # Add Trade.p_and_l to the Entry_Reason profit if it appears in reasons_entry
    for trade in trades:
        if trade.profit:
            wins += 1
            total_win += trade.p_and_l
        else:
            losses += 1
            total_loss += trade.p_and_l

    total_p_and_l = total_win - total_loss
    win_percentage = (wins / len(trades)) * 100
    average_win = total_win / wins if wins > 0 else Decimal("0.00")
    average_loss = total_loss / losses if losses > 0 else Decimal("0.00")
    context = {
        "strategies": strategies,
        "unique_dates": unique_dates,
        "Trade": Trade,
        "trades": trades,
        "entry_reasons_profit": entry_reasons_profit,
        "win_percentage": win_percentage,
        "average_win": average_win,
        "average_loss": average_loss,
        "total_p_and_l": total_p_and_l
    }
    return render(request, 'main/profile.html', context)

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

def strategy(request, strategy):
    strategy = Enter_Trade.objects.get(reason = strategy)
    user = request.user
    trades = user.trade_set.all()
    profit = sum(trade.p_and_l for trade in trades if strategy in trade.reasons_entry.all())
    strategies = Enter_Trade.objects.filter(user = user)
    count = 0
    pictures = []
    for trade in trades:
        for strat in strategies:
            if strat in trade.reasons_entry.all():
                count += 1
                pictures.append(trade.picture1)
    context = {
        "strategy": strategy,
        "trades": trades,
        "profit": profit,
        "count": count,
        "pictures": pictures
    }
    return render(request, 'main/strategy.html', context)