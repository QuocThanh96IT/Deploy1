from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Money
from ..serializers import MoneySerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi




@swagger_auto_schema(
    method='post', 
    responses={200: 'successful operation'},
    operation_summary="List all moneys",
    operation_description="Post and Receive a list money"
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def moneys(request, format=None):
  moneys = Money.objects.all()
  serializer = MoneySerializer(moneys,many = True)
  total_spend = total_earn =total_save = 0

  for money in moneys:
      if money.type.lower() == 'spend' :
          total_spend += money.amount
      elif money.type.lower() == 'earn' :
          total_earn += money.amount

  total_save = total_earn - total_spend
  context ={'total_spend':total_spend,'total_earn':total_earn,'total_save':total_save,'serializer':serializer.data}
  return Response(context, status=status.HTTP_200_OK)



# @permission_classes([IsAuthenticated])
@swagger_auto_schema(
    method='post', 
    request_body=MoneySerializer,
    operation_summary="Create a money",
    operation_description="Type correct the form and receive a money")
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_money(request):
    serializer = MoneySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return Response(serializer.errors)


user_response = openapi.Response('Successful operation')
@swagger_auto_schema(
    methods=['delete'], 
    responses={200: user_response},
    operation_summary="Delete a money",
    operation_description="Type correct id and delete a money"
    )
@swagger_auto_schema(
    methods=['get'], 
    responses={200: user_response},
    operation_summary="Get a money",
    operation_description="Type correct  id and get a money"
    )
@swagger_auto_schema(
    method='put', 
    request_body=MoneySerializer,
    operation_summary="Change a money",
    operation_description="Type correct id and change a money"
    )
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])

def money(request, id):
    try:
        money = Money.objects.get(pk=id)
    except Money.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MoneySerializer(money)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MoneySerializer(money, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        money.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)