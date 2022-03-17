from django.db import models
from django.contrib.auth.models import User

class WeaponType(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=32)
    damage = models.PositiveSmallIntegerField()
    cost = models.PositiveIntegerField()
    type = models.ForeignKey("WeaponType", on_delete=models.CASCADE)
    player_weapon = models.BooleanField(default=False)

    @property
    def sell_price(self):
        return int(self.cost / 2)

    def __str__(self):
        return self.name

class PlayerClass(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    weapon = models.ForeignKey("Weapon", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    char_name = models.CharField(max_length=32)
    max_hp = models.PositiveSmallIntegerField()
    current_hp = models.PositiveSmallIntegerField()
    new = models.BooleanField(default=True)
    player_class = models.ForeignKey("PlayerClass", on_delete=models.PROTECT)
    weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE)
    gold = models.PositiveIntegerField(default=100)
    forest_fights_per_day = models.PositiveSmallIntegerField(default=20)
    forest_fights_remaining = models.PositiveSmallIntegerField(default=20)
    last_day_played = models.DateField(auto_now=True)
    level = models.PositiveSmallIntegerField(default=1)
    charm = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.char_name

class NPC(models.Model):
    name = models.CharField(max_length=64)
    level = models.PositiveSmallIntegerField()
    weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE, null=True)
    gold = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Monster(NPC):
    pass

class Armor(models.Model):
    name = models.CharField(max_length=32)
    defence = models.PositiveSmallIntegerField()
    cost = models.PositiveIntegerField()
