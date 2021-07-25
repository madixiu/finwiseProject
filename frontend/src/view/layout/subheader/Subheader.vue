<template>
  <div
    class="subheader py-2 py-lg-4"
    v-bind:class="subheaderClasses"
    id="kt_subheader"
  >
    <div
      class="d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap"
      v-bind:class="{ 'container-fluid': widthFluid, container: !widthFluid }"
    >
      <div class="d-flex align-items-center flex-wrap mr-1">
        <li class="breadcrumb-item">
          <!-- <v-icon @click="ClickHome()">flaticon2-architecture-and-city </v-icon> -->
          <!-- <router-link :to="'/'" class="subheader-breadcrumbs-home"> -->
          <i
            class="flaticon2-architecture-and-city text-light icon-1x subheader-breadcrumbs-home"
            style="cursor:pointer;color:#6c7293 !important;"
            @click="ClickHome()"
          ></i>
          <!-- </router-link> -->
        </li>
        <v-icon x-small color="#6c7293" class="my-2 mr-1"
          >mdi-chevron-left</v-icon
        >
        <v-chip
          v-if="title.length"
          class="my-2 mr-1"
          label
          small
          outlined
          color="#6c7293"
          @click="ClickTitle()"
        >
          {{ title }}
        </v-chip>
        <!-- <span class="text-light my-2 mr-2">
          {{ title }}
        </span> -->
        <v-icon x-small color="#6c7293" class="my-2 mr-1"
          >mdi-chevron-left</v-icon
        >
        <ul
          class="breadcrumb breadcrumb-transparent breadcrumb-dot font-weight-bold p-0 my-2"
        >
          <template v-for="(breadcrumb, i) in breadcrumbs">
            <li
              class="breadcrumb-item"
              :key="`${i}-${breadcrumb.id}`"
              style="color:#6c7293"
            >
              <router-link
                v-if="breadcrumb.route"
                :key="i"
                :to="breadcrumb.route"
              >
                {{ breadcrumb.title }}
              </router-link>
              <span
                style="font-size:0.9em;font-family:'Vazir-Light-FD' color:#6c7293"
                :key="i"
                v-if="!breadcrumb.route"
              >
                {{ breadcrumb.title }}
              </span>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.custom-v-dropdown {
  &.dropdown-toggle {
    padding: 0;
    &:hover {
      text-decoration: none;
    }

    &.dropdown-toggle-no-caret {
      &:after {
        content: none;
      }
    }
  }

  &.dropdown-menu {
    margin: 0;
    padding: 0;
    outline: none;
    .b-dropdown-text {
      padding: 0;
    }
  }
}
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "KTSubheader",
  props: {
    breadcrumbs: Array,
    title: String
  },
  data() {
    return {
      TickerRouteList: [
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
        "TickerAssemblyReport",
        "TickerAssemblyDPSAndIC"
      ]
    };
  },
  methods: {
    ClickTitle() {
      if (this.TickerRouteList.includes(this.$route.name))
        this.$router.push({
          path: `/ticker/Overview/Overall/${this.getLiveTickerID}`
        });
    },
    ClickHome() {
      if (
        this.TickerRouteList.includes(this.$route.name) ||
        this.$route.name == "TickerOverall"
      )
        this.$router.push({
          name: "Dashboard"
        });
      else if (this.$route.name == "IndustriesDetail") {
        this.$router.push({
          name: "Industries"
        });
      } else if (this.$route.name == "SingleNonETF") {
        this.$router.push({
          name: "Funds"
        });
      }
    }
  },
  computed: {
    ...mapGetters(["layoutConfig", "getLiveTickerID"]),
    quickActionIcon() {
      return process.env.BASE_URL + "media/svg/icons/Files/File-plus.svg";
    },

    /**
     * Check if subheader width is fluid
     */
    widthFluid() {
      return this.layoutConfig("subheader.width") === "fluid";
    },

    subheaderClasses() {
      const classes = [];
      const style = this.layoutConfig("subheader.style");
      if (style) {
        classes.push(style);

        if (style === "solid") {
          classes.push("bg-white");
        }

        if (this.layoutConfig("subheader.fixed")) {
          classes.push("border-top");
        }
      }
      return classes.join(" ");
    }
  }
};
</script>
