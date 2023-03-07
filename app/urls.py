from django.urls import path
from .views import Dash

urlpatterns = [
    path('', Dash.home, name='home'),
    # path('other/', views.other, name='other')
]