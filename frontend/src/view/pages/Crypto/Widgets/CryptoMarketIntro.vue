/* eslint-disable no-unused-vars */
<template>
  <div>
    <v-card>
      <v-toolbar dense>
        <v-toolbar-title>دیده بان رمزارز های اصلی</v-toolbar-title>
      </v-toolbar>
      <div class="right_aligned">
        <v-row class="mt-1 pr-2">
          <v-col>
            <v-row no-gutters class="pb-2">
              <v-col>
                نماد
              </v-col>
              <v-col>
                نام
              </v-col>
              <v-col>
                قیمت ریالی(میلیون تومان)
              </v-col>
              <v-col>
                قیمت (دلار)
              </v-col>
              <v-col>
                حجم(میلیون)
              </v-col>
              <v-col>
                ارزش بازار (میلیون دلار)
              </v-col>
            </v-row>
            <v-row
              v-for="item in InputIntroMW"
              :key="item.fullName"
              no-gutters
              class="pb-2"
            >
              <v-col>{{ item.name }} </v-col>
              <v-col>{{ item.fullName }} </v-col>
              <v-col>
                {{ numberWithCommas(roundTo(item.RialPrice / 10000000, 4)) }}
                
              </v-col>
              <v-col>
                {{ numberWithCommas(roundTo(item.price, 3)) }} 
              </v-col>
              <v-col>
                {{ numberWithCommas(roundTo(item.volume / 1000000, 3)) }} 
              </v-col>
              <v-col>
                {{ numberWithCommas(roundTo(item.marketCap / 1000000, 3)) }}
                
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </div>
    </v-card>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: "IntroCryptoMW",
  props: { InputIntroMW: Array },
  data() {
    return {
      loading: true,
      jsonData: {}
    };
  },
  watch: {
    InputIntroMW() {
      // this.renderData();
    }
  },
  // In the beginning...
  mounted() {
    // this.renderData();
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
<style>
.right_aligned {
  text-align: right;
  font-size: 0.9em;
}
</style>
