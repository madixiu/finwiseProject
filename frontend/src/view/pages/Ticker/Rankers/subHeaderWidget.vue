<template>
  <!--begin::Mixed Widget 14-->
  <div>
    <v-card width="100%">
      <!-- <div class="row border-0 pb-4 pt-2"> -->
      <div class="row  pt-4 mb-2">
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
          نماد
        </v-chip> -->
          <div class="text-center">
            <b-button class="testB" color="#212529">
              نماد
              <br /><b-badge variant="light">{{ DataItems.ticker }}</b-badge>
            </b-button>
          </div>
          <!-- {{ DataItems.ticker }} -->
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            نام شرکت
          </v-chip>
          {{ DataItems.name }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              نام شرکت <br /><b-badge variant="light">{{
                DataItems.name
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            بازار
          </v-chip>
          {{ DataItems.market }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              بازار <br /><b-badge variant="light">{{
                DataItems.market
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            صنعت
          </v-chip>
          {{ DataItems.subIndustry }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              ارزش معاملات <br /><b-badge variant="light"
                >{{
                  numberWithCommas(
                    roundTo(DataItems.TradeValue / 1000000000, 2)
                  )
                }}
                میلیارد</b-badge
              >
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            تابلو
          </v-chip>
          {{ DataItems.board }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              قیمت پایانی <br />
              <b-badge variant="light"
                >{{ numberWithCommas(DataItems.close) }}ریال |
                <span
                  class="spandata"
                  v-bind:class="[
                    DataItems.close > DataItems.yesterday
                      ? 'greenItem ltr_aligned'
                      : 'redItem ltr_aligned'
                  ]"
                  >{{
                    Math.round(
                      (DataItems.close / DataItems.yesterday - 1) * 100 * 100
                    ) / 100
                  }}</span
                >
              </b-badge>
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            گروه
          </v-chip>
          {{ DataItems.parentIndustry }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              وضعیت <br /><b-badge variant="light">{{
                DataItems.Status
              }}</b-badge>
            </b-button>
          </div>
        </div>
      </div>
    </v-card>
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        {{ this.Nemad }}<span class="small mr-5">{{ this.tickerfull }}</span>
      </h3>
    </div> -->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import axios from "axios";
export default {
  name: "SubHeaderWidget",
  props: ["tickerdata"],
  data() {
    return {
      search: "",
      DataItems: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems = this.tickerdata;
      console.log(this.DataItems.length);
    },
    numberWithCommas(x) {
      if (isNaN(x)) {
        return "";
      }
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    setlastperc: function() {
      return;
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      if (n == "-") {
        return n;
      }

      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    tickerdata() {
      this.populateData();
      // console.log(this.tickerdata);
      // console.log("WatcherSubHeader");
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
  font-size: 0.8em;
}
.text-center * {
  font-family: "Dirooz FD";
  font-size: 1.1em;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
