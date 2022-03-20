from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.contrib import messages

def check_deposit(data, playergold):
    try:
        data = int(data)
    except:
        return False

    if int(data) > playergold:
        return False

    if int(data) < 0:
        return False

    return True

def deposit(request, player, raw_value):
    if check_deposit(raw_value, player.gold):
        player.gold -= int(raw_value)
        player.bank_account += int(raw_value)
        messages.add_message(request, messages.INFO, f"You deposited {raw_value}g")
    else:
        messages.add_message(request, messages.WARNING, "Hey there Sneaky Pete, none of that.")


# Create your views here.
class BankView(View):
    def get(self, request):
        player = User.objects.get(username=request.user.username).player
        return render(request, "bank.html", {'player': player})

    def post(self, request):
        player = User.objects.get(username=request.user.username).player
        data = request.POST
        print(data)
        if data["deposit-input"]:
            deposit(request, player, data["deposit-input"])

        player.save()
        return redirect('bank')
