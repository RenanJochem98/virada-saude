import { api } from '../boot/axios'

class GenericService {

    constructor() {
        throw new Error('Generic service não pode ser instanciada.')
    }

    static async Get(baseUrl, needHeaders) {
        const result = needHeaders ? 
                await api.get(baseUrl, this.mountHeaders()) : 
                await api.get(baseUrl)

        return result.data
    }
}

export {GenericService}