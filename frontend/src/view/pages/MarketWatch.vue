<template>
  <div>
    <!-- table -->
    <div class="row mr-1 ml-1">
      <v-card width="100%">
        <div id="marketwatchFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-2 col-lg-2 col-md-6 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-input-group-prepend is-text>
                <!-- <b-icon v-if="filter != ''" icon="x-circle" @click="filter=''"></b-icon>
                <b-icon v-else icon="search"></b-icon> -->
                <b-icon icon="search"></b-icon>
              </b-input-group-prepend>
              <b-form-input
                v-model="Tablefilter"
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
          class="ag-theme-balham"
          :columnDefs="MarketWatchHeader"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
          :cacheQuickFilter="true"
          :sideBar="sideBar"
          :enableRtl="true"
          :gridOptions="gridOptions"
          @grid-ready="onReady"
          @gridColumnsChanged="gridColumnsChanged"
          :localeText="localeText"
          :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
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
  name: "marketwatch",
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
      MarketWatchHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      tableData: null,
      asyncTransactionWaitMillis: 4000,
      interval: null,
      // * %%%%%%%%%%%%%%%
      height: "370px",
      isBusy: true,
      tableMarketSelected: "همه",
      tableMarketFilters: ["همه", "بورس", "فرابورس"],
      tableMarketTypeSelected: [],
      tableMarketTypeFilters: [],
      tableMarketIndustrySelected: [],
      tableMarketIndustryFilters: [],
      WebsocketRequest: false,
      selectedHeaderOptions: [],
      Tablefilter: "",
      // tableData: [],
      TypeSearch: "",
      IndustrySearch: "",
      value: []
    };
  },
  watch: {
    $route() {
      if (this.$route.name != "marketwatch") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    },
    tableData(newValue, oldValue) {
      if (oldValue == null && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }

      if (oldValue != null)
        if (this.dataFetch == true && oldValue.length != 0)
          for (let i = 0; i < this.tableData.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.lastPercent != newValue[i].lastPercent) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.lastPercent = itemUpdate.lastPercent;
              newItem.closePercent = itemUpdate.closePercent;
              newItem.last = itemUpdate.last;
              newItem.last = itemUpdate.close;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.gridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
    }
  },
  created() {
    document.title = "Finwise - دیده‌بان";
    // GRID LOCALE FILE LOAD
    this.localeText = AG_GRID_LOCALE_FA;

    // GRID OPTIONS
    this.gridOptions = {
      suppressColumnVirtualisation: true,
      rowDragManaged: true,
      animateRows: true,
      rowClass: "ag-grid-row-class",
      colResizeDefault: "shift",
      // headerHeight: 20,
      rowHeight: 22,
      getRowNodeId: data => data.ticker
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

    this.MarketWatchHeader = [
      {
        headerName: "نماد",
        field: "ticker",
        maxWidth: 120,
        sortable: true,

        pinned: "right",
        rowDrag: true,
        cellRenderer: params => {
          const link = document.createElement("a");
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.tickerClick(params.data);
          });
          return link;
        },
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
          // // "justify-content": "center",
          // "align-items": "center !important",
          // "height": "100%"
        }
      },
      {
        headerName: "بازار",
        field: "marketName",
        sortable: true,
        minWidth: 150
      },
      {
        headerName: "صنعت",
        field: "industry",
        sortable: true,
        minWidth: 250,
        hide: true
      },
      {
        headerName: "تعداد معاملات",
        field: "TradeCount",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم معاملات",
        field: "TradeVolume",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "ارزش معاملات",
        field: "TradeValue",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت دیروز",
        field: "yesterday",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "آخرین قیمت",
        field: "last",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          return params.value.toLocaleString();
        },
        cellRenderer: "agAnimateSlideCellRenderer"
      },
      {
        headerName: "درصد آخرین قیمت",
        field: "lastPercent",
        filter: "agNumberColumnFilter",
        cellStyle: params => {
          if (params.value > 0) {
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
        },
        sortable: true,
        valueFormatter: function(params) {
          let percent = params.value;
          if (percent < 0) percent = "(" + Math.abs(percent) + ")";

          return "%" + percent.toLocaleString();
        },
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "قیمت پایانی",
        field: "close",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          return params.value.toLocaleString();
        },
        cellRenderer: "agAnimateSlideCellRenderer"
      },
      {
        headerName: "درصد قیمت پایانی",
        filter: "agNumberColumnFilter",
        field: "closePercent",
        sortable: true,
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
        },
        valueFormatter: function(params) {
          let percent = params.value;
          if (percent < 0) percent = "(" + Math.abs(percent) + ")";

          return "%" + percent.toLocaleString();
        },
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "کف مجاز قیمت",
        field: "MinRange",
        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "سقف مجاز قیمت",
        field: "MaxRange",
        sortable: true,
        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "EPS",
        field: "EPS",
        hide: true,
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "بالاترین قیمت",
        field: "high",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "کمترین قیمت",
        field: "low",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "اولین قیمت",
        field: "first",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد خرید حقیقی",
        field: "CountBuy_Haghighi",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد خرید حقوقی",
        field: "CountBuy_Hoguhgi",
        filter: "agNumberColumnFilter",

        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم خرید حقیقی",
        field: "VolumeBuy_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم خرید حقوقی",
        field: "VolumeBuy_Hoghughi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد فروش حقیقی",
        field: "CountSell_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد فروش حقوقی",
        field: "CountSell_Hoghughi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم فروش حقیقی",
        field: "VolumeSell_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم فروش حقوقی",
        field: "VolumeSell_Hoghughi",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      }
    ];
  },
  mounted() {
    this.height = this.getHeight();
    this.loadData();
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // this.$socketMarketWatch.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    // this.$socketMarketWatch.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     this.$store.dispatch("setMarketWatchItems", JSON.parse(data.data));
    // };
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    onQuickFilterChanged(event) {
      // console.log(event.target.value);
      this.gridOptions.api.setQuickFilter(event.target.value);
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
      // this.gridColumnApi.autoSizeColumns(allColumnIds, true);
      this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      // this.gridApi.api.sizeColumnsToFit();
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    tickerClick(data) {
      // ! needs modification when ETF has been added
      if (!data.marketName.includes("ETF"))
        this.$router.push({ path: `/ticker/Overview/Overall/${data.ID}` });
    },

    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.MarketWatchTableReq().then(response => {
        this.MarketWatchFilterListReq();
      });
    },
    async MarketWatchTableReq() {
      this.isBusy = true;

      await this.axios
        .get("/api/marketwatch")
        .then(response => {
          this.isBusy = false;
          this.$store.dispatch("setMarketWatchItems", response.data);
          this.tableData = response.data;
        })
        .catch(error => {
          this.isBusy = false;

          console.error(error);
        });
    },
    async MarketWatchFilterListReq() {
      await this.axios.get("/api/marketwatchfilterlists").then(response => {
        this.tableMarketIndustryFilters = response.data;
      });
    },
    MarketWatchFilterPost() {
      this.axios({
        method: "post",
        url: "/api/marketwatch",
        data: {
          marketName: this.tableMarketSelected,
          // marketType: this.tableMarketTypeSelected,
          marketIndustry: this.tableMarketIndustrySelected
        },
        headers: { "Content-Type": "application/json" },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response2 => {
          // this.$store.dispatch("setMarketWatchItems", response2.data);
          this.tableData = response2.data;
          this.gridApi.setRowData(this.tableData);
        })
        .catch(error => {
          console.error(error);
        });
    },

    TypeonOptionClick({ option, addTag }) {
      addTag(option);
      this.TypeSearch = "";
      this.MarketWatchFilterPost();
    },
    IndustryonOptionClick({ option, addTag }) {
      addTag(option);
      this.IndustrySearch = "";
      this.MarketWatchFilterPost();
    },
    getHeight() {
      return (window.innerHeight - 100).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval._id);
          return;
        }
        // let barier = {
        //   request: "get",
        //   data: {
        //     marketName: this.tableMarketSelected,
        //     marketIndustry: this.tableMarketIndustrySelected
        //   }
        // };
        // this.$socketMarketWatch.send(JSON.stringify(barier));
        this.MarketWatchTableReq();
      }, 10000);
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
  beforeDestroy() {
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  }
};
</script>
<style>
/* 
TODO:Clean the CSS & add scoped based class
*/
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
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */

.form-input-class {
  direction: rtl;
}
.form-tag-class {
  direction: rtl !important;
}
</style>
