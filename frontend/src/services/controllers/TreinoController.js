import { GenericController } from './GenericController'
import { TreinoSerializer } from '../serializers/TreinoSerializer'

class TreinoController extends GenericController {
    
    constructor () {
        this.baseUrl = "/treino"
    }

    static async BuscarTreino (idUsuario, dataTreino) {
        const params = {
            id_usuario: idUsuario,
            data_treino: dataTreino
        }
        const result = await GenericController.Get("/treino", true, params)
        if(result.status) {
            return result
        }
        return TreinoSerializer.SerializeTreino(result[0])
    }

    static async BuscarProximoTreino (idUsuario) {
        const params = {
            id_usuario: idUsuario
        }
        const result = await GenericController.Get("/proximo_treino", true, params)
        if(result == null || result.length == 0 || result.status) {
            return result
        }
        return TreinoSerializer.SerializeTreino(result[0])
    }

    static async BuscarTreinosExecutados (idUsuario) {
        const params = {
            id_usuario: idUsuario
        }
        const result = await GenericController.Get("/treino_passado", true, params)
        if(result.status) {
            return result
        }
        return TreinoSerializer.SerializeListaTreino(result)
    }

    static async CancelarTreino (idTreino) {
        const result = await GenericController.Update("/treino_cancelado", idTreino, {})
        if(result.status) {
            return result
        }
        return TreinoSerializer.SerializeTreino(result)
    }
    
}


export {TreinoController}