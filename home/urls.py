from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name = 'home'),
    path('subcat/<slug>', SubcategoryView.as_view(),name = 'subcat'),
    path('detail/<slug>', DetailView.as_view(),name = 'detail'),
    path('search/', SearchView.as_view(),name = 'search'),
    path('register/', signup ,name = 'register'),
]
