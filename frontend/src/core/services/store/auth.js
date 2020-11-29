import JwtService from "@/core/services/jwt.service";
export const VERIFY_AUTH = "verifyAuth";
export const VERIFY = "verifyAccessToken";
export const LOGIN = "login";
export const LOGOUT = "logout";
export const REGISTER = "register";
export const UPDATE_USER = "updateUser";
export const PURGE_AUTH = "logOut";
export const SET_AUTH = "setUser";
export const SET_ERROR = "setError";
export const SET_ACCTOKEN = "setAccessToken";
export const RENEW_TOKEN = "RenewAccessToken";
export const SET_USER_ID = "setUserID";
export const SET_AUTH_NOT_VERIFIED = "setUserNotVerified";
// const apolloClient = ApolloService.init();
export default {
  state: {
    errors: [],
    user: {},
    AccessToken: "",
    // isAuthenticated: !!JwtService.getToken()
    isAuthenticated: false
  },
  getters: {
    errors: state => state.errors,
    currentUserAccessToken: state => state.AccessToken,
    currentUser: state => state.user,
    isAuthenticated: state => state.isAuthenticated
  },
  mutations: {
    [SET_ERROR](state, error) {
      state.errors = error;
    },
    [SET_AUTH](state, user) {
      state.isAuthenticated = true;
      state.user = user;
      state.errors = {};
      // JwtService.saveToken(state.user.token);
    },
    [SET_AUTH_NOT_VERIFIED](state, user) {
      state.user = user;
      state.errors = {};
    },
    [PURGE_AUTH](state) {
      state.isAuthenticated = false;
      state.user = {};
      state.errors = {};
      JwtService.destroyToken();
    },
    [SET_ACCTOKEN](state, token) {
      // state.user.token = token;
      state.AccessToken = token;
    },
    [SET_USER_ID](state, user) {
      state.user = user;
    }
  },
  actions: {
    LOGIN: ({ commit }, payload) => {
      commit(SET_AUTH, payload);
    },
    LOGOUT: ({ commit }) => {
      commit(PURGE_AUTH);
    },
    REGISTER: ({ commit }, payload) => {
      commit(SET_AUTH_NOT_VERIFIED, payload);
    },
    SET_ERROR: ({ commit }, payload) => {
      commit(SET_ERROR, payload);
    },
    RenewAccessToken: ({ commit }, payload) => {
      commit(SET_ACCTOKEN, payload);
    },
    SET_USER: ({ commit }, payload) => {
      commit(SET_USER_ID, payload);
    }
    // VERIFY: () => {
    //   // console.log(VERIFY_ACCESS_TOKEN.toString());
    //   console.log("vuex");
    //   Vue.apolloClient
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
    //     });
    //   // commit(SET_AUTH, payload)
    //   // commit(SET_AUTH, payload);
    // },
  }
};
