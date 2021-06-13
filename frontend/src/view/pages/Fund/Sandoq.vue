<template>
  <!-- <ErrorMine></ErrorMine> -->
  <div>
    <!-- table -->
    <div class="row mr-1 ml-1">
      <v-card width="100%">
        <div id="FundsFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-3 col-lg-3  col-md-8 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-form-input
                v-model="Tablefilter"
                type="search"
                id="filterInput"
                placeholder="فیلتر"
                @keyup="onQuickFilterChanged"
              ></b-form-input>
              <b-input-group-append>
                <b-button v-if="Tablefilter.length" @click="Tablefilter = ''"
                  >پاک کردن</b-button
                >
              </b-input-group-append>
            </b-input-group>
          </div>
          <!-- <div class="col-xxl-4 col-lg-4 col-md-8 col-sm-12 mt-1">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div> -->
        </div>
        <ag-grid-vue
          :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
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
        <div></div>
        <!-- <b-table
          thClass="Funds-table-head"
          class="Funds-table"
          tbody-tr-class="Funds-table-row"
          striped
          :busy.sync="isBusy"
          :sticky-header="height"
          dense
          :filter="Tablefilter"
          :filter-included-fields="filterOn"
          :sort-desc.sync="sortDesc"
          :sort-by.sync="sortBy"
          sort-direction="desc"
          sort-icon-left
          bordered
          no-border-collapse
          outlined
          small
          hover
          responsive
          :items="tableData"
          :fields="HD"
          @filtered="onFiltered"
        >
          <template #table-busy>
            <div class="text-center text-danger my-2">
              <b-spinner class="align-middle mr-2"></b-spinner>
              <strong>شکیبا باشید</strong>
            </div>
          </template>
          <template #cell(ticker)="data">
            <b class="Funds-table-cell-bold" @click="tickerClick(data)">{{
              data.value
            }}</b>
          </template>
          <template #cell(TradeCount)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(TradeVolume)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(TradeValue)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(yesterday)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(last)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(close)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(first)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(low)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(high)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(MinRange)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(MaxRange)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(EPS)="data">
            <b v-if="data.value == 'NaN'" class="Funds-table-cell">
              {{ "-" }}</b
            >
            <b v-else class="Funds-table-cell">
              {{ data.value.toLocaleString() }}</b
            >
          </template>
          <template #cell(CountBuy_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountBuy_Hoguhgi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeBuy_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeBuy_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountSell_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountSell_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeSell_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeSell_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(closePercent)="data">
            <b v-if="data.value > 0" class="Funds-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="Funds-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="Funds-table-cell"
              >{{ data.value }}%</b
            >
          </template>
          <template #cell(lastPercent)="data">
            <b v-if="data.value > 0" class="Funds-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="Funds-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="Funds-table-cell"
              >{{ data.value }}%</b
            >
          </template>
        </b-table> -->
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
      // AGgrid
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

      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

      height: "470px",
      WebsocketRequest: false,
      isBusy: true,
      sortDesc: false,
      filterOn: ["ticker"],
      tableData: null,
      sortBy: "ticker",
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      Tablefilter: "",
      TypeSearch: "",
      FundsTableHeader: [
        {
          label: "نماد",
          key: "ticker",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "بازار",
          key: "marketName",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "درصد آخرین قیمت",
          key: "lastPercent",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "درصد قیمت پایانی",
          key: "closePercent",
          thClass: "Funds-table-head",
          sortable: true
        },
        // { label: "نام", key: "name" },
        // { label: "صنعت", key: "industry" },
        // { label: "آخرین بروز رسانی", key: "updatedAt" },
        // {
        //   label: "کف مجاز قیمت",
        //   key: "MinRange",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "سقف مجاز قیمت",
        //   key: "MaxRange",
        //   thClass: "Funds-table-head"
        // },
        // // { label: "EPS", key: "EPS", thClass: "Funds-table-head" },
        // {
        //   label: "بالاترین قیمت",
        //   key: "high",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "کمترین قیمت",
        //   key: "low",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "اولین قیمت",
        //   key: "first",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        }
      ]
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

    this.FundsHeader = [
      {
        headerName: "نماد",
        field: "ticker",

        sortable: true,
        maxWidth: 100,
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
        sortable: true
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
    this.liveChecker();
    this.$socketSandoq.onmessage = data => {
      // this.tableData = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData = JSON.parse(data.data);
    };
  },
  computed: {
    HD() {
      return this.TriggerFilteredHeader();
    }
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        console.log("chaange");
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
    },
    onReady(params) {
      console.log("onReady");
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
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    getHeight() {
      return (window.innerHeight - 100).toString() + "px";
    },
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/Funds")
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
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.FundsTableHeader));
      let options = this.selectedHeaderOptions;
      let SwCase = 0;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "HH") SwCase = 2;
      } else if (options.length == 2) SwCase = 3;

      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 2:
          header.splice(5, 1);
          break;
        case 3:
          break;
        default:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      return header;
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketSandoq.send(JSON.stringify(barier));
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
    let barier = { request: "halt" };
    this.$socketSandoq.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
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
