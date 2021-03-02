<template>
  <TradingView></TradingView>
</template>
<script>
import { mapGetters } from "vuex";
import TradingView from "@/view/pages/Saham/Technical/TradingView.vue";
export default {
  name: "TickerTechnical",
  components: {
    TradingView
  },
  created() {
    console.log(this.searchItems);
  },
  mounted() {
    console.log(this.Ticker(this.$route.params.id));
    // console.log(this.$route.params.id);
    // console.log(this.$route.name);
    // console.log(this.$route.path);
    // console.log(this.getSearchListData);
  },
  computed: {
    // ...mapState({
    //   searchData: state => state.search.SearchBarListData
    // }),
    ...mapGetters({ searchItems: "getSearchListData" })
  },
  methods: {
    Ticker(ID) {
      let itemA = this.searchItems.filter(function(item) {
        return item.ID == ID && (item.TypeID == 25 || item.TypeID == 1);
      });
      console.log(this.itemA);
      return itemA.ticker;
    }
  }
};
</script>
