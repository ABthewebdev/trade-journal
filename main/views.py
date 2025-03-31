from django.shortcuts import render, redirect
from .models import Trade, Enter_Trade, Exit_Trade, OptionsTrade
from .forms import CreateFutures, CreateEntry, CreateExit, CreateOptions
import random
from decimal import Decimal

def home(request):
    class Quote:
        def __init__(self, quote, author):
            self.quote = quote
            self.author = author
    quotes = [
        Quote("Get a trade journal", "Hitler"),
        Quote("Thou shall not take pennies in profits and benji's in losses", "Shakespeare"),
        Quote("Let's bleed em dry", "AMC shareholders to the shorts"),
        Quote("You're fired", "Trump to the bulls"),
        Quote("What I've done now is I've changed and manipulated time", "Some guy who gets 21 days a week"),
        Quote("I just buy the stop losses of the stupid retail traders", "The hedgies"),
        Quote("Everyone has two lives, the first one is trading without a stop loss, the second one is for actually making money", "Confucious"),
        Quote("Don't get greedy, take your profits where you can get them", "A trader who loses money"),
        Quote("There is a time to go long, a time to go short, and a time to go fishing", "Jesse Livermore"),
        Quote("Derivatives are financial weapons of mass money duplication", "Bill Hwang"),
        Quote("The best way to predict the future is to manipulate it", "JPow"),
        Quote("Risk comes from not knowing what you're doing, which is why we just HODL", "Me holding my NVDL shares")
    ]
    return render(request, 'main/home.html', {"quote": quotes[random.randint(0, len(quotes) - 1)]})

def profile(request):
    user = request.user
    unique_dates = Trade.objects.values_list('date', flat=True).distinct().order_by('date')
    strategies = Enter_Trade.objects.filter(user = user)
    entry_reasons_profit = {strat: strat.profit for strat in strategies}

    # All stuff for futures trading
    futures_trades = user.trade_set.all()
    futures_wins = 0
    futures_total_win = Decimal(0.00)
    futures_losses = 0
    futures_total_loss = Decimal(0.00)
    # Add Trade.p_and_l to the Entry_Reason profit if it appears in reasons_entry
    for trade in futures_trades:
        if trade.profit:
            futures_wins += 1
            futures_total_win += trade.p_and_l
        else:
            futures_losses += 1
            futures_total_loss += trade.p_and_l
    futures_p_and_l = futures_total_win - futures_total_loss
    futures_percentage = futures_wins / len(futures_trades) * 100 if len(futures_trades) > 0 else 0
    average_futures_win = futures_total_win / futures_wins if futures_wins > 0 else Decimal("0.00")
    average_futures_loss = futures_total_loss / futures_losses if futures_losses > 0 else Decimal("0.00")

    # All stuff for options trading
    options_wins = 0
    options_losses = 0
    options_total_win = Decimal(0.00)
    options_total_loss = Decimal(0.00)
    options_trades = OptionsTrade.objects.filter(user = user)
    for trade in options_trades:
        if trade.profit:
            options_wins += 1
            options_total_win += trade.p_and_l
        else:
            options_losses += 1
            options_total_loss += trade.p_and_l
    options_p_and_l = options_total_win - options_total_loss
    options_percentage = options_wins / len(options_trades) * 100 if len(options_trades) > 0 else 0
    average_options_win = options_total_win / options_wins if options_wins > 0 else Decimal("0.00")
    average_options_loss = options_total_loss / options_losses if options_losses > 0 else Decimal("0.00")

    context = {
        "strategies": strategies,
        "unique_dates": unique_dates,
        "Trade": Trade,
        "futures_trades": futures_trades,
        "entry_reasons_profit": entry_reasons_profit,
        "futures_percentage": futures_percentage.__round__(),
        "average_futures_win": average_futures_win.__round__(),
        "average_futures_loss": average_futures_loss.__round__(),
        "futures_p_and_l": futures_p_and_l,
        "options_p_and_l": options_p_and_l.__round__(),
        "options_percentage": options_percentage.__round__(),
        "average_options_win": average_options_win.__round__(),
        "average_options_loss": average_options_loss.__round__()
    }
    return render(request, 'main/profile.html', context)

