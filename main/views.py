from django.shortcuts import render, redirect
from .models import Trade, Enter_Trade, Exit_Trade
from .forms import CreateTrade, CreateEntry, CreateExit
from django.http import JsonResponse
from django.conf import settings

def debug_allowed_hosts(request):
    return JsonResponse({"ALLOWED_HOSTS": settings.ALLOWED_HOSTS})

def home(request):
    unique_dates = Trade.objects.values_list('date', flat=True).distinct().order_by('date')
    return render(request, 'main/home.html', {'unique_dates': unique_dates})

def profile(request, date):
    user = request.user
    trades = user.trade_set.all()
    filtered_trades = trades.filter(date=date)
    return render(request, 'main/profile.html', {"filtered_trades": filtered_trades})

def trade(request):
    if request.method == "POST":
        form = CreateTrade(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            data = Trade(
                user=request.user,
                ticker=form.cleaned_data['ticker'],
                long=form.cleaned_data['long'],
                short=form.cleaned_data['short'],
                entry_price=form.cleaned_data['entry_price'],
                average_down=form.cleaned_data['average_down'],
                profit=form.cleaned_data['profit'],
                loss=form.cleaned_data['loss'],
                p_and_l=form.cleaned_data['p_and_l'],
                trim1=form.cleaned_data['trim1'],
                trim2=form.cleaned_data['trim2'],
                exit_price=form.cleaned_data['exit_price'],
                date = form.cleaned_data['date'],
                entry_time=form.cleaned_data['entry_time'],
                exit_time=form.cleaned_data['exit_time'],
                picture1=form.cleaned_data['picture1'],
                picture2=form.cleaned_data['picture2'],
            )
            print("Form created:", form.cleaned_data)
            data.save()
            # Set many-to-many relationships correctly - no commas after each line
            data.reasons_entry.set(form.cleaned_data['reasons_entry'])
            data.reasons_exit.set(form.cleaned_data['reasons_exit'])
            data.save()
            print("Date being saved:", data.date)  # Should print YYYY-MM-DD
        else:
            print("Form is not valid", form.errors)
            
            # Add a redirect after successful form submission
            return redirect('/profile')  # Replace with your actual URL name
    else:
        form = CreateTrade()
    return render(request, 'main/trade.html', {"form": form})

def entry(request):
    if request.method == "POST":
        entry_reason = CreateEntry(request.POST)
        if entry_reason.is_valid():
            a = entry_reason.cleaned_data['reason']
            f = Enter_Trade(reason = a)
            f.save()
    else:
        entry_reason = CreateEntry()
        return render(request, 'main/entry.html', {"entry": entry_reason})

def exit(request):
    if request.method == "POST":
        exit_reason = CreateExit(request.POST)
        if exit_reason.is_valid():
            b = exit_reason.cleaned_data['reason']
            e = Exit_Trade(reason = b)
            e.save()
    else:
        exit_reason = CreateExit()
        return render(request, 'main/exit.html', {"exit": exit_reason})