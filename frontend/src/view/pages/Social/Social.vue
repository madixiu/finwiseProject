<template>
  <div class="row" style="padding-top:5px">
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-card-title>LinkedIn</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider>
          <div id="curator-feed-new-feed-layout-linkedin">
            <a
              href="https://curator.io"
              target="_blank"
              class="crt-logo crt-tag"
              >Powered by Curator.io</a
            >
          </div>
        </v-card>
      </div>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-card-title>Instagram</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider>
          <div id="curator-feed-default-feed-layout">
            <a
              href="https://curator.io"
              target="_blank"
              class="crt-logo crt-tag"
              >Powered by Curator.io</a
            >
          </div>
        </v-card>
      </div>
    </div>
    <div class="col-xxl-6 col-lg-6 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-card-title>Twitch</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider>
          <iframe
            src="https://player.twitch.tv/finwiselive&parent=https://finwise.ir"
            height="400"
            width="100%"
            allowfullscreen="true"
          >
          </iframe>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
// import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
export default {
  name: "SocialMedia",
  components: {
    // IndexChart
  },
  data() {
    return {
      dataFetched: false,
      highestTvalueData: [],
      AssetTradeValue: [],
      TodayTepix: [],
      News: [],
      ImpactsData: [],
      HHData: [],
      QData: [],
      mostviewed: [],
      TechnicalData: [],
      ResponeseTimeout: {
        getImpacts: true,
        TradesValue: true,
        getTradesAll: true,
        getNews: true,
        getTepixToday: true,
        getHHData: true,
        getHighestQ: true,
        getTechnicalData: true
      }
    };
  },
  created() {
    document.title = "Finwise - شبکه های اجتماعی";
  },
  mounted() {
    // this.test();
    (function() {
      var i,
        e,
        d = document,
        s = "script";
      i = d.createElement("script");
      i.async = 1;
      i.src =
        "https://cdn.curator.io/published/4b49fed0-aa5f-47bf-9e4f-8b6ba06574fa.js";
      e = d.getElementsByTagName(s)[0];
      e.parentNode.insertBefore(i, e);
    })();
    (function() {
      var i,
        e,
        d = document,
        s = "script";
      i = d.createElement("script");
      i.async = 1;
      i.src =
        "https://cdn.curator.io/published/9167bc5f-ad8c-4984-9679-6fc2a72e1331.js";
      e = d.getElementsByTagName(s)[0];
      e.parentNode.insertBefore(i, e);
    })();
    // this.make_requests_handler();
  },
  methods: {}
};
</script>
