from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

class YourModelNameListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class YourModelNameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
