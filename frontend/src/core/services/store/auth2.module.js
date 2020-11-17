// import ApiService from "@/core/services/api.service";
import JwtService from "@/core/services/jwt.service";
import { LOGIN_USER, REGISTER_USER, VERIFY_USER } from "@/graphql/mutations";
// import { LOGIN_USER, REGISTER_USER } from "@/graphql/mutations";
// action types
export const VERIFY_AUTH = "verifyAuth";
export const LOGIN = "login";
export const LOGOUT = "logout";
export const REGISTER = "register";
export const UPDATE_USER = "updateUser";

// mutation types
export const PURGE_AUTH = "logOut";
export const SET_AUTH = "setUser";
export const SET_ERROR = "setError";

const state = {
  errors: null,
  user: {},
  isAuthenticated: !!JwtService.getToken()
};

const getters = {
  currentUser(state) {
    return state.user;
  },
  isAuthenticated(state) {
    return state.isAuthenticated;
  }
};

const actions = {
  [LOGIN](context, credentials) {
    return new Promise(resolve => {
      this.$apollo
        .mutate({
          mutations: LOGIN_USER,
          variables: {
            phoneNumber: credentials.phoneNumber,
            password: credentials.password
          }
        })
        .then(data => {
          console.log(data);
          context.commit(SET_AUTH, data);
          resolve(data);
        })
        .catch(error => {
          console.log(error);
          console.log(credentials.phoneNumber + " " + credentials.password);
          context.commit(SET_ERROR, error.data.errors);
        });
      //   ApiService.post("login", credentials)
      //     .then(({ data }) => {
      //       context.commit(SET_AUTH, data);
      //       resolve(data);
      //     })
      //     .catch(({ response }) => {
      //       context.commit(SET_ERROR, response.data.errors);
      //     });
    });
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH);
  },
  [REGISTER](context, credentials) {
    return new Promise((resolve, reject) => {
      this.$apollo
        .mutate({
          mutations: REGISTER_USER,
          variables: {
            email: credentials.email,
            password1: credentials.password,
            password2: credentials.password,
            username: credentials.username,
            phoneNumber: credentials.phoneNumber,
            firstName: credentials.firstName,
            lastName: credentials.lastName
          }
        })
        .then(data => {
          console.log(data);
          context.commit(SET_AUTH, data);
          resolve(data);
        })

        .catch(error => {
          console.log(error);
          console.log(credentials.phoneNumber + " " + credentials.username);
          context.commit(SET_ERROR, error.data.errors);
          reject(error);
        });
      // ApiService.post("users", { user: credentials })
      //   .then(({ data }) => {
      //     context.commit(SET_AUTH, data);
      //     resolve(data);
      //   })
      //   .catch(({ response }) => {
      //     context.commit(SET_ERROR, response.data.errors);
      //     reject(response);
      //   });
    });
  },
  [VERIFY_AUTH](context) {
    // if (JwtService.getToken()) {
    let s = true;
    if (s) {
      console.log("Local Token");
    }
      // console.log(JwtService.getToken());
    //   this.$apollo
    //     .mutate({
    //       mutations: VERIFY_USER,
    //       variables: {
    //         token: "hereis"
    //       }
    //     })
    //     .then(data => {
    //       console.log(data);
    //       context.commit(SET_AUTH, data);
    //     })
    //     .catch(error => {
    //       context.commit(SET_ERROR, error);
    //     });
    // } else {
    //   context.commit(PURGE_AUTH);
    // }
    // ApiService.setHeader();
    //   ApiService.get("verify")
    //     .then(({ data }) => {
    //       context.commit(SET_AUTH, data);
    //     })
    //     .catch(({ response }) => {
    //       context.commit(SET_ERROR, response.data.errors);
    //     });
    // } else {
    //   context.commit(PURGE_AUTH);
    // }
  },
  [UPDATE_USER](context, payload) {
    const { email, username, password, image, bio } = payload;
    const user = { email, username, bio, image };
    if (password) {
      user.password = password;
    }

    return 
    // ApiService.put("user", user).then(({ data }) => {
    //   context.commit(SET_AUTH, data);
    //   return data;
    // });
  }
};

const mutations = {
  [SET_ERROR](state, error) {
    state.errors = error;
  },
  [SET_AUTH](state, user) {
    state.isAuthenticated = true;
    state.user = user;
    state.errors = {};
    JwtService.saveToken(state.user.token);
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false;
    state.user = {};
    state.errors = {};
    JwtService.destroyToken();
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
