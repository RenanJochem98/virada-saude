import { GenericController } from './GenericController'
import { PerguntaFeedbackSerializer } from '../serializers/PerguntaFeedbackSerializer'

class PerguntasFeedbackController extends GenericController {

    static async BuscarTodasPerguntas () {
        const perguntas = await GenericController.Get('/pergunta_feedback/', true)
        if(perguntas.status) {
            return perguntas
        }
        return PerguntaFeedbackSerializer.SerializeListaPerguntaFeedback(perguntas)
    }

    static async BuscarTodasPerguntasParaSelectField () {
        const perguntas = await GenericController.Get('/pergunta_feedback/', true)
        if(perguntas.status) {
            return perguntas
        }
        return PerguntaFeedbackSerializer.SerializeListaPerguntaFeedbackParaSelectField(perguntas)
    }
}

export { PerguntasFeedbackController }