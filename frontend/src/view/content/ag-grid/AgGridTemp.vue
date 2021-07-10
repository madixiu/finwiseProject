<template>
  <div>
    <input
      class="mr-2 form-control d-inline-block"
      @keyup="onQuickFilterChanged"
      type="text"
      id="quickFilterInput"
      placeholder="Type text to filter..."
    />
    <ag-grid-vue
      style="width: 100%; height:  300px; font-family: 'Vazir-Medium-FD'"
      class="ag-theme-balham marketWatchTable"
      :columnDefs="cols"
      :defaultColDef="defaultColDef"
      :rowData="rows"
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
  </div>
</template>
<script>
// for enterprise features
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";

export default {
  name: "AgGridTemp",
  components: {
    AgGridVue
  },
  props: {
    rows: Array,
    cols: Array
  },
  data() {
    return {
      modules: AllModules,
      allColumnIds: [],
      filter: null,
      localeText: null,
      gridOptions: {
        suppressColumnVirtualisation: true,
        rowDragManaged: true,
        animateRows: true,
        rowHeight: 22,
        // rowStyle: { background: "black"},
        rowClass: "ag-grid-row-class"
        // skipHeaderOnAutoSize: true
      },
      gridColumnApi: null,
      gridApi: null,
      columnApi: null,
      defaultColDef: {
        flex: 1,
        cellClass: "align-center",
        resizable: true,
        filter: true,

        // minWidth: 50,

        enableCellChangeFlash: true
        // resizable: true,
      },
      sideBar: {
        toolPanels: [
          {
            id: "columns",
            labelDefault: "Columns",
            labelKey: "columns",
            iconKey: "columns",
            toolPanel: "agColumnsToolPanel",
            toolPanelParams: {
              suppressRowGroups: false,
              suppressValues: false,
              suppressPivots: true,
              suppressPivotMode: true,
              suppressSideButtons: true,
              suppressColumnFilter: true,
              suppressColumnSelectAll: false,
              suppressColumnExpandAll: false
            }
          }
        ],
        defaultToolPanel: ""
      }
    };
  },
  created() {
    this.localeText = AG_GRID_LOCALE_FA;
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    // this.gridColumnApi = this.gridOptions.columnApi;
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // setInterval(() => {

    //   let barier = {
    //     request: "get",
    //     data: {
    //       marketName: "همه",
    //       marketIndustry: []
    //     }
    //   };
    //   this.$socketMarketWatch.send(JSON.stringify(barier));
    // }, 5000);
    // this.$socketMarketWatch.send(JSON.stringify({ request: "get" }));
    // this.liveChecker();
    // this.$socketMarketWatch.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     this.rows = JSON.parse(data.data);
    // };
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
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
    },
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
      // this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
    }
  }
};
</script>
<style>
.ag-theme-balham .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
}
.ag-header-cell-label {
  color: black;
  font-size: 1em;
  align-items: center;
  text-align: center;
  margin-right: 1px !important;
  display: flex;
  justify-content: center;
  align-content: center;
}
.ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
</style>
