<template>
  <!-- <div class="d-flex flex-column flex-root" v-if="isAuthenticated"> -->
  <div class="d-flex flex-column flex-root">
    <!-- begin:: Header Mobile -->
    <KTHeaderMobile></KTHeaderMobile>
    <!-- end:: Header Mobile -->

    <Loader v-if="loaderEnabled" v-bind:logo="loaderLogo"></Loader>

    <!-- begin::Body -->
    <div class="d-flex flex-row flex-column-fluid page">
      <!-- begin:: Aside Left -->
      <KTAside v-if="selectedRouteAside"></KTAside>
      <!-- end:: Aside Left -->

      <div
        id="kt_wrapper"
        class="d-flex flex-column flex-row-fluid wrapper"
        style="background-color:#f5f8fa"
      >
        <!-- begin:: Header -->
        <KTHeader></KTHeader>
        <!-- end:: Header -->
        <!-- begin:: Content -->
        <div
          id="kt_content"
          class="content d-flex flex-column flex-column-fluid"
        >
          <!-- begin:: Content Head -->
          <TickerTapeContainer v-if="TickerTapeDisplay" />
          <!-- begin:: Content Head -->
          <KTSubheader
            v-if="subheaderDisplay"
            v-bind:breadcrumbs="breadcrumbs"
            v-bind:title="pageTitle"
          />
          <!-- end:: Content Head -->

          <!-- begin:: Content Body -->
          <div class="d-flex flex-column-fluid">
            <div
              :class="{
                'container-fluid': contentFluid,
                container: !contentFluid
              }"
            >
              <transition name="fade-in-up">
                <router-view />
              </transition>
            </div>
          </div>
        </div>
        <!-- <KTFooter></KTFooter> -->
        <NewsContainer v-if="$route.name == 'Dashboard'"></NewsContainer>
      </div>
    </div>
    <KTScrollTop></KTScrollTop>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import KTAside from "@/view/layout/aside/Aside.vue";
