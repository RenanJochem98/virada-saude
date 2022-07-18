import * as storage from '../storage'

export const ActionSetAccessToken = ({ commit }, payload) => {
  storage.setLocalAccessToken(payload)
  commit('SetAccessToken', payload)
}

export const ActionSetRefreshToken = ({ commit }, payload) => {
    storage.setLocalRefreshToken(payload)
    commit('SetRefreshToken', payload)
}

export const ActionLogout = ({ dispatch }) => {
    dispatch('ActionSetToken', '')
    dispatch('ActionSetRefreshToken', '')
  
    storage.removeLocalAccessToken()
    storage.removeLocalRefreshToken()
}
  