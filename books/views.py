from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

import books
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, viewsets


# Create your views here.

# class BooksListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status':F'Returned {len(books)} books',
            'books': serializer_data
        }

        return Response(data)


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        book = Book.object.get(id=pk)
        serializer_data = BookSerializer(book).data

        data = {
            'status':'Succesfull'
        }


class BookDestroyApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





class BookListCreateAPiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

