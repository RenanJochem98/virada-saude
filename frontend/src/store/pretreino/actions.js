import * as storage from '../storage'

export const ActionSetPreTreino = ({ commit }, payload) => {
  storage.setLocalPreTreino(payload)
  commit('SetPreTreino', payload)
}

  