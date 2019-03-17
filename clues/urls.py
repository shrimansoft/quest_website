from django.urls import path
from .views import clue_detail
from . import views
urlpatterns = [
    path('',views.clue_detail,name='clue')
]
