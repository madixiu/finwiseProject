export default {
  state: {
    LiveTickerData: null,
    TickerID: null
  },
  getters: {
    getLiveTickerData: state => state.LiveTickerData,
    getLiveTickerID: state => state.TickerID
  },
  mutations: {
    mutateLiveTickerID(state, payload) {
      state.TickerID = payload;
    },
    mutateLiveTickerData(state, payload) {
      if (state.LiveTickerData != null) state.LiveTickerData = null;

      state.LiveTickerData = payload;
    }
  },
  actions: {
    SetLiveTickerID: ({ commit }, payload) => {
      commit("mutateLiveTickerID", payload);
    },
    SetLiveTickerData: ({ commit }, payload) => {
      commit("mutateLiveTickerData", payload);
    }
  }
};
