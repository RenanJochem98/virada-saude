import * as storage from '../storage'

export const ActionSetPreTreino = ({ commit }, payload) => {
  storage.setLocalPreTreino(payload)
  commit('SetPreTreino', payload)
}

export const ActionSetTempoTreino = ({ commit }, payload) => {
  storage.setLocalTempoTreino(payload)
  commit('SetTempoTreino', payload)
}

export const ActionSetClimaTreino = ({ commit }, payload) => {
  storage.setLocalClimaTreino(payload)
  commit('SetClimaTreino', payload)
}

  