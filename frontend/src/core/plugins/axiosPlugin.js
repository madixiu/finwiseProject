import axios from "axios";
import VueAxios from "vue-axios";
export default {
  install(Vue) {
    axios.defaults.baseURL = "https://finwise.ir";
    // axios.defaults.baseURL = "http://localhost:8000";
    // axios.defaults.timeout = 2000;
    // axios.defaults.headers = {
    //   "Cache-Control": "no-cache",
    //   Pragma: "no-cache",
    //   Expires: "0"
    // };
    Vue.use(VueAxios, axios);
  }
};
