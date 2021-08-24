<template>
  <v-row class="mr-1 ml-1">
    <v-card width="100%" rounded="lg">
      <!-- <v-toolbar dense class="elevation-2" style="height:36px;">
        <v-toolbar-title style="height:20px;font-size:0.95em"
          >رمز ارزها</v-toolbar-title
        >
      </v-toolbar> -->
      <div id="CryptoWatchFilterRow" class="row pb-1 pt-1">
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
        class="ag-theme-balham CryptoWatchTable"
        :columnDefs="Header"
        :defaultColDef="defaultColDef"
        rowSelection="multiple"
        :cacheQuickFilter="true"
        :sideBar="sideBar"
        :enableRtl="true"
        :gridOptions="gridOptions"
        @grid-ready="onReady"
        :localeText="localeText"
        :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
      >
      </ag-grid-vue>
    </v-card>
  </v-row>
</template>
<script>
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "CryptoMarketWatch",
  components: {
    AgGridVue
  },
  data() {
    return {
      WebsocketRequest: true,
      Tablefilter: "",
      // * AGgrid base data
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      Header: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      tableData: null,
      asyncTransactionWaitMillis: 3000,
      interval: null
      // * %%%%%%%%%%%%%%%
    };
  },
  watch: {
    $route() {
      if (this.$route.name != "CryptoMarketWatch") {
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
            if (newItem.dayChange != newValue[i].dayChange) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.dayChange = itemUpdate.dayChange;
              newItem.price = itemUpdate.price;
              newItem.RialPrice = itemUpdate.RialPrice;
              newItem.volume = itemUpdate.volume;
              this.gridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
    }
  },
  computed: {
    height() {
      return (window.innerHeight - 100).toString() + "px";
    }
  },
  created() {
    document.title = "Finwise - دیده بان رمز ارز";
    this.loadData();
    let that = this;

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
    this.Header = [
      {
        headerName: "نماد",
        pinned: "right",
        field: "mapperName",
        maxWidth: 120,
        cellStyle: {
          "font-family": "IBMPlexSans",
          display: "flex",
          "justify-content": "flex-end",
          "align-items": "center"
          // direction: "ltr"
        },
        cellRenderer: function(params) {
          return `

          <span style=height:22px>
          ${params.value}
          </span>
            <img
            src="media/svg/crypto/${params.data.mapperName.toLowerCase()}.svg"
          width=17px height=17px />
          
          
           `;
        }
      },
      {
        headerName: "نام",
        field: "fullName",
        cellStyle: {
          "font-family": "IBMPlexSans",
          "font-weight": "600"
        }
      },
      {
        headerName: "قیمت (دلار)",
        field: "price",
        filter: "agNumberColumnFilter",
        valueFormatter: function(params) {
          return that.roundTo(params.value, 2).toLocaleString();
        },
        cellRenderer: "agAnimateSlideCellRenderer"
      },
      {
        headerName: "تغییر قیمت",
        field: "dayChange",
        filter: "agNumberColumnFilter",
        cellRenderer: "agAnimateShowChangeCellRenderer",
        valueFormatter: function(params) {
          if (params.value != "NaN") {
            let percent = Math.trunc(params.value * 100) / 100;
            if (params.value != 0) {
              if (percent < 0) percent = "(" + Math.abs(percent) + ")";
              return "%" + percent;
            } else return 0;
          } else return "-";
        },
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
        }
      },
      {
        headerName: "قیمت ریالی(میلیون تومان)",
        field: "RialPrice",
        filter: "agNumberColumnFilter",
        valueFormatter: function(params) {
          return that.roundTo(params.value / 10000000, 4).toLocaleString();
        }
      },
      {
        headerName: "حجم(میلیون)",
        field: "volume",
        filter: "agNumberColumnFilter",
        valueFormatter: function(params) {
          return that.roundTo(params.value / 1000000, 3).toLocaleString();
        }
      },
      {
        headerName: "ارزش بازار (میلیون دلار)",
        field: "marketCap",
        filter: "agNumberColumnFilter",
        valueFormatter: function(params) {
          return that.roundTo(params.value / 1000000, 2).toLocaleString();
        }
      }
    ];
  },

  mounted() {
    this.liveChecker();

    // eslint-disable-next-line no-unused-vars
    // let interval = setInterval(() => {
    //   this.loadData();
    // }, 10000);
  },
  methods: {
    onQuickFilterChanged(event) {
      // console.log(event.target.value);
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    onReady(params) {
      // let allColumnIds = [];
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;

      // this.gridColumnApi.getAllColumns().forEach(function(column) {
      //   allColumnIds.push(column.colId);
      // });
      // this.gridColumnApi.autoSizeColumns(allColumnIds, true);
      // this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      // params.api.sizeColumnsToFit();
      // this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
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
        this.loadData();
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getDay() != 0 && date.getDay() != 6) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    roundTo(n, digits) {
      if (n == "-") {
        return n;
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
      return parseFloat(n);
    },
    async loadData() {
      await this.axios
        .get("/api/Crypto/MarketwatchAll/")
        .then(response => {
          let data = response.data;
          this.tableData = data;
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    }
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
<style scoped>
/* ag Grid */
.CryptoWatchTable /deep/ .ag-root-wrapper {
  border-radius: 10px 10px 0px 0px;
}
.CryptoWatchTable /deep/ .ag-header {
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

.CryptoWatchTable /deep/ .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* .CryptoWatchTable /deep/ .ag-rtl {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
} */
/* header */
.CryptoWatchTable /deep/ .ag-header-cell-label {
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
.CryptoWatchTable /deep/ .ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */
</style>
