from django.shortcuts import render
from .models import Trade
from .forms import CreateTrade

# Create your views here.
def home(request):
    user = request.user
    trades = user.trade_set.all()
    return render(request, 'main/home.html', {"trades": trades})

def trade(request):
    if request.method == "POST":
        form = CreateTrade(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateTrade()
    return render(request, 'main/trade.html', {"form": form})