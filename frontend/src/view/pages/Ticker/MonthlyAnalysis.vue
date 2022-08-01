<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <MonthlyAnalysisWidget
          :notices="notice"
          :deposits="deposits"
          :typeOf="typeofReport"
          :portfos="portfo"
          :summaries="summary"
        ></MonthlyAnalysisWidget>
      </div>
    </div>
  </div>
</template>

<script>
import {
  SET_BREADCRUMB,
  ADD_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import MonthlyAnalysisWidget from "@/view/pages/Ticker/TickerWidgets/MonthlyAnalysisWidget.vue";
export default {
  name: "MonthlyAnalysis",
  components: {
    SubHeaderWidget,
    MonthlyAnalysisWidget
  },
  data() {
    return {
      subheaders: [],
      notice: [],
      deposits: [],
      portfo: [],
      summary: [],
      typeofReport: ""
    };
  },
  created() {
    document.title = "Finwise - گزارش ماهیانه";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "ماهیانه" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "تحلیل ماهیانه" }]);
    if (this.$store.getters.getLiveTickerData != null) {
      this.subheaders = this.$store.getters.getLiveTickerData;
      this.loadData();
    } else {
      // eslint-disable-next-line no-unused-vars
      this.getLiveTickerData().then(Response => {
        this.loadData();
      });
    }
  },
  mounted() {
    // this.loadData();
  },
  watch: {
    // subheaders() {
    //   this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    // }
  },
  methods: {
    async getLiveTickerData() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id)
        .then(LiveTickerResponse => {
          this.subheaders = LiveTickerResponse.data[0];
          this.$store.dispatch("SetLiveTickerData", this.subheaders);
          this.$store.dispatch("SetLiveTickerID", this.subheaders.ID);
          this.$store.dispatch(SET_BREADCRUMB_TITLE, this.subheaders.ticker);
        })
        .catch(error => {
          console.error(error);
        });
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getType().then(response => {
        if (this.typeofReport == "bank") {
          // eslint-disable-next-line no-unused-vars
          this.getTwo().then(response => {
            this.getThree();
          });
        }
        if (this.typeofReport == "leasing") {
          // eslint-disable-next-line no-unused-vars
          this.getleasingCost().then(response => {
            this.getleasingrevenue().then(function() {
              this.getleasingdelegated();
            });
          });
        }
        if (this.typeofReport == "production") {
          this.getProduction();
        }
        if (this.typeofReport == "service") {
          this.getService();
        }
        if (this.typeofReport == "insurance") {
          this.getInsurance();
        }
        if (this.typeofReport == "investment") {
          this.loadInvest();
        }
        if (this.typeofReport == "construction") {
          // eslint-disable-next-line no-unused-vars
          this.getConstructionSold().then(response => {
            this.getConstructionOngoing();
          });
        }
      });
      // });
    },
    async getleasingCost() {
      await this.axios
        .get("/api/Monthly/Leasing/Cost/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getleasingrevenue() {
      await this.axios
        .get("/api/Monthly/Leasing/Revenue/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response3 => {
          this.deposits = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getleasingdelegated() {
      await this.axios
        .get("/api/Monthly/Leasing/Delegated/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response4 => {
          this.portfo = response4.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getConstructionSold() {
      await this.axios
        .get("/api/Monthly/Construction/Sold/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getConstructionOngoing() {
      await this.axios
        .get("/api/Monthly/Construction/Ongoing/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.deposits = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getProduction() {
      await this.axios
        .get("/api/Monthly/ProductionAnalysis1/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data["1"];
          this.deposits = response2.data["2"];
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getService() {
      await this.axios
        .get("/api/Monthly/Service/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getInsurance() {
      await this.axios
        .get("/api/Monthly/Insurance/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getType() {
      await this.axios
        .get("/api/Monthly/Type/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          var items = response2.data;
          for (var item, i = 0; (item = items[i++]); ) {
            if (item.value == true) {
              this.typeofReport = item.type;
            }
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTwo() {
      await this.axios
        .get("/api/Monthly/Bank/Deposits/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.deposits = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      await this.axios
        .get("/api/Monthly/Bank/Facilities/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response3 => {
          this.notice = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTransIn() {
      await this.axios
        .get(
          "/api/Monthly/Investment/InTransactions/" + this.$route.params.id,
          {
            headers: {
              Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
            }
          }
        )
        .then(response3 => {
          this.notice = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTransOut() {
      await this.axios
        .get(
          "/api/Monthly/Investment/OutTransactions/" + this.$route.params.id,
          {
            headers: {
              Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
            }
          }
        )
        .then(response3 => {
          this.deposits = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getSummary() {
      await this.axios
        .get("/api/Monthly/Investment/Summary/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response3 => {
          this.summary = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getPortfo() {
      await this.axios
        .get("/api/Monthly/Investment/Portfolio/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response3 => {
          this.portfo = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    loadInvest() {
      // eslint-disable-next-line no-unused-vars
      this.getTransIn().then(response => {
        // eslint-disable-next-line no-unused-vars
        this.getTransOut().then(response => {
          // eslint-disable-next-line no-unused-vars
          this.getPortfo().then(response => {
            // eslint-disable-next-line no-unused-vars
            this.getSummary();
          });
        });
      });
    }
  }
};
</script>
