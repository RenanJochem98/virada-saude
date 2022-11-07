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

    static DeserializeUser(params) {
        return {
            idUser: params.id,
            firstName: params.first_name,
            lastName: params.last_name,
            email: params.email,
            password: params.password,
            empresa: params.idEmpresa
        }
    }
    
    static SerializeLogin(pEmail, senha) {
        return {
            email: pEmail,
            password: senha
        }
    }

    static DeserializeLogin(loginResult) {
        return {
            accessToken: loginResult.access,
            refreshToken: loginResult.refresh
        }
    }
}

export { UserSerializer }