def dates(request, date_str):  # Rename date to date_str initially
    user = request.user
    futures_trades = user.trade_set.all()
    options_trades = OptionsTrade.objects.filter(user = user)
    filtered_options_trades = options_trades.filter(date=date_str)
    filtered_futures_trades = futures_trades.filter(date=date_str)
    futures_profit = Decimal(0.00)
    options_profit = Decimal(0.00)
    date = date_str
    total_trades = filtered_futures_trades.count() + filtered_options_trades.count()
    futures_wins = 0
    futures_losses = Decimal(0.00)
    options_losses = Decimal(0.00)
    options_wins = 0
    for trade in filtered_futures_trades:
        if trade.profit:
            futures_wins += 1
            futures_profit += trade.p_and_l
        if trade.loss:
            futures_losses += trade.p_and_l
    for trade in filtered_options_trades:
        if trade.profit:
            options_wins += 1
            options_profit += trade.p_and_l
        if trade.loss:
            options_losses += trade.p_and_l
    wins = futures_wins + options_wins
    total_profit = futures_profit +  options_profit - futures_losses - options_losses
    if total_trades == 0:
        profit_percentage = 0.00
    else:
        profit_percentage = (wins / total_trades) * 100

    context = {
        "filtered_futures_trades": filtered_futures_trades,
        "filtered_options_trades": filtered_options_trades,
        "total_profit": total_profit,
        "date": date,
        "total_trades": total_trades,
        "profit_percentage": profit_percentage.__round__()
    }
    return render(request, 'main/dates.html', context)


def trade(request):
    if request.method == 'POST':
        form = CreateFutures(request.POST, user=request.user)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user  # Assign the user before saving
            trade.save()
            form.save_m2m()  # Save many-to-many fields if any
            return redirect('trade')  # Redirect to a success page
    else:
        form = CreateFutures(user=request.user)

    return render(request, 'main/trade.html', {'form': form})


def entry(request):
    user = request.user
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

def setup(request, setup):
    setup = Enter_Trade.objects.get(reason = setup)
    user = request.user
    # All futures tradng stuff
    futures_trades = user.trade_set.all()
    futures_profits = Decimal(0.00)
    futures_losses = Decimal(0.00)
    futures_pictures = []
    futures_count = 0
    futures_wins = 0
    for trade in futures_trades:
        if setup in trade.reasons_entry.all():
            futures_count += 1
            futures_pictures.append(trade)
            if trade.profit:
                futures_wins += 1
                futures_profits += trade.p_and_l
            else:
                futures_losses += trade.p_and_l

    # All options trading stuff
    options_profits = Decimal(0.00)
    options_losses = Decimal(0.00)
    options_pictures = []
    options_trades = OptionsTrade.objects.filter(user = user)
    options_count = 0
    options_wins = 0
    for trade in options_trades:
        if setup in trade.reasons_entry.all():
            options_count += 1
            options_pictures.append(trade)
            if trade.profit:
                options_wins += 1
                options_profits += trade.p_and_l
            elif trade.loss:
                options_losses += trade.p_and_l

    total_profit = options_profits + futures_profits - options_losses - futures_losses
    total_trades = futures_count + options_count
    wins = futures_wins + options_wins
    total_profit
    if total_trades == 0:
        profit_percentage = 0
    else:
        profit_percentage = (wins / total_trades) * 100

    context = {
        "setup": setup,
        "futures_trades": futures_trades,
        "futures_profits": futures_profits,
        "futures_pictures": futures_pictures,
        "options_trades": options_trades,
        "options_pictures": options_pictures,
        "total_trades": total_trades,
        "total_profit": total_profit,
        "profit_percentage": profit_percentage.__round__()
    }
    return render(request, 'main/strategy.html', context)

def options(request):
    if request.method == 'POST':
        form = CreateOptions(request.POST, user=request.user)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user  # Assign the user before saving
            trade.save()
            form.save_m2m()
            return redirect('options')
    else:
        form = CreateOptions(user=request.user)
    return render(request, 'main/options.html', {"form": form})
