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
}

export {GenericController}