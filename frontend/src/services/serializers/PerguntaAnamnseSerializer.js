import { GenericSerializer } from './GenericSerializer'

class PerguntaAnamnseSerializer extends GenericSerializer {

    static SerializePerguntaAnamnese(params) {
        return {
            idPerguntaAnamnese: params.id_pergunta_anamnese,
            texto: params.texto,
            tipo: params.tipo,
            campoAnamneseCorrespondente: params.campo_anamnese_correspondente,
            dependeDe: params.depende_de
        }
    }

    static SerializeListaPerguntaAnamnese(lista){
        let listResult = []
        lista.forEach(element => {
            let perguntaSerializada = this.SerializePerguntaAnamnese(element)
            listResult.push(perguntaSerializada)
        })
        return listResult
    }
    
    static DeserializeLogin(params) {
        return {
            id_pergunta_anamnese: params.idPerguntaAnamnese,
            texto: params.texto,
            tipo: params.tipo,
            campo_anamnese_correspondente: params.campoAnamneseCorrespondente,
            depende_de: params.dependeDe
        }
    }
}

export { PerguntaAnamnseSerializer }