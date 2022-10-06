import { GenericSerializer } from './GenericSerializer'

class PerguntaFeedbackSerializer extends GenericSerializer {

    static SerializePerguntaFeedback(params) {
        return {
            idPerguntaFeedback: params.id_pergunta_feedback,
            texto: params.texto_pergunta,
            dependeDe: params.depende_de == null ? null : this.SerializarOpcaoResposta(params.depende_de)
        }
    }

    static SerializeListaPerguntaFeedback(lista){
        let listResult = []
        lista.forEach(element => {
            let perguntaSerializada = this.SerializePerguntaFeedback(element)
            listResult.push(perguntaSerializada)
        })
        return listResult
    }

    static SerializePerguntaFeedbackParaSelectField(params) {
        return {
            idPerguntaFeedback: params.id_pergunta_feedback,
            texto: params.texto_pergunta,
            dependeDe: params.depende_de == null ? null : this.SerializarOpcaoResposta(params.depende_de),
            opcoesResposta: this.SerializeListToSelectField(params.opcoes, "texto", "id_opcao_resposta_feedback")
        }
    }

    static SerializeListaPerguntaFeedbackParaSelectField(lista){
        let listResult = []
        lista.forEach(element => {
            let perguntaSerializada = this.SerializePerguntaFeedbackParaSelectField(element)
            listResult.push(perguntaSerializada)
        })
        return listResult
    }
    
    

    static SerializarOpcaoResposta(params) {
        return {
            idOpcaoRespostaFeedback: params.id_opcao_resposta_feedback,
            idPerguntaFeedback: params.id_pergunta_feedback,
            texto: params.texto
        }
    }
}

export { PerguntaFeedbackSerializer }