<template>
  <div class="mt-2">
    <v-card width="100%">
      <ag-grid-vue
        :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
        class="ag-theme-balham"
        :columnDefs="AdjustedHeader"
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
  name: "adjustedWidget",
  components: {
    AgGridVue
  },
  props: {
    adjusted: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      // * AGgrid base data
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      AdjustedHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      // * %%%%%%%%%%%%%%%

      height: "470px",
      WebsocketRequest: false,
      isBusy: true,
      sortDesc: false,
      filterOn: ["persiandate"],
      tableData: null,
      sortBy: "persiandate",
      Tablefilter: "",
      TypeSearch: ""
    };
  },
  created() {
    document.title = "Finwise - قیمت تعدیلی";

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
      getRowNodeId: data => data.persiandate
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

    this.AdjustedHeader = [
      {
        headerName: "تاریخ شمسی",
        field: "persiandate",
        sortable: true,
        maxWidth: 130,
        pinned: "right",
        rowDrag: true,
        cellRenderer: params => {
          let A = params.value;

          return A.substring(0, 4)+'/'+A.substring(4, 6)+'/'+A.substring(6,8);
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
        headerName: "تاریخ میلادی",
        field: "engdate",
        sortable: true,
        hide: true
      },
      {
        headerName: "پایین ترین قیمت",
        field: "low",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "بالاترین قیمت",
        field: "high",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت پایانی",
        field: "closing",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "اولین قیمت",
        field: "first",
        filter: "agNumberColumnFilter",
        sortable: true,
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
        headerName: "قیمت دیروز",
        field: "yesterday",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "بالاترین-تعدیلی",
        field: "adjustedhigh",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "پایین ترین-تعدیلی",
        field: "adjustedlow",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "پایانی -تعدیلی",
        field: "adjustedclosing",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "آخرین - تعدیلی",
        field: "adjustedlast",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "اولین - تعدیلی",
        field: "adjustedfirst",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم معاملات",
        field: "volume",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "ارزش معاملات",
        field: "value",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد معاملات",
        field: "count",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      }
    ];
  },
  watch: {
    adjusted( ) {
      // console.log("🚀 ~ file: AdjustedPricesWidget.vue ~ line 306 ~ adjusted ~ this.adjusted", this.adjusted)
        this.gridApi.setRowData(this.adjusted);
        this.dataFetch = true;
    }
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
      if (this.adjusted != null) params.api.setRowData(this.adjusted);
    },
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    getHeight() {
      return (window.innerHeight - 200).toString() + "px";
    }
  },
  mounted() {
    this.height = this.getHeight();
  }
};
</script>
<style scoped>
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

.Funds-table-head {
  /* background-color: #e01313; */
  vertical-align: middle !important;
  font-size: 1.1em !important;
  font-weight: 600 !important ;
}
.Funds-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8em !important;
  line-height: 1 !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-row:hover {
  background-color: #999999 !important;
}
.Funds-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-cell-green {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-cell-red {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
  vertical-align: middle !important;
}
.Funds-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
</style>
