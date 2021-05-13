<template>
  <!-- <ErrorMine></ErrorMine> -->
  <div style="height: 100%">
    <div class="example-wrapper">
      <div>
        <span class="button-group">
          <button v-on:click="showPivotModeSection()">
            Show Pivot Mode Section
          </button>
          <button v-on:click="showRowGroupsSection()">
            Show Row Groups Section
          </button>
          <button v-on:click="showValuesSection()">Show Values Section</button>
          <button v-on:click="showPivotSection()">Show Pivot Section</button>
        </span>
      </div>
      <ag-grid-vue
        style="width: 300px; height: 300px;"
        class="ag-theme-alpine"
        id="myGrid"
        :gridOptions="gridOptions"
        :columnDefs="columnDefs"
        :defaultColDef="defaultColDef"
        :sideBar="sideBar"
        :rowData="rowData"
      ></ag-grid-vue>
    </div>
    <div>
      <button @click="getSelectedRows()">Get Selected Rows</button>

      <ag-grid-vue
        style="width: 500px; height: 500px;"
        class="ag-theme-alpine"
        :columnDefs="columnDefs"
        :defaultColDef="defaultColDef"
        :rowData="rowData"
        rowSelection="multiple"
        :sideBar="true"
      >
      </ag-grid-vue>
    </div>
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-6.vue";
import { AgGridVue } from "ag-grid-vue";

export default {
  name: "AI",
  components: {
    // Error,
    // ErrorMine
    AgGridVue
  },
  data() {
    return {
      gridOptions: null,
      gridColumnApi: null,
      gridApi: null,
      columnApi: null,
      columnDefs: [
        { headerName: "Col A", field: "make", sortable: true },
        { headerName: "Col B", field: "model", sortable: true },
        { headerName: "Col C", field: "price", sortable: true }
      ],
      defaultColDef: null,
      sideBar: {
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
              suppressSideButtons: true,
              suppressColumnFilter: true,
              suppressColumnSelectAll: true,
              suppressColumnExpandAll: true
            }
          }
        ],
        defaultToolPanel: "columns"
      },
      rowData: [
        { make: "Toyota", model: "Celica", price: 35000 },
        { make: "Ford", model: "Mondeo", price: 32000 },
        { make: "Porsche", model: "Boxter", price: 72000 }
      ],
      FundsTableHeader: [
        {
          headerName: "نماد",
          field: "ticker",

          sortable: true
        },
        {
          headerName: "بازار",
          field: "marketName",

          sortable: true
        },
        {
          headerName: "تعداد معاملات",
          field: "TradeCount",

          sortable: true
        },
        {
          headerName: "حجم معاملات",
          field: "TradeVolume",

          sortable: true
        },
        {
          headerName: "ارزش معاملات",
          field: "TradeValue",

          sortable: true
        },
        {
          headerName: "قیمت دیروز",
          field: "yesterday",

          sortable: true
        },
        {
          headerName: "آخرین قیمت",
          field: "last",

          sortable: true
        },
        {
          headerName: "درصد آخرین قیمت",
          field: "lastPercent",

          sortable: true
        },
        {
          headerName: "قیمت پایانی",
          field: "close",

          sortable: true
        },
        {
          headerName: "درصد قیمت پایانی",
          field: "closePercent",

          sortable: true
        },
        // { field: "نام", key: "name" },
        // { field: "صنعت", key: "industry" },
        // { field: "آخرین بروز رسانی", key: "updatedAt" },
        // {
        //   field: "کف مجاز قیمت",
        //   key: "MinRange",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   field: "سقف مجاز قیمت",
        //   key: "MaxRange",
        //   thClass: "Funds-table-head"
        // },
        // // { field: "EPS", key: "EPS", thClass: "Funds-table-head" },
        // {
        //   field: "بالاترین قیمت",
        //   key: "high",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   field: "کمترین قیمت",
        //   key: "low",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   field: "اولین قیمت",
        //   key: "first",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        {
          headerName: "تعداد خرید حقیقی",
          field: "CountBuy_Haghighi",

          sortable: true
        },
        {
          headerName: "تعداد خرید حقوقی",
          field: "CountBuy_Hoguhgi",

          sortable: true
        },
        {
          headerName: "حجم خرید حقیقی",
          field: "VolumeBuy_Haghighi",

          sortable: true
        },
        {
          headerName: "حجم خرید حقوقی",
          field: "VolumeBuy_Hoghughi",

          sortable: true
        },
        {
          headerName: "تعداد فروش حقیقی",
          field: "CountSell_Haghighi",

          sortable: true
        },
        {
          headerName: "تعداد فروش حقوقی",
          field: "CountSell_Hoghughi",

          sortable: true
        },
        {
          headerName: "حجم فروش حقیقی",
          field: "VolumeSell_Haghighi",

          sortable: true
        },
        {
          headerName: "حجم فروش حقوقی",
          field: "VolumeSell_Hoghughi",

          sortable: true
        }
      ]
    };
  },
  mounted() {
    this.loadData();
    this.gridOptions = {};
    // this.columnDefs = [
    //   {
    //     headerName: "Name",
    //     field: "athlete",
    //     minWidth: 200
    //   },
    //   {
    //     field: "age",
    //     enableRowGroup: true
    //   },
    //   {
    //     field: "country",
    //     minWidth: 200
    //   },
    //   { field: "year" },
    //   {
    //     field: "date",
    //     suppressColumnsToolPanel: true,
    //     minWidth: 180
    //   },
    //   {
    //     field: "sport",
    //     minWidth: 200
    //   },
    //   {
    //     field: "gold",
    //     aggFunc: "sum"
    //   },
    //   {
    //     field: "silver",
    //     aggFunc: "sum"
    //   },
    //   {
    //     field: "bronze",
    //     aggFunc: "sum"
    //   },
    //   {
    //     field: "total",
    //     aggFunc: "sum"
    //   }
    // ];
    this.defaultColDef = {
      flex: 1,
      minWidth: 100,
      sortable: true,
      enablePivot: true
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
            suppressSideButtons: true,
            suppressColumnFilter: true,
            suppressColumnSelectAll: true,
            suppressColumnExpandAll: true
          }
        }
      ],
      defaultToolPanel: "columns"
    };
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
  },
  created() {
    this.columnDefs = [
      { headerName: "Col A", field: "make", sortable: true },
      { headerName: "Col B", field: "model", sortable: true },
      { headerName: "Col C", field: "price", sortable: true }
    ];

    document.title = "Finwise - هوش مصنوعی";
  },
  methods: {
    showPivotModeSection() {
      var columnToolPanel = this.gridApi.getToolPanelInstance("columns");
      columnToolPanel.setPivotModeSectionVisible(true);
    },
    showRowGroupsSection() {
      var columnToolPanel = this.gridApi.getToolPanelInstance("columns");
      columnToolPanel.setRowGroupsSectionVisible(true);
    },
    showValuesSection() {
      var columnToolPanel = this.gridApi.getToolPanelInstance("columns");
      columnToolPanel.setValuesSectionVisible(true);
    },
    showPivotSection() {
      var columnToolPanel = this.gridApi.getToolPanelInstance("columns");
      columnToolPanel.setPivotSectionVisible(true);
    },
    // eslint-disable-next-line no-unused-vars
    onGridReady(params) {
      this.rowData = [
        { make: "Toyota", model: "Celica", price: 35000 },
        { make: "Ford", model: "Mondeo", price: 32000 },
        { make: "Porsche", model: "Boxter", price: 72000 }
      ];
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
    }
  }
};
</script>
