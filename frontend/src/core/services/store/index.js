import Vue from "vue";
import Vuex from "vuex";

// import auth from "./auth.module";
import auth2 from "./auth2.module";
import htmlClass from "./htmlclass.module";
import config from "./config.module";
import breadcrumbs from "./breadcrumbs.module";
import option from "./option.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth2,
    htmlClass,
    config,
    breadcrumbs,
    option
  }
});
