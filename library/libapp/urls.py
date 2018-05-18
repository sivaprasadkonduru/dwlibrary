from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'book_details/', views.book_details),
    url(r'book_details/', views.BookView.as_view()),
    url(r'book_data/', views.book_data)
]