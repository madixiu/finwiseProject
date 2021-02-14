export default {
  state: {
    SearchBarListData: []
  },
  getters: {
    getSearchListData: state => state.SearchBarListData
  },
  mutations: {
    addSearchData(state, payload) {
      state.SearchBarListData = payload;
    }
  },
  actions: {
    setSearch: ({ commit }, payload) => {
      commit("addSearchData", payload);
    }
  }
};
