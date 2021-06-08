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
              ></a
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
              ></a
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
          <VueTwitchPlayer :channel="channel" width="100%" height=500px></VueTwitchPlayer>
        </v-card>
      </div>
    </div>
  </div>
</template>
<script src="https://embed.twitch.tv/embed/v1.js"></script>
<script>
// import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
import VueTwitchPlayer from "vue-twitch-player";
export default {
  components: {
    VueTwitchPlayer
  },
  name: "SocialMedia",
  data() {
    return {
      channel: "finwiselive",
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
    ascpetedHeight=1366*16/9*0.5
    // new Twitch.Embed("twitch-embed", {
    //   width: 854,
    //   height: 480,
    //   channel: "finwiselive",
    //   // Only needed if this page is going to be embedded on other websites
    //   parent: ["https://finwise.ir"]
    // });
  },
  mounted() {
    // const options = {
    //   width: 854,
    //   height: 480,
    //   channel: 'finwiselive',
    // };
    // // you might need to pass an ID string as a first argument..
    // this.player = new Twitch.Player(this.$refs.twitchVideo, options);
    // this.player.setVolume(0.5);
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
