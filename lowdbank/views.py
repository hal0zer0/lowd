from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.contrib import messages

def check_deposit(data, player):
    
    return True

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
            check_deposit(data["deposit-input"], player.gold)

        messages.add_message(request, messages.INFO, "You tried to deposit or withdraw")

        return redirect('bank')