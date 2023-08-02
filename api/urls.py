from django.urls import path
from.views import ListCloths,DetailView,AddToCartView,UpdateView,DeleteView

urlpatterns =[
    path('cloths/',ListCloths.as_view(),name='cloth'),
    path('detail/<int:pk>/',DetailView.as_view(),name='view'),
    path('update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteView.as_view(),name='delete'),
    path('cart/',AddToCartView.as_view(),name='cart')

]