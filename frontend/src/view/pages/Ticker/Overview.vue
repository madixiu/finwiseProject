<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <liveWidget></liveWidget>
      </div>
      <div class="col-xxl-4">
        <FSWidget></FSWidget>
      </div>
      <div class="col-xxl-4">
        <VWidget></VWidget>
      </div>
      <div class="col-xxl-4 ">
        <PWidget></PWidget>
      </div>
      <div class="col-xxl-4">
        <ReturnWidget></ReturnWidget>
      </div>
      <div class="col-xxl-4 ">
        <DivWidget></DivWidget>
      </div>
      <div class="col-xxl-4 ">
        <MoreStatisticsWidget></MoreStatisticsWidget>
      </div>
      <div class="col-xxl-12 ">
        <AnalystWidget></AnalystWidget>
      </div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import liveWidget from "@/view/pages/Ticker/Rankers/liveWidget.vue";
import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
import AnalystWidget from "@/view/pages/Ticker/Rankers/AnalystWidget.vue";
import MoreStatisticsWidget from "@/view/pages/Ticker/Rankers/MoreInfoWidget.vue";

export default {
  name: "dashboard",
  components: {
    liveWidget,
    FSWidget,
    VWidget,
    PWidget,
    ReturnWidget,
    DivWidget,
    AnalystWidget,
    MoreStatisticsWidget
  },
  data() {
    return {
      search: "",
      Nemad: "شستا",
      tickerfull: "تامین اجتماعی"
      // prop
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.Nemad }]);
    let User = this.$route.params.id;
    console.log(User);
  },
  methods: {
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
