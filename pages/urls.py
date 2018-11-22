from django.urls import path

from .views import AboutPageView, HomePageView, JeszczePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('jeszcze/', JeszczePageView.as_view(), name='jeszcze')
]
