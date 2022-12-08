from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name="index"),
    path('register', v.register, name="register"),
    path('login', v.login, name="login"),
    path('logout', v.logout, name="logout"),
    path("delete/<item_id>", v.deleteItem, name="deleteItem"),
    path("update/<item_id>", v.updateItem, name="updateItem"),

]
