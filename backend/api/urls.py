from django.urls import path, re_path
from .views import moneys, create_money, money
from .views import register, login
from knox import views as knox_views

urlpatterns = [
    path('moneys/', moneys, name="moneys"),
    path('money/',create_money, name ="create-money"),
    path('money/<int:id>/', money, name='money'),
    path('user/register/', register, name='register'),
    path('user/login/', login,name='login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout1'),
]
