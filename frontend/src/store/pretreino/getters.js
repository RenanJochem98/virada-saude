import * as storage from '../storage'

export const getPreTreino = ({ preTreino }) => {
  if (!preTreino) {
    preTreino = storage.getLocalPreTreino()
  }
  return preTreino
}
