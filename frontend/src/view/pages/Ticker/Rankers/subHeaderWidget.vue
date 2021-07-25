<template>
  <div style="padding-top:0px">
    <v-row
      no-gutters
      class="d-flex flex-row justify-content-between"
      v-if="!loading"
      style="flex-wrap: nowrap"
    >
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            نماد
          </v-col>
          <v-col cols="12" style="padding-bottom:5px;padding-left:5px">
            <span>
              {{ LiveDataItems.ticker }}
            </span>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            آخرین قیمت
          </v-col>
          <v-col
            cols="12"
            class="d-flex justify-end"
            style="padding-bottom:5px;padding-left:5px"
          >
            <div class="d-flex mr-2">
              <span>{{ closePrice }} </span>
            </div>
            <div class="d-flex">
              <span
                dir="ltr"
                class="spandata"
                v-bind:class="[
                  [
                    LiveDataItems.last > LiveDataItems.yesterday
                      ? 'greenItem'
                      : LiveDataItems.last == LiveDataItems.yesterday
                      ? 'blackItem'
                      : LiveDataItems.last < LiveDataItems.yesterday
                      ? 'redItem'
                      : ''
                  ]
                ]"
                >%{{ closePercent }}</span
              >
            </div>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            قیمت پایانی
          </v-col>
          <v-col
            cols="12"
            class="d-flex justify-end"
            style="padding-bottom:5px;padding-left:5px"
          >
            <div class="d-flex mr-2">
              <span style="direction:ltr">{{ finalPrice }}</span>
            </div>
            <div class="d-flex">
              <span
                dir="ltr"
                class="spandata"
                v-bind:class="[
                  [
                    LiveDataItems.close > LiveDataItems.yesterday
                      ? 'greenItem'
                      : LiveDataItems.close == LiveDataItems.yesterday
                      ? 'blackItem'
                      : LiveDataItems.close < LiveDataItems.yesterday
                      ? 'redItem'
                      : ''
                  ]
                ]"
                >%{{ finalPercent }}</span
              >
            </div>
          </v-col>
        </v-card>
      </v-col>

      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            ارزش معاملات
          </v-col>
          <v-col
            class="d-flex justify-end"
            cols="12"
            style="padding-bottom:5px;padding-left:5px"
          >
            <div class="d-flex mr-2">
              <span>{{ Value }}</span>
            </div>
            <div class="d-flex align-center">
              <span style="font-size:0.8em">میلیارد ریال</span>
            </div>
          </v-col>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            حجم معاملات
          </v-col>
          <v-col
            class="d-flex justify-end"
            cols="12"
            style="padding-bottom:5px;padding-left:5px"
          >
            <div class="d-flex mr-2">
              <span>{{ Volume }}</span>
            </div>
            <div class="d-flex align-center">
              <span style="font-size:0.8em">میلیون</span>
            </div>
          </v-col>
        </v-card>
      </v-col>

      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pr-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            وضعیت
          </v-col>
          <v-col cols="12" style="padding-bottom:5px;padding-left:5px">
            <v-chip x-small outlined :color="StatusColor">
              {{ LiveDataItems.Status }}
            </v-chip>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "SubHeaderWidget",
  props: ["tickerdata"],
  data() {
    return {
      loading: true,
      search: "",
      LiveDataItems: []
    };
  },
  computed: {
    closePercent() {
      return (
        Math.round(
          (this.LiveDataItems.last / this.LiveDataItems.yesterday - 1) *
            100 *
            100
        ) / 100
      );
    },
    closePrice() {
      if (this.LiveDataItems.last != undefined)
        return this.LiveDataItems.last.toLocaleString();
      else return "-";
    },
    finalPrice() {
      if (this.LiveDataItems.close != undefined)
        return this.LiveDataItems.close.toLocaleString();
      else return "-";
    },
    finalPercent() {
      return (
        Math.round(
          (this.LiveDataItems.close / this.LiveDataItems.yesterday - 1) *
            100 *
            100
        ) / 100
      );
    },
    Volume() {
      if (this.LiveDataItems.TradeVolume != undefined)
        return this.roundTo(
          this.LiveDataItems.TradeVolume / 1000000,
          2
        ).toLocaleString();
      else return "-";
    },
    Value() {
      if (this.LiveDataItems.TradeValue != undefined)
        return this.roundTo(
          this.LiveDataItems.TradeValue / 1000000000,
          2
        ).toLocaleString();
      else return "-";
    },
    StatusColor() {
      if (this.LiveDataItems.Status == "مجاز") return "#014f86";
      else return "black";
    }
  },
  methods: {
    LivepopulateData() {
      this.LiveDataItems = this.tickerdata;
      if (this.LiveDataItems === undefined || this.LiveDataItems.length == 0) {
        this.LiveDataItems = [
          {
            ID: "-",
            englishDate: "-",
            Status: "-",
            Hour: "-",
            ticker: "-",
            name: "-",
            ShareCount: "-",
            Mabna: "-",
            Shenavari: "-",
            persianDate: "-",
            first: "-",
            close: "-",
            last: "-",
            low: "-",
            high: "-",
            yesterday: "-",
            TradeCount: "-",
            TradeValue: "-",
            TradeVolume: "-",
            EPS: "-",
            market: "-"
          }
        ];
      }
      this.loading = false;
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
    }
  },
  mounted() {
    this.LivepopulateData();
  },
  watch: {
    tickerdata() {
      this.LivepopulateData();
    }
  }
};
</script>
<style scoped>
.CardHeaderTitle {
  direction: ltr;
  align-items: right;
  display: flex;
  flex-wrap: nowrap;
  justify-content: flex-end;
  padding-bottom: 0px;
  padding-top: 5px;
  font-family: "Vazir-Light-FD";
  font-weight: 500;
  /* font-family: "IRANSansXFaNum-Regular"; */
}
.redItem {
  color: #ef5350 !important;
}

.greenItem {
  /* color: #088a2f93 !important; */
  color: green;
}
.blackItem {
  color: black;
}
</style>
