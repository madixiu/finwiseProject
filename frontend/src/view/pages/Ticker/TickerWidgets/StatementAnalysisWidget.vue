<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        روندهای صورتهای مالی
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading == true"
        ></b-spinner>
      </h3>
    </div>
    <div class="row" style="padding-top:5px" v-if="loading == false">
      <div class="col-xxl-12 col-md-12 col-sm-12 col-xs-12">
        <v-card shaped class="mt-2">
          <v-toolbar dense>
            <v-toolbar-title>روند آیتم های ترازنامه</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-row
            ><v-col></v-col>
            <v-col></v-col>
            <v-col>
                
            </v-col>
            <v-col
              ><v-select
                :items="Chart1"
                filled
                v-model="Chart1Selected"
                label="بازه نمودار "
                dense
                @input="GetFiltered"
              ></v-select></v-col
          ></v-row>

          <ApexChart
            :key="ApexChartcomponentKey"
            height="300%"
            width="100%"
            :series="Chart1options.series"
            :chartOptions="Chart1options"
          />
        </v-card>
      </div>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == '' && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "StatementAnalysisWidget",
  props: ["IS", "BS", "CF"],
  components: {
    ApexChart
  },
  data() {
    return {
      ApexChartcomponentKey: 0,
      ApexChartcomponentKey2: 0,
      Chart1options: {
        series: [],
        chart: {
          type: "bar",
          // background: '../../../../media/logos/fadedfinwise.png',
          stacked: true,
          toolbar: {
            show: true
          },
          zoom: {
            enabled: true
          }
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: {
                position: "bottom",
                offsetX: -10,
                offsetY: 0
              }
            }
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10
          }
        },
        xaxis: {
          // type: "datetime",
          categories: []
        },
        legend: {
          position: "right",
          offsetY: 40
        },
        fill: {
          opacity: 1
        }
      },
      Chart1ItemsSelected: [],
      Chart1AllItems: [{ key: 1, value: "" }],
      search: "",
      loading: true,
      type: "",
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      IncomeStatement: [],
      CashFlow: [],
      BalanceSheet: [],
      products: {},
      Chart1Data: [],
      Chart1: [
        "۶ ماه گذشته",
        "از ابتدای سال",
        "یک سال گذشته",
        "۳ سال گذشته",
        "۵ سال گذشته ",
        "از ابتدا"
      ],
      Chart1Selected: "۶ ماه گذشته",
      Chart1Categories: [],
      uniqeItems: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    AllProductionItems() {
      let x = [];
      let y = [];
      let counter = 0;
      this.DataItems2.filter(item => {
        counter = counter + 1;
        let temp = {};
        if (!y.includes(item.name)) {
          y.push(item.name);
          temp["key"] = counter;
          temp["value"] = item.name;
          x.push(temp);
        }
      });
      return x;
    }
  },
  methods: {
    numberWithCommas(x) {
      if (x === null) {
        return "-";
      }
      if (x == 0) {
        return "-";
      }
      if (x == "") {
        return "-";
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    roundTo(n, digits) {
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
    categoryProduct(x) {
      if (x === null) {
        return "";
      }
      if (x == "Domestic_Sale") {
        return "فروش داخلی";
      }
      if (x == "Export_Sale") {
        return "فروش صادراتی";
      }
      if (x == "Whole") {
        return "عمده";
      }
      if (x == "Discount") {
        return "تخفیف";
      }
      if (x == "Refund") {
        return "بازگشت از فروش";
      }
      if (x == "Service_revenue") {
        return "خدمات";
      }
      return "";
    },
    populateData() {
      this.IncomeStatement = this.IS;
      this.BalanceSheet = this.BS;
      this.CashFlow = this.CF;
      // console.log(this.DataItems2);
    },
    gettabs() {
      var lookup = {};
      var lookup2 = {};
      var items = this.BalanceSheet;
      var result = [];
      var result2 = [];
      var counter = 0;
      for (var item, i = 0; (item = items[i++]); ) {
        var name = item.toDate;
        if (!(name in lookup)) {
          lookup[name] = 1;
          var itemOne = {};
          itemOne["key"] = counter;
          itemOne["value"] = name;
          result.push(itemOne);
          counter += 1;
        }
        if (!(name.split("/")[0] in lookup2)) {
          lookup2[name.split("/")[0]] = 1;
          var itemTwo = {};
          itemTwo["key"] = counter;
          itemTwo["value"] = name.split("/")[0];
          result2.push(itemTwo);
          counter += 1;
        }
      }
      this.todates = result;
      this.todatesyears = result2;
    },
    GetFiltered() {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.ProductionDataToRender();
    },
    DataToRender() {
      let AcceptedDates = [];
      let AcceptedDates2 = [];
      if (this.Chart1Selected == "۶ ماه گذشته") {
        let A = this.todates.slice(0, 6).map(({ value }) => value);
        AcceptedDates = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.DataItems3.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "از ابتدای سال") {
        for (var item, i = 0; (item = this.DataItems2[i++]); ) {
          let name = item.toDate;
          let x = this.todatesyears[0].value;
          if (name.includes(x)) {
            AcceptedDates.push(item);
          }
          if (name.includes(x)) {
            AcceptedDates2.push(item);
          }
        }
      }
      if (this.Chart1Selected == "یک سال گذشته") {
        let A = this.todates.slice(0, 12).map(({ value }) => value);
        AcceptedDates = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "۳ سال گذشته") {
        let A = this.todates.slice(0, 36).map(({ value }) => value);
        AcceptedDates = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "۵ سال گذشته ") {
        let A = this.todates.slice(0, 60).map(({ value }) => value);
        AcceptedDates = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "از ابتدا") {
        let A = this.todates.map(({ value }) => value);
        AcceptedDates = this.DataItems2.filter(item => {
          // console.log(item.category)
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.DataItems2.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      this.Chart1Data = AcceptedDates;
      this.Chart2Data = AcceptedDates2;
      this.Chart1Categories = [];
      this.Chart1Data.filter(item => {
        if (!this.Chart1Categories.includes(item.toDate)) {
          this.Chart1Categories.push(item.toDate);
        }
      });
      this.Chart1Categories.sort((a, b) => b - a);
      // console.log(this.Chart1Categories);
      this.Chart1options.xaxis.categories = this.Chart1Categories;
      this.Chart2options.xaxis.categories = this.Chart1Categories;
      this.ApexChartcomponentKey = this.ApexChartcomponentKey + 1;
      this.ApexChartcomponentKey2 = this.ApexChartcomponentKey2 + 1;
      let ShowData = [];
      let ShowData2 = [];
      let uniqeItems = [];
      let uniqeItems2 = [];
      this.Chart1Data.filter(item => {
        let k = {};
        k["name"] = item.name;
        if (!uniqeItems.includes(item.name)) {
          uniqeItems.push(item.name);
        }
        k["toDate"] = item.toDate;
        k["Sale"] = item.Sale;
        ShowData.push(k);
      });
      this.Chart2Data.filter(item => {
        let k = {};
        k["name"] = item.category;
        if (!uniqeItems2.includes(item.category)) {
          uniqeItems2.push(item.category);
        }
        k["toDate"] = item.toDate;
        k["Sale"] = item.Sale;
        ShowData2.push(k);
      });
      // console.log(ShowData);
      let FinalData = [];
      let FinalData2 = [];
      // let DoneDates=[]
      let c = 0;
      for (let j in uniqeItems) {
        c = c + 1;
        this.Chart1AllItems.push({ key: c, value: "j" });
        let IT2 = uniqeItems[j];
        let temp = {};
        temp["name"] = IT2;
        temp["data"] = [];
        ShowData.filter(item2 => {
          if (item2.name == IT2) {
            temp["data"].push(item2.Sale);
          }
        });
        FinalData.push(temp);
      }
      for (let j in uniqeItems2) {
        let IT2 = uniqeItems2[j];
        let temp = {};
        temp["name"] = IT2;
        temp["data"] = [];
        ShowData2.filter(item2 => {
          if (item2.name == IT2) {
            temp["data"].push(item2.Sale);
          }
        });
        FinalData2.push(temp);
      }
      this.Chart1options.series = FinalData;
      this.Chart2options.series = FinalData2;
      // this.Chart1ItemsSelected=uniqeItems
      // console.log(this.Chart1AllItems);
    }
  },
  mounted() {},
  watch: {
    IS() {
      this.populateData();
      this.gettabs();
    //   this.DataToRender();
      this.loading = false;
    },
    BS() {
      this.populateData();
      this.gettabs();
      this.loading = false;
    },
    CF() {
      this.populateData();
      this.setType();
      this.loading = false;
    }
  }
};
</script>
<style scoped>
.cellItem {
  font-family: "Dirooz FD";
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
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
.itemFilters {
  font-family: "Dirooz FD";
  font-weight: 700;
  font-size: 1em;
}
table.v-table tbody td {
  font-family: "Dirooz FD" !important;
}
</style>
