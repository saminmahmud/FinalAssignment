from django.urls import path
from . import views
urlpatterns = [
    path('buy_ticket/<int:id>/', views.buy_ticket.as_view(), name='buy_ticket'),
    path('buy/<int:tid>/<int:sid>/', views.buy, name='buy'),
]
