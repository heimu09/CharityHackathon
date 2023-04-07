from django.contrib import admin
from django.urls import path
from .views import (BoardAPIViewPost,
                    BoardAPIViewGetList,
                    BoardAPIViewUpdate,
                    BoardAPIViewDelete)


urlpatterns = [
    path('board/create/', BoardAPIViewPost.as_view()),
    path('board/view/', BoardAPIViewGetList.as_view()),
    path('board/update/<int:pk>/', BoardAPIViewUpdate.as_view()),
    path('board/delete/', BoardAPIViewDelete.as_view()),
]
