import { GenericController } from './GenericController'
// import { AnamneseSerializer } from '../serializers/AnamneseSerializer'

class FeedbackController extends GenericController {

    static async CriarFeedback(params) {
        // const respostas = AnamneseSerializer.DeserializeAnamnese(params)
        const result = await GenericController.Post('/feedback/', params, true)
        return result
        // if(perguntas.status) {
        //     return perguntas
        // }
        // return PerguntaAnamnseSerializer.SerializeListaPerguntaAnamnese(perguntas)

    }
}

export { FeedbackController }