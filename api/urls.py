from django.urls import path
from .views import EmployeeView,PaysView,MarqueView,VilleView,Home


urlpatterns = [
    path('',Home,name="index"),
    path('employes', EmployeeView.as_view()),
    path('pays', PaysView.as_view()),
    path('ville', VilleView.as_view()),
    path('marques', MarqueView.as_view()),
]
