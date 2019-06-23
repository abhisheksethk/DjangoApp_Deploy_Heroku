from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    #path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('userList/',views.userList,name="userList"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('update/<int:id>/',views.update,name="update"),
     

]
