from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def logout_view(request):
    if request.method=="POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
def register_view(request):

    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        refresh = RefreshToken.for_user(account)

        return Response({
            'response': "Registration Successful!",
            'username': account.username,
            'email': account.email,
            'token': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)

    # Return validation errors with 400
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

