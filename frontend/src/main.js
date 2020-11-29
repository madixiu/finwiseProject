import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "@/core/services/store";
// import JwtService from "@/core/services/jwt.service";
// import ApiService from "@/core/services/api.service";
// import MockService from "@/core/mock/mock.service";
// import { VERIFY_AUTH } from "@/core/services/store/auth.module";
// import { PURGE_AUTH, RENEW_TOKEN } from "@/core/services/store/auth";
// import { VERIFY_ACCESS_TOKEN, REFRESH_ACCESS_TOKEN } from "@/graphql/mutations";
// import { RESET_LAYOUT_CONFIG } from "@/core/services/store/config.module";
// apollo imports for graphql
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import { setContext } from "apollo-link-context";
import VueApollo from "vue-apollo";
// vxe-table imports
import "./core/plugins/utils";
import "./core/plugins/table";
// import VXETable from "vxe-table";
// import "vxe-table/lib/style.css";
// import XEUtils from "xe-utils";

// import { VERIFY } from "@/core/services/store/auth";
// -------------------------
// import ApolloService from "@/core/services/apollo.service";
//vxe-table usage
// Vue.use(VXETable);
// Vue.use(XEUtils);

// HTTP connection to the API graphql/apollo
const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: "http://localhost:8000/graphql"
});
const authLink = setContext((_, { headers }) => {
  if (store.getters.currentUserAccessToken){
    var token = store.getters.currentUserAccessToken;
    console.log(store.getters.currentUserAccessToken);
  }
 
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      // authorization: token ? `Bearer ${token}` : ""
      Authorization: token ? `JWT ${token}` : ""
    }
  };
});
// Cache implementation graphql/apollo
const cache = new InMemoryCache();

// Create the apollo client graphql/apollo
const apolloClient = new ApolloClient({
  // link: httpLink,
  link: authLink.concat(httpLink),
  cache
});
// using apollo/graphql
Vue.use(VueApollo);
//-------------------------------

// The provider holds the Apollo client instances that can then be used by all the child components
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
  // loadingKey to ‘loading’ so that we can easily display a loading indicator in the UI
  // defaultOptions: {
  //   $loadingKey: "loading"
  // }
});
// const apolloProvider = ApolloService.init();
Vue.config.productionTip = false;

// Global 3rd party plugins
import "popper.js";
import "tooltip.js";
import PerfectScrollbar from "perfect-scrollbar";
window.PerfectScrollbar = PerfectScrollbar;
import ClipboardJS from "clipboard";
window.ClipboardJS = ClipboardJS;

// Vue 3rd party plugins
import i18n from "@/core/plugins/vue-i18n";
import vuetify from "@/core/plugins/vuetify";
import "@/core/plugins/portal-vue";
import "@/core/plugins/bootstrap-vue";
import "@/core/plugins/perfect-scrollbar";
import "@/core/plugins/highlight-js";
import "@/core/plugins/inline-svg";
import "@/core/plugins/apexcharts";
import "@/core/plugins/metronic";
import "@mdi/font/css/materialdesignicons.css";

// API service init
// ApiService.init();

// Remove this to disable mock API
// MockService.init();

//crypto JS//
import VueCryptojs from "vue-cryptojs";

Vue.use(VueCryptojs);

// router.beforeEach((to, from, next) => {

