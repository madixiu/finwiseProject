<template>
  <div class="row mr-1  ml-1" height="100%">
    <v-card rounded="lg" width="100%">
      <b-row>
        <b-col cols="2" class="my-1 mr-1">
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
            <b-input-group-append>
              <b-button v-if="Tablefilter.length" @click="Tablefilter = ''"
                >پاک کردن</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-col>
      </b-row>
      <ag-grid-vue
        :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
        class="taqadomTable ag-theme-balham"
        :columnDefs="TaqadomHeader"
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
</template>
<script>
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "Taghadom",
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
      TaqadomHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,

      // * %%%%%%%%%%%%%%%
      WebsocketRequest: false,
      height: "470px",
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
    document.title = "Finwise - حق تقدم";

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

    this.TaqadomHeader = [
      {
        headerName: "نماد",
        field: "ticker",
        maxWidth: 110,
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
        headerName: "بازار",
        field: "marketName",
        sortable: true,
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

        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "درصد آخرین قیمت",
        field: "lastPercent",
        filter: "agNumberColumnFilter",

        // cellStyle: {
        //   display: "flex",
        // color: "green",
        //   "justify-content": "center",
        //   "border-left-color": "#e2e2e2",

        //   "align-items": "center",
        //   direction: "ltr"
        // },
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
        sortable: true,
        cellRenderer: function(params) {
          let Class = "";
          let percent = params.value;
          if (percent > 0) Class = "greenCell";
          else if (percent < 0) {
            Class = "redCell";
            percent = "(" + Math.abs(percent) + ")";
          }
          return `<span class="${Class}"><span class="${Class}" style="font-size:0.9em">%</span>${percent}</span>`;
        }
      },
      {
        headerName: "قیمت پایانی",
        field: "close",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
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
        cellRenderer: function(params) {
          let Class = "";
          let percent = params.value;
          if (percent > 0) Class = "greenCell";
          else if (percent < 0) {
            Class = "redCell";
            percent = "(" + Math.abs(percent) + ")";
          }
          return `<span class="${Class}">%${percent}</span>`;
        }
      },
      {
        headerName: "آخرین قیمت دارایی پایه",
        field: "ParentLast",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: false,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "پوشش",
        field: "Coverage",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: false,
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
        cellRenderer: function(params) {
          let Class = "";
          let percent = params.value;
          if (percent > 0) Class = "greenCell";
          else if (percent < 0) {
            Class = "redCell";
            percent = "(" + Math.abs(percent) + ")";
          }
          return `<span class="${Class}">%${percent}</span>`;
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
    this.loadData();
    this.height = this.getHeight();
    // this.$socketTaqadom.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     this.tableData = JSON.parse(data.data);
    // };
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        // this.gridColumnApi.sizeColumnsToFit();

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
      // this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/HaghTaghadom")
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
        // this.$socketTaqadom.send(JSON.stringify(barier));
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
    // this.$socketTaqadom.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style scoped>
/* ag Grid */
.taqadomTable /deep/ .ag-root-wrapper {
  border-radius: 10px 10px 0px 0px;
}
.taqadomTable /deep/ .ag-header {
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

.taqadomTable /deep/ .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.taqadomTable /deep/ .ag-header-cell-label {
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
.taqadomTable /deep/ .ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */
</style>
