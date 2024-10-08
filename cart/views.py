# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.decorators import login_required
# from rest_framework.permissions import IsAuthenticated
# from .models import Cart, CartItem, Business
# from .serializers import CartSerializer, CartItemSerializer

# class CartAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             cart = Cart.objects.get(user=request.user)
#             serializer = CartSerializer(cart)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Cart.DoesNotExist:
#             return Response({"message": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

#     def post(self, request):
#         service_id = request.data.get("service_id")
#         quantity = request.data.get("quantity", 1)

#         try:
#             business= Business.objects.get(id=service_id)
#             cart, created = Cart.objects.get_or_create(user=request.user)
#             cart_item, created = CartItem.objects.get_or_create(cart=cart, business=business)

#             if not created:
#                 cart_item.quantity += quantity
#             else:
#                 cart_item.quantity = quantity

#             cart_item.save()
#             return Response({"message": "Item added to cart."}, status=status.HTTP_201_CREATED)
#         except Service.DoesNotExist:
#             return Response({"message": "businessnot found."}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, service_id):
#         try:
#             cart = Cart.objects.get(user=request.user)
#             cart_item = CartItem.objects.get(cart=cart, service__id=service_id)
#             cart_item.delete()
#             return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)
#         except CartItem.DoesNotExist:
#             return Response({"message": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)
# # 
# class CheckoutView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         try:
#             cart = Cart.objects.get(user=request.user)
#             cart_items = CartItem.objects.filter(cart=cart)

#             if not cart_items.exists():
#                 return Response({"message": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
#             totaldue=0
#             for cart_item in cart_items:
#                 totaldue += cart_item.service.price * cart_item.quantity
#             cart_items.delete()

#             return Response({"message":f"Checkout successful. your total due is {totaldue}"}, status=status.HTTP_201_CREATED)
#         except Cart.DoesNotExist:
#             return Response({"message": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
