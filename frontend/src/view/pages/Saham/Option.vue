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
            thClass="bb-table-head"
            class="bb-table"
            tbody-tr-class="bb-table-row"
            :sticky-header="height"
            dense
            :busy.sync="isBusy"
            :filter="filter"
            :filter-debounce="1200"
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
              <b class="bb-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(UnderLying)="data">
              <b class="bb-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(StrikePrice)="data">
              <b class="bb-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>

            <template #cell(AssetPrice)="data">
              <b class="bb-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(DifferenceToAverage)="data">
              <b v-if="data.value == 0" class="bb-table-cell">{{
                data.value
              }}</b>
              <b v-if="data.value > 0" class="bb-table-cell-green">{{
                data.value
              }}</b>
              <b
                v-if="
                  data.value < 0 &&
                    data.value != -100001 &&
                    data.value != -100000
                "
                class="bb-table-cell-red"
                >{{ data.value }}</b
              >
              <b v-if="data.value == -100001" class="bb-table-cell">{{
                "سفارش فروش ندارد"
              }}</b>
              <b v-if="data.value == -100000" class="bb-table-cell-red">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(PPP)="data">
              <b v-if="data.value > 0" class="bb-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value < 0" class="bb-table-cell-red">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value == 0" class="bb-table-cell">{{
                data.value.toLocaleString()
              }}</b>
            </template>
            <template #cell(ArzandegiLast)="data">
              <b v-if="data.value > 0" class="bb-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value < 0" class="bb-table-cell-red">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value == 0" class="bb-table-cell">{{
                data.value.toLocaleString()
              }}</b>
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
                      thClass="bb-table-head"
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
    isBusy: true,
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
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "دارایی پایه",
        key: "UnderLying",
        width: "100",
        thClass: "bb-table-head",
        sortable: true
      },

      {
        label: "قیمت اعمال",
        key: "StrikePrice",
        width: "100",
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "فاصله تا سر رسید",
        key: "TTM",
        width: "130",
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "قیمت دارایی پایه",
        key: "AssetPrice",
        width: "120",
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "قیمت عادلانه",
        key: "averageFairprice",
        width: "230",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle: "قیمت به دست آمده از مدل بلک شولز"
      },
      {
        label: "قیمت بهترین سفارش فروش",
        key: "priceseller",
        width: "130",
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "حجم بهترین سفارش  فروش",
        key: "volumeseller",
        width: "130",
        thClass: "bb-table-head",
        sortable: true
      },

      {
        label: "ارزندگی بهترین سفارش فروش",
        key: "DifferenceToAverage",
        width: "200",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle:
          "اختلاف قیمت میان بهترین سفارش فروش و قیمت عادلانه تقسیم بر قیمت عادلانه است که هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی قرارداد ارزان تر از قیمت واقعی اش می باشد"
      },

      {
        label: "پوشش قیمت سهام با بهترین سفارش فروش",
        key: "PPP",
        width: "200",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن و قیمت اعمال تقسیم بر قیمت کنونی سهام است که این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "پرداخت کنونی بهترین سفارش(میلیون ریال)",
        key: "TotalValue",
        width: "120",
        thClass: "bb-table-head",
        sortable: true
      },
      {
        label: "پرداخت نهایی بهترین سفارش(میلیون ریال)",
        key: "FinalPayment",
        width: "100",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، در روز اعمال باید پرداخته شود"
      },
      {
        label: "قیمت آخرین معامله",
        key: "LastTrade",
        width: "130",
        thClass: "bb-table-head",
        sortable: true
      },

      {
        label: "ارزندگی آخرین معامله",
        key: "DifferenceToLast",
        width: "200",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle:
          "اختلاف قیمت میان آخرین معامله و قیمت عادلانه تقسیم بر قیمت عادلانه است که هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی قرارداد ارزان تر از قیمت واقعی اش می باشد"
      },
      {
        label: "پوشش قیمت سهام با آخرین معامله",
        key: "ArzandegiLast",
        width: "130",
        thClass: "bb-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن و قیمت اعمال تقسیم بر قیمت کنونی سهام است که این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "حجم",
        key: "TradeVolume",
        width: "100",
        thClass: "bb-table-head",
        sortable: true
      }
    ]
  }),

  computed: {
    ...mapGetters(["getSahm"])
  },
  mounted() {
    // websocket//////////////////////////
    // this.$socket.onopen = (data) => console.log('data' + data);
    // this.$socket.onmessage = (data) => {
    // // console.log("data firm live is: " +data.data)
    // let obj = new Array()
    // obj = JSON.parse(data.data)
    // this.$store.dispatch('setSocketMessage',obj)
    this.loadData();

    // setInterval(() => {

    //       this.OptionTableReq()

    // }, 5000)

    this.height = this.getHeight();
    // console.log(window.innerHeight);
    // defer the execution of anonymous function for
    // 3 seconds and go to next line of code.
    // sleep(2000).then(() => { console.log("World!"); });
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
          console.log(data);
          if (data != "noData") {
            this.OptionAsset = data;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    async OptionTableReq() {
      this.isBusy = true;
      await this.axios
        .get("/api/options")
        .then(response => {
          let data = response.data;
          this.isBusy = false;
          console.log(data);
          if (data != "noData") {
            this.$store.dispatch("setSahm", data);
          }
        })
        .catch(error => {
          this.isBusy = false;
          console.log(error);
        });
    },
    getHeight() {
      //  return (window.innerHeight * 75)/100
      return (window.innerHeight - 150).toString() + "px";
    }
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
.bb-table-head {
  font-size: 0.8rem !important;
  font-weight: 500;
}
.bb-table {
  text-align: center;
  font-size: 1em;
  line-height: 1;
}
.bb-table-row:hover {
  background-color: #999999 !important;
}
.bb-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
}
.bb-table-cell-green {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
}
.bb-table-cell-red {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
}
.bb-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
}
.bb-table-row {
  direction: ltr;
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
