import json 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from oauth2_provider.decorators import protected_resource
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    my_field = serializers.CharField()

@swagger_auto_schema(
    operation_description="Custom description for this endpoint",
    request_body=MySerializer,
    responses={200: MySerializer},
    method='post'
)


@api_view(['POST'])
@authentication_classes([])
def login(request):
    body = json.loads(request.body)
    user_name = body["user_name"]
    password = body["password"]
    return HttpResponse(f"user_name: {user_name}")

# ###
# for user to login
# FE will make request to o/authorize/ with username password clientid and cliend_secret as grant type is resource owner
# and get the access token 
# needs to be saved as cookies
# for making request to other protected apis 
# ###

@swagger_auto_schema(
    operation_description="Custom description for this endpoint",
    request_body=MySerializer,
    responses={200: MySerializer},
    method='post'
)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def logout(request):
    token = request.auth
    if token:
        token.revoke()
    return Response({"status": "logged out"})


