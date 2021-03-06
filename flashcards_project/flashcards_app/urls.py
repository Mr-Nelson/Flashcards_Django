from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),
    path('flashcard/<int:collectionId>/', views.FlashcardList.as_view()),
    path('flashcard/', views.CreateFlashcard.as_view()),
    path('flashcardid/<int:pk>/', views.FlashcardDetails.as_view()),
]
