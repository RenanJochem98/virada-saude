import { GenericController } from './GenericController'
import { UserSerializer } from '../serializers/UserSerializer'

class UserController extends GenericController {

    static CriarUsuario (params) {
        const user = UserSerializer.SerializeUser(params)

        return GenericController.Post('/users/', user)
    }

    static BuscarUsuario (idUser) {
        UserSerializer.SerializeUser(params)

        const user =  GenericController.Get('/users/'+idUser+"/", true)
        if(user.status) {
            return user
        } else {
            return UserSerializer.DeserializeUser(user)
        }
    }

    static async Login (email, senha) {
        const loginParams = UserSerializer.SerializeLogin(email, senha) 
        const result = await GenericController.Post('/token/', loginParams)
        if(!result.status) {
            return UserSerializer.DeserializeLogin(result)
        } else {
            return result
        }
        
    }
}

export { UserController }