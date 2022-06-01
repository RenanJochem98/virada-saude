import { GenericService } from '../services/GenericService'

class EmpresaService extends GenericService {
    
    constructor () {
        this.baseUrl = "/empresa"
    }

    static async BuscarEmpresas () {
        const result = await GenericService.Get("/empresa", false)
        let returnResult = []
        result.forEach(element => {
            returnResult.push({label: element.nome, value: element.idempresa})
        })
        return returnResult
    }
}


export {EmpresaService}