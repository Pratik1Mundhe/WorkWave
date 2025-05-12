import json 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login(request):
    logger.info("Login endpoint accessed")
    logger.info(f"Request headers: {request.headers}")
    logger.info(f"Request method: {request.method}")
    return Response({"status": "ok"})

@csrf_exempt
def logout(request):
    body = json.loads(request.body)
    user_name = body["user_name"]
    password = body["password"]
    # interactor = PlayerInteractor(
    #     storage=StorageImplementation(),
    #     presenter=PresenterImplementation()
    # )

    # try:
    #     response = interactor.create_player(
    #         user_name=user_name,
    #         password=password
    #     )
    # except Exception as err:
    #     return HttpResponse(f"error: {str(err)}")

    return HttpResponse("Username: ", user_name, " Password: ", password)

