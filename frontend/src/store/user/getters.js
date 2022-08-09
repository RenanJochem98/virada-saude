import * as storage from '../storage'

export const getIdUser = ({ idUser }) => {
  if (!idUser) {
    idUser = storage.getLocalIdUser()
  }
  return idUser
}
