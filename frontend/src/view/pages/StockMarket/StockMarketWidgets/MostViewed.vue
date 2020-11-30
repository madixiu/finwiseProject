<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        پر بازدید
      </h3>
      <v-subheader class="ltr_aligned" v-if="loading == false">
        آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }}
      </v-subheader>
    </div>
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
            :hide-default-header="true"
            class="elevation-1 FinancialStrength"
            :header-props="{ sortIcon: null }"
          >
            <template v-slot:[`item.ticker`]="{ item }">
              <v-chip
                small
                label
                :to="{ name: 'TickerOverall', params: { id: item.ID } }"
                target="_blank"
                >{{ item.ticker }}</v-chip
              >
            </template>
          </v-data-table>
        </v-tab-item>
      </v-tabs>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import axios from "axios";
export default {
  name: "MostViewed",
  //   props: ["mostviewed"],
  data() {
    return {
      search: "",
      selectedMarket: 1,
      loading: true,
      DataItems: [],
      markets: [
        { key: 1, value: "بورس", shorthanded: "بورس" },
        { key: 2, value: "فرابورس", shorthanded: "فرابورس" },
        { key: 8, value: "بازار پایه زرد فرابورس", shorthanded: "پایه زرد" },
        {
          key: 9,
          value: "بازار پایه نارنجی فرابورس",
          shorthanded: "پایه نارنجی"
        },
        { key: 10, value: "بازار پایه قرمز فرابورس", shorthanded: "پایه قرمز" }
      ],
      WebsocketRequest: true,
      mvheaders: [
        { text: "رتبه", value: "Rank", sortabale: false },
        { text: "نماد", value: "ticker", sortabale: false }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      //   console.log(this.selectedMarket);
      return this.DataItems.filter(item => {
        return item.marketID == this.selectedMarket;
      });
    }
  },
  methods: {
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketMostViewed.send(JSON.stringify(barier));
        // console.log(this.WebsocketRequest);
      }, 300000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getHours() > 8 && date.getHours() < 15) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    },
    GetFiltered(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.selectedMarket = selectedItem;
    }
  },
  mounted() {
    this.$socketMostViewed.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    this.$socketMostViewed.onmessage = data => {
      // store.dispatch ('setMarketWatchItems',JSON.parse(data.data))
      this.DataItems = JSON.parse(data.data);
      this.loading = false;
    };
    // watch: {
    //   mostviewed() {
    //     this.populateData();
    //     // console.log("WatcherSubHeader");
    //   }
    // }
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketMostViewed.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
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
</style>
