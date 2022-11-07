import { GenericSerializer } from './GenericSerializer'

class TempoDisponivelSerializer  extends GenericSerializer {

    static SerializeTempoDisponivel(params) {
        return {
            idTempoDisponivel: params.id_tempo_disponivel,
            idDiaSemana: {
                id: params.id_dia_semana.id_dia_semana,
                nome: params.id_dia_semana.nome
            },
            idUsuario: params.id_usuario,
            periodoDisponivel: params.periodo_disponivel
        }
    }

    static SerializeListaTempoDisponivel(lista){
        let listResult = []
        lista.forEach(element => {
            let tempoSerializada = this.SerializeTempoDisponivel(element)
            listResult.push(tempoSerializada)
        })
        return listResult
    }

    static DeserializeTempoDisponivel(params) {
        return {
            id_tempo_disponivel: params.idTempoDisponivel,
            id_dia_semana: params.idDiaSemana,
            id_usuario: params.idUsuario,
            periodo_disponivel: params.periodoDisponivel
        }
    }
}

export { TempoDisponivelSerializer }