// if (
//   to.name !== "login" &&
//   !store.getters.isAuthenticated &&
//   !JwtService.getToken()
// ) {
//   next({ name: "login" });
//   console.log("nothing");
// } else if (JwtService.getToken() && !store.getters.isAuthenticated) {
//   console.log("here1");
//   console.log(!!store.getters.currentUser.length);
//   let hasUser = !!store.getters.currentUser.length
//   if (hasUser) {
//     console.log("here1");
//     // var LoginData;
//     apolloClient
//       .mutate({
//         mutation: VERIFY_ACCESS_TOKEN,
//         variables: {
//           token: store.getters.currentUser.token
//         }
//       })
//       .then(data => {
//         console.log(data);
//         let LoginData = data.data.verifyToken;
//         console.log(LoginData.success);
//         if (LoginData.success) {
//           next();
//         } else if (LoginData == false) {
//           let Rtoken = Vue.CryptoJS.AES.decrypt(
//             JwtService.getToken(),
//             "key"
//           ).toString(Vue.CryptoJS.enc.Utf8);
//           apolloClient
//             .mutate({
//               mutation: REFRESH_ACCESS_TOKEN,
//               variables: {
//                 token: Rtoken
//               }
//             })
//             .then(data => {
//               console.log(data);
//               if ( !data.data.errors) {
//                 let LoginData = data.data.verifyToken;
//                 console.log(LoginData.success);
//                 if (LoginData.success) {
//                   // store new acc token to vuex
//                   store.dispatch("RenewAccessToken");
//                   next();
//                 } else {
//                   store.dispatch("LOGOUT");
//                   next({ name: "login" });
//                 }
//               }else {
//                 console.log(LoginData.errors.nonFieldErrors[0].message);
//               }

//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       })
//       .catch(error => {
//         console.log(error);
//       });
//   } else {
//     console.log("else");
//     next({ name: "login" });
//     return;

//   }
// }

// console.log(to.name);
// console.log(!store.getters.isAuthenticated);
// console.log(!JwtService.getToken());
// if (JwtService.getToken()) {
//   let Rtoken = Vue.CryptoJS.AES.decrypt(
//     JwtService.getToken(),
//     "key"
//   ).toString(Vue.CryptoJS.enc.Utf8);
//   // let Atoken = Vue.CryptoJS.AES.encrypt(store.getters.currentUserAccessToken, JwtService.getToken() ).toString();
//   console.log(Rtoken);
//   console.log("ficj");
//   if (store.getters.isAuthenticated) {
//     let LoginData;
//     apolloClient
//       .mutate({
//         mutation: VERIFY_ACCESS_TOKEN,
//         variables: {
//           token: store.getters.currentUser.token
//         }
//       })
//       .then(data => {
//         LoginData = data.data.verifyToken;
//         console.log(LoginData.success);
//       });
//     if (LoginData.success) {
//       next();
//     } else if (LoginData == false) {
//       apolloClient
//         .mutate({
//           mutation: REFRESH_ACCESS_TOKEN,
//           variables: {
//             token: Rtoken
//           }
//         })
//         .then(data => {
//           let LoginData = data.data.verifyToken;
//           console.log(LoginData.success);
//           if (LoginData.success) {
//             // store new acc token to vuex
//             store.dispatch("RenewAccessToken");
//             next();
//           } else {
//             store.dispatch("LOGOUT");
//             next();
//           }
//         });
//     }
//     // let enc = this.Cryptojs.AES.encrypt(LoginData.success, "key").toString();
//     // console.log(enc);
//   }
// } else {
//   store.dispatch("LOGOUT");
//   next();

// }
// Promise.all(
//   apolloClient
//     .mutate({
//       mutation: VERIFY_ACCESS_TOKEN,
//       variables: {
//         token:
//           "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjA5Mzg2ODg2NjE2IiwiZXhwIjoxNjA1OTQ5MDAwLCJvcmlnSWF0IjoxNjA1OTQ4MzQwfQ.eeW-t3wNG0eSuaoTiZEVqNdrdfY46yK_CT7vx7vQrwM"
//       }
//     })
//     .then(data => {
//       let LoginData = data.data.verifyToken;
//       console.log(LoginData.success);
//       // let enc = this.Cryptojs.AES.encrypt(LoginData.success, "key").toString();
//       // console.log(enc);
//     }),
//   [store.dispatch(VERIFY)]
// ).then(next);

// reset config to initial state
// store.dispatch(RESET_LAYOUT_CONFIG);
//   next();
//   router.push({ name: "dashboard" });
//   // Scroll page to top on every route change
//   setTimeout(() => {
//     window.scrollTo(0, 0);
//   }, 100);
// });

new Vue({
  VueCryptojs,
  router,
  store,
  i18n,
  vuetify,
  // injecting apolloProvider here // eslint-disable-next-line
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
