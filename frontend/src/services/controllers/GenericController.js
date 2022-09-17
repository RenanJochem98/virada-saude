import { api } from '../../boot/axios'
import store from '../../store'
// import { store } from "quasar/wrappers";
// import { Store } from "vuex";

class GenericController {


    constructor() {
        throw new Error('Generic Controller não pode ser instanciada.')
    }

    static mountHeaders(){
        return { headers: { Authorization: 'Bearer ' + store.getters['login/getAccessToken'] } }
    }

    static async Get(baseUrl, needHeaders) {
        this.Get(baseUrl, needHeaders, {})
    }

    static async Get(baseUrl, needHeaders, params) {
        if(params){
            let queryParams =Object.entries(params).map(([key, value]) => `${key}=${value}`).
            join('&')

            baseUrl = baseUrl + '?' +queryParams
        }
        try {
            const result = needHeaders ? 
                    await api.get(baseUrl, this.mountHeaders()) : 
                    await api.get(baseUrl)
            return result.data
        }catch(err){
            if(err.response){
                return {
                    status: err.response.status,
                    mensagem: err.response.data.detail
                }
            } else {
                console.error("Erro get generic: ", err)
            }
            
        }
    }

    static async Post(baseUrl, data, needHeaders) {
        try {
            const result = needHeaders ? 
                await api.post(baseUrl, data, this.mountHeaders()): 
                await api.post(baseUrl, data)
            return result.data
        }catch(err){
            if(err.response){
                return {
                    status: err.response.status,
                    mensagem: err.response.data.detail
                }
            } else {
                return {
                    status: 404,
                    mensagem: "Não foi possível estabelecer conexão para realizar operação."
                }
            }
            
        }
    }
}

export {GenericController}