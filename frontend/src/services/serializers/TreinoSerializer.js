import { GenericSerializer } from './GenericSerializer'

class TreinoSerializer extends GenericSerializer {

    static SerializeTreino(params) {
        return {
            idTreino: params.id_treino,
            dataExecucaoPrevista: params.data_execucao_prevista,
            dataExecucao: params.data_execucao,
            usuario: params.usuario,
            cancelado: params.cancelado,
            exercicios: (params.exercicio == null || params.exercicio.length == 0) ? null : this.SerializeListaExercicio(params.exercicio)
        }
    }
    
    static SerializeListaTreino(lista){
        let listResult = []
        lista.forEach(element => {
            let treinoSerializado = this.SerializeTreino(element)
            listResult.push(treinoSerializado)
        })
        return listResult
    }

    static SerializeExercicio(params) {
        return {
            idExercicio: params.id_exercicio,
            tipoTreino: params.tipo_treino,
            intensidade: params.intensidade,
            porcentagemTreino: params.porcentagem_treino,
        }
    }

    static SerializeListaExercicio(lista){
        let listResult = []
        lista.forEach(element => {
            let exercicioSerializado = this.SerializeExercicio(element)
            listResult.push(exercicioSerializado)
        })
        return listResult
    }

    static SerializeListaPerguntaAnamnese(lista){
        let listResult = []
        lista.forEach(element => {
            let perguntaSerializada = this.SerializePerguntaAnamnese(element)
            listResult.push(perguntaSerializada)
        })
        return listResult
    }

    static SerializePerguntaAnamneseParaSelectField(params) {
        return {
            idPerguntaAnamnese: params.id_pergunta_anamnese,
            texto: params.texto,
            tipo: params.tipo,
            campoAnamneseCorrespondente: params.campo_anamnese_correspondente,
            dependeDe: params.depende_de == null ? null : this.SerializarOpcaoResposta(params.depende_de),
            opcoesResposta: this.SerializeListToSelectField(params.opcoes, "texto", "id_opcao_resposta_anamnese")
        }
    }

    static SerializeListaPerguntaAnamneseParaSelectField(lista){
        let listResult = []
        lista.forEach(element => {
            let perguntaSerializada = this.SerializePerguntaAnamneseParaSelectField(element)
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

    static SerializarOpcaoResposta(params) {
        return {
            idOpcaoRespostaAnamnese: params.id_opcao_resposta_anamnese,
            idPerguntaAnamnese: params.id_pergunta_anamnese,
            texto: params.texto
        }
    }
}

export { TreinoSerializer }