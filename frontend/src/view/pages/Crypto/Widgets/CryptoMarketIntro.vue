<template>
  <div>
    <v-card rounded="lg">
      <v-toolbar dense class="elevation-2" style="height:36px;">
        <v-toolbar-title style="height:20px;font-size:0.95em"
          >دیده بان رمز ارز های اصلی</v-toolbar-title
        >
      </v-toolbar>
      <ag-grid-vue
        :style="
          `width: 100%; height:  ${height}px; font-family: Vazir-Medium-FD`
        "
        class="ag-theme-material CryptoMarketIntroTable mt-1 pb-1"
        :localeText="localeText"
        :defaultColDef="defaultColDef"
        :columnDefs="Header"
        :enableRtl="true"
        :gridOptions="gridOptions"
        @grid-ready="onGridReady"
        :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
      ></ag-grid-vue>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable no-unused-vars */
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "IntroCryptoMW",
  props: { InputIntroMW: Array },
  components: {
    AgGridVue
  },
  data() {
    return {
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      Header: [],
      tableData: null,
      localeText: null,
      dataFetch: false,
      asyncTransactionWaitMillis: 4000,
      interval: null,
      modules: AllModules,

      loading: true
    };
  },
  watch: {
    InputIntroMW(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }
      if (oldValue != undefined)
        if (this.dataFetch == true && oldValue.length != 0) {
          for (let i = 0; i < this.InputIntroMW.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.price != newValue[i].price) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.price = itemUpdate.price;
              newItem.volume = itemUpdate.volume;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.gridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
        }
    }
  },
  // In the beginning...
  created() {
    let that = this;
    this.localeText = AG_GRID_LOCALE_FA;
    this.defaultColDef = {
      flex: 1,
      // minWidth: 100,
      sortable: true,
      // headerHeight: 12,
      suppressMenu: true,
      enablePivot: false,
      cellStyle: {
        display: "flex",
        "justify-content": "center",
        "align-items": "center",
        direction: "ltr"
      }
    };
    this.gridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 25,
      getRowNodeId: data => data.id
    };
    this.Header = [
      {
        headerName: "نماد",
        field: "mapperName",
        cellStyle: {
          display: "flex",
          "justify-content": "flex-end",
          "align-items": "center"
          // direction: "ltr"
        },
        cellRenderer: function(params) {
          return `
          <span>
          ${params.value} </span>
          
             <img
            src="media/svg/crypto/${params.value.toLowerCase()}.svg"
          width=17px height=17px />`;
        }
      },
      {
        headerName: "نام",
        field: "fullName"
      },
      // {
      //   headerName: "قیمت ریالی(میلیون تومان)",
      //   field: "RialPrice",
      //   valueFormatter: function(params) {
      //     return that.roundTo(params.value / 10000000, 4).toLocaleString();
      //   }
      // },
      {
        headerName: "قیمت (دلار)",
        field: "price",
        valueFormatter: function(params) {
          return that.roundTo(params.value, 3).toLocaleString();
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
              "align-items": "center",
              direction: "ltr"
            };
          } else if (params.value < 0) {
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "align-items": "center",
              direction: "ltr"
            };
          } else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "align-items": "center",
              direction: "ltr"
            };
        }
      },
      {
        headerName: "حجم(میلیون)",
        field: "volume",
        valueFormatter: function(params) {
          return that.roundTo(params.value / 1000000, 3).toLocaleString();
        }
      },
      {
        headerName: "ارزش بازار (میلیون دلار)",
        field: "marketCap",
        valueFormatter: function(params) {
          return that.roundTo(params.value / 1000000, 3).toLocaleString();
        }
      }
    ];
    //// this.renderData();
  },
  computed: {
    height() {
      if (this.InputIntroMW.lenghth)
        return (
          this.gridOptions.headerHeight +
          this.gridOptions.rowHeight * this.InputIntroMW.length +
          5
        );
      else return 400;
    }
  },
  methods: {
    onGridReady(params) {
      this.gridApi = params.api;
      params.api.setRowData(this.InputIntroMW);
    },
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
    isRealValue(obj) {
      return obj && obj !== "null" && obj !== "undefined";
    }
    // renderData() {
    //   if (!(this.inpuDataCorr === undefined || this.inpuDataCorr.length == 0)) {
    //     let data = [...this.inpuDataCorr];
    //     let that = this;
    //     this.updatedAt = data[0].englishDate;
    //     let json_data = JSON.parse(data[0].corrMatrix);
    //     var result = [];
    //     var labels = [];
    //     for (var i in json_data) {
    //       let dictionary = json_data[i];
    //       var values = Object.keys(dictionary).map(function(key) {
    //         return that.roundTo(dictionary[key], 2);
    //       });
    //       result.push(values);
    //     }
    //     this.ChartData2 = result;
    //     for (var j in json_data) {
    //       labels.push(j);
    //     }
    //     this.ChartLabels2 = labels;
    //   }
    // }
  }
};
</script>
<style scoped>
.CryptoMarketIntroTable /deep/ .ag-header-cell-label {
  color: black;
  font-size: 0.8em;
  font-weight: 300;
  align-items: center;
  text-align: center;
  margin-right: 2px !important;
  display: flex;
  justify-content: center;
  align-content: center;
}
.CryptoMarketIntroTable /deep/ .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.8em;
  overflow: hidden;
}
.CryptoMarketIntroTable /deep/ .ag-header-cell-text {
  color: black;
  padding-right: 2px;
  padding-left: 2px;
  /* Force the width corresponding at how much width
    we need once the text is laid out vertically */
  /* width: 30px; */
  /* transform: rotate(90deg); */
  /* margin-top: 50px; */
  /* Since we are rotating a span */
  display: inline-block;
}
.right_aligned {
  text-align: right;
  font-size: 0.9em;
}
</style>
