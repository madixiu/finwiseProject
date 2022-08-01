<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row" style="padding-top:5px">
      <div class="col-xxl-12 col-lg-12 col-md-12 pb-1">
        <v-card>
          <div class="d-flex flex-row">
            <div class="col-xxl-4 col-lg-4 col-md-12 rtl_centerd ">
              <h4>
                عنوان صندوق :
                <span class="spandata">
                  {{ this.metadata.FundTitle }}
                </span>
              </h4>
              <h6>
                آخرین به روز رسانی :
                <span class="spandata"> {{ metadata.LastNavDate }}</span>
              </h6>
              <v-btn icon @click="ClickFundLink">
                <v-icon color="#188dc9">mdi-web</v-icon>
              </v-btn>
            </div>
            <div class="col-xxl-4 col-lg-4 col-md-12 ">
              <h4 class="titleHeaders ">
                جمع خالص دارایی ها :
                <span class="spandata">
                  {{
                    numberWithCommas(
                      roundTo(metadata.NetAssetValue / 10000000000, 2)
                    )
                  }}
                  میلیارد تومان
                </span>

                <v-icon left small>
                  <!-- v-bind:class="[this.close >= this.open ? 'greenItem' : 'redItem']" -->
                  <!-- mdi-chevron-{{this.close >= this.open ? "up" : "down"}} -->
                </v-icon>
              </h4>
              <h4 class="titleHeaders ">
                قیمت صدور:
                <span class="spandata">
                  {{ numberWithCommas(metadata.SubscriptionNav) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                قیمت ابطال:
                <span class="spandata">
                  {{ numberWithCommas(metadata.RedemptionNav) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                وضعیت صندوق:
                <span class="spandata">
                  {{ metadata.Status }}
                </span>
              </h4>
            </div>
            <div class="col-xxl-4 col-lg-4 col-md-12 ">
              <h4 class="titleHeaders ">
                تعداد واحد:
                <span class="spandata">
                  {{ numberWithCommas(metadata.TotalUnit) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                شروع فعالیت:
                <span class="spandata">
                  {{ metadata.ActivityStartDate }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                اندازه:
                <span class="spandata">
                  {{ metadata.Size }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                نوع:
                <span class="spandata">
                  {{ metadata.Type }}
                </span>
              </h4>
            </div>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:0px">
        <liveWidget
          :meta="metadata"
          :industry="industrydata"
          :assettype="assettypedata"
          :historicNav="historicNavData"
          :liveNav="LiveNavData"
        ></liveWidget>
      </div>
      <!-- <div class="col-xxl-3 col-lg-3 col-md-12">
        <asideWidget></asideWidget>
      </div> -->
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import {
  SET_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
import liveWidget from "@/view/pages/Fund/Widgets/NonETFLive.vue";
// import asideWidget from "@/view/pages/Fund/Widgets/NonETFAside.vue";
// import SubHeaderWidget from "@/view/pages/Crypto/Widgets/CryptoSubHeader.vue";

export default {
  name: "SingleNonETF",
  components: {
    liveWidget
    // asideWidget
    // SubHeaderWidget
  },
  data() {
    return {
      search: "",
      logourl: "",
      subheaders: {},
      metadata: [],
      industrydata: [],
      assettypedata: [],
      historicNavData: [],
      LiveNavData: [],
      cryptolive: [],
      lastUpdated: ""
    };
  },
  created() {
    document.title = "Finwise - صندوق غیر بورسی";
    this.$store.dispatch(SET_BREADCRUMB_TITLE, "");
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "صندوق غیر بورسی" }]);

    this.loadData();
  },
  mounted() {},
  watch: {
    "$route.params": {
      handler(newValue, oldValue) {
        if (newValue != oldValue) {
          this.loadData();
        }
      },
      immediate: true
    }
  },
  methods: {
    ClickFundLink() {
      if (!String(this.metadata.webSite).includes("http")) {
        window.open("http://" + this.metadata.webSite, "_blank");
      } else {
        window.open(this.metadata.webSite, "_blank");
      }
    },
    numberWithCommas(x) {
      if (x == "-" || x === undefined) {
        return "-";
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    roundTo(n, digits) {
      if (n == "-" || n === undefined) {
        return n;
      }

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
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(responx => {
        // eslint-disable-next-line no-unused-vars
        this.getTwo().then(reposonseY => {
          // eslint-disable-next-line no-unused-vars
          this.getThree().then(reposonseN => {
            // eslint-disable-next-line no-unused-vars
            this.getFour().then(reposonseF => {
              // eslint-disable-next-line no-unused-vars
              this.getFive();
            });
          });
        });
      });
    },

    async getOne() {
      this.metadata = [];
      await this.axios
        .get("/api/Funds/FundsMeta/" + this.$route.params.id)
        .then(response1 => {
          this.metadata = response1.data[0];
          // this.$store.dispatch(SET_BREADCRUMB, [{ title: "صندوق غیر بورسی" }]);
          this.$store.dispatch(SET_BREADCRUMB_TITLE, this.metadata.FundTitle);
          document.title = "Finwise - " + this.metadata.FundTitle;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTwo() {
      this.industrydata = [];

      await this.axios
        .get("/api/Funds/FundsIndustry/" + this.$route.params.id)
        .then(response1 => {
          this.industrydata = response1.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      this.assettypedata = [];

      await this.axios
        .get("/api/Funds/FundsAsset/" + this.$route.params.id)
        .then(response1 => {
          this.assettypedata = response1.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getFour() {
      this.historicNavData = [];
      await this.axios
        .get("/api/Funds/FundsHistoricNAV/" + this.$route.params.id)
        .then(response1 => {
          this.historicNavData = response1.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getFive() {
      this.LiveNavData = [];
      await this.axios
        .get("/api/Funds/FundsLive/" + this.$route.params.id)
        .then(response1 => {
          this.LiveNavData = response1.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    setActiveTab1(event) {
      this.tabIndex = this.setActiveTab(event);
    },
    setActiveTab2(event) {
      this.tabIndex2 = this.setActiveTab(event);
    },
    /**
     * Set current active on click
     * @param event
     */
    setActiveTab(event) {
      // get all tab links
      const tab = event.target.closest('[role="tablist"]');
      const links = tab.querySelectorAll(".nav-link");
      // remove active tab links
      for (let i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
      }

      // set current active tab
      event.target.classList.add("active");

      // set clicked tab index to bootstrap tab
      return parseInt(event.target.getAttribute("data-tab"));
    }
  }
};
</script>
<style scoped>
.web-icon {
  color: black;
}
.cellItem {
  direction: ltr;
  text-align: right;
  font-family: "Vazir-Medium-FD";
  font-weight: 700;
  font-size: 1.1em;
}
.spandata {
  font-family: "Vazir-Medium-FD";
}
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
  text-align: left;
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
  font-family: "Vazir-Medium-FD";
}
.titleHeaders span {
  font-family: "Vazir-Medium-FD";
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
