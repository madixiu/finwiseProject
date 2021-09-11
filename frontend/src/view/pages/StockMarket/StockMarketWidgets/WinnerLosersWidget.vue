<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <div class="col-12" style="padding-right:0px;padding-top:0px;margin-top:10px">
    <v-card width="100%" shaped>
      <!--begin::Header-->
      <!-- <div class="card-header border-0 pt-2"> -->
      <!-- <h3 class="card-title font-weight-bolder FinancialStrength">
        بیشترین ارزش معاملات
      </h3> -->
      <v-toolbar dense class="elevation-2" style="height:36px;">
        <v-toolbar-title style="height:20px;font-size:0.95em">
          برنده ها و بازنده های بازار امروز
        </v-toolbar-title>
        <!-- <template v-slot:extension>
        </template> -->
      </v-toolbar>
      <v-tabs
        v-model="selectedAttribute"
        fixed-tabs
        height="30"
        background-color="#f0efeb"
        color="#4682B4"
        class="mt-1"
      >
        <v-tabs-slider></v-tabs-slider>
        <v-tab>
          <v-icon color="#1AA47C" small>mdi-trending-up</v-icon>

          <span style="font-weight:600">برنده ها</span>
        </v-tab>

        <v-tab>
          <v-icon color="#9E2A2B" small>mdi-trending-down</v-icon>

          <span style="font-weight:600">بازنده ها</span>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="selectedAttribute">
        <v-tab-item
          v-for="itemR in markets"
          :key="itemR.key"
          :value="itemR.key"
        >
          <div class="FinancialStrength" v-if="loading">
            <b-spinner small></b-spinner>
            در حال بارگزاری
          </div>

          <v-data-table
            dense
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
              <router-link :to="linkcreated(item)">{{
                item.ticker
              }}</router-link>
            </template>
            <template v-slot:[`item.sum`]="{ item }">
              <div style="direction:ltr">
                <span class="cellItem">{{ item.sum }}</span>
              </div>
            </template>
          </v-data-table>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "TradeValues",
  props: { inputWinLose: Array },
  data() {
    return {
      sortBy: "Value",
      sortDesc: true,
      selectedMarket: 1,
      loading: true,
      DataItems: [],
      markets: [
        { key: 0, value: "برنده ها", shorthanded: "برنده ها" },
        { key: 1, value: "بازنده ها", shorthanded: "بازنده ها" }
      ],
      // WebsocketRequest: true,
      lowestValues: [],
      highestValues: [],
      selectedAttribute: 0,
      mvheaders: [
        { text: "نماد", value: "ticker", sortable: false, align: "center" },
        {
          text: "تغییر",
          value: "returnDaily",
          sortable: false,
          align: "center"
        }
      ]
    };
  },
  computed: {
    filteredItems() {
      if (this.selectedAttribute == 1) {
        return this.highestValues;
      } else {
        return this.lowestValues;
      }
    }
  },
  methods: {
    linkcreated(item) {
      return { name: "TickerOverall", params: { id: item.ID } };
    },
    // GetFiltered(selectedItem) {
    //   this.selectedAttribute = selectedItem;
    // },
    loadData() {
      if (!(this.inputWinLose === undefined || this.inputWinLose.length == 0)) {
        this.loading = false;
        this.highestValues = this.inputWinLose.slice(0, 10);
        this.highestValues.sort(function(a, b) {
          return a.returnDaily - b.returnDaily;
        });
        this.lowestValues = this.inputWinLose.slice(10, 20);
        this.lowestValues.sort(function(a, b) {
          return b.returnDaily - a.returnDaily;
        });


      }
    }
  },
  watch: {
    inputWinLose() {
      this.loadData();
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
/* .cellItem { */
/* font-family: "Vazir-Light-FD"; */
/* font-weight: 700; */
/* } */
</style>
