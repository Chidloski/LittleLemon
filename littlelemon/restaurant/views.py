from django.shortcuts import render
from rest_framework import generics, response, status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    '''def get(self, request):
        return response.Response({"message": "menu"}, status.HTTP_200_OK)
    
    def post(self, request):
        return response.Response({"message": "new menu item added"}, status.HTTP_201_CREATED)'''


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer




    