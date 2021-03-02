from django.urls import path
from .views import HomePageView, PrecioPageView, AboutPageView

urlpatterns = [
    path('about', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'home'),
    path('precio', PrecioPageView.as_view(), name = 'precio')



]