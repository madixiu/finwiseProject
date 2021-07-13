<template>
  <!--begin::Mixed Widget 14-->
  <div>
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
        <!-- <v-tab class="FinancialStrength">
          اطلاعات معامله
          <v-icon left small>mdi-shopping</v-icon>
        </v-tab> -->
        <v-tab class="FinancialStrength">
          چارت
          <v-icon left small>mdi-poll</v-icon>
        </v-tab>
        <!-- <v-tab class="FinancialStrength">
          اخبار
          <v-icon left small>mdi-newspaper</v-icon>
        </v-tab> -->
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
        <!-- <v-tab class="FinancialStrength">
          بازدهی صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab> -->
        <v-tab class="FinancialStrength">
          اطلاعات صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text>
              <div class="row">
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات قیمت</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    قیمت صدور لحظه ای :
                    <span class="spandata">{{
                      numberWithCommas(LiveDataBox.LiveSub)
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    قیمت ابطال لحظه ای :
                    <span class="spandata">{{
                      numberWithCommas(LiveDataBox.LiveRed)
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    قیمت آماری لحظه ای :
                    <span class="spandata">{{
                      numberWithCommas(LiveDataBox.LiveStat)
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    جمع دارایی لحظه ای:
                    <span class="spandata"
                      >{{
                        numberWithCommas(
                          roundTo(LiveDataBox.LiveNavAm / 10000000000, 2)
                        )
                      }}
                      میلیارد تومان</span
                    >
                  </h5>
                </div>

                <div
                  class="col-xl-4 col-lg-5 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">نوع سرمایه گذاران</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    درصد صاحبان واحد حقیقی:
                    <span class="spandata">{{
                      roundTo(LiveDataBox.RetailPerc, 2)
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    درصد صاحبان واحد حقوقی:
                    <span class="spandata">{{
                      roundTo(LiveDataBox.InstituePerc, 2)
                    }}</span>
                  </h5>
                </div>
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد کل واحدها:
                    <span class="spandata">{{
                      numberWithCommas(LiveDataBox.TotalUnit)
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد کل واحدهای واگذار شده:
                    <span class="spandata">{{
                      numberWithCommas(LiveDataBox.TotalSold)
                    }}</span>
                  </h5>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>

        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text>
              <v-radio-group
                v-model="TimeFrameNAV"
                row
                dense
                @change="GetFiltered"
              >
                <v-radio
                  class="radioBTN"
                  label="یک هفته اخیر"
                  value="1W"
                ></v-radio>
                <v-radio
                  class="radioBTN"
                  label="یک ماه اخیر"
                  value="1M"
                ></v-radio>
                <v-radio
                  class="radioBTN"
                  label="از ابتدای سال"
                  value="YTD"
                ></v-radio>
                <v-radio
                  class="radioBTN"
                  label="یک سال اخیر"
                  value="1Y"
                ></v-radio>
                <v-radio
                  class="radioBTN"
                  label="از ابتدا"
                  value="All"
                ></v-radio>
              </v-radio-group>
              <hr />
              <div class="d-flex flex-row">
                <div class="col-lg-6 col-md-12 col-xs-12">
                  <ApexChart
                    type="area"
                    width="100%"
                    height="140%"
                    :key="NavChartKey"
                    :series="NavChart.series"
                    :chartOptions="NavChartOptions"
                  />
                </div>
                <div class="col-lg-6 col-md-12 col-xs-12">
                  <ApexChart
                    type="area"
                    width="100%"
                    height="140%"
                    :key="NavChartKey2"
                    :series="NavChart2.series"
                    :chartOptions="NavChartOptions2"
                  />
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <ag-grid-vue
              :style="`width: 100%;height:560px;  font-family: Vazir-Medium-FD`"
              class="ag-theme-balham"
              :columnDefs="FundsHeader"
              :defaultColDef="defaultColDef"
              :cacheQuickFilter="true"
              :sideBar="sideBar"
              :enableRtl="true"
              :gridOptions="gridOptions"
              @grid-ready="onReady"
              @gridColumnsChanged="gridColumnsChanged"
              :localeText="localeText"
            >
            </ag-grid-vue>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <ApexChart
              type="pie"
              width="100%"
              height="200%"
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
            <v-card-text>
              <div class="row">
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات افراد</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    عنوان صندوق:
                    <span class="spandata">{{ meta.FundTitle }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    مدیر صندوق:
                    <span class="spandata">{{ meta.Manager }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    مدیر سرمایه گذاری:
                    <span class="spandata">{{
                      meta.InvestmentManagerName
                    }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حسابرس:
                    <span class="spandata">{{ meta.AuditorName }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    متولی:
                    <span class="spandata">{{ meta.CustodianName }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    ضامن نقد شوندگی:
                    <span class="spandata">{{
                      meta.LiquidityGuaranteeName
                    }}</span>
                  </h5>
                </div>

                <div
                  class="col-xl-4 col-lg-5 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">تاریخچه</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    شروع فعالیت:
                    <span class="spandata">{{ meta.ActivityStartDate }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تاریخ آخرین آمار اعلامی:
                    <span class="spandata">{{ meta.LastNavDate }}</span>
                  </h5>
                </div>
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">سایر</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    نوع صندوق:
                    <span class="spandata">{{ meta.Type }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    اندازه
                    <span class="spandata">{{ meta.Size }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    وضعیت
                    <span class="spandata">{{ meta.Status }}</span>
                  </h5>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "NonETFMainWidget",
  components: {
    ApexChart,
    AgGridVue
  },
  props: ["meta", "industry", "assettype", "historicNav", "liveNav"],
  data() {
    return {
      // * AGgrid base data
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      FundsHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      // * %%%%%%%%%%%%%%%
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
        noData: {
          text: "No Data",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        responsive: [
          {
            kpoint: 380,
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
  
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em>${n}</span>

            

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
        noData: {
          text: "No Data",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
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
            console.log(series);
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em>${n}</span>

            

              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        }
      },
      NavChartKey: 0,
      NavChartKey2: 0,
      TimeFrameNAV: "1W",
      NavChart: {
        series: []
      },
      NavChartOptions: {
        chart: {
          id: "area-datetime",
          type: "area",
          toolbar: {
            show: false
          },
          height: 350
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0,
          style: "hollow"
        },
        xaxis: {
          // type: "datetime",
          // min: new Date("01 Mar 2012").getTime(),
          tooltip: {
            // eslint-disable-next-line no-unused-vars
            formatter: function(value, timestamp) {
              return new Date(
                timestamp.w.globals.seriesX[timestamp.seriesIndex][
                  timestamp.dataPointIndex
                ]
              ).toLocaleDateString("fa-IR");
            }
          },
          tickAmount: 6,
          labels: {
            formatter: function(value, timestamp) {
              return new Date(timestamp).toLocaleDateString("fa-IR");
            }
          }
        },
        yaxis:{
          title:{
            text: "ریال"

          }
        },
        noData: {
          text: "بدون داده",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        tooltip: {
          // x: {
          //   show: true
          // }
          // eslint-disable-next-line no-unused-vars
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            // let n = series[seriesIndex][dataPointIndex];
            // console.log(w);
            let date = new Date(
              w.globals.seriesX[seriesIndex][dataPointIndex]
            ).toLocaleDateString("fa-IR");
            console.log(w);

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${date}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class='apexcharts-tooltip-marker' style='background-color: ${w.globals.colors[0]}'></span>

              <span style='font-size:0.8em'>${w.globals.seriesNames[0]}: </span>
              
              <span style='font-size:0.8em'>${series[0][dataPointIndex]}</span>
            

              </div>
              <div class="bottomDivTooltip">
              <span class='apexcharts-tooltip-marker' style='background-color: ${w.globals.colors[1]}'></span>

              <span style='font-size:0.8em'>${w.globals.seriesNames[1]}: </span>

              <span style='font-size:0.8em'>${series[1][dataPointIndex]}</span>
            

              </div>
              <div class="bottomDivTooltip">
              <span class='apexcharts-tooltip-marker' style='background-color: ${w.globals.colors[2]}'></span>
              <span style='font-size:0.8em'>${w.globals.seriesNames[2]}: </span>

              <span style='font-size:0.8em'>${series[2][dataPointIndex]}</span>
            

              </div>
              </div>
            `;
            // let backgroundColor = w.config.colors[seriesIndex];
            // console.log(backgroundColor);
            // date
            // console.log(w.globals.seriesX[]);
            // console.log(seriesIndex);
            // console.log(series);
            // console.log(dataPointIndex);
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0.7,
            stops: [0, 100]
          }
        }
      },
      NavChart2: {
        series: []
      },
      NavChartOptions2: {
        chart: {
          id: "area-datetime2",
          type: "area",
          toolbar: {
            show: false
          },
          height: 350
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0,
          style: "hollow"
        },
        noData: {
          text: "بدون داده",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        yaxis: {
          title: {
            // text: "میلیارد ریال",
            text: "لایر درایلیم",
            style: {
              cssClass: "apexcharts-yaxis-title"
            }
          },
          labels: {
            formatter: function(val) {
              return val / 1000000000;
            }
          },
        },
        xaxis: {
          tooltip: {
            formatter: function(value, timestamp) {
              return new Date(
                timestamp.w.globals.seriesX[timestamp.seriesIndex][
                  timestamp.dataPointIndex
                ]
              ).toLocaleDateString("fa-IR");
            }
          },
          // type: "datetime",
          // min: new Date("01 Mar 2012").getTime(),
          tickAmount: 6,
          labels: {
            formatter: function(value, timestamp) {
              return new Date(timestamp).toLocaleDateString("fa-IR");
            }
          }
        },
        tooltip: {
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            // let n = series[seriesIndex][dataPointIndex];
            // console.log(w);
            let date = new Date(
              w.globals.seriesX[seriesIndex][dataPointIndex]
            ).toLocaleDateString("fa-IR");
            console.log(w);

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${date}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class='apexcharts-tooltip-marker' style='background-color: ${w.globals.colors[0]}'></span>

              <span style='font-size:0.8em'>${w.globals.seriesNames[0]}: </span>
              
              <span style='font-size:0.8em'>${series[0][dataPointIndex]}</span>
            

              </div>
      
              </div>
            `;
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0.7,
            stops: [0, 100]
          }
        }
      },
      LiveDataBox: {
        LiveSub: "",
        LiveRed: "",
        LiveStat: "",
        RetailPerc: "",
        InstituePerc: "",
        TotalUnit: "",
        TotalSold: "",
        LiveNavAm: ""
      }
    };
  },
  created() {
    // GRID LOCALE FILE LOAD
    this.localeText = AG_GRID_LOCALE_FA;

    // GRID OPTIONS
    this.gridOptions = {
      suppressColumnVirtualisation: true,
      rowDragManaged: true,
      animateRows: true,
      rowClass: "ag-grid-row-class",

      // headerHeight: 20,
      rowHeight: 22
      // getRowNodeId: data => data.persianDate
    };
    this.defaultColDef = {
      flex: 1,
      minWidth: 100,
      filter: true,
      // sortable: true,
      // headerHeight: 12,
      enablePivot: false,
      suppressMenu: true,
      cellStyle: {
        display: "flex",
        "justify-content": "center",
        "border-left-color": "#e2e2e2",
        "align-items": "center",
        direction: "ltr"
      }
    };
    // AG Sidebar
    this.sideBar = {
      toolPanels: [
        {
          id: "columns",
          labelDefault: "Columns",
          labelKey: "columns",
          iconKey: "columns",
          toolPanel: "agColumnsToolPanel",
          toolPanelParams: {
            suppressRowGroups: true,
            suppressValues: true,
            suppressPivots: true,
            suppressPivotMode: true,
            suppressSideButtons: false,
            suppressColumnFilter: false,
            suppressColumnSelectAll: false,
            suppressColumnExpandAll: false
          }
        },

        {
          id: "filters",
          labelDefault: "Filters",
          labelKey: "filters",
          iconKey: "filter",
          toolPanel: "agFiltersToolPanel"
        }
      ],
      defaultToolPanel: ""
    };

    this.FundsHeader = [
      {
        headerName: "تاریخ شمسی",
        field: "persianDate",

        sortable: true,
        pinned: "right",
        rowDrag: true,
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
          // // "justify-content": "center",
          // "align-items": "center !important",
          // "height": "100%"
        }
      },
      {
        headerName: "تاریخ میلادی",
        field: "englishDate",
        sortable: true
      },
      {
        headerName: "قیمت صدور",
        field: "purchasePrice",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت ابطال",
        field: "redeptionPrice",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت آماری",
        field: "statisticalValue",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "مجموع دارایی ها",
        field: "total_net_asset_value_with_sell_commission",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      }
    ];
  },
  methods: {
    GetFiltered() {
      if (!(this.historicNav === undefined || this.historicNav.length == 0)) {
        // eslint-disable-next-line no-unused-vars
        let tempData = [];
        let today = new Date();
        let lastweek = new Date();
        lastweek.setDate(lastweek.getDate() - 7);
        let lastMonth = new Date();
        lastMonth.setDate(lastMonth.getDate() - 31);
        let lastYear = new Date();
        lastYear.setDate(lastYear.getDate() - 365);
        let pYear = "1400";
        if (this.historicNav[0].persianDate.includes("/")) {
          pYear = this.historicNav[0].persianDate.split("/")[0];
        } else {
          pYear = this.historicNav[0].persianDate.split("-")[0];
        }
        let filtered = [];
        let filtered2 = [];
        let filtered3 = [];
        let filtered4 = [];
        if (this.TimeFrameNAV == "1W") {
          this.historicNav.filter(d => {
            let D = new Date(
              d.englishDate.split("-")[0],
              d.englishDate.split("-")[1],
              d.englishDate.split("-")[2]
            );
            if (D >= lastweek && D <= today) {
              filtered.push([D.getTime(), d.purchasePrice]);
              filtered2.push([D.getTime(), d.redeptionPrice]);
              filtered3.push([D.getTime(), d.statisticalValue]);
              filtered4.push([
                D.getTime(),
                d.total_net_asset_value_with_sell_commission
              ]);
            }
          });
        }

        if (this.TimeFrameNAV == "1M") {
          this.historicNav.filter(d => {
            let D = new Date(
              d.englishDate.split("-")[0],
              d.englishDate.split("-")[1],
              d.englishDate.split("-")[2]
            );
            if (D >= lastMonth && D <= today) {
              filtered.push([D.getTime(), d.purchasePrice]);
              filtered2.push([D.getTime(), d.redeptionPrice]);
              filtered3.push([D.getTime(), d.statisticalValue]);
              filtered4.push([
                D.getTime(),
                d.total_net_asset_value_with_sell_commission
              ]);
            }
          });
        }
        if (this.TimeFrameNAV == "YTD") {
          this.historicNav.filter(d => {
            let D = new Date(
              d.englishDate.split("-")[0],
              d.englishDate.split("-")[1],
              d.englishDate.split("-")[2]
            );
            if (
              (d.persianDate.includes("-") &&
                d.persianDate.split("-")[0] == pYear) ||
              (d.persianDate.includes("/") &&
                d.persianDate.split("/")[0] == pYear)
            ) {
              filtered.push([D.getTime(), d.purchasePrice]);
              filtered2.push([D.getTime(), d.redeptionPrice]);
              filtered3.push([D.getTime(), d.statisticalValue]);
              filtered4.push([
                D.getTime(),
                d.total_net_asset_value_with_sell_commission
              ]);
            }
          });
        }
        if (this.TimeFrameNAV == "1Y") {
          this.historicNav.filter(d => {
            let D = new Date(
              d.englishDate.split("-")[0],
              d.englishDate.split("-")[1],
              d.englishDate.split("-")[2]
            );
            if (D >= lastYear && D <= today) {
              filtered.push([D.getTime(), d.purchasePrice]);
              filtered2.push([D.getTime(), d.redeptionPrice]);
              filtered3.push([D.getTime(), d.statisticalValue]);
              filtered4.push([
                D.getTime(),
                d.total_net_asset_value_with_sell_commission
              ]);
            }
          });
        }
        if (this.TimeFrameNAV == "All") {
          this.historicNav.filter(d => {
            let D = new Date(
              d.englishDate.split("-")[0],
              d.englishDate.split("-")[1],
              d.englishDate.split("-")[2]
            );
            filtered.push([D.getTime(), d.purchasePrice]);
            filtered2.push([D.getTime(), d.redeptionPrice]);
            filtered3.push([D.getTime(), d.statisticalValue]);
            filtered4.push([
              D.getTime(),
              d.total_net_asset_value_with_sell_commission
            ]);
          });
        }
        console.log(filtered4);
        this.NavChart.series = [];
        this.NavChart2.series = [];
        this.NavChart.series.push({ name: "قیمت صدور", data: filtered });
        this.NavChart.series.push({ name: "قیمت ابطال", data: filtered2 });
        this.NavChart.series.push({ name: "قیمت آماری", data: filtered3 });
        this.NavChart2.series.push({
          name: "جمع خالص دارایی",
          data: filtered4
        });
        this.NavChartKey += 1;
        this.NavChartKey2 += 1;
      }
    },
    numberWithCommas(x) {
      if (x == "-" || x == "") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    roundTo(n, digits) {
      if (n == "-" || n == "") {
        return n;
      }
      if (n == "-" || n == "اطلاعات وجود ندارد") {
        return "اطلاعات وجود ندارد";
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
    populateData() {
      if (!(this.meta === undefined || this.meta.length == 0)) {
        for (const [key, value] of Object.entries(this.meta)) {
          if (String(value).includes("Element")) {
            this.meta[key] = "اطلاعات وجود ندارد";
          }
        }
      }
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
    populateData5() {
      if (!(this.liveNav === undefined || this.liveNav.length == 0)) {
        //      LiveDataBox: {
        //   : "",
        //   LiveNavAm:""
        // }
        if (this.liveNav[0].SubscriptionUnit != null) {
          this.LiveDataBox.TotalSold = this.liveNav[0].SubscriptionUnit;
        } else {
          this.LiveDataBox.TotalSold = "اطلاعات وجود ندارد";
        }
        if (this.liveNav[0].InstitutionalInvestorUnitPercent != null) {
          this.LiveDataBox.InstituePerc = this.liveNav[0].InstitutionalInvestorUnitPercent;
        } else {
          this.LiveDataBox.InstituePerc = "اطلاعات وجود ندارد";
        }
        if (this.liveNav[0].RetailInvestorUnitsPercent != null) {
          this.LiveDataBox.RetailPerc = this.liveNav[0].RetailInvestorUnitsPercent;
        } else {
          this.LiveDataBox.RetailPerc = "اطلاعات وجود ندارد";
        }
        if (this.liveNav[0].SubscriptionNAV != null) {
          this.LiveDataBox.LiveSub = this.liveNav[0].SubscriptionNAV;
        } else {
          if (
            this.liveNav[0].purchasePrice != null &&
            this.liveNav[0].purchasePrice != 0
          ) {
            this.LiveDataBox.LiveSub = this.liveNav[0].purchasePrice;
          } else {
            this.LiveDataBox.LiveSub = "اطلاعات وجود ندارد";
          }
        }

        if (this.liveNav[0].RedemptionNAV != null) {
          this.LiveDataBox.LiveRed = this.liveNav[0].RedemptionNAV;
        } else {
          if (
            this.liveNav[0].redeptionPrice != null &&
            this.liveNav[0].redeptionPrice != 0
          ) {
            this.LiveDataBox.LiveRed = this.liveNav[0].redeptionPrice;
          } else {
            this.LiveDataBox.LiveRed = "اطلاعات وجود ندارد";
          }
        }
        if (this.liveNav[0].StaticalNAV != null) {
          this.LiveDataBox.LiveStat = this.liveNav[0].StaticalNAV;
        } else {
          if (
            this.liveNav[0].statisticalValue != null &&
            this.liveNav[0].statisticalValue != 0
          ) {
            this.LiveDataBox.LiveStat = this.liveNav[0].statisticalValue;
          } else {
            this.LiveDataBox.LiveStat = "اطلاعات وجود ندارد";
          }
        }
        if (this.liveNav[0].TotalUnit != null) {
          this.LiveDataBox.TotalUnit = this.liveNav[0].TotalUnit;
        } else {
          if (
            this.liveNav[0].total_unit_count != null &&
            this.liveNav[0].total_unit_count != 0
          ) {
            this.LiveDataBox.TotalUnit = this.liveNav[0].total_unit_count;
          } else {
            this.LiveDataBox.TotalUnit = "اطلاعات وجود ندارد";
          }
        }
        if (this.liveNav[0].NetAssetValue != null) {
          this.LiveDataBox.LiveNavAm = this.liveNav[0].NetAssetValue;
        } else {
          if (
            this.liveNav[0].total_net_asset_value_with_sell_commission !=
              null &&
            this.liveNav[0].total_net_asset_value_with_sell_commission != 0
          ) {
            this.LiveDataBox.LiveNavAm = this.liveNav[0].total_net_asset_value_with_sell_commission;
          } else {
            this.LiveDataBox.LiveNavAm = "اطلاعات وجود ندارد";
          }
        }
      }
    },
    //? AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
    },
    tickerClick(data) {
      this.$router.push({ path: `/ticker/Overview/Overall/${data.ID}` });
    },
    onReady(params) {
      let allColumnIds = [];
      // this.gridOptions.api.closeToolPanel();
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;

      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      // this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
      // this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.historicNav != null) params.api.setRowData(this.historicNav);
    }
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  mounted() {
    // this.populateData();
    // this.populateData2();
    // this.populateData3();
    this.GetFiltered();
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
    historicNav(newValue, oldValue) {
      if (oldValue == null && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }
      this.GetFiltered();
    },
    liveNav() {
      this.populateData5();
    }
  }
};
</script>
<style scoped>
/* Radio Button classes */
.radioBTN /deep/ .v-input--selection-controls__ripple {
  height: 16px !important;
  width: 16px !important;
  left: -3px !important;
  top: calc(50% - 15px) !important;
}
.radioBTN /deep/ .v-icon.v-icon {
  font-size: 18px !important;
}
.radioBTN /deep/ .v-application--is-rtl .v-input--selection-controls__input {
  margin-left: 1px;
}

.radioBTN /deep/ label {
  display: inline-block;
  margin-bottom: 0rem;
}
.radioBTN /deep/ .v-label {
  font-size: 0.8em !important;
  font-family: "Vazir-Light-FD";
}
.radioBTN /deep/ .theme--light.v-label {
  color: #000 !important;
}
/************* Radio Button classes ************/
.apexcharts-yaxis-title{
  direction: rtl !important;
}
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

.v-radio > .v-label {
  direction: rtl;
  text-align: right;
  font-size: 0.8em;

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
