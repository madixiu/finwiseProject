<template>
  <div>
    <div class="row mr-1 ml-1">
      <v-card rounded="lg" width="100%">
        <div id="FundsFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-2 col-lg-2  col-md-8 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-input-group-prepend is-text>
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
          class="sandoqTable ag-theme-balham"
          :columnDefs="FundsHeader"
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
  name: "Funds",
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
      FundsHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      // * %%%%%%%%%%%%%%%
      height: "470px",
      WebsocketRequest: false,
      isBusy: true,
      tableData: null,
      Tablefilter: ""
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
    document.title = "Finwise - صندوق";

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
      getRowNodeId: data => data.ID
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
        headerName: "نام",
        field: "name",

        sortable: true,
        // maxWidth: 100,
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
        headerName: "بورسی",
        field: "ETF",
        sortable: true
      },
      {
        headerName: "اندازه صندوق",
        field: "Size",
        sortable: true
      },
      {
        headerName: "نوع صندوق",
        field: "Type",
        sortable: true
      },
      {
        headerName: "قیمت صدور",
        field: "SubscriptionNav",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت ابطال",
        field: "SubscriptionNav",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت آماری",
        field: "StaticalNav",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "مجموع دارایی خالص",
        field: "NetAssetValue",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد واحد صندوق",
        field: "TotalUnit",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "متولی",
        field: "CustodianName",
        sortable: true,
        hide: true
      },
      {
        headerName: "مدیر صندوق",
        field: "ManagerName",
        sortable: true,
        hide: true
      },
      {
        headerName: "ضامن نقد شوندگی",
        field: "LiquidityGuaranteeName",
        sortable: true,
        hide: true
      },
      {
        headerName: "مدیر صندوق",
        field: "ManagerName",
        sortable: true,
        hide: true
      },
      {
        headerName: "مدیر سرمایه گذاری",
        field: "InvestmentManagerName",
        sortable: true,
        hide: true
      },
      {
        headerName: "تاریخ شروع به کار",
        field: "ActivityStartDate",
        sortable: true,
        hide: true
      }
    ];
  },
  mounted() {
    this.loadData();
    this.height = this.getHeight();
    this.liveChecker();
    // this.$socketSandoq.onmessage = data => {
    //   // this.tableData = JSON.parse(data.data);
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     // this.$store.dispatch("setSahm", JSON.parse(data.data));
    //     this.tableData = JSON.parse(data.data);
    // };
  },
  methods: {
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
      this.$router.push({ path: `/SingleNonETF/${data.ID}` });
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
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    getHeight() {
      return (window.innerHeight - 100).toString() + "px";
    },
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/FundsAll")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData = data;
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },

    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        // let barier = { request: "get" };
        // this.$socketSandoq.send(JSON.stringify(barier));
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
        // this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketSandoq.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style scoped>
/* ag Grid */
.sandoqTable /deep/ .ag-root-wrapper {
  border-radius: 10px 10px 0px 0px;
}
.sandoqTable /deep/ .ag-header {
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

.sandoqTable /deep/ .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.sandoqTable /deep/ .ag-header-cell-label {
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
.sandoqTable /deep/ .ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */
</style>
