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
          class="mr-2 py-lg-2 py-xxl-3"
          style="height: 100% overflow: hidden; 
    text-align: center; direction:rtl"
        >
          <span class="tickerTapeTicker mr-1 ml-1" @click="clickMarquee(item)">
            {{ item.ticker }}
          </span>
          <span v-if="TickerType" class="tickerTapeClose">
            {{ item.close }}
          </span>
          <v-chip
            label
            v-bind:class="[item.Change >= 0 ? 'greenItem' : 'redItem']"
            @click="clickMarquee(item)"
            ><span class="tickerTapeChange">{{ item.Change }}%</span></v-chip
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
      paused: false
    };
  },
  methods: {
    clickMarquee(item) {
      console.log("CLICKED", item);
      if (this.TickerType)
        this.$router.push({ path: `/ticker/Overview/Overall/${item.ID}` });
      else this.$router.push({
        name: "IndustriesDetail",
        params: { id: item.ID }
      });
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
.redItem {
  color: aliceblue;
  background-color: red !important;
  font-family: "Vazir-Medium-FD" !important;
}
.greenItem {
  color: aliceblue;
  background-color: green !important;
  font-family: "Vazir-Medium-FD" !important;
}
.v-chip.v-size--default {
  font-size: 0.8em;
  height: 1.8em;
  direction: ltr;
  padding-right: 0.8em;
  padding-left: 0.8em;
}
</style>
