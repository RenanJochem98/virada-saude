import { GenericController } from './GenericController'
import { TempoDisponivelSerializer } from '../serializers/TempoDisponivelSerializer'

class TempoDisponivelController extends GenericController {
    
    StaticUrl = "/TempoDisponivel/"

    static async BuscarTempoDisponivel(paramsBusca) {
        const result = await GenericController.Get("/TempoDisponivel/", true, paramsBusca)
        if(result.status) {
            return result
        }
        return TempoDisponivelSerializer.SerializeListaTempoDisponivel(result)
    }

    static async CriarTempoDisponivel (params) {
        const result = await GenericController.Post("/TempoDisponivel/", params, true)
        //return GenericSerializer.SerializeListToSelectField(result, "nome", "id_dia_semana")
        return result
    }
}


export {TempoDisponivelController}