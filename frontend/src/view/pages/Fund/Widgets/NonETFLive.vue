<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <v-skeleton-loader
      type=" table-heading, table-thead, table-tbody"
      v-if="loading"
    ></v-skeleton-loader>
    <v-card>
      <v-tabs grow center-active color="#333333" v-if="loading == false">
        <v-tabs-slider color="#333333"></v-tabs-slider>
        <v-tab class="FinancialStrength">
          نگاه کلی
          <v-icon left small>mdi-poll</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اطلاعات معامله
          <v-icon left small>mdi-shopping</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          چارت
          <v-icon left small>mdi-poll</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اخبار
          <v-icon left small>mdi-newspaper</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          تاریخچه
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          نوع دارایی
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          صنایع سرمایه گذاری شده
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          بازدهی صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اطلاعات صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab-item>
          <!-- <v-card height="450" flat>
            <v-card-text>
              <div class="row">
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات قیمت</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    قیمت پایانی :
                    <span class="spandata">{{ this.close }} ریال</span> (
                    <span
                      dir="ltr"
                      class="spandata"
                      v-bind:class="[
                        this.close > this.open ? 'greenItem' : 'redItem'
                      ]"
                    >
                      %{{ setclosingperc.toString() }}
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
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    قیمت آخرین معامله :
                    <span class="spandata">{{ this.last }} ریال</span> (
                    <span
                      dir="ltr"
                      class="spandata"
                      v-bind:class="[
                        last > open ? 'greenItem' : 'redItem ltr_aligned'
                      ]"
                      >% {{ setlastperc }}</span
                    >)
                    <v-icon
                      left
                      v-bind:class="[
                        this.last >= this.open ? 'greenItem' : 'redItem'
                      ]"
                      small
                      >mdi-chevron-{{
                        this.last >= this.open ? "up" : "down"
                      }}</v-icon
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    اولین قیمت :
                    <span class="spandata">{{ this.first }} ریال</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    ارزش بازار :
                    <span class="spandata" v-if="!isNaN(this.marketcap)"
                      >{{
                        numberWithCommas(
                          roundTo(this.marketcap / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                  </h5>
                </div>

                <div
                  class="col-xl-4 col-lg-5 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">مشخصات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    وضعیت:
                    <span class="spandata">{{ this.status }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    EPS (منبع TSE):
                    <span class="spandata" dir="ltr">{{ this.eps }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد سهام:
                    <span class="spandata" dir="ltr">
                      {{
                        numberWithCommas(
                          roundTo(this.sharecount / 1000000000, 2)
                        )
                      }}
                      میلیارد
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    درصد شناوری :
                    <span class="spandata">{{ this.shenavar }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم مبنا :
                    <span class="spandata">
                      {{ numberWithCommas(roundTo(this.mabna / 1000000, 2)) }}
                      میلیون سهم</span
                    >
                  </h5>
                </div>
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد معاملات :
                    <span class="spandata">
                      {{ numberWithCommas(this.tradecount) }}
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم معاملات :
                    <span class="spandata" v-if="!isNaN(this.tradeVolume)"
                      >{{
                        numberWithCommas(roundTo(this.tradeVolume / 1000000, 2))
                      }}
                      میلیون</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    ارزش معاملات :
                    <span class="spandata" v-if="!isNaN(this.tradevalue)"
                      >{{
                        numberWithCommas(
                          roundTo(this.tradevalue / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                  </h5>
                </div>
              </div>
            </v-card-text>
          </v-card> -->
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <ApexChart
              type="pie"
              width="100%"
              height="180%"
              :series="AssetTypePie"
              :chartOptions="AssetTypeValueOptions"
            />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <ApexChart
              type="pie"
              width="100%"
              height="180%"
              :series="IndustryPie"
              :chartOptions="IndustriesValueOptions"
            />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "NonETFMainWidget",
  components: {
    ApexChart
  },
  props: ["meta", "industry", "assettype", "historicNav"],
  data() {
    return {
      loading: false,
      priceOverViewSeries: [
        {
          name: "series1",
          data: [31, 40, 28, 51, 42, 109, 100]
        }
      ],
      priceOverViewchartOptions: {
        chart: {
          height: 350,
          type: "area",
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 2,
          curve: "smooth"
        }
      },
      IndustryPie: [],
      IndustriesValueOptions: {
        chart: {
          width: 380,
          type: "pie",
          fontFamily: "Vazir-Medium-FD",
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            // },
            dataPointSelection: (event, chartContext, config) => {
              this.ChartClick(
                "Industries",
                chartContext,
                config.dataPointIndex
              );
            }
          }
        },
        // colors: ["#011627", "#E09F3E", "#9E2A2B"
        // , "#1AA47C", "#003049","#0E5D52","#540B0E","#069E97","#068292"
        // ,"#05668D"],
        colors: ["#EF476F", "#E09F3E", "#06D6A0", "#118AB2", "#073B4C"],
        labels: [],
        legend: {
          show: true,
          position: "right"
        },
        responsive: [
          {
            breakpoint: 380,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ],
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        tooltip: {
          // eslint-disable-next-line no-unused-vars
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let backgroundColor = w.config.colors[seriesIndex];
            let n = series[seriesIndex];
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              let val = (n / 1000000000).toLocaleString();
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em class=mr-1>میلیارد ریال</span>
              <span style=color:#000;font-size:0.8em>${val}</span>

            

              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        }
      },
      AssetTypePie: [],
      AssetTypeValueOptions: {
        chart: {
          width: 380,
          type: "pie",
          fontFamily: "Vazir-Medium-FD",
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            // },
            dataPointSelection: (event, chartContext, config) => {
              this.ChartClick(
                "Industries",
                chartContext,
                config.dataPointIndex
              );
            }
          }
        },
        // colors: ["#011627", "#E09F3E", "#9E2A2B"
        // , "#1AA47C", "#003049","#0E5D52","#540B0E","#069E97","#068292"
        // ,"#05668D"],
        colors: ["#EF476F", "#E09F3E", "#06D6A0", "#118AB2", "#073B4C"],
        labels: [],
        legend: {
          show: true,
          position: "right"
        },
        responsive: [
          {
            breakpoint: 380,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ],
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        tooltip: {
          // eslint-disable-next-line no-unused-vars
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let backgroundColor = w.config.colors[seriesIndex];
            let n = series[seriesIndex];
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              let val = (n / 1000000000).toLocaleString();
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em class=mr-1>میلیارد ریال</span>
              <span style=color:#000;font-size:0.8em>${val}</span>

            

              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        }
      }
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    setclosingperc: function() {
      return Math.round((this.close / this.open - 1) * 100 * 100) / 100;
    },
    setlastperc: function() {
      return Math.round((this.last / this.open - 1) * 100 * 100) / 100;
    }
  },
  methods: {
    numberWithCommas(x) {
      // if (x == "-") {
      //   return x;
      // }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      // if (n == "-") {
      //   return n;
      // }

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
    populateData() {
      this.DataItems1 = this.meta;
    },
    populateData2() {
      let temp1 = [];
      let temp2 = [];

      this.industry.filter(item => {
        temp1.push(item.Title);
        temp2.push(item.ratio);
      });
      this.IndustryPie = temp2;
      this.IndustriesValueOptions.labels = temp1;
    },
    populateData3() {
      let temp1 = [];
      let temp2 = [];
      this.assettype.filter(item => {
        temp1.push(item.item);
        temp2.push(item.perc);
      });
      this.AssetTypePie = temp2;
      this.AssetTypeValueOptions.labels = temp1;
    },
    populateData4() {
      console.log(this.historicNav);
    }
  },
  mounted() {
    this.populateData();
    this.populateData2();
    this.populateData3();
    this.populateData4();
  },
  watch: {
    meta() {
      this.populateData();
    },
    industry() {
      this.populateData2();
    },
    assettype() {
      // this.loading = false;
      this.populateData3();
    },
    historicNav() {
      // this.loading = false;
      this.populateData4();
    }
  }
};
</script>
<style scoped>
.subheaderTitles {
  font-size: 1.1em;
  font-weight: 900;
  text-align: center;
}

.FinancialStrength {
  direction: rtl;
  text-align: right;
  font-size: 1em;

  letter-spacing: 0px;
}
/* .v-tab {
color: black;
} */

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
.titleHeaders-smallest {
  padding: 5px;
  font-size: 1em;
  font-weight: 700;
  text-align: right;
  font-family: "Vazir-Medium-FD";
}
.titleHeaders-smaller {
  padding: 5px;
  font-size: 1.2em;
  font-weight: 700;
  /* text-align: right; */
  font-family: "Vazir-Medium-FD";
}
.spandata {
  color: rgb(4, 17, 53);
  font-size: 1.1em;
  font-weight: 800;
  margin-top: 5px;
  font-family: "Vazir-Medium-FD";
}
</style>
