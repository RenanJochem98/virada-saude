import * as storage from '../storage'

export const getPreTreino = ({ preTreino }) => {
  if (!preTreino) {
    preTreino = storage.getLocalPreTreino()
  }
  return preTreino
}

export const getTempoTreino = ({ tempoTreino }) => {
  if (!tempoTreino) {
    tempoTreino = storage.getLocalTempoTreino()
  }
  return tempoTreino
}

export const getClimaTreino = ({ climaTreino }) => {
  if (!climaTreino) {
    climaTreino = storage.getLocalClimaTreino()
  }
  return climaTreino
}
