<template>
  <!--begin::Mixed Widget 14-->
  <div>
    <v-card width="100%">
      <div class="row mb-1" v-if="!loading">
        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
          نماد
        </v-chip> -->
          <div class="text-center">
            نماد
            <br />{{ LiveDataItems.ticker }}
          </div>
          <!-- {{ LiveDataItems.ticker }} -->
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            نام شرکت
          </v-chip>
          {{ LiveDataItems.name }} -->
          <div class="text-center">
            آخرین قیمت <br />
            (
            <span
              class="spandata ltr_aligned"
              v-bind:class="[
                LiveDataItems.last > LiveDataItems.yesterday
                  ? 'greenItem ltr_aligned'
                  : 'redItem ltr_aligned'
              ]"
              >%{{
                Math.round(
                  (LiveDataItems.last / LiveDataItems.yesterday - 1) * 100 * 100
                ) / 100
              }}</span
            >)
            <span>{{ numberWithCommas(LiveDataItems.last) }} </span>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            تابلو
          </v-chip>
          {{ LiveDataItems.board }} -->
          <div class="text-center">
            قیمت پایانی <br />
            (
            <span
              class="spandata ltr_aligned"
              v-bind:class="[
                LiveDataItems.close > LiveDataItems.yesterday
                  ? 'greenItem ltr_aligned'
                  : 'redItem ltr_aligned'
              ]"
              >%{{
                Math.round(
                  (LiveDataItems.close / LiveDataItems.yesterday - 1) *
                    100 *
                    100
                ) / 100
              }}</span
            >)
            <span style="direction:ltr">{{
              numberWithCommas(LiveDataItems.close)
            }}</span>
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            صنعت
          </v-chip>
          {{ LiveDataItems.subIndustry }} -->
          <div class="text-center">
            ارزش معاملات <br /><span class="text-center">{{
              numberWithCommas(
                roundTo(LiveDataItems.TradeValue / 1000000000, 2)
              )
            }}</span>
            میلیارد ریال
          </div>
        </div>
        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            بازار
          </v-chip>
          {{ LiveDataItems.market }} -->
          <div class="text-center">
            حجم معاملات <br /><span class="text-center"
              >{{
                numberWithCommas(
                  roundTo(LiveDataItems.TradeVolume / 1000000, 2)
                )
              }}
            </span>
            میلیون
          </div>
        </div>

        <div
          class="col-xxl-2 col-lg-2 col-md-4 col-sm-4 col-xs-4 col-4 FinancialStrength "
        >
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            گروه
          </v-chip>
          {{ LiveDataItems.parentIndustry }} -->
          <div class="text-center">وضعیت <br />{{ LiveDataItems.Status }}</div>
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
      if (this.LiveDataItems === undefined || this.LiveDataItems.length == 0) {
        this.LiveDataItems = [
          {
            ID: "-",
            englishDate: "-",
            Status: "-",
            Hour: "-",
            ticker: "-",
            name: "-",
            ShareCount: "-",
            Mabna: "-",
            Shenavari: "-",
            persianDate: "-",
            first: "-",
            close: "-",
            last: "-",
            low: "-",
            high: "-",
            yesterday: "-",
            TradeCount: "-",
            TradeValue: "-",
            TradeVolume: "-",
            EPS: "-",
            market: "-"
          }
        ];
      }
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
  font-size: 1em;
  font-family: "Vazir-Medium-FD";
}
.text-center * {
  font-family: "Vazir-Medium-FD";
  font-size: 1em;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left !important;
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
