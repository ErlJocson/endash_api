from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_all_cards, get_card, add_card, delete_card, update_card

@api_view(["GET"])
def get_all_cards_api(request) -> Response:
    cards = get_all_cards(doc_name = 'endashDB')
    print(cards)
    return Response(cards, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_card_api(request, row_id: int) -> Response:
    doc_name = 'endashDB'

    if not row_id:
        return Response({"error": "ID parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        row_id = int(row_id)
    except ValueError:
        return Response({"error": "ID must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

    card = get_card(doc_name=doc_name, row_id=row_id)
    
    if card:
        return Response(card, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Card not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def add_card_api(request) -> Response:
    doc_name = 'endashDB'
    card_data = request.data

    if not card_data:
        return Response({"Error":"Card data is required"})
    
    success = add_card(doc_name=doc_name, card_data=card_data)

    if success:
        return Response({"message":"Card added successfully"}, status=status.HTTP_201_CREATED)
    return Response({"error":"Failed to add card"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_card_api(request, row_id: int) -> Response:
    doc_name = 'endashDB'
    result = delete_card(doc_name=doc_name, row_id=row_id)

    if result:
        return Response({"message":"Card deleted"}, status=status.HTTP_202_ACCEPTED)
    return Response({"error":"Failed to delete card"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_card_api(request, row_id: int) -> Response:
    doc_name = 'endashDB'
    result = update_card(doc_name=doc_name, row_id=row_id, new_data=request.data)

    if result:
        return Response({"message":"Card updated"}, status=status.HTTP_202_ACCEPTED)
    return Response({"error":"Faild to update card"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    