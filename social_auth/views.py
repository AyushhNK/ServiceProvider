from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import google.oauth2.id_token
from google.auth.transport import requests

User = get_user_model()

class GoogleLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        access_token = request.data.get('access_token')
        if not access_token:
            return Response({'error': 'Access token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = self.authenticate_with_google(access_token)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def authenticate_with_google(self, access_token):
        try:
            idinfo = google.oauth2.id_token.verify_oauth2_token(
                access_token, requests.Request(), settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)
            email = idinfo['email']
            first_name = idinfo.get('given_name', '')
            last_name = idinfo.get('family_name', '')
            picture = idinfo.get('picture', '')
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name, 
                }
            )

            return user
        except ValueError:
            return None