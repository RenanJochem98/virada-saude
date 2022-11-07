import { GenericController } from './GenericController'
import { AnamneseSerializer } from '../serializers/AnamneseSerializer'

class AnamneseController extends GenericController {

    static async CriarAnamnese(params) {
        // const respostas = AnamneseSerializer.DeserializeAnamnese(params)
        const result = await GenericController.Post('/anamnese/', params, true)
        return result
        // if(perguntas.status) {
        //     return perguntas
        // }
        // return PerguntaAnamnseSerializer.SerializeListaPerguntaAnamnese(perguntas)

    }
}

export { AnamneseController }