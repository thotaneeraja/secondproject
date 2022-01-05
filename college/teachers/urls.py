from django.urls import path,include
from.views import index
from.views import cre
from.views import func
from.views import create,edit,update,delete,home,login,user_logout
urlpatterns=[
    path('neeru/',func),
    path('teja/',cre),
    path('index/',index),
    path('kesavulu/',create),
    path("edit/<str:name>/",edit),
    path('update/<str:name>/',update),
    path('delete/<str:name>/',delete),
    path('login/',login),
    path('logout/',user_logout),
    path('',home),

]