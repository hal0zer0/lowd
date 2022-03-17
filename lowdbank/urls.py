from django.urls import path
from django.contrib.auth.decorators import login_required
from lowdbank.views import BankView

urlpatterns = [
    path('', login_required(BankView.as_view()), name="bank"),
    #path('deposit/', login_required(views.HomeView.as_view()), name="home"),
    ]