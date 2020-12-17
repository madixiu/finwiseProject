<template>
  <!-- begin:: Aside -->
  <div
    class="aside aside-left aside-fixed d-flex flex-column flex-row-auto"
    id="kt_aside"
    ref="kt_aside"
    @mouseover="mouseEnter"
    @mouseleave="mouseLeave"
  >
    <!-- begin:: Aside -->
    <KTBrand></KTBrand>
    <!-- end:: Aside -->

    <!-- begin:: Aside Menu -->
    <div
      class="aside-menu-wrapper flex-column-fluid"
      id="kt_aside_menu_wrapper"
    >
      <div
        ref="kt_aside_menu"
        id="kt_aside_menu"
        class="aside-menu my-4"
        data-menu-vertical="1"
        data-menu-dropdown-timeout="500"
        v-bind:class="asideMenuClass"
      >
        <!-- example static menu here -->
        <perfect-scrollbar
          class="aside-menu scroll"
          style="max-height: 90vh; position: relative;"
        >
          <!-- <KTMenu v-if="menuItemsList == '/market/dashboard'"></KTMenu> -->
          <KTMenu v-if="AsideState1"></KTMenu>
          <!-- <KTMenu2 v-if="menuItemsList == '/builder'"></KTMenu2> -->
          <KTMenu2 v-if="AsideState2"></KTMenu2>
          <KTMenu3 v-if="AsideState3"></KTMenu3>
        </perfect-scrollbar>
      </div>
    </div>
  </div>
  <!-- end:: Aside -->
</template>

<script>
import { mapGetters } from "vuex";
import KTBrand from "@/view/layout/brand/Brand.vue";

import KTLayoutAside from "@/assets/js/layout/base/aside.js";
import KTLayoutAsideMenu from "@/assets/js/layout/base/aside-menu.js";
import KTMenu from "@/view/layout/aside/Menu.vue";
import KTMenu2 from "@/view/layout/aside/Menu2.vue";
import KTMenu3 from "@/view/layout/aside/Menu3.vue";
export default {
  name: "KTAside",
  data() {
    return {
      insideTm: 0,
      outsideTm: 0,
      saham: [
        "StockMarket",
        "Dashboard",
        // "marketwatch",
        "Industries",
        "IndustriesDetail",
        "Screener",
        "Fundamental",
        "TechnicalDashboard",
        "TechnicalTools",
        "TechnicalData",
        "AssemblyCalendar",
        "AssemblyDecisions",
        "AssemblyIC",
        "Taghadom",
        "Option",
        "Funds"
      ],
      kala: ["bourse", "global"],
      ticker: [
        "TickerOverall",
        "Administration",
        "Notifications",
        "StatusChange",
        "HH",
        "Board",
        "shareholders",
        "AdjustedPrices",
        "TickerFundamental",
        "TickerTechnical",
        "Sheets",
        "Monthly",
        "sahmRobot",
        "TickerRatio",
        "TickerIndustry",
        "TickerAssembly",
        "TickerAssemblyCalendar",
        "TickerAssemblyReport",
        "TickerAssemblyDPS",
        "TickerAssemblyIC",
        "sarmaye"
      ],
      AsideState1: true,
      AsideState2: false,
      AsideState3: false
    };
  },
  // props: {
  //   selectedTopBar: {
  //     type: String
  //   }
  // },
  components: {
    KTBrand,
    KTMenu,
    KTMenu2,
    KTMenu3
  },
  watch: {
    $route: "fetchRoute"
  },
  mounted() {
    this.fetchRoute();
    this.$nextTick(() => {
      // Init Aside
      KTLayoutAside.init(this.$refs["kt_aside"]);

      // Init Aside Menu
      KTLayoutAsideMenu.init(this.$refs["kt_aside_menu"]);
    });
  },
  methods: {
    fetchRoute() {
      // console.log(this.$route.path);
      // console.log(this.$route.name);
      let path = this.$route.name;
      this.AsideState1 = this.saham.includes(path);
      this.AsideState2 = this.kala.includes(path);
      this.AsideState3 = this.ticker.includes(path);
      // if (!this.AsideState1 && !this.AsideState2) {
      //   this.AsideState3 = true;
      // } else {
      //   this.AsideState3 = false;
      // }
    },
    /**
     * Use for fixed left aside menu, to show menu on mouseenter event.
     */
    mouseEnter() {
      if (this.layoutConfig("aside.self.minimize.hoverable")) {
        // check if the left aside menu is fixed
        if (document.body.classList.contains("aside-fixed")) {
          if (this.outsideTm) {
            clearTimeout(this.outsideTm);
            this.outsideTm = null;
          }

          // if the left aside menu is minimized
          if (document.body.classList.contains("aside-minimize")) {
            document.body.classList.add("aside-minimize-hover");

            // show the left aside menu
            document.body.classList.remove("aside-minimize");
          }
        }
      }
    },

    /**
     * Use for fixed left aside menu, to show menu on mouseenter event.
     */
    mouseLeave() {
      if (this.layoutConfig("aside.self.minimize.hoverable")) {
        if (document.body.classList.contains("aside-fixed")) {
          if (this.insideTm) {
            clearTimeout(this.insideTm);
            this.insideTm = null;
          }

          if (document.querySelector(".aside-menu .scroll")) {
            document.querySelector(".aside-menu .scroll").scrollTop = 0;
          }

          // if the left aside menu is expand
          if (document.body.classList.contains("aside-minimize-hover")) {
            // hide back the left aside menu
            document.body.classList.remove("aside-minimize-hover");
            document.body.classList.add("aside-minimize");
          }
        }
      }
    }
  },
  computed: {
    ...mapGetters(["layoutConfig", "getClasses"]),

    /**
     * Get extra classes for menu based on the options
     */
    asideMenuClass() {
      const classes = this.getClasses("aside_menu");
      if (typeof classes !== "undefined") {
        return classes.join(" ");
      }
      return null;
    }
  }
};
</script>
