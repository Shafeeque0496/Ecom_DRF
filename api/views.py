import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Cloths,Cart
from .serializers import ClothSerializer,CartSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
class ListCloths(ListCreateAPIView):
    queryset = Cloths.objects.all()  # for getting all value in a table
    serializer_class = ClothSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClothSerializer(queryset,many=True)
        return Response(serializer.data)

class UpdateView(UpdateAPIView):
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

class DeleteView(DestroyAPIView):
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

class DetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothSerializer(queryset,many=False)
        return Response(serializer.data)



class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product = Cloths.objects.get(id=product_id)
            cart_item = Cart(user=request.user,product=product,quantity=quantity)
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error":"product not found."},status=status.HTTP_404_NOT_FOUND)

# class ChecklistView(APIView):
#     serializer_class = CartSerializer
#     queryset = Cart.objects.all()
#
#     def get(self,request):
