export default {
  state: {
    sahm: []
  },
  getters: {
    getSahm: state => state.sahm
  },
  mutations: {
    changeSahm(state, payload) {
      state.sahm = payload;
    }
  },
  actions: {
    setSahm: ({ commit }, payload) => {
      commit("changeSahm", payload);
    }
  }
};
