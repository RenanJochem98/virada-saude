import { GenericController } from './GenericController'
import { PerguntaAnamnseSerializer } from '../serializers/PerguntaAnamnseSerializer'

class PerguntaAnamnseController extends GenericController {

    static async BuscarTodasPerguntas () {
        const perguntas = await GenericController.Get('/perguntas_anamnese/', true)
        if(perguntas.status) {
            return perguntas
        }
        return PerguntaAnamnseSerializer.SerializeListaPerguntaAnamnese(perguntas)
    }

    static async BuscarTodasPerguntasParaSelectField () {
        const perguntas = await GenericController.Get('/perguntas_anamnese/', true)
        if(perguntas.status) {
            return perguntas
        }
        return PerguntaAnamnseSerializer.SerializeListaPerguntaAnamneseParaSelectField(perguntas)
    }
}

export { PerguntaAnamnseController }