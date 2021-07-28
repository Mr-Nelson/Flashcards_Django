from rest_framework import serializers
from .models import Collection, Flashcard


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name']


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer', 'collection']