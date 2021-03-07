export default {
  state: {
    sahm: [],
    Locked: true
  },
  getters: {
    getSahm: state => state.sahm,
    getLockStatus: state => state.Locked
  },
  mutations: {
    changeSahm(state, payload) {
      state.sahm = payload;
    },
    changeOptionLock(state, payload) {
      state.Locked = payload;
    }
  },
  actions: {
    setSahm: ({ commit }, payload) => {
      commit("changeSahm", payload);
    },
    setOptionStatus: ({ commit }, payload) => {
      commit("changeOptionLock", payload);
    }
  }
};
