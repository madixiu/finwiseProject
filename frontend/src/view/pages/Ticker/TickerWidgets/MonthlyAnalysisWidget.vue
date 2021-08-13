<template>
  <div>
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        تحلیل
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading == false"
        ></b-spinner>
      </h3>
    </div> -->
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column" v-if="type == 'bank'"></div>
    <div class="card-body d-flex flex-column" v-if="type == 'insurance'"></div>
    <v-row no-gutters v-if="type == 'production'">
      <v-card rounded="lg" class="mt-2" width="100%">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >روند تولید و فروش کل</v-toolbar-title
          >
          <v-spacer></v-spacer>
          <v-col class="d-flex justify-content-end" cols="3">
            <v-select
              class="vuetifySelectCustom flex-grow-1"
              :items="Chart1"
              v-model="Chart1Selected"
              solo-inverted
              dense
              @input="GetFiltered"
            ></v-select>
          </v-col>
        </v-toolbar>

        <!-- <v-row
            ><v-col></v-col>
            <v-col></v-col>
            <v-col></v-col>
            <v-col
              ><v-select
                :items="Chart1"
                filled
                v-model="Chart1Selected"
                label="بازه نمودار "
                dense
                @input="GetFiltered"
              ></v-select></v-col
          ></v-row> -->

        <ApexChart
          :key="ApexChartcomponentKey"
          height="200%"
          width="100%"
          :series="Chart1options.series"
          :chartOptions="Chart1options"
        />
      </v-card>
      <v-card rounded="lg" class="mt-2" width="100%">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >روند تولید و فروش به تفکیک صادراتی و داخلی</v-toolbar-title
          >
          <v-spacer></v-spacer>
        </v-toolbar>
        <ApexChart
          :key="ApexChartcomponentKey2"
          height="200%"
          width="100%"
          :series="Chart2options.series"
          :chartOptions="Chart2options"
        />
      </v-card>
    </v-row>

    <div class="card-body d-flex flex-column" v-if="type == 'leasing'"></div>
    <div class="card-body d-flex flex-column" v-if="type == 'service'"></div>
    <div class="card-body d-flex flex-column" v-if="type == 'investment'"></div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'construction'"
    ></div>
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
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "MonthlyAnalysisWidget",
  props: ["notices", "deposits", "portfos", "summaries", "typeOf"],
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
      Chart2options: {
        series: [],
        chart: {
          type: "bar",
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
      DataItems2: [],
      DataItems3: [],
      DataItems4: [],
      DataItems5: [],
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
    AllProductionItems() {
      let x = [];
      let y = [];
      let counter = 0;
      this.notices.filter(item => {
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
    gettabs() {
      var lookup = {};
      var lookup2 = {};
      var items = this.notices;
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
      this.ProductionDataToRender();
    },
    setType() {
      this.type = this.typeOf;
      let uniqeItems = [];
      this.notices.filter(item => {
        if (!uniqeItems.includes(item.name)) {
          uniqeItems.push(item.name);
        }
      });
      this.Chart1ItemsSelected = uniqeItems;
      this.ProductionDataToRender();
    },
    ProductionDataToRender() {
      let AcceptedDates = [];
      let AcceptedDates2 = [];
      if (this.Chart1Selected == "۶ ماه گذشته") {
        let A = this.todates.slice(0, 6).map(({ value }) => value);
        AcceptedDates = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.deposits.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "از ابتدای سال") {
        for (var item, i = 0; (item = this.notices[i++]); ) {
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
        AcceptedDates = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "۳ سال گذشته") {
        let A = this.todates.slice(0, 36).map(({ value }) => value);
        AcceptedDates = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "۵ سال گذشته ") {
        let A = this.todates.slice(0, 60).map(({ value }) => value);
        AcceptedDates = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.notices.filter(item => {
          if (A.includes(item.toDate)) {
            return item;
          }
        });
      }
      if (this.Chart1Selected == "از ابتدا") {
        let A = this.todates.map(({ value }) => value);
        AcceptedDates = this.notices.filter(item => {
          // console.log(item.category)
          if (A.includes(item.toDate)) {
            return item;
          }
        });
        AcceptedDates2 = this.notices.filter(item => {
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
      let FinalData = [];
      let FinalData2 = [];
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
    notices() {
      this.gettabs();
      this.setType();
      // this.gettabs();
      // this.getOnesfromthisyear();
      this.loading = false;
    },
    deposits() {
      this.setType();
      // this.gettabs();
      // this.getOnesfromthisyear();
      this.loading = false;
    },
    portfos() {
      this.setType();
      // this.gettabs();
      // this.getOnesfromthisyear();
      this.loading = false;
    },
    summaries() {
      this.setType();
      // this.gettabs();
      // this.getOnesfromthisyear();
      this.loading = false;
    },
    selectedYear() {
      this.setType();
      // this.gettabs();
      // this.getOnesfromthisyear();
      this.loading = false;
    }
  }
};
</script>
<style scoped>
.vuetifySelectCustom /deep/ .v-input__control {
  min-height: 25px !important;
  height: 25px !important;
}
.vuetifySelectCustom /deep/ .v-input__control {
  font-size: 0.7em !important;
}
.vuetifySelectCustom /deep/ .v-chip.v-size--small {
  border-radius: 3px;
  font-size: 10px;
  height: 17px;
}
.vuetifySelectCustom /deep/ .v-chip .v-chip__close.v-icon {
  font-size: 12px !important;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}

.itemFilters {
  font-family: "Vazir-Light-FD";
  font-weight: 700;
  font-size: 1em;
}
</style>
