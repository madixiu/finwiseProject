<template>
  <div>
    <v-card>
      <v-tabs background-color="white" color="deep-purple accent-4" right>
        <v-tab>نگاه کلی</v-tab>
        <v-tab>طلا و ارز</v-tab>
        <v-tab>شاخص های جهانی</v-tab>
        <v-tab>فلزات اساسی</v-tab>
        <v-tab>پتروشیمی</v-tab>
        <v-tab>پالایشی</v-tab>
        <v-tab>فارکس</v-tab>

        <v-tab-item>
          <v-row no-gutters class="pb-2">
            <v-col>
              <v-card>
                <v-card-title>دلار و طلا</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in dollargold"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col
              ><v-card>
                <v-card-title>انرژی</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in energy1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card></v-col
            >
            <v-col>
              <v-card>
                <v-card-title>فارکس</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      <span style="text-align:center;">قیمت</span>
                    </v-col>
                    <v-col>
                      <span style="text-align:center">تاریخ</span>
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in forex1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card></v-col
            >
            <v-col>
              <v-card>
                <v-card-title>فلزات</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in metal1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                   <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card></v-col
            >
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row>
            <v-col>
              <v-card>
                <v-card-title>طلا</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in gold"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col>
              <v-card>
                <v-card-title>ارز</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in currencies"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item
          ><v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>Word of the Day2</div>
              <p class="display-1 text--primary">
                be•nev•o•lent
              </p>
              <p>adjective</p>
              <div class="text--primary">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="deep-purple accent-4">
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card></v-tab-item
        >
        <v-tab-item
          ><v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>Word of the Day3</div>
              <p class="display-1 text--primary">
                be•nev•o•lent
              </p>
              <p>adjective</p>
              <div class="text--primary">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="deep-purple accent-4">
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card></v-tab-item
        >
        <v-tab-item
          ><v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>Word of the Day4</div>
              <p class="display-1 text--primary">
                be•nev•o•lent
              </p>
              <p>adjective</p>
              <div class="text--primary">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="deep-purple accent-4">
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card></v-tab-item
        >
        <v-tab-item
          ><v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>Word of the Day4</div>
              <p class="display-1 text--primary">
                be•nev•o•lent
              </p>
              <p>adjective</p>
              <div class="text--primary">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="deep-purple accent-4">
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card></v-tab-item
        >
        <v-tab-item
          ><v-card class="mx-auto" max-width="344">
            <v-card-text>
              <div>Word of the Day4</div>
              <p class="display-1 text--primary">
                be•nev•o•lent
              </p>
              <p>adjective</p>
              <div class="text--primary">
                well meaning and kindly.<br />
                "a benevolent smile"
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="deep-purple accent-4">
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card></v-tab-item
        >
      </v-tabs>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "Commodities",
  components: {
    // Error,
  },
  data() {
    return {
      WebsocketRequest: true,
      isBusy: true,
      tableData: null,
      tableData2: null,
      dollargold: [],
      energy1: [],
      metal1: [],
      forex1: [],
      currencies: [],
      gold: []
    };
  },
  created() {
    document.title = "Finwise - بازار جهانی";
  },
  mounted() {
    this.loadData();
    this.loadData2();
    this.liveData();
    // console.log(this.tableData);
    this.$socketIRCommodities.onmessage = data => {
      // this.tableData = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) {
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData = JSON.parse(data.data);
        this.prepareData();
      }
    };
    this.$socketInvCommodities.onmessage = data => {
      // this.tableData = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) {
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData2 = JSON.parse(data.data);
        this.prepareData2();
      }
    };
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
    prepareData() {
      if (this.tableData == null) {
        console.log("False");
      }
      this.dollargold = this.tableData[1];
      this.currencies = this.tableData[2];
      this.gold = this.tableData[3];
      // console.log(this.dollargold);
    },
    prepareData2() {
      if (this.tableData2 == null) {
        console.log("False");
      }
      // console.log(this.tableData2);
      this.metal1 = this.tableData2[1];
      this.energy1 = this.tableData2[2];
      this.forex1 = this.tableData2[3];
      // console.log(this.dollargold);
    },
    async loadData() {
      this.isBusy = true;
      await this.axios
        .get("/api/Commodities/IR")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData = data;
          this.prepareData();
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    async loadData2() {
      this.isBusy = true;
      await this.axios
        .get("/api/Commodities/Investing")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData2 = data;
          this.prepareData2();
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketIRCommodities.send(JSON.stringify(barier));
      }, 3000);
      let interval2 = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval2);
          return;
        }
        let barier = { request: "get" };
        this.$socketInvCommodities.send(JSON.stringify(barier));
      }, 3000);
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketIRCommodities.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.chips {
  font-family: "Vazir-Medium-FD" !important;
  font: size 0.6em;
  text-align: right;
}
.comItems {
  font-family: "Vazir-Medium-FD" !important;
  font: size 1em;
  text-align: right;
}
.comDates {
  font-family: "Vazir-Medium-FD" !important;
  font: size 0.7em;
  text-align: right;
}
</style>
