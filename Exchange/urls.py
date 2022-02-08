from django.urls import path
from .views import home_index, exchange_detail


urlpatterns = [
    path('', home_index, name='home'),
    path('<slug:exchange_slug>/', exchange_detail, name='exchange_detail'),

]