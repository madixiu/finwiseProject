<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        بررسی صورت سود و زیان
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading == true"
        ></b-spinner
        ><v-chip small v-if="loading == true">در حال بارگزاری</v-chip>
      </h3>
    </div>
    <div
      class="row"
      style="padding-top:5px"
      v-if="empty == false && loading == false"
    >
      <div class="col-xxl-12 col-md-12 col-sm-12 col-xs-12">
        <v-card shaped class="mt-2">
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >روند آیتم های ترازنامه</v-toolbar-title
            >
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-row>
            <v-col sm="6" md="4" lg="1">
              <v-select
                label="دوره ترازنامه"
                :items="ISCHART_Period"
                v-model="ISCHART_Period_Selected"
                filled
                dense
                @input="GetFiltered"
              ></v-select>
            </v-col>
            <v-col sm="6" md="4" lg="1">
              <v-select
                :items="ISCHART_Aggregated"
                filled
                v-model="ISCHART_Aggregated_Selected"
                label="تلفیقی"
                dense
                @input="GetFiltered"
              ></v-select>
            </v-col>

            <v-col sm="6" md="4" lg="2"
              ><v-select
                :items="ISCHART_Length"
                filled
                v-model="ISCHART_Length_Selected"
                label="بازه نمودار "
                dense
                @input="GetFiltered"
              ></v-select
            ></v-col>
            <v-col sm="12" md="12" lg="8">
              <v-autocomplete
                chips
                clearable
                deletable-chips
                dense
                filled
                multiple
                small-chips
                :items="ISCHART_Items"
                v-model="ISCHART_Items_Selected"
                label="آیتم"
                hint="آیتم های مورد نظر برای نمایش در چارت را انتخاب کنید"
                persistent-hint
                @input="GetFiltered"
              ></v-autocomplete>

              <!-- <v-select
                :items="ISCHART_Items"
                v-model="ISCHART_Items_Selected"
                label="آیتم"
                multiple
                chips
                hint="آیتم های مورد نظر برای نمایش در چارت را انتخاب کنید"
                persistent-hint
                @input="GetFiltered"
              ></v-select -->
            </v-col>
          </v-row>

          <ApexChart
            :key="ApexChartcomponentKey"
            height="300%"
            width="100%"
            :series="Chart1options.series"
            :chartOptions="Chart1options"
          />
        </v-card>
      </div>
      <!-- <div class="col-xxl-12 col-md-12 col-sm-12 col-xs-12">
        <v-card shaped class="mt-2">
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em">تفکیک گروه های ترازنامه</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-row>
            <v-col sm="6" md="6" lg="3">
              <v-select
                label="دوره ترازنامه"
                :items="ISCHART2_Period"
                v-model="ISCHART2_Period_Selected"
                filled
                dense
                @input="GetFiltered2"
              ></v-select>
            </v-col>
            <v-col sm="6" md="6" lg="3">
              <v-select
                :items="ISCHART2_Aggregated"
                filled
                v-model="ISCHART2_Aggregated_Selected"
                label="تلفیقی"
                dense
                @input="GetFiltered2"
              ></v-select>
            </v-col>

            <v-col sm="6" md="6" lg="3"
              ><v-select
                :items="ISCHART2_Length"
                filled
                v-model="ISCHART2_Length_Selected"
                label="بازه نمودار "
                dense
                @input="GetFiltered2"
              ></v-select
            ></v-col>
            <v-col sm="6" md="6" lg="3">
              <v-autocomplete
                dense
                filled
                :items="ISCHART2_Items"
                v-model="ISCHART2_Items_Selected"
                label="دسته بندی"
                hint="دسته ی مورد نظر برای نمایش در چارت را انتخاب کنید"
                persistent-hint
                @input="GetFiltered2"
              ></v-autocomplete>
            </v-col>
          </v-row>

          <ApexChart
            :key="ApexChartcomponentKey2"
            height="400%"
            width="100%"
            :series="Chart2options.series"
            :chartOptions="Chart2options"
          />
        </v-card>
      </div> -->
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="empty == true && loading == false"
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
  name: "IncomeStatementAnalysisWidget",
  props: ["ISAGG", "IS"],
  components: {
    ApexChart
  },
  data() {
    return {
      ApexChartcomponentKey: 0,
      ApexChartcomponentKey2: 0,
      Chart1options: {
        chart: {
          height: 350,
          type: "line",
          dropShadow: {
            enabled: true,
            color: "#000",
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2
          },
          toolbar: {
            show: false
          }
        },
        colors: ["#77B6EA", "#545454"],
        dataLabels: {
          enabled: true
        },
        stroke: {
          curve: "smooth"
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5
          }
        },
        markers: {
          size: 1
        },
        xaxis: {},
        yaxis: [
          {
            title: {
              text: "مبلغ (میلیون ریال)"
            }
          },
          {
            seriesName: "هر سهم",
            opposite: true,
            title: {
              text: "هر سهم (ریال)"
            }
          }
        ]
        // legend: {
        //   position: 'top',
        //   horizontalAlign: 'right',
        //   floating: true,
        //   offsetY: -25,
        //   offsetX: -5
        // }
      },
      Chart2options: {
        series: [],
        chart: {
          type: "bar",
          fontFamily: "Vazir-Medium-FD",
          // background: '../../../../media/logos/fadedfinwise.png',
          stacked: true,
          toolbar: {
            show: false
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
        noData: {
          text: "برای پارامترهای انتخابی داده ای وجود ندارد",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        xaxis: {
          // type: "datetime",
          categories: []
        },
        dataLabels: {
          enabled: false,
          formatter: function(x) {
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
          }
        },
        yaxis: {
          title: {
            text: "میلیون ریال",
            fontFamily: "Vazir-Medium-FD"
          },
          labels: {
            fontFamily: "Vazir-Medium-FD",
            formatter: function(x) {
              if (x === null || x === undefined) {
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
            }
          }
        },
        legend: {
          position: "right",
          offsetY: 40,
          fontFamily: "Vazir-Medium-FD"
        },
        fill: {
          opacity: 1
        }
      },
      loading: true,
      empty: false,
      todates: [],
      todatesyears: [],
      IncomeAgg: [],
      Income: [],
      Chart1Data: [],
      Chart1Categories: [],
      Chart2Data: [],
      Chart2Categories: [],
      ISCHART_Period: ["۳ ماهه", "۶ ماهه", "۹ ماهه", "۱۲ ماهه"],
      ISCHART_Period_Selected: "۱۲ ماهه",
      ISCHART_Aggregated: ["بدون تلفیق"],
      ISCHART_Aggregated_Selected: "بدون تلفیق",
      ISCHART_Length: ["۵ دوره اخیر", "۱۰ دوره اخیر", "از ابتدا"],
      ISCHART_Length_Selected: "۵ دوره اخیر",
      ISCHART_Items: [],
      ISCHART_Items_Selected: [],
      ////second One
      ISCHART2_Period: ["۳ ماهه", "۶ ماهه", "۹ ماهه", "۱۲ ماهه"],
      ISCHART2_Period_Selected: "۱۲ ماهه",
      ISCHART2_Aggregated: ["بدون تلفیق"],
      ISCHART2_Aggregated_Selected: "بدون تلفیق",
      ISCHART2_Length: ["۵ دوره اخیر", "۱۰ دوره اخیر", "از ابتدا"],
      ISCHART2_Length_Selected: "۵ دوره اخیر",
      ISCHART2_Items: ["دارایی", "حقوق صاحبان سهام", "بدهی"],
      ISCHART2_Items_Selected: "دارایی"
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
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
      this.IncomeAgg = this.ISAGG;
      if (!(this.IncomeAgg.length === 0)) {
        this.ISCHART_Aggregated.push("تلفیقی");
        this.ISCHART2_Aggregated.push("تلفیقی");
      }

      this.Income = this.IS;
      if (!(this.Income.length === 0)) {
        this.Income.filter(d => {
          if (!this.ISCHART_Items.includes(d.Translated)) {
            if (!(d.Translated === null)) {
              this.ISCHART_Items.push(d.Translated);
            }
          }
        });
        this.ISCHART_Items.sort((a, b) => b - a);
        if (this.ISCHART_Items.includes("درآمدهای عملیاتی")) {
          this.ISCHART_Items_Selected.push("درآمدهای عملیاتی");
        } else {
          if (this.ISCHART_Items.includes("جمع درآمدهای عملیاتی")) {
            this.ISCHART_Items_Selected.push("جمع درآمدهای عملیاتی");
          }
        }
        if (this.ISCHART_Items.includes("سود زیان خالص هر سهم ریال")) {
          this.ISCHART_Items_Selected.push("سود زیان خالص هر سهم ریال");
        }

        // if (this.ISCHART_Items.includes("جمع دارایی‌ها")) {
        //   this.ISCHART_Items_Selected.push("جمع دارایی‌ها");
        // }
      }
    },
    GetFiltered() {
      // console.log(this.ISCHART_Items_Selected);
      // eslint-disable-next-line no-unused-vars
      let tempData = [];
      if (this.ISCHART_Aggregated_Selected == "تلفیقی") {
        tempData = this.IncomeAgg;
      } else {
        tempData = this.Income;
      }
      // eslint-disable-next-line no-unused-vars
      let x = [];
      x = tempData.filter(d => {
        if (this.ISCHART_Period_Selected == "۱۲ ماهه") {
          if (d.period == 12) {
            return d;
          }
        }
        if (this.ISCHART_Period_Selected == "۹ ماهه") {
          if (d.period == 9) {
            return d;
          }
        }
        if (this.ISCHART_Period_Selected == "۶ ماهه") {
          if (d.period == 6) {
            return d;
          }
        }
        if (this.ISCHART_Period_Selected == "۳ ماهه") {
          if (d.period == 3) {
            return d;
          }
        }
      });

      let uq = [];
      x.filter(d => {
        if (!uq.includes(d.toDate)) {
          uq.push(d.toDate);
        }
      });
      let A = [];
      if (this.ISCHART_Length_Selected == "۳ دوره اخیر") {
        A = uq.slice(0, 3);
      }
      if (this.ISCHART_Length_Selected == "۵ دوره اخیر") {
        A = uq.slice(0, 5);
      }
      if (this.ISCHART_Length_Selected == "۱۰ دوره اخیر") {
        A = uq.slice(0, 10);
      }
      if (this.ISCHART_Length_Selected == "از ابتدا") {
        A = uq.slice(0, 1000);
      }
      // eslint-disable-next-line no-unused-vars
      let filtered = [];
      x.filter(d => {
        if (
          this.ISCHART_Items_Selected.includes(d.Translated) &&
          A.includes(d.toDate)
        ) {
          // console.log(d.Translated);
          filtered.push(d);
        }
      });
      this.Chart1Categories = [];
      filtered.filter(item => {
        if (!this.Chart1Categories.includes(item.toDate)) {
          this.Chart1Categories.push(item.toDate);
        }
      });
      this.Chart1Categories.sort((a, b) => a - b);
      this.Chart1options.xaxis.categories = this.Chart1Categories;

      let ShowData = [];
      let uniqeItems = [];

      filtered.filter(item => {
        let k = {};
        if (!uniqeItems.includes(item.Translated)) {
          uniqeItems.push(item.Translated);
        }
        k["name"] = item.Translated;
        k["toDate"] = item.toDate;
        k["Value"] = item.thisPeriod;
        ShowData.push(k);
      });
      // console.log(uniqeItems);
      ShowData.sort(function(first, second) {
        return ("" + first.toDate).localeCompare(second.toDate);
      });
      // console.log(ShowData);
      let FinalData = [];
      // let c = 0;
      for (let j in uniqeItems) {
        // c = c + 1;
        // this.Chart1AllItems.push({ key: c, value: "j" });
        let IT2 = uniqeItems[j];
        let temp = {};
        temp["name"] = IT2;
        temp["data"] = [];
        ShowData.filter(item2 => {
          if (item2.name == IT2) {
            temp["data"].push(item2.Value);
          }
        });
        FinalData.push(temp);
      }
      this.Chart1options.series = FinalData;
      this.ApexChartcomponentKey = this.ApexChartcomponentKey + 1;
    },
    GetFiltered2() {
      // console.log(this.ISCHART_Items_Selected);
      // eslint-disable-next-line no-unused-vars
      let tempData = [];
      if (this.ISCHART2_Aggregated_Selected == "تلفیقی") {
        tempData = this.IncomeAgg;
      } else {
        tempData = this.IncomeAgg;
      }
      // eslint-disable-next-line no-unused-vars
      let x = [];
      x = tempData.filter(d => {
        if (this.ISCHART2_Period_Selected == "۱۲ ماهه") {
          if (d.period == 12) {
            return d;
          }
        }
        if (this.ISCHART2_Period_Selected == "۹ ماهه") {
          if (d.period == 9) {
            return d;
          }
        }
        if (this.ISCHART2_Period_Selected == "۶ ماهه") {
          if (d.period == 6) {
            return d;
          }
        }
        if (this.ISCHART2_Period_Selected == "۳ ماهه") {
          if (d.period == 3) {
            return d;
          }
        }
      });

      let uq = [];
      x.filter(d => {
        if (!uq.includes(d.toDate)) {
          uq.push(d.toDate);
        }
      });
      // eslint-disable-next-line no-unused-vars
      let A = [];
      if (this.ISCHART2_Length_Selected == "۳ دوره اخیر") {
        A = uq.slice(0, 3);
      }
      if (this.ISCHART2_Length_Selected == "۵ دوره اخیر") {
        A = uq.slice(0, 5);
      }
      if (this.ISCHART2_Length_Selected == "۱۰ دوره اخیر") {
        A = uq.slice(0, 10);
      }
      if (this.ISCHART2_Length_Selected == "از ابتدا") {
        A = uq.slice(0, 1000);
      }
      let tempkey = null;
      if (this.ISCHART2_Items_Selected == "بدهی") {
        tempkey = "Liability";
      }
      if (this.ISCHART2_Items_Selected == "حقوق صاحبان سهام") {
        tempkey = "Equity";
      }
      if (this.ISCHART2_Items_Selected == "دارایی") {
        tempkey = "Asset";
      }
      // eslint-disable-next-line no-unused-vars
      let filtered = [];
      // console.log(x)
      x.filter(d => {
        if (d.type == tempkey && A.includes(d.toDate)) {
          filtered.push(d);
        }
      });
      this.Chart2Categories = [];
      filtered.filter(item => {
        if (!this.Chart2Categories.includes(item.toDate)) {
          this.Chart2Categories.push(item.toDate);
        }
      });
      this.Chart2Categories.sort((a, b) => a - b);
      this.Chart2options.xaxis.categories = this.Chart2Categories;
      // console.log(this.Chart2options.xaxis.categories)
      let ShowData = [];
      let uniqeItems = [];

      filtered.filter(item => {
        let k = {};
        if (!uniqeItems.includes(item.Translated)) {
          uniqeItems.push(item.Translated);
        }
        k["name"] = item.Translated;
        k["toDate"] = item.toDate;
        k["Value"] = item.thisPeriod;
        ShowData.push(k);
      });
      ShowData.sort(function(first, second) {
        return ("" + first.toDate).localeCompare(second.toDate);
      });
      // console.log(ShowData);
      let FinalData = [];
      // let c = 0;
      for (let j in uniqeItems) {
        // c = c + 1;
        // this.Chart1AllItems.push({ key: c, value: "j" });
        let IT2 = uniqeItems[j];
        let temp = {};
        temp["name"] = IT2;
        temp["data"] = [];
        ShowData.filter(item2 => {
          if (item2.name == IT2) {
            temp["data"].push(item2.Value);
          }
        });
        FinalData.push(temp);
      }

      // console.log(FinalData);
      this.Chart2options.series = FinalData;
      this.ApexChartcomponentKey2 = this.ApexChartcomponentKey2 + 1;
    }
  },
  mounted() {},
  watch: {
    ISAGG() {
      this.populateData();
      this.GetFiltered();
      this.GetFiltered2();
      this.loading = false;
    },
    IS() {
      this.populateData();
      this.GetFiltered();
      this.GetFiltered2();
      this.loading = false;
    }
  }
};
</script>
<style scoped></style>