import KTHeader from "@/view/layout/header/Header.vue";
import KTHeaderMobile from "@/view/layout/header/HeaderMobile.vue";
// import KTFooter from "@/view/layout/footer/Footer.vue";
import HtmlClass from "@/core/services/htmlclass.service";
import KTSubheader from "@/view/layout/subheader/Subheader.vue";
import KTScrollTop from "@/view/layout/extras/ScrollTop";
import Loader from "@/view/content/Loader.vue";
import {
  ADD_BODY_CLASSNAME,
  REMOVE_BODY_CLASSNAME
} from "@/core/services/store/htmlclass.module.js";
import TickerTapeContainer from "@/view/content/TickerTapeContainer.vue";
import NewsContainer from "@/view/content/NewsContainer.vue";
export default {
  name: "Layout",
  components: {
    KTAside,
    KTHeader,
    KTHeaderMobile,
    // KTFooter,
    KTSubheader,
    // KTStickyToolbar,
    KTScrollTop,
    Loader,
    TickerTapeContainer,
    NewsContainer
  },
  data() {
    return {
      selectedRouteAside: true,
      subheaderDisplay: false,
      TickerTapeDisplay: false,
      TickerTapeRoutes: ["Dashboard", "Industries"],
      BreadCrumbRoutes: [
        "TickerOverall",
        "Administration",
        "Notifications",
        "StatusChange",
        "Board",
        "shareholders",
        "AdjustedPrices",
        "TechnicalMoreInfo",
        "MonthlyAnalysis",
        "Monthly",
        "StatementAnalysis",
        "BalanceSheet",
        "IncomeStatementAnalysis",
        "IncomeStatement",
        "CashFlow",
        "IndustriesDetail",
        "TickerAssemblyReport",
        "TickerAssemblyDPSAndIC",
        "CryptoSingle",
        "SingleNonETF"
      ],
      NonAsideRoutes: [
        "marketmap",
        "marketwatch",
        "oraq",
        "shakhes",
        "robot",
        "Funds",
        "profile",
        "SocialMedia",
        "ai",
        "commodities",
        "SingleNonETF"
      ]
    };
  },
  beforeMount() {
    // show page loading
    this.$store.dispatch(ADD_BODY_CLASSNAME, "page-loading");

    // initialize html element classes
    HtmlClass.init(this.layoutConfig());
  },
  mounted() {
    this.BreadCrumbRouteCheck();
    this.AsideRouteCheck();
    // this.TickerTapeRouteCheck();
    // check if current user is authenticated
    // if (!this.isAuthenticated) {
    //   this.$router.push({ name: "login" });
    // }

    // Simulate the delay page loading
    setTimeout(() => {
      // Remove page loader after some time
      this.$store.dispatch(REMOVE_BODY_CLASSNAME, "page-loading");
    }, 5000);
  },
  watch: {
    // $route: "fetchRoute"
    $route() {
      this.AsideRouteCheck();
      // this.TickerTapeRouteCheck();
      this.BreadCrumbRouteCheck();
      // react to route changes...
    }
  },
  methods: {
    BreadCrumbRouteCheck() {
      let route = this.$route.name;
      if (
        this.BreadCrumbRoutes.includes(route) ||
        this.TickerTapeRoutes.includes(route)
      ) {
        this.$store.dispatch(ADD_BODY_CLASSNAME, "subheader-fixed");
        this.$store.dispatch(ADD_BODY_CLASSNAME, "subheader-enabled");
        if (this.BreadCrumbRoutes.includes(route)) {
          this.subheaderDisplay = true;
          this.TickerTapeDisplay = false;
        } else {
          this.TickerTapeDisplay = true;
          this.subheaderDisplay = false;
        }
      } else {
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "subheader-fixed");
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "subheader-enabled");
        this.subheaderDisplay = false;
        this.TickerTapeDisplay = false;
      }
    },
    TickerTapeRouteCheck() {
      let route = this.$route.name;

      if (this.TickerTapeRoutes.includes(route)) {
        this.TickerTapeDisplay = true;
        this.$store.dispatch(ADD_BODY_CLASSNAME, "subheader-fixed");
        this.$store.dispatch(ADD_BODY_CLASSNAME, "subheader-enabled");
      } else {
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "subheader-fixed");
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "subheader-enabled");
        this.TickerTapeDisplay = false;
      }
    },
    AsideRouteCheck() {
      let route = this.$route.name;
      if (this.NonAsideRoutes.includes(route)) {
        this.selectedRouteAside = false;
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "aside-enabled");
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "aside-fixed");
        // this.$store.dispatch(REMOVE_BODY_CLASSNAME, "aside-static");
        this.$store.dispatch(REMOVE_BODY_CLASSNAME, "aside-minimize");
      } else {
        this.selectedRouteAside = true;
        this.$store.dispatch(ADD_BODY_CLASSNAME, "aside-enabled");
        this.$store.dispatch(ADD_BODY_CLASSNAME, "aside-fixed");
        // this.$store.dispatch(ADD_BODY_CLASSNAME, "aside-static");
        this.$store.dispatch(ADD_BODY_CLASSNAME, "aside-minimize");
      }
    }
  },
  computed: {
    ...mapGetters([
      "isAuthenticated",
      "breadcrumbs",
      "pageTitle",
      "layoutConfig"
    ]),

    /**
     * Check if the page loader is enabled
     * @returns {boolean}
     */
    loaderEnabled() {
      return !/false/.test(this.layoutConfig("loader.type"));
    },

    /**
     * Check if container width is fluid
     * @returns {boolean}
     */
    contentFluid() {
      return this.layoutConfig("content.width") === "fluid";
    },

    /**
     * Page loader logo image using require() function
     * @returns {string}
     */
    loaderLogo() {
      return process.env.BASE_URL + this.layoutConfig("loader.logo");
    },

    /**
     * Check if the left aside menu is enabled
     * @returns {boolean}
     */
    asideEnabled() {
      return !!this.layoutConfig("aside.self.display");
    },

    /**
     * Set the right toolbar display
     * @returns {boolean}
     */
    toolbarDisplay() {
      // return !!this.layoutConfig("toolbar.display");
      return true;
    }

    /**
     * Set the subheader display
     * @returns {boolean}
     */
    // subheaderDisplay() {
    //   return !!this.layoutConfig("subheader.display");
    // }
  }
};
</script>
