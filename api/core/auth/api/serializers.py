from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from anamnese.models import Anamnese
from TempoDisponivel.models import TempoDisponivel
# from anamnese.models import PerguntasAnamnese, OpcaoRespostaAnamnese, Anamnese 
# from users.api.serializers import UserSerializer
class AuthSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(AuthSerializer, cls).get_token(user)

        # Add custom claims
        token['id_user'] = user.id
        token['email'] = user.email
        token['possui_anamnese'] = len(Anamnese.objects.filter(usuario_id = user.id)) > 0
        token['possui_tempo_disponivel_cadastrado'] =  len(TempoDisponivel.objects.filter(id_usuario = user.id)) > 0
        #adicionar função para buscar se tem anamnese
        #adicionar função para buscar se já adicionouo tempo disponivel
        return token

