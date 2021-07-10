<template>
  <div>
    <!-- User Interface controls -->
    <v-card :loading="!dataFetch && !cardKey">
      <v-toolbar dense>
        <v-toolbar-title v-if="cardKey">لیست مجامع</v-toolbar-title>
        <v-toolbar-title v-if="!cardKey">{{ AssemblyName }}</v-toolbar-title>
        <v-card-subtitle style="textalign:right" v-if="!cardKey">
          <span> {{ subTitle }}</span>
        </v-card-subtitle>
        <v-spacer></v-spacer>

        <v-btn v-if="!cardKey" icon @click="cardKey = !cardKey">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
      </v-toolbar>
      <transition-group name="slide-fade" tag="div">
        <div v-show="cardKey" key="1">
          <ag-grid-vue
            :style="
              `width: 100%; height:  ${height}px; font-family: Vazir-Medium-FD`
            "
            class="ag-theme-balham AssemblyListTable"
            :localeText="localeText"
            :defaultColDef="defaultColDef"
            :columnDefs="DecisionTableHeader"
            :enableRtl="true"
            :gridOptions="gridOptions"
            :allowContextMenuWithControlKey="false"
            @grid-ready="onReady"
          ></ag-grid-vue>
          <div
            id="AssemblyTablePaginationContainer"
            style="
              display: flex;
              justify-content: center;width:100%"
          >
            <div class="col-6">
              <v-pagination
                v-model="tablePaginationNumber"
                :length="tablePaginationLength"
                :total-visible="10"
              ></v-pagination>
            </div>
          </div>
        </div>
        <div v-if="!cardKey" key="2" class="mt-2">
          <!-- ******************** TABLE COMPONENT ********************* -->
          <AssemblyTables
            v-if="dataFetch"
            :ShareholdersItems="ShareholdersData"
            :ChiefItems="ChiefData"
            :SummaryItems="SummaryData"
            :ICitems="ICData"
            :StatementItems="StatementData"
            :CEOItems="CEOData"
            :BoardItems="BoardData"
            :NewBoardItems="NewBoardData"
            :WageItems="WageData"
          >
          </AssemblyTables>
          <!-- ******************** TABLE COMPONENT ********************* -->
        </div>
      </transition-group>
    </v-card>
    <!-- </div> -->
  </div>
