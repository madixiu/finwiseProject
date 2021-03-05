<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12 card card-custom">
    <v-card>
      <!--begin::Header-->
      <!-- <div class="card-header border-0 pt-2"> -->
      <!-- <h3 class="card-title font-weight-bolder FinancialStrength">
        بیشترین ارزش معاملات
      </h3> -->
      <v-card-title>
        ربات تحلیلگر تکنیکال
      </v-card-title>
      <!-- </div> -->
      <!--end::Header-->
      <!--begin::Body-->
      <div class="card-body d-flex flex-column">
        <v-tabs vertical>
          <v-tab
            v-for="item in markets"
            :key="item.key"
            @click="GetFiltered(item.key)"
          >
            {{ item.shorthanded }}
          </v-tab>

          <v-tab-item v-for="itemR in markets" :key="itemR.key">
            <div class="FinancialStrength" v-if="loading">
              <b-spinner small></b-spinner>
              در حال بارگزاری
            </div>

            <v-data-table
              v-if="loading == false"
              :headers="mvheaders"
              :items="filteredItems"
              :hide-default-footer="true"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
              class="elevation-1 FinancialStrength"
              :items-per-page="10"
            >
              <template v-slot:[`item.ticker`]="{ item }">
                <v-chip small label :to="linkcreated(item)">{{
                  item.ticker
                }}</v-chip>
              </template>
              <template v-slot:[`item.sum`]="{ item }">
                <span class="cellItem ">{{ item.sum }}</span>
              </template>
            </v-data-table>
          </v-tab-item>
        </v-tabs>
      </div>
      <!--end::Body-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import axios from "axios";
export default {
  name: "TradeValues",
  props: ["inputDataTechnical"],
  data() {
    return {
      search: "",
      sortBy: "Value",
      sortDesc: true,
      selectedMarket: 1,
      loading: true,
      DataItems: [],
      markets: [
        { key: 1, value: "بهترین", shorthanded: "بهترین" },
        { key: 2, value: "بدترین", shorthanded: "بدترین" }
      ],
      WebsocketRequest: true,
      lowestValues: [],
      highestValues: [],
      selectedAttribute: 1,
      mvheaders: [
        { text: "نماد", value: "ticker" },
        { text: "امتیاز", value: "sum" }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      //   console.log(this.selectedMarket);
      if (this.selectedAttribute == 2) {
        return this.highestValues;
      } else {
        return this.lowestValues;
      }
    }
  },
  methods: {
    linkcreated(item) {
      return { name: "TickerOverall", params: { id: item.firm } };
    },
    numberWithCommas(x) {
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
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
    },
    GetFiltered(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.selectedAttribute = selectedItem;
      // console.log(this.selectedAttribute)
    },
    populateData() {
      this.DataItems = [...this.inputDataTechnical];
      //   console.log(this.inputDataTechnical);
      if (!(this.DataItems === undefined || this.DataItems.length == 0)) {
        this.loading = false;
        this.DataItems.forEach(
          function(d) {
            d.sum =
              (d.Signal_EMA200 != "NaN" ? d.Signal_EMA200 : 0) +
              (d.Signal_EMA10 != "NaN" ? d.Signal_EMA10 : 0) +
              (d.Signal_HMA != "NaN" ? d.Signal_HMA : 0) +
              (d.Signal_ICHI != "NaN" ? d.Signal_ICHI : 0) +
              (d.Signal_EMA50 != "NaN" ? d.Signal_EMA50 : 0) +
              (d.Signal_EMA5 != "NaN" ? d.Signal_EMA5 : 0) +
              (d.Signal_EMA20 != "NaN" ? d.Signal_EMA20 : 0) +
              (d.Signal_KETLER != "NaN" ? d.Signal_KETLER : 0) +
              (d.Signal_MACD != "NaN" ? d.Signal_MACD : 0) +
              (d.Signal_EMA100 != "NaN" ? d.Signal_EMA100 : 0) +
              (d.Signal_Awesome != "NaN" ? d.Signal_Awesome : 0) +
              (d.Signal_CCI != "NaN" ? d.Signal_CCI : 0) +
              (d.Signal_MFI != "NaN" ? d.Signal_MFI : 0) +
              (d.Signal_MOM != "NaN" ? d.Signal_MOM : 0) +
              (d.Signal_PSAR != "NaN" ? d.Signal_PSAR : 0) +
              (d.Signal_RSI != "NaN" ? d.Signal_RSI : 0) +
              (d.Signal_Stoch != "NaN" ? d.Signal_Stoch : 0) +
              (d.Signal_StochRSI != "NaN" ? d.Signal_StochRSI : 0) +
              (d.Signal_Ultimate != "NaN" ? d.Signal_Ultimate : 0) +
              (d.Signal_VAMA != "NaN" ? d.Signal_VAMA : 0) +
              (d.Signal_Williams != "NaN" ? d.Signal_Williams : 0) +
              (d.Signal_SMA50 != "NaN" ? d.Signal_SMA50 : 0) +
              (d.Signal_SMA5 != "NaN" ? d.Signal_SMA5 : 0) +
              (d.Signal_SMA200 != "NaN" ? d.Signal_SMA200 : 0) +
              (d.Signal_SMA20 != "NaN" ? d.Signal_SMA20 : 0) +
              (d.Signal_SMA10 != "NaN" ? d.Signal_SMA10 : 0) +
              (d.Signal_SMA100 != "NaN" ? d.Signal_SMA100 : 0);
          },
          // eslint-disable-next-line no-unused-vars
          function(error, data) {
            if (error) throw error;
          }
        );
      }
      this.DataItems.sort((a, b) => a.sum - b.sum);
      this.highestValues = this.DataItems.slice(0, 10);
      this.DataItems.sort((a, b) => b.sum - a.sum);
      this.lowestValues = this.DataItems.slice(0, 10);
      // console.log(this.lowestValues)
      // console.log(this.highestValues)
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    inputDataTechnical() {
      this.populateData();
      // console.log("WatcherSubHeader");
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
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
.cellItem {
  font-family: "Dirooz FD";
  font-weight: 700;
}
</style>
