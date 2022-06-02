import { GenericController } from './GenericController'
import { GenericSerializer } from '../serializers/GenericSerializer'
class EmpresaController extends GenericController {
    
    constructor () {
        this.baseUrl = "/empresa"
    }

    static async BuscarEmpresas () {
        const result = await GenericController.Get("/empresa", false)
        return GenericSerializer.SerializeListToSelectField(result, "nome", "idempresa")
    }
}


export {EmpresaController}