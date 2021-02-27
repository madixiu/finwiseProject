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
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "گزارش های خام ماهیانه" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
      // console.log(this.notices);
    }
  },
  methods: {
    loadData() {
      this.getOne().then(response => {
        console.log(response);
        //add this to package.json in developement
        //         "eslintConfig": {
        //     "rules": {
        //       "no-console": "off",
        //       "no-unused-vars": "off"
        //     }
        // },
        this.getType().then(response => {
          console.log(response);
          console.log(this.typeofReport);
          if (this.typeofReport == "bank") {
            this.getTwo().then(response => {
              console.log(response);
              this.getThree().then(function() {
                console.log("ChainDone");
              });
            });
          }
          if (this.typeofReport == "leasing") {
            this.getleasingCost().then(response => {
              console.log(response);
              this.getleasingrevenue().then(function() {
                this.getleasingdelegated().then(function() {
                  console.log("ChainDone");
                });
              });
            });
          }
          if (this.typeofReport == "production") {
            this.getProduction().then(response => {
              console.log(response);
            });
          }
          if (this.typeofReport == "service") {
            this.getService().then(response => {
              console.log(response);
            });
          }
          if (this.typeofReport == "insurance") {
            this.getInsurance().then(response => {
              console.log(response);
            });
          }
          if (this.typeofReport == "investment") {
            this.loadInvest();
          }
          if (this.typeofReport == "construction") {
            // eslint-disable-next-line no-unused-vars
            this.getConstructionSold().then(response => {
              // console.log(response);
              this.getConstructionOngoing().then(function() {
                console.log("ChainDone");
              });
            });
          }
        });
      });
    },
    async getleasingCost() {
      await this.axios
        .get("/api/Monthly/Leasing/Cost/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getleasingrevenue() {
      await this.axios
        .get("/api/Monthly/Leasing/Revenue/" + this.$route.params.id + "/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.deposits = response3.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getleasingdelegated() {
      await this.axios
        .get("/api/Monthly/Leasing/Delegated/" + this.$route.params.id + "/")
        .then(response4 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.portfo = response4.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getConstructionSold() {
      await this.axios
        .get("/api/Monthly/Construction/Sold/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getConstructionOngoing() {
      await this.axios
        .get("/api/Monthly/Construction/Ongoing/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.deposits = response2.data;
          console.log(this.deposits);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getProduction() {
      await this.axios
        .get("/api/Monthly/Production/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getService() {
      await this.axios
        .get("/api/Monthly/Service/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          console.log(this.notice);
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getInsurance() {
      await this.axios
        .get("/api/Monthly/Insurance/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getType() {
      await this.axios
        .get("/api/Monthly/Type/" + this.$route.params.id + "/")
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
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getTwo() {
      await this.axios
        .get("/api/Monthly/Bank/Deposits/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.deposits = response2.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getThree() {
      await this.axios
        .get("/api/Monthly/Bank/Facilities/" + this.$route.params.id + "/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response3.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
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
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response3.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
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
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.deposits = response3.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getSummary() {
      await this.axios
        .get("/api/Monthly/Investment/Summary/" + this.$route.params.id + "/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.summary = response3.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getPortfo() {
      await this.axios
        .get("/api/Monthly/Investment/Portfolio/" + this.$route.params.id + "/")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.portfo = response3.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    loadInvest() {
      this.getTransIn().then(response => {
        console.log(response);
        this.getTransOut().then(response => {
          console.log(response);
          this.getPortfo().then(response => {
            console.log(response);
            this.getSummary().then(response => {
              console.log(response);
            });
          });
        });
      });
    },
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
        .then(response1 => {
          // console.log("firstDone");
          this.subheaders = response1.data[0];
          // console.log(response1.data);
        })
        .catch(error => {
          // console.log("GetOneCatch");
          console.log(error);
        });
    }
  }
};
</script>
