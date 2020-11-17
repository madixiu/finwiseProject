<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <NotificationsWidget></NotificationsWidget>
      </div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import NotificationsWidget from "@/view/pages/Ticker/TickerWidgets/NotificationsWidget.vue";

export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    NotificationsWidget
  },
  data() {
    return {
      search: "",
      Nemad: "",
      tickerfull: ""
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعیه های کدال" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.Nemad }]);
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
