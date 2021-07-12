/* eslint-disable no-unused-vars */
<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <MonthlyWidget
          :notices="notice"
          :deposits="deposits"
          :typeOf="typeofReport"
          :portfos="portfo"
          :summaries="summary"
        ></MonthlyWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import MonthlyWidget from "@/view/pages/Ticker/TickerWidgets/MonthlyWidget.vue";
// import axios from "axios";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    MonthlyWidget
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
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "گزارش های خام ماهیانه" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response => {
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
                this.getleasingdelegated().then(function() {});
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
      });
    },
    async getleasingCost() {
      await this.axios
        .get("/api/Monthly/Leasing/Cost/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Leasing/Revenue/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Leasing/Delegated/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Construction/Sold/" + this.$route.params.id + "/", {
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
        .get(
          "/api/Monthly/Construction/Ongoing/" + this.$route.params.id + "/",
          {
            headers: {
              Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
            }
          }
        )
        .then(response2 => {
          this.deposits = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getProduction() {
      await this.axios
        .get("/api/Monthly/Production/" + this.$route.params.id + "/", {
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
    async getService() {
      await this.axios
        .get("/api/Monthly/Service/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Insurance/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Type/" + this.$route.params.id + "/", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          //typeofReport
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
        .get("/api/Monthly/Bank/Deposits/" + this.$route.params.id + "/", {
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
        .get("/api/Monthly/Bank/Facilities/" + this.$route.params.id + "/", {
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
          "/api/Monthly/Investment/InTransactions/" +
            this.$route.params.id +
            "/"
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
          "/api/Monthly/Investment/OutTransactions/" +
            this.$route.params.id +
            "/"
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
        .get("/api/Monthly/Investment/Summary/" + this.$route.params.id + "/", {
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
        .get(
          "/api/Monthly/Investment/Portfolio/" + this.$route.params.id + "/",
          {
            headers: {
              Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
            }
          }
        )
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
            this.getSummary().then(response => {});
          });
        });
      });
    },
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response1 => {
          this.subheaders = response1.data[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
