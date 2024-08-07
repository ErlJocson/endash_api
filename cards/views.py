from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cards
from .serializers import CardSerializer

@api_view(['GET'])
def get_all_cards(request):
    instance = Cards.objects.all().order_by('position')

    data = CardSerializer(instance, many=True).data

    if data:
        return Response(data, status=status.HTTP_200_OK)
    return Response({"msg": "There are no CARDS"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_card(requets, id):
    instance = get_object_or_404(Cards, id = id)
    data = CardSerializer(instance).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_card(request):
    serializer = CardSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_card(request, id):
    instance = get_object_or_404(Cards, id = id)
    instance.delete()
    return Response({"msg":f"Card of id number {id} is deleted"}, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_card(request, id):
    instance = get_object_or_404(Cards, id = id)

    serializer = CardSerializer(instance, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
