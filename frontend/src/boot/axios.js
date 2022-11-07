import { boot } from "quasar/wrappers";
import axios from "axios";
import { Notify, Loading } from 'quasar'
// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create({ baseURL: process.env.URL_API });
function showCustom () {
  Notify.create({
    type: 'warning',
    message: 'Processando requisição',
    spinner: true,
    timeout: 1000
  })
}
api.interceptors.request.use(function (request) {
  showCustom()
  Loading.show({
    message: '<b>Processando requisição</b>',
    html: true,
    backgroundColor: 'grey-10'
  })
  return request
}, function (error) {
  Loading.hide()
  return Promise.reject(error)
})

api.interceptors.response.use(function (response) {
  Loading.hide()
  return response
}, function (error) {
  Loading.hide()
  return Promise.reject(error)
})

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };
