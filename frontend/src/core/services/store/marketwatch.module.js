export default {
  state: {
    marketWatchItems: [],
    marketWatchHeaders: [],
    marketWatchFilteredHeaders: [],
    marketWatchTypeFilterList: [],
    marketWatchIndustryFilterList: []
  },
  mutations: {
    changeMarketFilteredHeaders(state, payload) {
      state.marketWatchFilteredHeaders = payload;
    },
    changeMarketTypeFilter(state, payload) {
      state.marketWatchTypeFilterList = payload;
    },
    changeMarketIndustryFilter(state, payload) {
      state.marketWatchIndustryFilterList = payload;
    },
    changeMarketItems(state, payload) {
      state.marketWatchItems = payload;
    },
    changeMarketWatchHeaders(state, payload) {
      state.marketWatchHeaders = payload;
    }
  },
  actions: {
    setMarketFilteredHeaders: ({ commit }, payload) => {
      commit("changeMarketFilteredHeaders", payload);
    },
    setMarketTypeFilter: ({ commit }, payload) => {
      commit("changeMarketTypeFilter", payload);
    },
    setMarketIndustryFilter: ({ commit }, payload) => {
      commit("changeMarketIndustryFilter", payload);
    },
    setMarketWatchItems: ({ commit }, payload) => {
      commit("changeMarketItems", payload);
    },
    setMarketWatchHeaders: ({ commit }, payload) => {
      commit("changeMarketWatchHeaders", payload);
    }
  },
  getters: {
    getMarketFilteredHeader: state => state.marketWatchFilteredHeaders,
    getMarketItems: state => state.marketWatchItems,
    getMarketHeaders: state => state.marketWatchHeaders,
    getMarketTypeFilters: state => state.marketWatchTypeFilterList,
    getMarketIndustryFilters: state => state.marketWatchIndustryFilterList
  }
};
