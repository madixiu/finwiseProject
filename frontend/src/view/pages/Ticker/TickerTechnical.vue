<template>
  <div v-if="ticker.length">
    <TradingView :symbol="ticker"></TradingView>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TradingView from "@/view/pages/Saham/Technical/TradingView.vue";
export default {
  name: "TickerTechnical",
  components: {
    TradingView
  },
  data() {
    return {
      items: [],
      ticker: ""
    };
  },
  watch: {
    "$route.params": {
      handler(newValue, oldValue) {
        if (newValue != oldValue && newValue != undefined) {
          this.ticker = this.Ticker(newValue.id);
        }
      },
      immediate: true
    },
    searchItems(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        this.ticker = this.Ticker(this.$route.params.id);
      }
    }
  },
  computed: {
    ...mapGetters({ searchItems: "getSearchListData" })
  },

  methods: {
    Ticker(ID) {
      let itemA = this.searchItems.filter(function(item) {
        return item.ID == ID && (item.TypeID == 25 || item.TypeID == 1);
      });
      return itemA[0].ticker;
    }
  }
};
</script>
