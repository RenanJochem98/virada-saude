import { store } from "quasar/wrappers";
import { createStore } from "vuex";
import login from './login'
import user from './user'
import pretreino from './pretreino'
// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default createStore({
  modules: {
    login,
    user,
    pretreino
  },

  // enable strict mode (adds overhead!)
  // for dev mode and --debug builds only
  strict: process.env.DEBUGGING,
});
// export default store(function (/* { ssrContext } */) {
//   const Store = createStore({
//     modules: {
//       login
//     },

//     // enable strict mode (adds overhead!)
//     // for dev mode and --debug builds only
//     strict: process.env.DEBUGGING,
//   });

//   return Store;
// });
