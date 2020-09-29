from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name="index"),
path('index.html',views.index,name="index"),
path('login',views.login,name="login"),
path('about.html',views.about,name="about"),
path('contact.html',views.contact,name="contact"),
path('portfolio.html',views.portfolio,name="portfolio"),
path('services.html',views.services,name="services"),
path('portfolio_details.html',views.portfolio_details,name="portfolio_details"),

]