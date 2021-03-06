from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog_index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<int:book_id>/', views.book_details, name="book_details"),
    path('<int:book_id>/reserve/', views.reserve_book, name="reserve_book"),
    path('profile/', views.profile, name='profile')
]
