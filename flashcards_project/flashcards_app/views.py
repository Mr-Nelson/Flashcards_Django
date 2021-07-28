from django.http import Http404
from .models import Collection, Flashcard
from .serializers import CollectionSerializer, FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer (collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardList(APIView):

    def get_by_id(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection_id = self.get_by_id(pk)
        flashcard = Flashcard.objects.all(collection_id)
        serializer = FlashcardSerializer (flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetails(APIView):

    def get_by_id(self, pk):
        try:
            return Flashcard.objects.get(pk=pk)
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flashcard_id = self.get_by_id(pk)
        serializer = FlashcardSerializer(flashcard_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        flashcard_id = self.get_by_id(pk)
        deleteFlashcard = FlashcardSerializer(flashcard_id)
        flashcard_id.delete()
        return Response(deleteFlashcard.data, status=status.HTTP_200_OK)
