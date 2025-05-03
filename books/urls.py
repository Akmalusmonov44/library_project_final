from tkinter.font import names
from rest_framework.routers import SimpleRouter

from django.urls import path


from .views import BookDetailApiView, BookUpdateApiView, BookDestroyApiView, BookCreateApiView, \
    BookListCreateAPiView, BookUpdateDeleteView, BookListApiView, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view(),),
    # path('book/', BookListCreateAPiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view(),),
    # path('book/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view(),),
    # path('books/<int:pk>/delete', BookDestroyApiView.as_view()),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view()),

]

urlpatterns = urlpatterns + router.urls