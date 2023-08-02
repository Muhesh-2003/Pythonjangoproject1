from django.urls import path
from website import views
app_name='website'

urlpatterns = [
    path('index', views.index, name = "index"),
    path('contact', views.contact, name = "contact"),
    path('events', views.events, name = "events"),
    path('reservation', views.reservation, name = "reservation"),
    path('rooms', views.rooms, name = "rooms"),
    path('about', views.about, name = "about"),
    path('index', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),

]