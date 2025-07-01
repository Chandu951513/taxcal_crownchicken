from django.urls import path
from . import views

urlpatterns = [
    path('',views.taxcal,name='taxcal'),
    path('removedata',views.removedata,name='removedata'),
    path('removeitem/<int:id>',views.removeitem,name='removeitem')
]



