<template>
<div v-if="ticker.length">
  <TradingView  :symbol="ticker"></TradingView>

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
  watch: {
    searchItems() {
      // this.ticker = "شتران"
      // if(this.searchItems.length)
    }
  },
  data() {
    return {
      items: [],
      ticker: ""
    }
  },
  props:{
    // ticker: String
  },
  created() {
    console.log(this.searchItems);
  },
  computed: {
    // ...mapState({
    //   searchData: state => state.search.SearchBarListData
    // }),
    ...mapGetters({ searchItems: "getSearchListData" })
  },
  mounted() {
    this.ticker = this.Ticker(this.$route.params.id)

    if (this.searchItems.length)
    // console.log(this.Ticker(this.$route.params.id));
    console.log(this.$route.params.id);
    // console.log(this.$route.name);
    // console.log(this.$route.path);
    // console.log(this.searchItems);
  },

  methods: {
    Ticker(ID) {
      console.log(this.searchItems);
      let itemA = this.searchItems.filter(function(item) {
        return item.ID == ID && (item.TypeID == 25 || item.TypeID == 1);
      });
      console.log(itemA[0].ticker);
      return itemA[0].ticker;
    }
  }
};
</script>
