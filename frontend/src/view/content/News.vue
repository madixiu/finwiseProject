<template>
  <marquee-text
    class="newsTape"
    reverse
    :paused="paused"
    :duration="2700"
    :repeat="2"
  >
    <div
      class="row"
      style="background-color: #1e1e2d;"
      @mouseenter="paused = !paused"
      @mouseleave="paused = false"
    >
      <div v-for="item in News" :key="item.id" class="mr-4">
        <div
          class="mr-2 py-xl-3 py-lg-3 py-sm-3 py-xs-3 py-3"
          style="height: 100% overflow: hidden; 
        text-align: center; direction:rtl"
        >
          <span
            class="newsTapeTitle pr-2 pl-2 ml-1"
            @click="clickMarquee(item)"
          >
            {{ item.title }}</span
          >
          <v-chip x-small label outlined color="#E09F3E">
            <span>{{ item.source }}</span>
          </v-chip>
        </div>
      </div>
    </div>
  </marquee-text>
</template>
<script>
import MarqueeText from "vue-marquee-text-component";
export default {
  name: "News",
  components: {
    MarqueeText
  },
  props: {
    News: Array
  },
  data() {
    return {
      // News: null,
      paused: false
    };
  },
  methods: {
    clickMarquee(item) {
      window.open(item.href, "_blank");
    }
  }
};
</script>
<style scoped>
.newsTape {
  direction: ltr;
  background-color: newsTape;
}
.newsTapeNewsSpan {
  font-family: "Vazir-Medium-FD";
}
.newsTapeTitle {
  font-size: 0.9em;
  color: white;
}
.newsTapeTitle:hover {
  cursor: pointer;
  color: #e09f3e;
}
</style>
