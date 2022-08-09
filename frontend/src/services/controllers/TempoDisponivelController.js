import { GenericController } from './GenericController'
import { GenericSerializer } from '../serializers/GenericSerializer'

class TempoDisponivelController extends GenericController {
    
    static async CriarTempoDisponivel (params) {
        const result = await GenericController.Post("/TempoDisponivel/", params, true)
        //return GenericSerializer.SerializeListToSelectField(result, "nome", "id_dia_semana")
        return result
    }
}


export {TempoDisponivelController}