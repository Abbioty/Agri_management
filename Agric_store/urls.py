from django.urls import path
from .views import index_view, product_detail


urlpatterns = [
    path('', index_view, name='index'),
   path('<slug:product_slug>/', product_detail, name='product_detail'),

]