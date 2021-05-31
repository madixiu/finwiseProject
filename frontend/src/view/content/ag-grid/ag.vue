<template>
  <div style="height: 100%">
    <div class="example-wrapper">
      <div style="margin-bottom: 5px;">
        <button v-on:click="onFlushTransactions()">Flush Transactions</button>
        <span id="eMessage"></span>
      </div>
      <ag-grid-vue
        style="width: 100%; height: 100%;"
        class="ag-theme-alpine"
        id="myGrid"
        :gridOptions="gridOptions"
        @grid-ready="onGridReady"
        :columnDefs="columnDefs"
        :suppressAggFuncInHeader="true"
        :animateRows="true"
        :rowGroupPanelShow="rowGroupPanelShow"
        :pivotPanelShow="pivotPanelShow"
        :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
        :getRowNodeId="getRowNodeId"
        :defaultColDef="defaultColDef"
        :autoGroupColumnDef="autoGroupColumnDef"
        :modules="modules"
      ></ag-grid-vue>
    </div>
  </div>
</template>
<script>
// for enterprise features
// import { AllModules } from "@ag-grid-enterprise";
// import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
import { AllModules } from "ag-grid-enterprise";

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
      //*********************NEW DATA *************
      products: [
        "Palm Oil",
        "Rubber",
        "Wool",
        "Amber",
        "Copper",
        "Lead",
        "Zinc",
        "Tin",
        "Aluminium",
        "Aluminium Alloy",
        "Nickel",
        "Cobalt",
        "Molybdenum",
        "Recycled Steel",
        "Corn",
        "Oats",
        "Rough Rice",
        "Soybeans",
        "Rapeseed",
        "Soybean Meal",
        "Soybean Oil",
        "Wheat",
        "Milk",
        "Coca",
        "Coffee C",
        "Cotton No.2",
        "Sugar No.11",
        "Sugar No.14"
      ],
      modules: AllModules,
      rowGroupPanelShow: "always",
      pivotPanelShow: "always",
      columnDefs: [
        {
          headerName: "Product",
          field: "product",
          enableRowGroup: true,
          enablePivot: true,
          rowGroupIndex: 0,
          hide: true
        },
        {
          headerName: "Portfolio",
          field: "portfolio",
          enableRowGroup: true,
          enablePivot: true,
          rowGroupIndex: 1,
          hide: true
        },
        {
          headerName: "Book",
          field: "book",
          enableRowGroup: true,
          enablePivot: true,
          rowGroupIndex: 2,
          hide: true
        },
        {
          headerName: "Trade",
          field: "trade",
          width: 100
        },
        {
          headerName: "Current",
          field: "current",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "Previous",
          field: "previous",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "Deal Type",
          field: "dealType",
          enableRowGroup: true,
          enablePivot: true
        },
        {
          headerName: "Bid",
          field: "bidFlag",
          enableRowGroup: true,
          enablePivot: true,
          width: 100
        },
        {
          headerName: "PL 1",
          field: "pl1",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "PL 2",
          field: "pl2",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "Gain-DX",
          field: "gainDx",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "SX / PX",
          field: "sxPx",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "99 Out",
          field: "_99Out",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "Submitter ID",
          field: "submitterID",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        },
        {
          headerName: "Submitted Deal ID",
          field: "submitterDealID",
          width: 200,
          aggFunc: "sum",
          enableValue: true,
          cellClass: "number",
          valueFormatter: this.numberCellFormatter(),
          cellRenderer: "agAnimateShowChangeCellRenderer"
        }
      ],
      allColumnIds: [],
      asyncTransactionWaitMillis: 4000,
      gridOptions: null,
      gridApi: null,
      columnApi: null,
      getRowNodeId: null,
      defaultColDef: null,
      autoGroupColumnDef: null,
      MIN_BOOK_COUNT: 10,
      MAX_BOOK_COUNT: 20,
      MIN_TRADE_COUNT: 1,
      MAX_TRADE_COUNT: 10,

      portfolios: [
        "Aggressive",
        "Defensive",
        "Income",
        "Speculative",
        "Hybrid"
      ],
      nextBookId: 62472,
      nextTradeId: 24287,
      UPDATE_COUNT: 20,
      globalRowData: []
      // ******************************************
    };
  },
  created() {
    this.gridOptions = {};
    this.rowGroupPanelShow = "always";
    this.pivotPanelShow = "always";
    this.columnDefs[
      ({
        headerName: "Product",
        field: "product",
        enableRowGroup: true,
        enablePivot: true,
        rowGroupIndex: 0,
        hide: true
      },
      {
        headerName: "Portfolio",
        field: "portfolio",
        enableRowGroup: true,
        enablePivot: true,
        rowGroupIndex: 1,
        hide: true
      },
      {
        headerName: "Book",
        field: "book",
        enableRowGroup: true,
        enablePivot: true,
        rowGroupIndex: 2,
        hide: true
      },
      {
        headerName: "Trade",
        field: "trade",
        width: 100
      },
      {
        headerName: "Current",
        field: "current",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "Previous",
        field: "previous",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "Deal Type",
        field: "dealType",
        enableRowGroup: true,
        enablePivot: true
      },
      {
        headerName: "Bid",
        field: "bidFlag",
        enableRowGroup: true,
        enablePivot: true,
        width: 100
      },
      {
        headerName: "PL 1",
        field: "pl1",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "PL 2",
        field: "pl2",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "Gain-DX",
        field: "gainDx",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "SX / PX",
        field: "sxPx",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "99 Out",
        field: "_99Out",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "Submitter ID",
        field: "submitterID",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "Submitted Deal ID",
        field: "submitterDealID",
        width: 200,
        aggFunc: "sum",
        enableValue: true,
        cellClass: "number",
        valueFormatter: this.numberCellFormatter(),
        cellRenderer: "agAnimateShowChangeCellRenderer"
      })
    ],
   
    this.defaultColDef = {
      width: 120,
      sortable: true,
      resizable: true
    };
    this.autoGroupColumnDef = { width: 250 };
  },
  computed: {
      getRowNodeId() {
          return data.trade
      }
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
    this.createRowData();
  },
  methods: {
    onFlushTransactions() {
      this.gridApi.flushAsyncTransactions();
    },
    onGridReady(params) {
      // this.createRowData();
      params.api.setRowData(this.globalRowData);
      this.startFeed(params.api);
    },
    createRowData() {
      console.log("here");
      console.log(this.products);

      for (var i = 0; i < this.products.length; i++) {
        var product = this.products[i];
        for (var j = 0; j < this.portfolios.length; j++) {
          var portfolio = this.portfolios[j];
          var bookCount = this.randomBetween(
            this.MAX_BOOK_COUNT,
            this.MIN_BOOK_COUNT
          );
          for (var k = 0; k < bookCount; k++) {
            var book = this.createBookName();
            var tradeCount = this.randomBetween(
              this.MAX_TRADE_COUNT,
              this.MIN_TRADE_COUNT
            );
            for (var l = 0; l < tradeCount; l++) {
              var trade = this.createTradeRecord(product, portfolio, book);
              this.globalRowData.push(trade);
            }
          }
        }
      }
      // console.log(this.globalRowData);
    },
    randomBetween(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },
    createTradeRecord(product, portfolio, book) {
      var current = Math.floor(Math.random() * 100000) + 100;
      var previous = current + Math.floor(Math.random() * 10000) - 2000;
      var trade = {
        product: product,
        portfolio: portfolio,
        book: book,
        trade: this.createTradeId(),
        submitterID: this.randomBetween(10, 1000),
        submitterDealID: this.randomBetween(10, 1000),
        dealType: Math.random() < 0.2 ? "Physical" : "Financial",
        bidFlag: Math.random() < 0.5 ? "Buy" : "Sell",
        current: current,
        previous: previous,
        pl1: this.randomBetween(100, 1000),
        pl2: this.randomBetween(100, 1000),
        gainDx: this.randomBetween(100, 1000),
        sxPx: this.randomBetween(100, 1000),
        _99Out: this.randomBetween(100, 1000)
      };
      return trade;
    },
    numberCellFormatter(params) {
      return Math.floor(params.value)
        .toString()
        .replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
    },
    createBookName() {
      this.nextBookId++;
      return "GL-" + this.nextBookId;
    },
    createTradeId() {
      this.nextTradeId++;
      return this.nextTradeId;
    },
    startFeed(api) {
      console.log("start");

      var count = 1;
      setInterval(function() {
        var thisCount = count++;
        var updatedIndexes = {};
        var newItems = [];
        for (var i = 0; i < this.UPDATE_COUNT; i++) {
          var index = Math.floor(Math.random() * this.globalRowData.length);
          if (updatedIndexes[index]) {
            continue;
          }
          var itemToUpdate = this.globalRowData[index];
          var newItem = this.copyObject(itemToUpdate);
          newItem.previous = newItem.current;
          newItem.current = Math.floor(Math.random() * 100000) + 100;
          newItems.push(newItem);
        }
        var resultCallback = function() {
          console.log("transactionApplied() - " + thisCount);
        };
        api.applyTransactionAsync({ update: newItems }, resultCallback);
        console.log("applyTransactionAsync() - " + thisCount);
      }, 500);
    },
    copyObject(object) {
      var newObject = {};
      Object.keys(object).forEach(function(key) {
        newObject[key] = object[key];
      });
      return newObject;
    }
  }
};
</script>
<style>
.ag-theme-balham .ag-rtl .ag-cell {
  /* font-family: "Vazir-Medium-FD"; */
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
  align-items: center !important;
}
</style>
