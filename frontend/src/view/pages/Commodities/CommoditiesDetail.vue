<template>
  <div>
    <div class="row">
      <div class="col-3">
        <v-card color="#385F73" dark class="rounded-card">
          <v-card-title class="">
            {{ tableData[0].persianName }}
          </v-card-title>

          <!-- <v-card-subtitle
            >Listen to your favorite artists and albums whenever and wherever,
            online and offline.</v-card-subtitle
          > -->

          <!-- <v-card-actions>
            <v-btn text>
              Listen Now
            </v-btn>
          </v-card-actions> -->
        </v-card>
      </div>
      <div class="col-9">
        <v-card>
          <ApexChart
            v-if="series.length"
            type="line"
            width="100%"
            height="100%"
            :series="series"
            :chartOptions="ChartAOption"
          />
          <ApexChart
            v-if="series.length"
            type="area"
            width="100%"
            height="100%"
            :series="series"
            :chartOptions="ChartBOption"
          />
        </v-card>
      </div>
    </div>
    <div>
      <v-card>
        <ag-grid-vue
          v-if="request == 'IR'"
          :style="`width: 100%; height:500px; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
          :columnDefs="TableHeader"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
          :cacheQuickFilter="true"
          :sideBar="sideBar"
          :enableRtl="true"
          :gridOptions="gridOptions"
          @grid-ready="onReady"
          @gridColumnsChanged="gridColumnsChanged"
          :localeText="localeText"
        >
        </ag-grid-vue>
        <ag-grid-vue
          v-if="request == 'IN'"
          :style="`width: 100%; height:500px; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
          :columnDefs="TableHeaderIN"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
          :cacheQuickFilter="true"
          :sideBar="sideBar"
          :enableRtl="true"
          :gridOptions="gridOptions"
          @grid-ready="onReady"
          @gridColumnsChanged="gridColumnsChanged"
          :localeText="localeText"
        >
        </ag-grid-vue>
        <ag-grid-vue
          v-if="request == 'PL'"
          :style="`width: 100%; height:500px; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
          :columnDefs="TableHeaderPL"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
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
    </div>
  </div>
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "CommoditiesDetail",
  components: {
    ApexChart,
    AgGridVue
  },
  props: {
    request: String
  },
  data() {
    return {
      // AGgrid
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      TableHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      asyncTransactionWaitMillis: 4000,
      interval: null,
      tableData: null,

      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      RawData: null,
      series: [],
      ChartData: {},
      ChartAOption: {
        chart: {
          id: "chart2",
          type: "line",
          height: 230,
          toolbar: {
            autoSelected: "pan",
            show: false
          }
        },
        colors: ["#546E7A"],
        stroke: {
          width: 3
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          opacity: 1
        },
        markers: {
          size: 0
        },
        xaxis: {
          categories: [],
          tickAmount: 30

          // type: "datetime"
        }
      },
      ChartBOption: {
        // series: [
        //   {
        //     data: data
        //   }
        // ],
        chart: {
          id: "chart1",
          height: 130,
          type: "area",
          brush: {
            target: "chart2",
            enabled: true
          },
          selection: {
            enabled: true,
            xaxis: {
              // min: new Date("19 Jun 2019").getTime(),
              // max: new Date("14 Aug 2020").getTime()
            }
          }
        },
        colors: ["#008FFB"],
        fill: {
          type: "gradient",
          gradient: {
            opacityFrom: 0.91,
            opacityTo: 0.1
          }
        },
        xaxis: {
          // type: "datetime",
          tickAmount: 30,
          tooltip: {
            enabled: false
          }
        },
        yaxis: {
          // tickAmount: 2
        }
      }
    };
  },
  watch: {
    tableData(newValue, oldValue) {
      if (oldValue == null && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }
    }
  },
  created() {
    document.title = "Finwise - کالا";
    this.localeText = AG_GRID_LOCALE_FA;
    // GRID OPTIONS
    this.gridOptions = {
      suppressColumnVirtualisation: true,
      rowDragManaged: true,
      animateRows: true,

      // headerHeight: 20,
      rowHeight: 22,
      getRowNodeId: data => data.iid
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
    this.TableHeader = [
      {
        headerName: "عنوان",
        field: "persianName",
        minWidth: 110,
        sortable: true,
        pinned: "right",
        rowDrag: true,
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
        }
      },
      {
        headerName: "تاریخ میلادی",
        field: "timestamp",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "تاریخ شمسی",
        field: "persianDate",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "قیمت",
        field: "price",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تغییرات قیمت",
        field: "d",
        filter: "agNumberColumnFilter",

        sortable: true,
        valueFormatter: function(params) {
          return params.value.toLocaleString();
        },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
          } else if (params.value < 0) {
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
          } else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
        }
      }
    ];
    this.TableHeaderIN = [
      {
        headerName: "عنوان",
        field: "persianName",
        minWidth: 110,
        sortable: true,
        pinned: "right",
        rowDrag: true,
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
        }
      },
      {
        headerName: "تاریخ میلادی",
        field: "engDate",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "تاریخ شمسی",
        field: "persianDate",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "قیمت",
        field: "Close",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "بالاترین",
        field: "High",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "پایین ترین",
        field: "Low",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "اولین",
        field: "Open",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم",
        field: "Volume",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      }
    ];
    this.TableHeaderPL = [
      {
        headerName: "عنوان",
        field: "persianName",
        minWidth: 110,
        sortable: true,
        pinned: "right",
        rowDrag: true,
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
        }
      },
      {
        headerName: "تاریخ میلادی",
        field: "engdate",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "تاریخ شمسی",
        field: "persianDate",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "لوکیشن",
        field: "location",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "دسته بندی",
        field: "persianCategory",
        sortable: true,
        minWidth: 160
      },
      {
        headerName: "قیمت",
        field: "price",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "واحد",
        field: "unit",
        sortable: true,
        minWidth: 160
      }
    ];
  },
  mounted() {
    if (this.request == "IR") {
      this.loadDataIR();
    }
    if (this.request == "IN") {
      this.loadDataIN();
    }
    if (this.request == "PL") {
      this.loadDataPL();
    }
  },
  computed: {
    ApexWeek() {
      let lastDay = this.RawData[0];
      let margin = 7 * 24 * 3600 * 1000;

      let result;
      for (let item of this.RawData)
        if (item.unix < lastDay && item.unix >= margin) result.push(item);

      return result;
    },
    ApexMonth() {
      let data = this.ChartData.chart;
      let lastDay = data.unix[data.unix.length - 1];
      let margin = 30 * 24 * 3600 * 1000;
      let firstDayUnix = lastDay - margin;
      let result;
      for (let item of data) if (item.unix >= firstDayUnix) result.push(item);

      return result;
    },
    Apex3Month() {
      let lastDay = this.RawData[0];
      let margin = 90 * 24 * 3600 * 1000;
      let result;
      for (let item of this.RawData)
        if (item.unix < lastDay && item.unix >= margin) result.push(item);

      return result;
    },
    Apex6Month() {
      return null;
    },
    ApexYear() {
      return null;
    },
    Apex5Year() {
      return null;
    },
    ChartAdata() {
      // let result =[]
      let series = [];
      let categories;
      for (let item of this.RawData) {
        series.push(item.price);
        categories.push(item.persianDate);
      }
      return { series: series, categories: categories };
    }
  },
  methods: {
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
      // this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
    },
    onReady(params) {
      let allColumnIds = [];
      // this.gridOptions.api.closeToolPanel();
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;

      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      console.log(allColumnIds);
      // this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
      // this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      // this.gridColumnApi.autoSizeColumns(["market"], false);

      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    async loadDataIR() {
      await this.axios
        .get("/api/CommoditiesDetail/IR/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(IRresponse => {
          this.RawData = IRresponse.data;
          // let series = [];
          // let categories = [];
          // console.log(this.RawData);

          // for (let item of this.RawData) {
          //   if (item.price != undefined && item.persianDate != undefined) {
          //     series.push(item.price);
          //     // if (item.persianDate != undefined)
          //     categories.push(item.persianDate);
          //   }
          // }
          // this.ChartData = { series: series, categories: categories };
          this.ChartData = IRresponse.data.chart;
          this.series = [{ data: this.RawData.chart.series }];
          this.ChartAOption.series = [{ data: this.RawData.chart.series }];
          this.ChartBOption.series = [{ data: this.RawData.chart.series }];

          this.ChartAOption.xaxis.categories = this.RawData.chart.categories;
          this.ChartBOption.xaxis.categories = this.RawData.chart.categories;
          this.tableData = IRresponse.data.table;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async loadDataIN() {
      await this.axios
        .get("/api/CommoditiesDetail/IN/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(IRresponse => {
          this.RawData = IRresponse.data;
          // let series = [];
          // let categories = [];
          // console.log(this.RawData);

          // for (let item of this.RawData) {
          //   if (item.price != undefined && item.persianDate != undefined) {
          //     series.push(item.price);
          //     // if (item.persianDate != undefined)
          //     categories.push(item.persianDate);
          //   }
          // }
          // this.ChartData = { series: series, categories: categories };
          this.ChartData = IRresponse.data.chart;
          this.series = [{ data: this.RawData.chart.series }];
          this.ChartAOption.series = [{ data: this.RawData.chart.series }];
          this.ChartBOption.series = [{ data: this.RawData.chart.series }];

          this.ChartAOption.xaxis.categories = this.RawData.chart.categories;
          this.ChartBOption.xaxis.categories = this.RawData.chart.categories;
          this.tableData = IRresponse.data.table;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async loadDataPL() {
      await this.axios
        .get("/api/CommoditiesDetail/PL/" + this.$route.params.id, {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(IRresponse => {
          this.RawData = IRresponse.data;
          // let series = [];
          // let categories = [];
          // console.log(this.RawData);

          // for (let item of this.RawData) {
          //   if (item.price != undefined && item.persianDate != undefined) {
          //     series.push(item.price);
          //     // if (item.persianDate != undefined)
          //     categories.push(item.persianDate);
          //   }
          // }
          // this.ChartData = { series: series, categories: categories };
          this.ChartData = IRresponse.data.chart;
          this.series = [{ data: this.RawData.chart.series }];
          this.ChartAOption.series = [{ data: this.RawData.chart.series }];
          this.ChartBOption.series = [{ data: this.RawData.chart.series }];

          this.ChartAOption.xaxis.categories = this.RawData.chart.categories;
          this.ChartBOption.xaxis.categories = this.RawData.chart.categories;
          this.tableData = IRresponse.data.table;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
<style>
/* ag Grid */
.ag-theme-balham .ag-header {
  background-color: #f5f7f7;
  background-color: var(--ag-header-background-color, #f5f7f7);
  border-top: solid 1px;
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-top-color: #bdc3c7;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-radius: 10px 10px 0px 0px;
}

.ag-theme-balham .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.ag-header-cell-label {
  color: black;
  font-size: 1em;
  font-weight: 300;
  align-items: center;
  text-align: center;
  margin-right: 2px !important;
  display: flex;
  justify-content: center;
  align-content: center;
}
.ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5 */

.rounded-card {
  border-radius: 10px;
}
</style>
