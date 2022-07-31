import { api } from '../../boot/axios'
import store from '../../store'
// import { store } from "quasar/wrappers";
// import { Store } from "vuex";

class GenericController {

    constructor() {
        throw new Error('Generic Controller não pode ser instanciada.')
    }

    static mountHeaders(){
        console.log("store login", store.getters['login/getAccessToken'])
        // console.log("mountHeaders", store.dispatch('login/ActionGetAccessToken'))
        return { headers: { Authorization: 'Bearer ' + store.getters['login/getAccessToken'] } }
        // return store.getters['login/getAccessToken']
    }

    static async Get(baseUrl, needHeaders) {
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
                console.log("Erro get generic: ", err)
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
            return {
                status: err.response.status,
                mensagem: err.response.data.detail
            }
        }
    }
}

export {GenericController}