<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-2 col-lg-3">
        <MostViewedWidget></MostViewedWidget>
      </div>
      <div class="col-xxl-2 col-lg-4">
        <Impacts></Impacts>
      </div>
      <div class="col-xxl-4 col-lg-5">
        <HighestTradeValue></HighestTradeValue>
      </div>
      <div class="col-xxl-4 col-lg-6">
        <v-tabs>
          <v-tab>تقاضا</v-tab>
          <v-tab>عرضه</v-tab>
          <v-tab-item><HighestDemand></HighestDemand></v-tab-item>
          <v-tab-item><HighestSupply></HighestSupply></v-tab-item>
        </v-tabs>
      </div>
      <!-- <div class="col-xxl-4"></div> -->
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

// import axios from "axios";
export default {
  name: "Dashboard",
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
    // this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);
  },
  methods: {
    // loadData() {
    //   this.getMostViewed().then(response => {
    //   });
    // },
    // async getMostViewed() {
    //   await axios
    //     .get("http://localhost:8000/api/tse/top5MostViewed/")
    //     .then(response3 => {

    //       this.mostViewed = response3.data;

    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
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
