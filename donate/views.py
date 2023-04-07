from rest_framework import generics
from .models import BulletinBoard
from .serializers import BulletinBoardSerializer


# POST
class BoardAPIViewPost(generics.CreateAPIView):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer    


# GET
class BoardAPIViewGetList(generics.ListCreateAPIView):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer


# PUT / PATCH
class BoardAPIViewUpdate(generics.UpdateAPIView):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer


# DELETE
class BoardAPIViewDelete(generics.DestroyAPIView):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer

