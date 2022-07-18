import { GenericSerializer } from './GenericSerializer'

class UserSerializer extends GenericSerializer {

    static SerializeUser(params) {
        return {
            first_name: params.firstName,
            last_name: params.lastName,
            email: params.email,
            password: params.password,
            empresa: params.idEmpresa
        }
    }
}

export { UserSerializer }