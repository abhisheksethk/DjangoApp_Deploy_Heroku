from django.urls import path,include
from .import views
app_name='authapp'
urlpatterns = [
    path('register/',views.register,name="register"),
   #path('',views.list,name="list"),
   #path('new',views.create,name="create"),
   #path('update/<int:id>',views.update,name="update"),
   #path('delete/<int:id>',views.delete,name="delete"),
]
