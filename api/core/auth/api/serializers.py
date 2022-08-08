from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from anamnese.models import PerguntasAnamnese, OpcaoRespostaAnamnese, Anamnese 
# from users.api.serializers import UserSerializer
class AuthSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(AuthSerializer, cls).get_token(user)

        # Add custom claims
        token['id_user'] = user.id
        token['email'] = user.email
        return token

