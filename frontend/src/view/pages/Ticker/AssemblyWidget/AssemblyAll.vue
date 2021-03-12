<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 mb-2">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>

      <div class="col-xxl-12">
        <Wizard />
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import Wizard from "@/view/pages/Ticker/AssemblyWidget/content/Wizard.vue";

// import axios from "axios";
export default {
  // name: "Notifications",
  name: "TickerAssemblyReport",
  components: {
    SubHeaderWidget,
    Wizard
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  mounted() {
    // this.loadData2();
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "گزارش مجامع" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    },
    allowed() {
      // var flag = false;
      for (var i = 0; i < this.allowed.length; i++) {
        var obj = this.allowed[i];
        if (obj.ID == this.$route.params.id) {
          // flag = true;
        }
      }
      // if (!flag) {
      //   this.$router.push({ name: "wizard" });
      // }
    }
  },
  methods: {
    loadData() {
      // this.getAllowed().then(response => {
      //add this to package.json in developement
      //         "eslintConfig": {
      //     "rules": {
      //       "no-console": "off",
      //       "no-unused-vars": "off"
      //     }
      // },
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response2 => {
        this.getTwo();
      });
      // });
    },
    // async getAllowed() {
    //   await this.axios
    //     .get("/api/tickerallnames")
    //     .then(response3 => {
    //       this.allowed = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
    async getTwo() {
      await this.axios
        .get("/api/Alldps/" + this.$route.params.id + "/")
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
        .then(response1 => {
          this.subheaders = response1.data[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
