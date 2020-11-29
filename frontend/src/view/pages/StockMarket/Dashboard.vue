<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-2">
        <MostViewedWidget></MostViewedWidget>
      </div>
      <div class="col-xxl-2">
        <Impacts></Impacts>
      </div>
      <div class="col-xxl-4"><HighestTradeValue></HighestTradeValue></div>
      <div class="col-xxl-4">
        <v-tabs>
          <v-tab>عرضه</v-tab>
          <v-tab>تقاضا</v-tab>
          <v-tab-item><HighestDemand></HighestDemand></v-tab-item>
          <v-tab-item><HighestSupply></HighestSupply></v-tab-item>
        </v-tabs>
      </div>
      <div class="col-xxl-4"></div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import MostViewedWidget from "@/view/pages/StockMarket/StockMarketWidgets/MostViewed.vue";
import HighestTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/HighestTradeValues.vue";
import HighestDemand from "@/view/pages/StockMarket/StockMarketWidgets/HighestDemand.vue";
import HighestSupply from "@/view/pages/StockMarket/StockMarketWidgets/HighestSupply.vue";
import Impacts from "@/view/pages/StockMarket/StockMarketWidgets/ImpactOnIndex.vue";
import axios from "axios";
export default {
  name: "dashboard",
  components: {
    MostViewedWidget,
    Impacts,
    HighestTradeValue,
    HighestDemand,
    HighestSupply
  },
  data() {
    return {
      mostViewed: []
    };
  },
  mounted() {
    this.loadData3();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);
  },
  methods: {
    loadData3() {
      this.getMostViewed().then(response => {
        console.log(response);
        //add this to package.json in developement
        //         "eslintConfig": {
        //     "rules": {
        //       "no-console": "off",
        //       "no-unused-vars": "off"
        //     }
        // },
        // this.getOne().then(response2 => {
        //   console.log(response2);
        //   this.getTwo().then(function() {});
        //   // console.log("ChainDone");
        // });
      });
    },
    async getMostViewed() {
      await axios
        .get("http://localhost:8000/api/tse/top5MostViewed/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.mostViewed = response3.data;
          // console.log("GetTwoStart:");
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    setActiveTab1(event) {
      this.tabIndex = this.setActiveTab(event);
    },
    setActiveTab2(event) {
      this.tabIndex2 = this.setActiveTab(event);
    },
    /**
     * Set current active on click
     * @param event
     */
    setActiveTab(event) {
      // get all tab links
      const tab = event.target.closest('[role="tablist"]');
      const links = tab.querySelectorAll(".nav-link");
      // remove active tab links
      for (let i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
      }

      // set current active tab
      event.target.classList.add("active");

      // set clicked tab index to bootstrap tab
      return parseInt(event.target.getAttribute("data-tab"));
    }
  }
};
</script>
