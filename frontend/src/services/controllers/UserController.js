import { GenericController } from './GenericController'
import { UserSerializer } from '../serializers/UserSerializer'

class UserController extends GenericController {

    static CriarUsuario (params) {
        const user = UserSerializer.SerializeUser(params)

        return GenericController.Post('/users/', user)
    }
}

export { UserController }