</template>
<script>
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
import AssemblyTables from "@/view/pages/Ticker/AssemblyWidget/content/AssemblyTables.vue";
export default {
  name: "Decisions",
  components: { AssemblyTables, AgGridVue },
  data() {
    return {
      // * AGgrid base data
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      DecisionTableHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      loading: true,
      dataFetch: false,
      tableData: [],
      height: 400,
      tablePaginationLength: 10,
      tablePaginationNumber: 1,
      // * %%%%%%%%%%%%%%%
      cardKey: true,
      AssemblyName: "",
      subTitle: "",
      totalRows: 1,
      currentPage: 1,
      perPage: 15,
      isBusy: false,
      ListData: null,
      filter: null,
      // test DATA BELOW *******************************************

      pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      ShareholdersData: [],
      ChiefData: [],
      SummaryData: [],
      ICData: [],
      StatementData: [],
      CEOData: [],
      BoardData: [],
      NewBoardData: [],
      WageData: []
      // filterOn: []
    };
  },
  watch: {
    tablePaginationNumber(newValue, oldValue) {
      if (oldValue + 1 == newValue) {
        this.gridApi.paginationGoToNextPage();
      } else if (oldValue == newValue + 1) {
        this.gridApi.paginationGoToPreviousPage();
      } else {
        this.gridApi.paginationGoToPage(newValue - 1);
      }
    },
    tableData(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        this.gridApi.setRowData(newValue);

        this.tablePaginationLength = this.gridApi.paginationGetTotalPages();
        this.gridOptions.api.hideOverlay();
        // this.dataFetch = true;
      }
    }
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    }
  },
  created() {
    document.title = "Finwise - تصمیمات مجامع";

    // GRID LOCALE FILE LOAD
    this.localeText = AG_GRID_LOCALE_FA;
    // GRID OPTIONS
    this.gridOptions = {
      headerHeight: 30,
      rowHeight: 25,
      // enables pagination in the grid
      pagination: true,

      // sets 10 rows per page (default is 100)
      paginationPageSize: 10,
      paginationAutoPageSize: true,
      suppressPaginationPanel: true,
      // getRowNodeId: data => data.ID
      floatingFilter: true,
      resizable: true,
      suppressContextMenu: true
      // overlayLoadingTemplate:
      //   '<span class="ag-overlay-loading-center">Please wait while your rows are loading</span>'
      // domLayout: 'autoHeight'
    };

    this.defaultColDef = {
      flex: 1,
      // sortable: true,
      paginationAutoPageSize: true,
      suppressMenu: true,
      enablePivot: false,
      cellStyle: {
        display: "flex",
        "justify-content": "center",
        "align-items": "center",
        direction: "ltr"
      }
    };
    this.DecisionTableHeader = [
      {
        headerName: "تاریخ انتشار",
        field: "PublishTime",
        maxWidth: 200,
        filter: "agSetColumnFilter",
        filterParams: {
          applyMiniFilterWhileTyping: true
        }
      },
      {
        headerName: "سهم",
        field: "Ticker",
        maxWidth: 170,
        filter: "agSetColumnFilter",
        filterParams: {
          applyMiniFilterWhileTyping: true
        },
        cellStyle: {
          color: "#067BDA",
          "font-weight": "500"
        },
        cellRenderer: params => {
          const link = document.createElement("a");
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.tickerClick(params.data);
          });
          return link;
        }
      },
      {
        headerName: "عنوان",
        field: "title",
        cellStyle: {
          color: "#067BDA",
          "font-weight": "500"
        },
        cellRenderer: params => {
          const link = document.createElement("a");
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.titleClick(params.data);
          });
          return link;
        }
      },
      {
        headerName: "لینک کدال",
        field: "HtmlUrl",
        maxWidth: 100,
        cellRenderer: function(params) {
          const div = document.createElement("div");
          const html = `<button type="button" class="v-icon notranslate mr-1 v-icon--link mdi mdi-link-variant theme--light" style="font-size: 15px; color: rgb(70, 130, 180); caret-color: rgb(70, 130, 180);"></button>`;
          div.innerHTML = html;
          div.addEventListener("click", () => {
            window.open("https://codal.ir" + params.value, "_blank");
          });
          return div;
        }
      }
    ];
  },
  mounted() {
    this.height = this.getHeight();
    this.loadData();
  },
  methods: {
    getHeight() {
      return (
        window.innerHeight -
        115 -
        document.getElementById("AssemblyTablePaginationContainer").offsetHeight
      );
    },
    onReady(params) {
      let allColumnIds = [];
      // this.gridOptions.api.closeToolPanel();
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;
      // show 'loading' overlay
      this.gridOptions.api.showLoadingOverlay();
      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      this.allColumnIds = allColumnIds;
      if (this.tableData != null) {
        params.api.setRowData(this.tableData);
        this.gridOptions.api.hideOverlay();
      }
    },
    tickerClick(item) {
      // console.log(item);
      this.$router.push({
        name: "TickerOverall",
        params: { id: item.StockID }
      });
    },

    async loadData() {
      this.isBusy = true;

      await this.axios
        .get("/api/MainAssemblyDataList")
        .then(response => {
          this.isBusy = false;
          this.totalRows = response.data.length;
          // this.ListData = response.data;
          this.tableData = response.data;
          this.tablePaginationLength = response.data.length;
        })
        .catch(error => {
          this.isBusy = false;

          console.error(error);
        });
    },
    TablesReq(ID, type) {
      this.axios({
        method: "post",
        url: "/api/tickerAssemblyStepTwo",
        data: {
          SummaryID: ID,
          Type: "Assembly" + type
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          let data = response.data;
          if (type == "General") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
            this.dataFetch = true;
          } else if (type == "Extra") {
            this.StatementData = [];
            this.CEOData = [];
            this.BoardData = [];
            this.NewBoardData = [];
            this.WageData = [];
            this.ICData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.SummaryData = data[3];
            this.dataFetch = true;
          } else if (type == "GeneralExtra") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
            this.dataFetch = true;
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    titleClick(item) {
      this.dataFetch = false;
      this.TablesReq(item.ID, item.Type);
      // console.log(item.item);
      this.subTitle = item.title;
      this.AssemblyName = item.Ticker;
      this.cardKey = false;
    },
    info(item) {
      window.open("https://codal.ir" + item.HtmlUrl, "_blank");
    }
    // onFiltered(filteredItems) {
    //   // Trigger pagination to update the number of buttons/pages due to filtering
    //   this.totalRows = filteredItems.length;
    //   this.currentPage = 1;
    // }
  }
};
</script>
<style scoped>
/* ag Grid */
.AssemblyListTable /deep/ .ag-theme-balham .ag-header {
  background-color: var(--ag-header-background-color, #fff) !important;

  /* border-top: solid 1px;
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-top-color: #bdc3c7;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-radius: 10px 10px 0px 0px !important; */
}
.AssemblyListTable /deep/ .ag-header-cell {
  /* background-color: rgb(153, 153, 153); */
  background-color: var(--ag-foreground-color, #f5f5f5);
  /* color: #fff; */
  color: var(--ag-background-color, #000);
  outline-color: #000 !important;
  /* %%%%%%%%%%%%%%%%%%%% */
  /* border-top: solid 1px;
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-top-color: #bdc3c7;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-radius: 10px 10px 0px 0px !important; */
}
.AssemblyListTable /deep/ .ag-header-row-column {
  border-top: solid 1px;
  outline-color: #000 !important;
  /* background-color: #4682b4; */
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--ag-border-color, #4a525a);
  border-top-color: #4a525a;
  border-top-color: var(--ag-border-color, #4a525a);
  border-radius: 30px 30px 0px 0px !important;
}
.AssemblyListTable /deep/ .ag-theme-balham .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.AssemblyListTable /deep/ .ag-header-cell-label {
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
.AssemblyListTable /deep/ .ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


/* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
/* .AssemblyTitle {
  color: #4682b4;
  cursor: pointer;
}
.Descision-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.Descision-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.Descision-table-row {
  direction: ltr;
  vertical-align: middle !important;
} */
</style>
