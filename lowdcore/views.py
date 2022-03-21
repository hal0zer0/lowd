import random
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from lowddb.models import PlayerClass, Monster, Weapon
from django.contrib import messages

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class LoginView(TemplateView):
    template_name = "login.html"

class TownSquareView(View):
    template_name = "town_square.html"

    def get(self, request):
        player = User.objects.get(username=request.user.username).player
        return render(request, "town_square.html", {"player": player})


class NewPlayerView(TemplateView):
    def get(self, request):
        classes = PlayerClass.objects.all()
        return render(request, "new_player.html", {"classes": classes})

    def post(self, request):
        pclass = request.POST["class_buttons"]
        pclass_obj = PlayerClass.objects.get(name=pclass)

        player = User.objects.get(username=request.user.username).player
        player.player_class = pclass_obj
        player.char_name = request.POST["name_input"]
        #player.new = False

        player.save()
        return redirect("town_square")


class ForestView(View):
     def get(self, request):
        player = User.objects.get(username=request.user.username).player
        return render(request, "forest.html", {'player': player})


class FightView(View):
    def get(self, request):
        player = User.objects.get(username=request.user.username).player
        mob = random.choice(Monster.objects.filter(level=player.level, instance=False))
        mob.pk = None
        mob.id = None
        mob.name = mob.name + " INSTANCE"
        mob.instance = True
        mob.save()
        player.current_mob = mob
        player.save()
        return render(request, "fight.html", {'player': player,
                                              'monster': player.current_mob})


class WeaponShopView(View):
    def get(self, request):
        player = User.objects.get(username=request.user.username).player
        weapons = Weapon.objects.filter(shop_weapon=True).order_by('level')
        return render(request, "weapon_shop.html", {'player': player,
                                                    'weapons': weapons})
    def post(self, request):
        player = User.objects.get(username=request.user.username).player
        to_buy = Weapon.objects.get(id=int(request.POST["weapon-selection"]))

        if to_buy.cost > (player.gold + player.weapon.sell_price):
            messages.add_message(request, messages.WARNING, f'You cannot afford {to_buy.name}!')
            return redirect('weapon_shop')

        # auto-sell current weapon
        player.gold += player.weapon.sell_price
        player.gold -= to_buy.cost
        try:
            assert player.gold >= 0
        except:
            messages.add_message(request, messages.WARNING, f'You tried something fishy.  No.')
            return redirect('weapon_shop')

        player.weapon = to_buy
        player.save()

        messages.add_message(request, messages.INFO, f'You are now the proud owner of a {to_buy.name}!')
        return redirect('weapon_shop')


@login_required()
def check_new(request):
    user = User.objects.get(username=request.user.username)
    if user.player.new:
        return redirect('new_player')
    else:
        return redirect('town_square')

class AttackView(View):
    def get(self, request):
        player = User.objects.get(username=request.user.username).player
        messages.add_message(request, messages.INFO, f'{ player.weapon.damage}')
        return redirect('fight')


