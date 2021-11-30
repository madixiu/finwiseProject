<template>
  <v-row>
    <v-col xl="12" lg="12" md="12" sm="12" class="pt-0">
      <CryptoIntroMW :InputIntroMW="IntroMW"></CryptoIntroMW>
    </v-col>
    <v-col xl="6" lg="6" md="12" sm="12" class="pt-0" style="padding-left:5px">
      <TechnicalCharts :inpuDataTechnical="TechnicalData"></TechnicalCharts>
    </v-col>
    <v-col xl="6" lg="6" md="12" sm="12" class="pt-0" style="padding-right:5px">
      <CorrMatrix :inpuDataCorr="CorrData"></CorrMatrix>
    </v-col>
  </v-row>
</template>
<script>
//// import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import TechnicalCharts from "@/view/pages/Crypto/Widgets/TechnicalChart.vue";
import CorrMatrix from "@/view/pages/Crypto/Widgets/CorrMatrix.vue";
import CryptoIntroMW from "@/view/pages/Crypto/Widgets/CryptoMarketIntro.vue";
export default {
  name: "CryptoDashboard",
  components: {
    TechnicalCharts,
    CorrMatrix,
    CryptoIntroMW
  },
  data() {
    return {
      interval: null,
      dataFetched: false,
      TechnicalData: [],
      CorrData: [],
      IntroMW: [],
      WebsocketRequest: true
    };
  },
  watch: {
    $route() {
      if (this.$route.name != "CryptoDashboard") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    }
  },
  created() {
    document.title = "FinWise - رمز ارز";
    //// this.$store.dispatch(SET_BREADCRUMB, [{ title: "داشبورد رمز ارز" }]);
    this.loadData();
  },
  mounted() {
    // this.liveData();
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getIntroMW().then(resp0 => {
        // eslint-disable-next-line no-unused-vars
        this.getTechnical().then(resp1 => {
          // eslint-disable-next-line no-unused-vars
          this.getCorrelationM().then(resp2 => {
            this.liveData();
          });
        });
      });
    },
    async getTechnical() {
      await this.axios
        .get("/api/CryptoTechincalAll")
        .then(getHighestQResp => {
          this.TechnicalData = getHighestQResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getCorrelationM() {
      await this.axios
        .get("/api/CryptoHistoricCorr")
        .then(getHighestQResp => {
          this.CorrData = getHighestQResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getIntroMW() {
      await this.axios
        .get("/api/Crypto/Marketwatch/")
        .then(getIntro => {
          this.IntroMW = getIntro.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval._id);
          return;
        }
        // let barier = { request: "get" };
        // this.$socketMarketMap.send(JSON.stringify(barier));
        this.getIntroMW();
      }, 5000);
    }
    // liveChecker() {
    //   let date = new Date();
    //   if (date.getDay() != 5 && date.getDay() != 4) {
    //     this.WebsocketRequest = true;
    //     this.liveData();
    //   } else {
    //     this.WebsocketRequest = false;
    //   }
    // }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  }
};
</script>
