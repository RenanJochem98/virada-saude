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
}


export {TreinoController}