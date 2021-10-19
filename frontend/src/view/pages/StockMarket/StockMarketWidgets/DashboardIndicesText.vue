/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom card-stretch gutter-b FinancialStrength">
    <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->
    <v-card>
      <v-card-title><span class="BigOne">شاخص کل بورس</span></v-card-title>
      <div class="row">
        <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12">
          <v-divider></v-divider>
          <div class="mb-1 mr-2">
            <v-chip class="bigchip">مقدار شاخص</v-chip>
            <span class="bigchip"> ۱۲۲۲۲۲۲ </span>
          </div>
          <br />
          <div class="mb-1 mr-2">
            <v-chip class="bigchip">مقدار شاخص</v-chip>
            <span class="bigchip"> ۱۲۲۲۲۲۲ </span>
          </div>
          <br />
          <div class="mb-1 mr-2">
            <v-chip class="smallchip">مقدار شاخص</v-chip>
            <span class="bigchip"> ۱۲۲۲۲۲۲ </span>
          </div>
          <br />
          <div class="mb-3 mr-2">
            <v-chip class="smallchip">مقدار شاخص</v-chip>
            <span class="bigchip"> ۱۲۲۲۲۲۲ </span>
          </div>
        </div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: "DashboardIndicesText",
  props: { inputData: Object },
  data() {
    return {
      loading: true,
      jsonData: {}
    };
  },
  watch: {
    inputData() {
      this.loading = false;
      this.renderData();
    }
  },

  // In the beginning...
  mounted() {
    // this.renderChart();
  },
  computed: {},
  methods: {
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
      return n;
    },
    isNull(obj, key) {
      return obj[key] == null || obj[key] === undefined || obj[key] === "null";
    },
    validate(obj) {
      let objKeys = Object.keys(obj);
      objKeys.forEach(key => {
        if (this.isNull(obj, key)) {
          obj[key] = 0;
        }
        if (typeof obj[key] == "object") {
          this.validate(obj[key]);
        }
      });
    },
    renderData() {
      this.jsonData = {
        Haghighi: 0,
        Hoghughi: 0,
        Stock: 0,
        StockBlock: 0,
        HaghTradeValues: 0,
        HaghTradeValuesBlock: 0,
        ETF: 0,
        ETFBlock: 0,
        Bond: 0,
        BondBlock: 0,
        Blocks: 0,
        IFB: 0,
        Tepix: 0,
        Total2: 0
      };
      if (this.inputData[0] !== null) {
        this.jsonData.Haghighi = this.inputData[0][0]["Haghighi"] * 100;
        this.jsonData.Hoghughi = this.inputData[0][0]["Hoghughi"] * 100;
      }

      if (this.inputData[2] !== null) {
        this.jsonData.Bond = this.inputData[2].filter(item => {
          if (item["Type"] == "BondTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.BondBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "BondTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETF = this.inputData[2].filter(item => {
          if (item["Type"] == "ETFTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETFBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "ETFTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValues = this.inputData[2].filter(item => {
          if (item["Type"] == "HaghTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValuesBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "HaghTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.Stock = this.inputData[2].filter(item => {
          if (item["Type"] == "StockTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.StockBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "StockTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.validate(this.jsonData);
        this.jsonData.Blocks =
          this.jsonData.StockBlock +
          this.jsonData.HaghTradeValuesBlock +
          this.jsonData.ETFBlock +
          this.jsonData.BondBlock;
        this.jsonData.Total =
          this.jsonData.Blocks +
          this.jsonData.Bond +
          this.jsonData.Stock +
          this.jsonData.ETF +
          this.jsonData.HaghTradeValues;
      }
      if (this.inputData[3] !== null) {
        this.jsonData.Tepix = this.inputData[3][0]["TradeValue"] = this
          .inputData[3][0]["TradeValue"]
          ? this.inputData[3][0]["TradeValue"]
          : 0;
        this.jsonData.IFB = this.inputData[3][1]["TradeValue"] = this
          .inputData[3][1]["TradeValue"]
          ? this.inputData[3][1]["TradeValue"]
          : 0;
        this.jsonData.Total2 = this.jsonData.Tepix + this.jsonData.IFB;
      }
    }
  }
};
</script>

<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.BigOne {
  font-size: 1.3em;
}
.bigchip {
  font-size: 1.2em;
}
.smallchip {
  font-size: 0.9em;
}
</style>
