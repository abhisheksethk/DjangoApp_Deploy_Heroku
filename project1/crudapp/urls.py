from django.urls import path,include
from . import views
app_name='crudapp'
urlpatterns = [
    #path('',views.home,name="home"),
   path('',views.list,name="list"),
   path('new',views.create,name="create"),
   path('update/<int:id>',views.update,name="update"),
   path('delete/<int:id>',views.delete,name="delete"),
]
