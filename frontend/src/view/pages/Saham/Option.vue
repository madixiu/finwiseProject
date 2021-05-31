<template>
  <div>
    <div class="row">
      <!-- OPTION TABLE *************************************************** -->
      <div class="col-12">
        <v-card>
          <b-col lg="4">
            <b-input-group size="sm">
              <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="فیلتر"
              ></b-form-input>
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''"
                  >پاک کردن</b-button
                >
              </b-input-group-append>
            </b-input-group>
          </b-col>
          <b-table
            thClass="option-table-head"
            class="option-table"
            tbody-tr-class="option-table-row"
            :sticky-header="height"
            dense
            striped
            :busy.sync="isBusy"
            :filter="filter"
            :filter-included-fields="filterOn"
            :filter-debounce="100"
            :sort-desc.sync="sortDesc"
            :sort-by.sync="sortBy"
            sort-direction="desc"
            sort-icon-left
            bordered
            no-border-collapse
            outlined
            small
            hover
            responsive
            :items="getSahm"
            :fields="headersBoot"
            @filtered="onFiltered"
          >
            <template #table-busy>
              <div class="text-center text-danger my-2">
                <b-spinner class="align-middle mr-2"></b-spinner>
                <strong>شکیبا باشید</strong>
              </div>
            </template>
            <template #cell(Nemad)="data">
              <b class="option-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(UnderLying)="data">
              <b class="option-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(StrikePrice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(TTM)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(averageFairprice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(priceseller)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(volumeseller)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(AssetPrice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(DifferenceToAverage)="data">
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value
              }}</b>
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -10001 && data.value != -10000
                "
                class="option-table-cell-red"
                >{{ data.value }}</b
              >
              <b v-if="data.value == -10001" class="option-table-cell-s">{{
                "سفارش فروش ندارد"
              }}</b>
              <b v-if="data.value == -10000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(PPP)="data">
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value.toLocaleString() }}</b
              >
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "سفارش فروش ندارد"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value.toLocaleString()
              }}</b>
            </template>
            <template #cell(TotalValue)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(FinalPayment)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(LastTrade)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(DifferenceToLast)="data">
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value }}</b
              >
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value
              }}</b>
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "بدون معامله"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(ArzandegiLast)="data">
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value.toLocaleString() }}</b
              >
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "بدون معامله"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(TradeVolume)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
          </b-table>
        </v-card>
      </div>

      <!-- EXTRA STUFF ************************************************************************* -->
      <div class="col-12">
        <div class="row">
          <!-- custom card1 -->

          <!-- custom card2 -->

          <div
            class="px-sm-2 pb-2 pb-sm-6 px-xs-0 col-sm-4 col-md-4 col-lg-4 col-12"
          >
            <!-- <div class="filterBox"> -->
            <v-card round elevation="15">
              <v-toolbar dense flat>
                <v-toolbar-title v-if="card2Key">تلاطم</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-btn v-if="card2Key" icon @click="card2Key = !card2Key">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
                <v-btn v-if="!card2Key" icon @click="card2Key = !card2Key">
                  <v-icon>mdi-arrow-left</v-icon>
                </v-btn>
              </v-toolbar>
              <div class="filterBox">
                <transition name="fade">
                  <div v-if="card2Key" key="1">
                    <v-data-table
                      thClass="option-table-head"
                      fixed-header
                      height="196"
                      :headers="card1Header"
                      :items="OptionAsset"
                      item-key="name"
                      class="elevation-1 cardTable"
                      :hide-default-footer="true"
                    ></v-data-table>
                  </div>

                  <div
                    v-if="!card2Key"
                    class="cardExplanation ml-4 mr-4"
                    key="2"
                  >
                    <p>
                      در این جدول مقدار تلاطم (Volatility) یک ساله برای دارایی
                      های پایه قابل مشاهده است. محاسبه این مقادیر به کمک قیمت
                      تعدیل شده انجام گرفته است.
                    </p>
                  </div>
                </transition>
              </div>
              <v-card-actions>
                <span class="cardFooter">{{ OptionAsset.length }}</span>
                <span v-if="OptionAsset.length" class="cardFooter mr-2"
                  >نتیجه</span
                >
              </v-card-actions>
            </v-card>
          </div>
          <div class="col-8">
            <v-card height="280">
              <v-card-title>
                <i class="flaticon2-pen text-danger"></i>

                <span>نحوه محاسبه</span>
              </v-card-title>
              <div style="direction:rtl;text-align:right" class="mr-5 ml-5">
                <span
                  >در این قسمت محاسباتی برای معامله بهتر اختیارات خرید به
                  کاربران ارائه شده است. قیمت های عادلانه با استفاده از مدل بلک
                  شولز محاسبه شده اند. نرخ بهره با ۴ سناریوی مختلف و تلاطم در ۵
                  بازه زمانی کوتاه مدت تا بلند مدت محاسبه و نهایتا ۲۰ سناریو
                  متفاوت برای قیمت اختیار در نظر گرفته می شود. میانگین وزنی این
                  ۲۰ سناریو به عنوان خروجی نهایی قیمت عادلانه معرفی شده است.
                  برای اطلاعات بیشتر نشانگر را روی نام هر ستون قرار دهید.</span
                >
              </div>
            </v-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Option",

  data: () => ({
    WebsocketRequest: false,
    isBusy: true,
    filterOn: ["Nemad", "UnderLying"],
    sortDesc: true,
    sortBy: "DifferenceToAverage",
    OptionAsset: [],
    card1Key: true,
    card2Key: true,
    card1Header: [
      { text: "اسم سهم", align: "center", value: "ticker", sortable: false },
      {
        text: "مقدار تلاطم",
        align: "center",
        value: "round",
        sortable: false
      }
    ],
    filter: null,
    height: "450px",
    search: "",
    headersBoot: [
      {
        label: "نماد",
        key: "Nemad",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "دارایی پایه",
        key: "UnderLying",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "قیمت اعمال",
        key: "StrikePrice",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "فاصله تا سر رسید",
        key: "TTM",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "قیمت دارایی پایه",
        key: "AssetPrice",
        width: "120",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "قیمت عادلانه",
        key: "averageFairprice",
        width: "230",
        thClass: "option-table-head",
        sortable: true,
        headerTitle: "قیمت به دست آمده از مدل بلک شولز"
      },
      {
        label: "قیمت بهترین سفارش فروش",
        key: "priceseller",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "حجم بهترین سفارش فروش",
        key: "volumeseller",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "ارزندگی بهترین سفارش فروش",
        key: "DifferenceToAverage",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },

      {
        label: "پوشش قیمت سهام با بهترین سفارش فروش",
        key: "PPP",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "پرداخت کنونی بهترین سفارش(میلیون ریال)",
        key: "TotalValue",
        width: "120",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، امروز باید پرداخت شود"
      },
      {
        label: "پرداخت نهایی بهترین سفارش(میلیون ریال)",
        key: "FinalPayment",
        width: "100",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، در روز اعمال باید پرداخت شود"
      },
      {
        label: "قیمت آخرین معامله",
        key: "LastTrade",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "ارزندگی آخرین معامله",
        key: "DifferenceToLast",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },
      {
        label: "پوشش قیمت سهام با آخرین معامله",
        key: "ArzandegiLast",
        width: "130",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت آخرین معامله آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "حجم",
        key: "TradeVolume",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      }
    ]
  }),

  computed: {
    ...mapGetters(["getSahm"])
  },
  created() {
    document.title = "Finwise - آپشن";
  },
  mounted() {
    this.loadData();

    this.height = this.getHeight();

    this.liveChecker();
    this.$socketOptions.onmessage = data => {
      // this.DataItems = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
        this.$store.dispatch("setSahm", JSON.parse(data.data));
    };
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.OptionAssetReq().then(response => {
        this.OptionTableReq();
      });
      // this.OptionAssetReq().then(this.OptionTableReq());
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    async OptionAssetReq() {
      await this.axios
        .get("/api/ViewOptionAssetVolatility")
        .then(response => {
          let data = response.data;
          if (data != "noData") {
            this.OptionAsset = data;
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    async OptionTableReq() {
      this.isBusy = true;
      await this.axios
        .get("/api/options")
        .then(response => {
          let data = response.data;
          this.isBusy = false;
          if (data != "noData") {
            this.$store.dispatch("setSahm", data);
          }
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    getHeight() {
      return (window.innerHeight - 150).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketOptions.send(JSON.stringify(barier));
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (
        date.getHours() > 8 &&
        date.getHours() < 14 &&
        date.getDay() != 5 &&
        date.getDay() != 4
      ) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$$socketOptions.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.cardFooter {
  color: #7c6f68;
  font-size: 0.9rem;
}
.v-toolbar__content,
.v-toolbar__extension {
  padding: 0px 4px !important;
}
.filterBox {
  height: 196px;
  overflow: hidden;
  position: relative;
}
.cardExplanation {
  height: 196px;
  font-size: 0.8rem;
  text-align: right;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
/* always present */
.expand-transition {
  transition: all 0.6s ease;
  height: 30px;
  padding: 10px;
  background-color: #eee;
  overflow: hidden;
}
/* .expand-enter defines the starting state for entering */
/* .expand-leave defines the ending state for leaving */
.expand-enter,
.expand-leave {
  height: 0;
  padding: 0 10px;
  opacity: 0;
}
.list-enter,
.list-leave-to {
  visibility: hidden;
  height: 0;
  margin: 0;
  padding: 0;
  opacity: 0;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.3s;
}
.theme--light.v-data-table
  > .v-data-table__wrapper
  > table
  > thead
  > tr:last-child
  > th {
  border-bottom-width: 0px !important;
}
.cardTable {
  direction: rtl;
  text-align: right;
}
.Mychips {
  text-align: center;
}
.option-table-head {
  font-size: 1.1em !important;
  font-weight: 500;
}
.option-table {
  text-align: center;
  font-size: 0.8rem;
  vertical-align: middle !important;
  line-height: 1;
  font-family: "Vazir-Medium-FD";
}
.option-table-row:hover {
  background-color: #999999 !important;
}
@media screen and (max-width: 1366px) {
  .option-table-cell-s {
    vertical-align: middle !important;
    text-align: center;
    font-size: 0.9em;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (min-width: 1600px) {
  .option-table-cell-s {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (max-width: 1366px) {
  .option-table-cell-r {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    color: red;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (min-width: 1600px) {
  .option-table-cell-r {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    line-height: 1;
    color: red;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
.option-table-cell {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
/* .option-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
} */
.option-table-cell-green {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.option-table-cell-red {
  text-align: center;
  vertical-align: middle !important;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.option-table-cell-bold {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
  /* font-family: "Vazir-Medium-FD";  */
  font-family: "Vazir-Medium-FD";
}
.option-table-row {
  direction: ltr;
  vertical-align: middle !important;
}

/* .vxe-toolbar .vxe-button--wrapper {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  text-align: right !important;
}
.vxe-input--inner {
  border: 1px solid black !important;
}
.vxe-input {
  display: inline-block;
  position: relative;
  width: 300px !important;
  height: 30px !important;
  margin-right: 10px;
} */
</style>
