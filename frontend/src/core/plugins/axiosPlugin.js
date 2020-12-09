import axios from "axios";
import VueAxios from "vue-axios";
export default {
  install(Vue) {
    axios.defaults.baseURL = "http://localhost:8000";
    Vue.use(VueAxios, axios);
  }
};
