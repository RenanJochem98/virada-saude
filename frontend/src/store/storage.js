export const getLocalAccessToken = () => localStorage.getItem('accessToken')
export const removeLocalAccessToken = () => localStorage.removeItem('accessToken')
export const setLocalAccessToken = (accessToken) => localStorage.setItem('accessToken', accessToken)

export const getLocalRefreshToken = () => localStorage.getItem('refreshToken')
export const removeLocalRefreshToken = () => localStorage.removeItem('refreshToken')
export const setLocalRefreshToken = (refreshToken) => localStorage.setItem('refreshToken', refreshToken)