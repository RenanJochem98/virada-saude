import * as storage from '../storage'

export const ActionSetIdUser = ({ commit }, payload) => {
  storage.setLocalAccessToken(payload)
  commit('SetIdUser', payload)
}

  