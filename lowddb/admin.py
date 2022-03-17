from django.contrib import admin
from lowddb.models import Player, PlayerClass, Weapon, WeaponType, NPC, Monster
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class PlayerInline(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'players'

class UserAdmin(BaseUserAdmin):
    inlines = (PlayerInline,)


class PlayerClassAdmin(admin.ModelAdmin):
    pass


class WeaponTypeAdmin(admin.ModelAdmin):
    pass

class WeaponAdmin(admin.ModelAdmin):
    pass

class NPCAdmin(admin.ModelAdmin):
    pass

class MonsterAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(PlayerClass, PlayerClassAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(WeaponType, WeaponTypeAdmin)
admin.site.register(NPC, NPCAdmin)
admin.site.register(Monster, MonsterAdmin)

