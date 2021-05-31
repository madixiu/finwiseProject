<template>
  <!-- <ErrorMine></ErrorMine> -->
  <div style="height: 100%">
    <div>
      <!-- <input
        type="text"
        id="filter-text-box"
        placeholder="Filter..."
        v-model="filter"
        oninput="onFilterTextBoxChanged()"
      />
      <button style="margin-left: 20px;" onclick="onPrintQuickFilterTexts()">
        Print Quick Filter Texts
      </button> -->
      <!-- <ag-grid-vue
        style="width: 100%; height: 500px;"
        class="ag-theme-balham"
        :columnDefs="MarketTableHeader"
        :defaultColDef="defaultColDef"
        :rowData="rowDataComputed"
        rowSelection="multiple"
        :cacheQuickFilter="true"
        :sideBar="true"
        :enableRtl="true"
        :localeText="localeText"
      >
      </ag-grid-vue> -->
      <RawGridTemp v-if="flag" :rows="rowData" :cols="MarketTableHeader" />
    </div>

    <div>
      <agGridTemp />
    </div>
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-6.vue";

import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
// import { AgGridVue } from "ag-grid-vue";
import agGridTemp from "@/view/content/ag-grid/AgGrid.vue";
import RawGridTemp from "@/view/content/ag-grid/AgGridTemp.vue";
// import newAG from "@/view/content/ag-grid/ag.vue"
export default {
  name: "AI",
  components: {
    // Error,
    // ErrorMine
    agGridTemp,
    RawGridTemp
    // newAG
    // AgGridVue
  },
  data() {
    return {
      flag: false,
      filter: null,
      localeText: null,
      gridOptions: null,
      gridColumnApi: null,
      gridApi: null,
      columnApi: null,
      columnDefs: [
        { headerName: "Col Aa", field: "make", sortable: true, filter: true },
        { headerName: "Col B", field: "model", sortable: true, filter: true },
        { headerName: "Col C", field: "price", sortable: true, filter: true }
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
      rowDataTemp: [
        { make: "Toyota", model: "Celica", price: 35000 },
        { make: "Ford", model: "Mondeo", price: 32000 },
        { make: "Porsche", model: "Boxter", price: 72000 }
      ],
      MarketTableHeader: [
        {
          headerName: "نماد",
          field: "ticker",
          sortable: true,
          rowDrag: true,
          pinned: "right"
        },
        {
          headerName: "بازار",
          field: "marketName",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },

          sortable: true
        },
        {
          headerName: "عدد",
          field: "number",
          cellStyle: params => {
            if (params.value > 0) {
              //mark police cells as red
              return {
                color: "green",
                display: "flex",
                "justify-content": "center",
                direction: "ltr",

                "align-items": "center"
              };
            } else if (params.value < 0) {
              return {
                color: "red",
                display: "flex",
                "justify-content": "center",
                direction: "ltr",

                "align-items": "center"
              };
            } else
              return {
                color: "black",
                display: "flex",
                "justify-content": "center",
                direction: "ltr",

                "align-items": "center"
              };
          },
          sortable: true
        },
        {
          headerName: "تعداد معاملات",
          field: "TradeCount",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "حجم معاملات",
          field: "TradeVolume",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "ارزش معاملات",
          field: "TradeValue",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "قیمت دیروز",
          field: "yesterday",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "آخرین قیمت",
          field: "last",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "درصد آخرین قیمت",
          field: "lastPercent",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center",
            direction: "ltr"
          },
          sortable: true
        },
        {
          headerName: "قیمت پایانی",
          field: "close",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "درصد قیمت پایانی",
          field: "closePercent",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "کف مجاز قیمت",
          field: "MinRange",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "سقف مجاز قیمت",
          field: "MaxRange",
          sortable: true,
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          }
        },
        { headerName: "EPS", field: "EPS", hide: true },
        {
          headerName: "بالاترین قیمت",
          field: "high",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "کمترین قیمت",
          field: "low",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "اولین قیمت",
          field: "first",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true
        },
        {
          headerName: "تعداد خرید حقیقی",
          field: "CountBuy_Haghighi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "تعداد خرید حقوقی",
          field: "CountBuy_Hoguhgi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "حجم خرید حقیقی",
          field: "VolumeBuy_Haghighi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "حجم خرید حقوقی",
          field: "VolumeBuy_Hoghughi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "تعداد فروش حقیقی",
          field: "CountSell_Haghighi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "تعداد فروش حقوقی",
          field: "CountSell_Hoghughi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "حجم فروش حقیقی",
          field: "VolumeSell_Haghighi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        },
        {
          headerName: "حجم فروش حقوقی",
          field: "VolumeSell_Hoghughi",
          cellStyle: {
            display: "flex",
            "justify-content": "center",

            "align-items": "center"
          },
          sortable: true,
          hide: true
        }
      ],
      FundsTableHeader: [
        {
          headerName: "نماد",
          field: "ticker",
          sortable: true,
          rowDrag: true,
          pinned: "right"
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
          sortable: true,
          cellStyle: params => {
            if (params.value > 0) {
              //mark police cells as red
              return { color: "green" };
            } else if (params.value < 0) {
              return { color: "red" };
            } else return { color: "black" };
          }
        },

        // { field: "نام", field: "name" },
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
  computed: {
    rowDataComputed() {
      if (this.filter == null) {
        return this.rowData;
      } else {
        // return this.rowData.filter(el =>{
        //   el.make = this.filter;

        let rowData = this.rowData.filter(function(el) {
          return el.make == this.filter;
        });
        return rowData;
        // });
      }
    }
  },
  mounted() {
    this.localeText = AG_GRID_LOCALE_FA;
    this.loadData();
    // setInterval(() => {
    //   this.loadData();
    // }, 2000);
    this.gridOptions = {
      // localeText: localeText,
    };

    this.defaultColDef = {
      flex: 1,
      minWidth: 100,
      sortable: true,
      enablePivot: false
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
    // this.columnDefs = [
    //   { headerName: "Col A", field: "make", sortable: true },
    //   { headerName: "Col B", field: "model", sortable: true },
    //   { headerName: "Col C", field: "price", sortable: true }
    // ];

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
      await this.axios

        .get("/api/marketwatch")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.rowData = data;
          this.flag = true;
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    }
  }
};
</script>
<style lang="scss">
// @import "ag-grid-community/dist/styles/ag-grid.css";
// @import "ag-grid-community/dist/styles/ag-theme-balham.css";
</style>
