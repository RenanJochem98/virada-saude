import * as storage from '../storage'

export const getAccessToken = ({ accessToken }) => {
  if (!accessToken) {
    accessToken = storage.getLocalAccessToken()
  }
  return accessToken
}

export const getRefreshToken = ({ refreshToken }) => {
    if (!refreshToken) {
      refreshToken = storage.getLocalRefreshToken()
    }
    return refreshToken
  }
