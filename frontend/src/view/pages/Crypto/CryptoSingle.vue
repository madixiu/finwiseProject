<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row mt-2">
      <div class="col-xxl-12 col-lg-12 col-md-12">
        <v-card>
          <div class="row">
            <div class="col-xxl-4 col-lg-4 col-md-12 rtl_centerd ">
              <img v-bind:src="logourl" width="20%" />
              <h2>{{ this.subheaders.original_symbol }}</h2>
              <h2>{{ this.subheaders.name }}</h2>

              <h4>
                رتبه ارزش بازار :
                <span class="spandata"> #{{ cryptolive.marketCapRank }}</span>
              </h4>
              <h6>
                آخرین به روز رسانی :
                <span class="spandata"> {{ lastUpdated }}</span>
              </h6>
              <v-btn icon :href="this.subheaders.websiteUrl" target="_blank">
                <v-icon color="#188dc9">mdi-web</v-icon>
              </v-btn>
              <v-btn icon :href="this.subheaders.facebookUrl" target="_blank">
                <v-icon color="#3b5998">mdi-facebook</v-icon>
              </v-btn>
              <v-btn icon :href="this.subheaders.twitterUrl" target="_blank">
                <v-icon color="#00acee">mdi-twitter</v-icon>
              </v-btn>
              <v-btn icon :href="this.subheaders.githubUrl" target="_blank">
                <v-icon color="#e94e31">mdi-git</v-icon>
              </v-btn>
            </div>
            <div class="col-xxl-4 col-lg-4 col-md-12 ">
              <h4 class="titleHeaders ">
                قیمت :
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{ this.roundTo(cryptolive.price, 7) }}
                </span>
                (
                <span
                  dir="ltr"
                  class="spandata"
                  v-bind:class="[
                    this.cryptolive.change > 0 ? 'greenItem' : 'redItem'
                  ]"
                >
                  %{{ this.cryptolive.change }}
                </span>
                )

                <v-icon
                  left
                  small
                  v-bind:class="[
                    this.close >= this.open ? 'greenItem' : 'redItem'
                  ]"
                  >mdi-chevron-{{
                    this.close >= this.open ? "up" : "down"
                  }}</v-icon
                >
              </h4>
              <h4 class="titleHeaders ">
                قیمت بر حسب بیتکوین :
                <span class="spandata"
                  >{{ this.roundTo(cryptolive.priceBtc, 7) }} بیت کوین</span
                >
              </h4>
              <h4 class="titleHeaders ">
                ارزش بازار :
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(cryptolive.marketCap / 1000000, 2)
                    )
                  }}
                  میلیون
                </span>
              </h4>
              <h4 class="titleHeaders ">
                ارزش بازار بر حسب بیتکوین‌ :
                <span class="spandata"
                  >{{
                    this.roundTo(cryptolive.marketCapBtc / 1000000, 2)
                  }}
                  میلیون بیتکوین</span
                >
              </h4>

              <h4 class="titleHeaders ">
                حجم معاملات :
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(cryptolive.volume / 1000000, 2)
                    )
                  }}
                  میلیون
                </span>
              </h4>
              <h4 class="titleHeaders ">
                حجم معاملات بر حسب بیتکوین:
                <span class="spandata"
                  >{{ this.roundTo(cryptolive.volumeBtc / 1000000, 2) }} میلیون
                  بیتکوین</span
                >
              </h4>
              <h4 class="titleHeaders ">
                کل عرضه:
                <span class="spandata"
                  >{{ this.roundTo(cryptolive.totalSupply / 1000000, 0) }}
                  میلیون
                </span>
              </h4>
              <h4 class="titleHeaders ">
                عرضه موجود:
                <span class="spandata"
                  >{{ this.roundTo(cryptolive.emission / 1000000, 2) }} میلیون
                </span>
              </h4>
            </div>
            <div class="col-xxl-4 col-lg-4 col-md-12 ">
              <h4 class="titleHeaders ">
                قیمت شروع دیروز :
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{ numberWithCommas(cryptolive.yesterdayData.open) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                قیمت پایانی دیروز :
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{ numberWithCommas(cryptolive.yesterdayData.close) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                پایین ترین قیمت دیروز:
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{ numberWithCommas(cryptolive.yesterdayData.close) }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                تغییرات قیمت دیروز:
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(cryptolive.yesterdayData.change, 2)
                    )
                  }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                تغییرات قیمت دلاری دیروز:
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(cryptolive.yesterdayData.change_usd, 2)
                    )
                  }}
                </span>
              </h4>
              <h4 class="titleHeaders ">
                حجم معاملات دیروز:
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(cryptolive.yesterdayData.volume / 1000000, 2)
                    )
                  }}
                  میلیون
                </span>
              </h4>
              <h4 class="titleHeaders ">
                ارزش بازار دیروز:
                <v-icon small>mdi-currency-usd</v-icon>
                <span class="spandata"
                  >{{
                    numberWithCommas(
                      this.roundTo(
                        cryptolive.yesterdayData.marketCap / 1000000,
                        2
                      )
                    )
                  }}
                  میلیون</span
                >
              </h4>
            </div>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12">
        <liveWidget
          :statistics="stats"
          :hh="hhdata"
          :liveData="livedata"
        ></liveWidget>
      </div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import liveWidget from "@/view/pages/Crypto/Widgets/CryptoLiveWidget.vue";
// import SubHeaderWidget from "@/view/pages/Crypto/Widgets/CryptoSubHeader.vue";

export default {
  name: "cryptoSingle",
  components: {
    liveWidget
    // SubHeaderWidget
  },
  data() {
    return {
      search: "",
      logourl: "",
      subheaders: {},
      // allowed: [],
      stats: [],
      hhdata: [],
      livedata: [],
      cryptolive: [],
      lastUpdated: ""
    };
  },
  created() {
    document.title = "Finwise - رمز ارز";
  },
  mounted() {
    this.loadData();
    // setInterval(() => {
    //     // this.getLivePrices()
    // }, 5000);
  },
  watch: {
    "$route.params": {
      handler(newValue, oldValue) {
        if (newValue != oldValue) {
          //   this.loadData();

          this.$store.dispatch(SET_BREADCRUMB, [{ title: "رمزارز" }]);
          this.$store.dispatch(ADD_BREADCRUMB, [
            { title: "خلاصه اطلاعات رمزارز" }
          ]);
        }
      },
      immediate: true
    }
  },
  methods: {
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      if (n == "-") {
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
      // this.getAllowed().then(response => {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(responx => {
        // eslint-disable-next-line no-unused-vars
        this.getLivePrices().then(reposonseY => {});
      });
      // });
    },
    // async getAllowed() {
    //   await this.axios
    //     .get("/api/tickerallnames")
    //     .then(response3 => {
    //       this.allowed = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },

    async getOne() {
      await this.axios
        .get("/api/CryptoSingleBasic/" + this.$route.params.id + "/")
        .then(response1 => {
          this.subheaders = response1.data[0];
          this.logourl = this.subheaders.logoUrl;
          this.$store.dispatch(ADD_BREADCRUMB, [
            { title: this.subheaders.name }
          ]);
          document.title = "Finwise - " + this.subheaders.original_symbol;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getLivePrices() {
      await this.axios
        .get("/api/CryptoSingleLive/" + this.subheaders.original_symbol + "/")
        .then(response1 => {
          this.cryptolive = response1.data;
          this.lastUpdated = new Date();
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
.web-icon{
  color:black
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
