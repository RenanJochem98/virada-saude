import { api } from '../../boot/axios'

class GenericController {

    constructor() {
        throw new Error('Generic Controller não pode ser instanciada.')
    }

    static async Get(baseUrl, needHeaders) {
        const result = needHeaders ? 
                await api.get(baseUrl, this.mountHeaders()) : 
                await api.get(baseUrl)

        return result.data
    }

    static async Post(baseUrl, data, needHeaders) {
        try {
            const result = needHeaders ? 
                await api.post(baseUrl, data, this.mountHeaders()): 
                await api.post(baseUrl, data)
            return result.data
        }catch(err){
            return {
                status: err.response.status,
                mensagem: err.response.data.detail
            }
        }
    }
}

export {GenericController}