<template>
  <!--begin::Mixed Widget 14-->
  <div>
    <v-card width="100%">
      <v-skeleton-loader
        type=" table-heading, table-thead, table-tbody"
        v-if="loading"
      ></v-skeleton-loader>

      <div class="row  pt-4 mb-2" v-if="!loading">
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
          نماد
        </v-chip> -->
          <div class="text-center">
            <b-button class="testB" color="#212529">
              نماد
              <br /><b-badge variant="light">{{
                LiveDataItems.ticker
              }}</b-badge>
            </b-button>
          </div>
          <!-- {{ LiveDataItems.ticker }} -->
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            نام شرکت
          </v-chip>
          {{ LiveDataItems.name }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              آخرین قیمت <br />
              <b-badge style="direction:ltr" variant="light"
                >(
                <span
                  class="spandata"
                  v-bind:class="[
                    LiveDataItems.last > LiveDataItems.yesterday
                      ? 'greenItem ltr_aligned'
                      : 'redItem ltr_aligned'
                  ]"
                  >{{
                    Math.round(
                      (LiveDataItems.last / LiveDataItems.yesterday - 1) *
                        100 *
                        100
                    ) / 100
                  }}</span
                >)
                <span>{{ numberWithCommas(LiveDataItems.last) }} </span>
              </b-badge>
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            تابلو
          </v-chip>
          {{ LiveDataItems.board }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              قیمت پایانی <br />
              <b-badge style="direction:ltr" variant="light">
                (
                <span
                  class="spandata"
                  v-bind:class="[
                    LiveDataItems.close > LiveDataItems.yesterday
                      ? 'greenItem ltr_aligned'
                      : 'redItem ltr_aligned'
                  ]"
                  >{{
                    Math.round(
                      (LiveDataItems.close / LiveDataItems.yesterday - 1) *
                        100 *
                        100
                    ) / 100
                  }}</span
                >)
                <span>{{ numberWithCommas(LiveDataItems.close) }}</span>
              </b-badge>
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            صنعت
          </v-chip>
          {{ LiveDataItems.subIndustry }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              ارزش معاملات <br /><b-badge variant="light"
                >{{
                  numberWithCommas(
                    roundTo(LiveDataItems.TradeValue / 1000000000, 2)
                  )
                }}
                میلیارد ریال</b-badge
              >
            </b-button>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            بازار
          </v-chip>
          {{ LiveDataItems.market }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              حجم معاملات <br /><b-badge variant="light"
                >{{
                  numberWithCommas(
                    roundTo(LiveDataItems.TradeVolume / 1000000, 2)
                  )
                }}
                میلیون</b-badge
              >
            </b-button>
          </div>
        </div>

        <div
          class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 col-xs-6 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            گروه
          </v-chip>
          {{ LiveDataItems.parentIndustry }} -->
          <div class="text-center">
            <b-button color="#6c757d">
              وضعیت <br /><b-badge variant="light">{{
                LiveDataItems.Status
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
      loading: true,
      search: "",
      LiveDataItems: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    LivepopulateData() {
      this.LiveDataItems = this.tickerdata;
      this.loading = false;
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
    // LivepopulateData() {
    //   this.LiveDataItems = this.mostviewed;
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
    this.LivepopulateData();
  },
  watch: {
    tickerdata() {
      this.LivepopulateData();
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
