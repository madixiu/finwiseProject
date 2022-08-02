import axios from "axios";
import VueAxios from "vue-axios";
export default {
  install(Vue) {
    // axios.defaults.baseURL = process.env.VUE_APP_BASE_URL_LOCAL;
    axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;

    // axios.defaults.timeout = 2000;
    // axios.defaults.headers = {
    //   "Cache-Control": "no-cache",
    //   Pragma: "no-cache",
    //   Expires: "0"
    // };
    Vue.use(VueAxios, axios);
  }
};
