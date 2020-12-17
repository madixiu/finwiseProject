<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <BoardCeoWidget :notices="notice" :deposits="deposit"></BoardCeoWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import BoardCeoWidget from "@/view/pages/Ticker/TickerWidgets/BoardCeoWidget.vue";
// import axios from "axios";
export default {
  name: "BoardView",
  components: {
    SubHeaderWidget,
    BoardCeoWidget
  },
  data() {
    return {
      subheaders: [],
      notice: [],
      deposit: []
    };
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات هیيت مدیره" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
      // console.log(this.notices);
    }
  },
  methods: {
    loadData() {
      this.getOne().then(response => {
        console.log(response);
        //add this to package.json in developement
        //         "eslintConfig": {
        //     "rules": {
        //       "no-console": "off",
        //       "no-unused-vars": "off"
        //     }
        // },
        this.getTwo().then(response => {
          console.log(response);
          this.getThree().then(function() {
            console.log("ChainDone");
          });
        });
      });
    },
    async getTwo() {
      await this.axios
        .get("/api/CurrentBoard/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getThree() {
      await this.axios
        .get("/api/CurrentCeo/" + this.$route.params.id + "/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.deposit = response3.data;
          // console.log(response3.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/SubHeaderW/" + this.$route.params.id + "/")
        .then(response1 => {
          // console.log("firstDone");
          this.subheaders = response1.data[0];
          // console.log(response1.data);
        })
        .catch(error => {
          // console.log("GetOneCatch");
          console.log(error);
        });
    }
  }
};
</script>
