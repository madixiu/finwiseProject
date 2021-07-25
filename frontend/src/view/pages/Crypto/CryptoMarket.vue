<template>
  <div>
    <v-card>
      <v-toolbar dense class="elevation-2" style="height:36px;">
        <v-toolbar-title style="height:20px;font-size:0.95em"
          >رمز ارزها</v-toolbar-title
        >
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
              v-for="item in tableData"
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
export default {
  name: "Crypto",
  components: {},
  data() {
    return {
      WebsocketRequest: true,
      tableData: null
    };
  },
  created() {
    document.title = "Finwise - دیده بان رمز ارز";
  },

  mounted() {
    this.loadData();
    // eslint-disable-next-line no-unused-vars
    let interval = setInterval(() => {
      this.loadData();
    }, 10000);
  },
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
    async loadData() {
      await this.axios
        .get("/api/Crypto/MarketwatchAll/")
        .then(response => {
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
<style>
.right_aligned {
  text-align: right;
  font-size: 0.9em;
}
</style>
