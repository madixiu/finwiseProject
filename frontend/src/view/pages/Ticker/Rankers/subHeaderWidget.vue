<template>
  <div style="padding-top:5px">
    <v-row
      no-gutters
      class="d-flex flex-row justify-content-between"
      v-if="!loading"
      style="flex-wrap: nowrap"
    >
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            نماد
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            <span>
              {{ LiveDataItems.ticker }}
            </span>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            آخرین قیمت
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            <span
              class="spandata ltr_aligned mr-1"
              v-bind:class="[
                [
                  LiveDataItems.last > LiveDataItems.yesterday
                    ? 'greenItem ltr_aligned'
                    : LiveDataItems.last == LiveDataItems.yesterday
                    ? 'blackItem ltr_aligned'
                    : LiveDataItems.last < LiveDataItems.yesterday
                    ? 'redItem ltr_aligned'
                    : ''
                ]
              ]"
              >%{{
                Math.round(
                  (LiveDataItems.last / LiveDataItems.yesterday - 1) * 100 * 100
                ) / 100
              }}</span
            >
            <span>{{ numberWithCommas(LiveDataItems.last) }} </span>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            قیمت پایانی
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            <span
              class="spandata ltr_aligned"
              v-bind:class="[
                [
                  LiveDataItems.close > LiveDataItems.yesterday
                    ? 'greenItem ltr_aligned'
                    : LiveDataItems.close == LiveDataItems.yesterday
                    ? 'blackItem ltr_aligned'
                    : LiveDataItems.close < LiveDataItems.yesterday
                    ? 'redItem ltr_aligned'
                    : ''
                ]
              ]"
              >%{{
                Math.round(
                  (LiveDataItems.close / LiveDataItems.yesterday - 1) *
                    100 *
                    100
                ) / 100
              }}</span
            >
            <span style="direction:ltr">{{
              numberWithCommas(LiveDataItems.close)
            }}</span>
          </v-col>
        </v-card>
      </v-col>

      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            ارزش معاملات
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            <span>{{
              numberWithCommas(
                roundTo(LiveDataItems.TradeValue / 1000000000, 2)
              )
            }}</span>
            <span>میلیارد ریال</span>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            حجم معاملات
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            <span>{{
              numberWithCommas(roundTo(LiveDataItems.TradeVolume / 1000000, 2))
            }}</span>
            <span>میلیون</span>
          </v-col>
        </v-card>
      </v-col>

      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pr-1">
        <v-card height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            وضعیت
          </v-col>
          <v-col cols="12" style="padding-bottom:5px">
            {{ LiveDataItems.Status }}
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </div>
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
.CardHeaderTitle {
  direction: ltr;
  align-items: right;
  display: flex;
  flex-wrap: nowrap;
  justify-content: flex-end;
  padding-bottom: 0px;
  padding-top: 5px;
  font-family: "Vazir-Light-FD";
  font-weight: 500;
  /* font-family: "IRANSansXFaNum-Regular"; */
}
.flex-item {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  align-items: center;
  justify-content: center;
  order: 0;
}
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
