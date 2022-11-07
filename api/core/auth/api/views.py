from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializers import AuthSerializer

class AuthViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthSerializer
    
