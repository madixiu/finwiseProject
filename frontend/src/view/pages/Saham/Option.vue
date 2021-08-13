/* eslint-disable no-unused-vars */
<template>
  <div>
    <div class="row mr-1 ml-1">
      <!-- OPTION TABLE *************************************************** -->
      <v-card rounded="lg" width="100%">
        <div id="marketwatchFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-2 col-lg-2 col-md-6 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-input-group-prepend is-text>
                <b-icon icon="search"></b-icon>
              </b-input-group-prepend>
              <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="جستجو"
                @keyup="onQuickFilterChanged"
              ></b-form-input>
            </b-input-group>
          </div>
        </div>
        <ag-grid-vue
          :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
          class="optionTable ag-theme-balham"
          :columnDefs="OptionHeader"
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
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "Option",
  components: {
    AgGridVue
  },

  data() {
    return {
      // * AGgrid base data
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      OptionHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      tableData: null,
      // * %%%%%%%%%%%%%%%
      WebsocketRequest: false,
      isBusy: true,
      OptionAsset: [],
      filter: null,
      height: "450px"
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
    document.title = "Finwise - آپشن";
    // GRID LOCALE FILE LOAD
    this.localeText = AG_GRID_LOCALE_FA;

    // GRID OPTIONS
    this.gridOptions = {
      suppressColumnVirtualisation: true,
      rowDragManaged: true,
      animateRows: true,
      rowClass: "ag-grid-row-class",

      // headerHeight: 20,
      rowHeight: 22,
      getRowNodeId: data => data.id
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

    this.OptionHeader = [
      {
        headerName: "نماد",
        field: "Nemad",

        sortable: true,
        minWidth: 120,
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
        headerName: "دارایی پایه",
        field: "UnderLying",
        sortable: true
      },

      {
        headerName: "قیمت اعمال",
        field: "StrikePrice",

        sortable: true,
        filter: "agNumberColumnFilter",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "فاصله تا سر رسید",
        field: "TTM",
        width: "130",
        filter: "agNumberColumnFilter",
        sortable: true
      },
      {
        headerName: "قیمت دارایی پایه",
        field: "AssetPrice",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت عادلانه",
        field: "averageFairprice",

        sortable: true,
        filter: "agNumberColumnFilter",

        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip: "قیمت به دست آمده از مدل بلک شولز"
      },
      {
        headerName: "قیمت بهترین سفارش فروش",
        field: "priceseller",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم بهترین سفارش فروش",
        field: "volumeseller",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },

      {
        headerName: "ارزندگی بهترین سفارش فروش",
        field: "DifferenceToAverage",
        filter: "agNumberColumnFilter",
        sortable: true,
        headerTooltip:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است",
        valueFormatter: function(params) {
          if (params.value == -10001) return "سفارش فروش ندارد";
          else if (params.value == -10000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (
            (params.value < 0 || params.value == -10000) &&
            params.value != -10001
          )
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        }
      },

      {
        headerName: "پوشش قیمت سهام با بهترین سفارش فروش",
        field: "PPP",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "سفارش فروش ندارد";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        headerName: "پرداخت کنونی بهترین سفارش(میلیون ریال)",
        field: "TotalValue",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، امروز باید پرداخت شود"
      },
      {
        headerName: "پرداخت نهایی بهترین سفارش(میلیون ریال)",
        field: "FinalPayment",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، در روز اعمال باید پرداخت شود"
      },
      {
        headerName: "قیمت آخرین معامله",
        field: "LastTrade",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },

      {
        headerName: "ارزندگی آخرین معامله",
        field: "DifferenceToLast",
        filter: "agNumberColumnFilter",

        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "بدون معامله";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },
      {
        headerName: "پوشش قیمت سهام با آخرین معامله",
        field: "ArzandegiLast",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "بدون معامله";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          "قیمت تمام شده سهام با توجه به قیمت آخرین معامله آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        headerName: "حجم",
        field: "TradeVolume",
        filter: "agNumberColumnFilter",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        sortable: true
      }
      // &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&
      // &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&
    ];
  },
  mounted() {
    this.loadData();

    this.height = this.getHeight();

    this.liveChecker();
    // this.$socketOptions.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     this.$store.dispatch("setSahm", JSON.parse(data.data));
    // };
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // eslint-disable-next-line no-unused-vars
    onQuickFilterChanged(event) {
      // this.gridOptions.api.setQuickFilter(event.target.value);
      this.gridOptions.api.setQuickFilter(this.filter);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
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
      this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    loadData() {
      // eslint-disable-next-line no-unused-vars
      // this.OptionAssetReq().then(response => {
      //   this.OptionTableReq();
      // });
      this.OptionTableReq();
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
        .get("/api/options", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response => {
          let data = response.data;
          this.isBusy = false;
          if (data != "noData" && data != "AccessDenied") {
            this.tableData = data;
            // this.$store.dispatch("setSahm", data);
          } else if (data == "AccessDenied") {
            this.$store.dispatch("AutoRenewAccessToken");
            this.OptionTableReq();
          }
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    getHeight() {
      return (window.innerHeight - 100).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        // let barier = { request: "get" };
        // this.$socketOptions.send(JSON.stringify(barier));
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
    // let barier = { request: "halt" };
    // this.$$socketOptions.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style scoped>
/* ag Grid */
.optionTable /deep/ .ag-root-wrapper {
  border-radius: 10px 10px 0px 0px;
}
.optionTable /deep/ .ag-header {
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

.optionTable /deep/ .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.optionTable /deep/ .ag-header-cell-label {
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
.optionTable /deep/ .ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */

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
</style>
