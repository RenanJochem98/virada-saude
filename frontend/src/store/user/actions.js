import * as storage from '../storage'

export const ActionSetIdUser = ({ commit }, payload) => {
  storage.setLocalIdUser(payload)
  commit('SetIdUser', payload)
}

  