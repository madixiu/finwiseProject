<template>
  <div>
    <div class="row">
      <div class="col-12">
        <div class="row">
          <!-- custom card1 -->
          <div
            class="px-sm-2 pb-2 pb-sm-6 px-xs-0 col-sm-2 col-md-2 col-lg-2 col-12"
          >
            <!-- <div class="filterBox"> -->
            <v-card round elevation="15">
              <v-toolbar dense flat>
                <v-toolbar-title v-if="card1Key">نرخ بهره</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-btn v-if="card1Key" icon @click="card1Key = !card1Key">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
                <v-btn v-if="!card1Key" icon @click="card1Key = !card1Key">
                  <v-icon>mdi-arrow-left</v-icon>
                </v-btn>
              </v-toolbar>
              <div class="filterBox">
                <transition name="fade">
                  <div v-if="card1Key" key="1">
                    <v-data-table
                      fixed-header
                      height="196"
                      :headers="card1Header"
                      :items="card1Items"
                      item-key="name"
                      class="elevation-1 cardTable"
                      :hide-default-footer="true"
                    ></v-data-table>
                  </div>

                  <div
                    v-if="!card1Key"
                    class="cardExplanation ml-4 mr-4"
                    key="2"
                  >
                    <p>
                      در این جدول مفروضات مدل قیمت گذاری آپشن و محاسبه ی لحظه ای
                      آن قرار داده شده است. مدل قیمت گذاری با ۴ مقدار کمینه،
                      بیشینه، محاسبه شده از اوراق و سود بانکی برای نرخ بهره بدون
                      ریسک (Risk-Free Rate) قرار داده شده است. قیمت گذاری برای
                      ۲۰ حالت مختلف ( ۵ حالت از تلاطم دارايی پایه [۳ ماهه، ۶
                      ماهه، یک ساله، دو ساله و پنج ساله] و ۴ حالت نرخ بهره بدون
                      ریسک) انجام شده و اطلاعات جدول زیر محاسبه گردیده است.
                    </p>
                  </div>
                </transition>
              </div>
              <v-card-actions>
                <span class="cardFooter">{{ card1Items.length }}</span>
                <span v-if="card1Items.length" class="cardFooter mr-2"
                  >نتیجه</span
                >
              </v-card-actions>
            </v-card>
          </div>

          <!-- custom card2 -->

          <div
            class="px-sm-2 pb-2 pb-sm-6 px-xs-0 col-sm-2 col-md-2 col-lg-2 col-12"
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
              Lorem ipsum, or lipsum as it is sometimes known, is dummy text
              used in laying out print, graphic or web designs. The passage is
              attributed to an unknown typesetter in the 15th century who is
              thought to have scrambled parts of Cicero's De Finibus Bonorum et
              Malorum for use in a type specimen book.
            </v-card>
          </div>
        </div>
      </div>
      <div class="col-12">
        <v-card>
          <b-col lg="4" class="my-1">
            <b-input-group size="sm">
              <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="جستجو"
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
            striped
            sticky-header
            dense
            :filter="filter"
            bordered
            outlined
            small
            hover
            responsive
            foot-clone
            :items="getSahm"
            :fields="headersBoot"
            @filtered="onFiltered"
          >
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
              <b v-if="data.value > 0" class="bb-table-cell-green">{{
                data.value
              }}</b>
              <b v-if="data.value < 0" class="bb-table-cell-red">{{
                data.value
              }}</b>
            </template>
            <template #cell(PPP)="data">
              <b v-if="data.value > 0" class="bb-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value < 0" class="bb-table-cell-red">{{
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
      <div class="col-3">
        <v-card>
          <div class="Mychips pt-5 pb-5 pr-3 pl-3">
            <v-chip class="mx-auto" label large>
              نرخ بهره
              <v-chip color="#ad0018" small dark label class="mr-3">
                17%
              </v-chip>
            </v-chip>
          </div>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Option",

  data: () => ({
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
    card1Items: [
      {
        round: "۱۷%",
        ticker: "فولاد"
      }
    ],
    tab: "tab-1",
    filterName: "",
    temp: [],
    flag: 0,
    filter: null,
    height: 400,
    search: "",
    headersBoot: [
      { label: "نماد", key: "Nemad", thClass: "bb-table-head" },
      { label: "دارایی پایه", key: "UnderLying", width: "100" },
      { label: "پرداخت نهایی", key: "FinalPayment", width: "100" },
      { label: "مبلغ کل اردر اول", key: "Totalkey", width: "120" },
      { label: "قیمت اعمال", key: "StrikePrice", width: "100" },
      { label: "قیمت دارایی پایه", key: "AssetPrice", width: "120" },
      {
        label: "فاصله تا قیمت عادلانه",
        key: "DifferenceToAverage",
        width: "200"
      },
      {
        label: "میانگین قیمت عادلانه",
        key: "averageFairprice",
        width: "130"
      },
      { label: "قیمت اردر فروش", key: "priceseller", width: "130" },
      { label: "حجم اردر فروش", key: "volumeseller", width: "130" },
      { label: "فاصله تا سر رسید", key: "TTM", width: "130" },
      {
        label: "قیمت فروش+قیمت قرارداد / قیمت دارایی پایه",
        key: "PPP",
        width: "200"
      },
      { label: "حجم قرارداد", key: "TradeVolume", width: "100" },
      { label: "قیمت آخرین معامله", key: "LastTrade", width: "130" },
      { label: "ارزندگی آخرین معامله", key: "ArzandegiLast", width: "130" },
      {
        label: "فاصله آخرین معامله تا قیمت عادلانه",
        key: "DifferenceToLast",
        width: "200"
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
    changeTab() {
      if (this.tab == "tab-2") this.tab = "tab-1";
      else this.tab = "tab-2";
    },

    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    makeToast(item) {
      // console.log(this.$store.getters.getSahm[0].DifferenceToLast);
      // console.log(this.$store.getters.getSahm.length);
      this.$bvToast.toast(item.DifferenceToLast, {
        title: item.Nemad,
        variant: "success",
        solid: false,
        noAutoHide: true,
        toaster: "b-toaster-bottom-left",
        enableSounds: true,
        sounds: {
          info:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233294/info.mp3",
          // path to sound for successfull message:
          success:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233524/success.mp3",
          // path to sound for warn message:
          warning:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233563/warning.mp3",
          // path to sound for error message:
          error:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233574/error.mp3"
        }
      });
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
      let vm = this;
      await this.axios
        .get("/api/options")
        .then(response => {
          let data = response.data;
          // var cars = new Array();
          // cars = response.data
          // var json = JSON.parse(update);
          console.log(data);
          if (data != "noData") {
            this.$store.dispatch("setSahm", data);
            let items = data;

            for (let item of items) {
              if (item.TradeVolume != 0 && item.DifferenceToLast > 0.2) {
                if (this.flag == 0) {
                  vm.makeToast(item);
                  this.temp.push(item);
                  this.flag++;
                } else {
                  for (let tempItem of this.temp) {
                    if (
                      tempItem.Nemad == item.Nemad &&
                      tempItem.DifferenceToLast != item.DifferenceToLast
                    ) {
                      vm.makeToast(item);
                      this.temp.pop();
                      this.temp.push(item);
                    }
                  }
                }
              }
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getHeight() {
      //  return (window.innerHeight * 75)/100
      return window.innerHeight - 77;
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
  font-size: 0.8rem;
  font-weight: 500;
}
.bb-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.bb-table-row:hover {
  background-color: #999999 !important;
}
.bb-table-cell {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
}
.bb-table-cell-green {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: green;
  font-weight: 400;
}
.bb-table-cell-red {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: red;
  font-weight: 400;
}
.bb-table-cell-bold {
  text-align: center;
  font-size: 0.8rem;
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
