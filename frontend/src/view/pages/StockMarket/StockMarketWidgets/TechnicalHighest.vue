<template>
  <div class="col-12" style="padding-right:0px;padding-top:0px">
    <v-card width="100%" shaped>
      <!--begin::Header-->
      <v-toolbar dense class="elevation-2" style="height:36px;">
        <v-toolbar-title style="height:20px;font-size:0.95em">
          ربات تحلیلگر تکنیکال
        </v-toolbar-title>
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

          <span style="font-weight:600">بهترین</span>
        </v-tab>

        <v-tab>
          <v-icon color="#9E2A2B" small>mdi-trending-down</v-icon>

          <span style="font-weight:600">بدترین</span>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="selectedAttribute">
        <v-tab-item
          v-for="itemR in markets"
          :key="itemR.key"
          :value="itemR.key"
        >
          <div style="text-align: center; direction: rtl" v-if="loading">
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
            class="elevation-1"
            :items-per-page="10"
          >
            <template v-slot:[`item.ticker`]="{ item }">
              <router-link :to="linkcreated(item)">{{
                item.ticker
              }}</router-link>
            </template>
            <template v-slot:[`item.sum`]="{ item }">
              <div style="direction:ltr">
                <span>{{ item.sum }}</span>
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
  name: "TechnicalHighest",
  props: { inputDataTechnical: Array },
  data() {
    return {
      sortBy: "Value",
      sortDesc: true,
      selectedMarket: 1,
      loading: true,
      DataItems: [],
      markets: [
        { key: 0, value: "بهترین", shorthanded: "بهترین" },
        { key: 1, value: "بدترین", shorthanded: "بدترین" }
      ],
      // WebsocketRequest: true,
      lowestValues: [],
      highestValues: [],
      selectedAttribute: 0,
      mvheaders: [
        { text: "نماد", value: "ticker", sortable: false, align: "center" },
        { text: "امتیاز", value: "sum", sortable: false, align: "center" }
      ]
    };
  },
  computed: {
    filteredItems() {
      if (this.selectedAttribute == 0) {
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
    loadData() {
      if (
        !(
          this.inputDataTechnical === undefined ||
          this.inputDataTechnical.length == 0
        )
      ) {
        this.loading = false;
        this.highestValues = this.inputDataTechnical[0];
        this.lowestValues = this.inputDataTechnical[1];
      }
    }
  },
  mounted() {
    this.loadData();
  },
  watch: {
    inputDataTechnical() {
      this.loadData();
    }
  }
};
</script>
