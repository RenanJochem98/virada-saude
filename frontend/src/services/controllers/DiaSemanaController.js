import { GenericController } from './GenericController'
import { GenericSerializer } from '../serializers/GenericSerializer'
class DiaSemanaController extends GenericController {
    
    static async BuscarDiasSemana () {
        const result = await GenericController.Get("/DiaSemana", true)
        return GenericSerializer.SerializeListToSelectField(result, "nome", "id_dia_semana")
    }
}


export {DiaSemanaController}