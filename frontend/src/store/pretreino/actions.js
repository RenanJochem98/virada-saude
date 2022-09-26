import * as storage from '../storage'

export const ActionSetPreTreino = ({ commit }, payload) => {
  storage.setPreTreino(payload)
  commit('SetPreTreino', payload)
}

  