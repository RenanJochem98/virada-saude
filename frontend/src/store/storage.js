export const clearLocalStorage = () => localStorage.clear()

export const getLocalAccessToken = () => localStorage.getItem('accessToken')
export const removeLocalAccessToken = () => localStorage.removeItem('accessToken')
export const setLocalAccessToken = (accessToken) => localStorage.setItem('accessToken', accessToken)

export const getLocalRefreshToken = () => localStorage.getItem('refreshToken')
export const removeLocalRefreshToken = () => localStorage.removeItem('refreshToken')
export const setLocalRefreshToken = (refreshToken) => localStorage.setItem('refreshToken', refreshToken)

export const getLocalIdUser = () => localStorage.getItem('idUser')
export const removeLocalIdUser = () => localStorage.removeItem('idUser')
export const setLocalIdUser = (idUser) => localStorage.setItem('idUser', idUser)

export const getLocalPreTreino = () => localStorage.getItem('preTreino')
export const removeLocalPreTreino = () => localStorage.removeItem('preTreino')
export const setLocalPreTreino = (preTreino) => localStorage.setItem('preTreino', preTreino)

export const getLocalClimaTreino = () => localStorage.getItem('climaTreino')
export const removeLocalClimaTreino = () => localStorage.removeItem('climaTreino')
export const setLocalClimaTreino = (climaTreino) => localStorage.setItem('climaTreino', climaTreino)

export const getLocalTempoTreino = () => localStorage.getItem('tempoTreino')
export const removeLocalTempoTreino = () => localStorage.removeItem('tempoTreino')
export const setLocalTempoTreino = (tempoTreino) => localStorage.setItem('tempoTreino', tempoTreino)