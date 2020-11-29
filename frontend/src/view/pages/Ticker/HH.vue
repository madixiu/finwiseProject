<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <!-- <SubHeaderWidget></SubHeaderWidget> -->
      </div>
      <div class="col-xxl-12">
        <HHW :datalabels.sync="labels"></HHW>
      </div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import HHW from "@/view/pages/Ticker/TickerWidgets/‌HHWidget.vue";
import axios from "axios";
export default {
  name: "Notifications",
  components: {
    // SubHeaderWidget,
    HHW
  },
  data() {
    return {
      search: "",
      Nemad: "شستا",
      tickerfull: "تامین اجتماعی",
      labels: []
    };
  },
  mounted() {
    this.getData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "حقیقی و حقوقی" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.Nemad }]);
  },
  methods: {
    getData() {
      axios
        .get(
          // "http://localhost:8000/api/CodalNotices/" + this.$route.params.id + "/"
          "http://localhost:8000/api/HHhistoryGraph/2788/"
        )
        .then(response => {
          // console.log(response.data[0][0]);
          // this.labels = response.data[0][0];
          console.log(response.data[0]);
        });
      // this.options.labels = response.data.data[0];

      // return response.data.data;
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
