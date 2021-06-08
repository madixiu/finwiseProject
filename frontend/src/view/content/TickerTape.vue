<template>
  <marquee-text
    class="tickerTape"
    reverse
    :repeat="5"
    :duration="duration"
    :paused="paused"
  >
    <div
      class="row"
      style="background-color: #27273b;"
      @mouseenter="paused = !paused"
      @mouseleave="paused = false"
    >
      <div v-for="item in this.TickerData" :key="item.ticker" class=" mr-4">
        <div
          class="mr-2"
          v-bind:class="[
            LowRes
              ? 'py-xl-4 py-lg-4 py-sm-4 py-xs-4 py-4'
              : 'py-xl-4 py-lg-4 py-sm-4 py-xs-4 py-4'
          ]"
          style="height: 100% overflow: hidden; 
    text-align: center; direction:rtl"
        >
          <span class="tickerTapeTicker mr-1 ml-1" @click="clickMarquee(item)">
            {{ item.ticker }}
          </span>
          <span v-if="TickerType" class="tickerTapeClose">
            {{ item.close }}
          </span>
          <!-- <v-chip
            label
            v-bind:class="[item.Change >= 0 ? 'greenItem' : 'redItem']"
            @click="clickMarquee(item)"
            ></v-chip
          > -->
          <!-- <div style="direction:ltr">
            
          </div> -->
          <!-- <span
            dir="ltr"
            :class="[
              item.Change >= 0 ? 'tickerTapeChangeGreen' : 'tickerTapeChangeRed'
            ]"
            >%{{ item.Change }}</span
          > -->
          <span dir="ltr" :class="checkSign(item.Change)">{{
            ChangeValue(item.Change)
          }}</span>
          <v-icon
            v-if="item.Change != 0"
            small
            v-bind:class="[
              item.Change > 0 ? 'tickerTapeChangeGreen' : 'tickerTapeChangeRed'
            ]"
            >mdi-menu-{{ item.Change > 0 ? "up" : "down" }}</v-icon
          >
        </div>
      </div>
    </div>
  </marquee-text>
</template>
<script>
import MarqueeText from "vue-marquee-text-component";
export default {
  name: "TickerTape",
  components: {
    MarqueeText
  },
  props: { TickerData: Array, duration: Number, TickerType: Boolean },
  data() {
    return {
      paused: false,
      LowRes: false
    };
  },

  mounted() {
    this.checkResolution();
  },
  methods: {
    checkSign(change) {
      if (change > 0) return "tickerTapeChangeGreen";
      else if (change < 0) return "tickerTapeChangeRed";
      else return "tickerTapeChangeWhite";
    },
    ChangeValue(item) {
      if (item >= 0) return "%" + item;
      else if (item < 0) return "%" + "(" + Math.abs(item) + ")";
    },
    clickMarquee(item) {
      if (this.TickerType)
        this.$router.push({ path: `/ticker/Overview/Overall/${item.ID}` });
      else
        this.$router.push({
          name: "IndustriesDetail",
          params: { id: item.ID }
        });
    },
    checkResolution() {
      if (window.screen.height < 1080) this.LowRes = true;
      else this.LowRes = false;
    }
  }
};
</script>
<style scoped>
.tickerTape {
  direction: ltr;
  background-color: tickerTape;
}
.tickerTapeTicker {
  color: aliceblue;
  font-family: "Vazir-Medium-FD" !important;
}
.tickerTapeTicker:hover {
  cursor: pointer;
  color: yellow;
}
.tickerTapeClose {
  color: aliceblue;
  font-size: 0.8rem;
  font-family: "Vazir-Medium-FD" !important;
}
.tickerTapeChange {
  font-family: "Vazir-Medium-FD" !important;
  color: white;
  /* font-size: 1.1em; */
}
.tickerTapeChangeGreen {
  font-family: "Vazir-Medium-FD" !important;
  color: #2cd85d;
}
.tickerTapeChangeRed {
  font-family: "Vazir-Medium-FD" !important;
  color: rgb(255, 25, 25);
}
.tickerTapeChangeWhite {
  font-family: "Vazir-Medium-FD" !important;
  color: white;
}
/* .redItem {
  color: aliceblue;
  background-color: red !important;
  font-family: "Vazir-Medium-FD" !important;
}
.greenItem {
  color: aliceblue;
  background-color: green !important;
  font-family: "Vazir-Medium-FD" !important;
} */
.v-chip.v-size--default {
  font-size: 0.8em;
  height: 1.8em;
  direction: ltr;
  padding-right: 0.8em;
  padding-left: 0.8em;
}
</style>
