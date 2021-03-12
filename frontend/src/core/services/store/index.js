import Vue from "vue";
import Vuex from "vuex";

// import auth from "./auth.module";
import htmlClass from "./htmlclass.module";
import config from "./config.module";
import breadcrumbs from "./breadcrumbs.module";
import option from "./option.module";
import marketwatch from "./marketwatch.module";
import auth from "./auth";
import search from "./search.module";
import profile from "./profile.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    htmlClass,
    config,
    breadcrumbs,
    option,
    marketwatch,
    search,
    profile
  }
});
