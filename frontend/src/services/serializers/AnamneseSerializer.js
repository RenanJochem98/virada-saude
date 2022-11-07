import { GenericSerializer } from './GenericSerializer'

class AnamneseSerializer extends GenericSerializer {

    static DeserializeAnamnese(params) {
        return {
            usuario: params.idPerguntaAnamnese,
            pratica_corrida: params.praticaCorrida,
            atividade_fisica: params.atividadeFisica,
            dieta: params.dieta
        }
    }
}

export { AnamneseSerializer }