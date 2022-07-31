import { GenericController } from './GenericController'
import { PerguntaAnamnseSerializer } from '../serializers/PerguntaAnamnseSerializer'

class PerguntaAnamnseController extends GenericController {

    static async BuscarTodasPerguntas () {
        const perguntas = await GenericController.Get('/perguntas_anamnese/', true)
        return PerguntaAnamnseSerializer.SerializeListaPerguntaAnamnese(perguntas)
    }

    static async BuscarTodasPerguntasParaSelectField () {
        const perguntas = await BuscarTodasPerguntas()
        return PerguntaAnamnseSerializer.SerializeListToSelectField(perguntas, "idPerguntaAnamnese", "texto")
    }

    // static CriarUsuario (params) {
    //     const user = UserSerializer.SerializeUser(params)

    //     return GenericController.Post('/users/', user)
    // }

    // static async Login (email, senha) {
    //     const loginParams = UserSerializer.SerializeLogin(email, senha) 
    //     const result = await GenericController.Post('/token/', loginParams)
    //     if(!result.status) {
    //         return UserSerializer.DeserializeLogin(result)
    //     } else {
    //         return result
    //     }
        
    // }
}

export { PerguntaAnamnseController }