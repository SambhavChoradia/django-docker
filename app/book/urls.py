from django.urls import path
from book.views import BookView

urlpatterns = [
    path('book/', BookView.as_view()),

]
