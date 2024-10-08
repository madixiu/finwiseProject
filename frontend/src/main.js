import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "@/core/services/store";
// import WsService from "@/core/services/websocket.service.js";
import MarqueeText from "vue-marquee-text-component";
import "core-js/stable";
// import '@mdi/font/css/materialdesignicons.css'
// import JwtService from "@/core/services/jwt.service";
// import ApiService from "@/core/services/api.service";
// import MockService from "@/core/mock/mock.service";
// import { VERIFY_AUTH } from "@/core/services/store/auth.module";
// import { RESET_LAYOUT_CONFIG } from "@/core/services/store/config.module";
//? apollo imports for graphql
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import { setContext } from "apollo-link-context";
import VueApollo from "vue-apollo";

// ag grid
// only needed if you use ag-grid enterprise features
import "ag-grid-enterprise";
import { LicenseManager } from "ag-grid-enterprise";

LicenseManager.setLicenseKey(process.env.VUE_APP_AG_GRID_LICENSE);

import "ag-grid-community/dist/styles/ag-grid.css";
// import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import "ag-grid-community/dist/styles/ag-theme-balham.css";
import "ag-grid-community/dist/styles/ag-theme-material.css";

// Adding GOOGLE ANALYTICS
// import VueGtag from "vue-gtag";
// Vue.use(VueGtag, {
//   config: { id: "G-YGH92K65WQ" }
// });
import LoadScript from "vue-plugin-load-script";

Vue.use(LoadScript);

//? importing HighChart
import Highcharts from "highcharts";

import hcMore from "highcharts/highcharts-more";
import Stock from "highcharts/modules/stock";
import HighchartsVue from "highcharts-vue";
hcMore(Highcharts);
Stock(Highcharts);
Vue.use(HighchartsVue);

// import panZoom from "vue-panzoom";

// install plugin
// Vue.use(panZoom);

import moment from "vue-jalali-moment";

// !Removed Calendar
// import PersianCalendar from "vue-persian-calendar";
import VuePersianDatetimePicker from "vue-persian-datetime-picker";
Vue.component("date-picker", VuePersianDatetimePicker);

// imported persian calendar
Vue.use(moment);
// Vue.use(PersianCalendar);

// -------------------------
// import ApolloService from "@/core/services/apollo.service";

// HTTP connection to the API graphql/apollo
const httpLink = new HttpLink({
  // You should use an absolute URL here
  // uri: "https://finwise.ir/graphql"
  uri: "http://localhost:8000/graphql"
});
const authLink = setContext((_, { headers }) => {
  if (store.getters.currentUserAccessToken) {
    var token = store.getters.currentUserAccessToken;
  }

  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
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
import "tooltip.js";
import PerfectScrollbar from "perfect-scrollbar";
window.PerfectScrollbar = PerfectScrollbar;
import ClipboardJS from "clipboard";
window.ClipboardJS = ClipboardJS;

// Vue 3rd party pluginsu
// import i18n from "@/core/plugins/vue-i18n";
import vuetify from "@/core/plugins/vuetify";
import "@/core/plugins/portal-vue";
import "@/core/plugins/bootstrap-vue";
import "@/core/plugins/perfect-scrollbar";
// import "@/core/plugins/highlight-js";
import "@/core/plugins/inline-svg";
import "@/core/plugins/apexcharts";
import "@/core/plugins/metronic";
import "@mdi/font/css/materialdesignicons.css";
import axiosPlugin from "@/core/plugins/axiosPlugin.js";

Vue.use(axiosPlugin);
// API service init
// ApiService.init();
// WsService.init();

// Remove this to disable mock API
// MockService.init();

//crypto JS//
import VueCryptojs from "vue-cryptojs";

Vue.use(VueCryptojs);

// ticker tape component
Vue.component("marquee-text", MarqueeText);
export const EventBus = new Vue();
// //? SENTRY SDK
// import * as Sentry from "@sentry/vue";
// import { Integrations } from "@sentry/tracing";

// Sentry.init({
//   Vue,
//   dsn:
//     "https://cddff09ed1bc44179d651acd6b0e4973@o880789.ingest.sentry.io/5868804",
//   integrations: [new Integrations.BrowserTracing()],

//   // Set tracesSampleRate to 1.0 to capture 100%
//   // of transactions for performance monitoring.
//   // We recommend adjusting this value in production
//   tracesSampleRate: 1.0
// });

new Vue({
  VueCryptojs,
  router,
  store,
  // i18n,
  vuetify,
  // injecting apolloProvider here // eslint-disable-next-line
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
