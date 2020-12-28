<template>
  <div id="mapparent" class="container-fluid">
    <div class="row"><treemap /></div>
    <!-- <treemap></treemap> -->
  </div>
</template>
<script>
import treemap from "@/view/content/d3/treemap";

// import ErrorMine from "@/view/pages/error/Error-6.vue";
export default {
  name: "marketmap",
  components: {
    // Error,
    treemap
    
    // ErrorMine
  },
  mounted() {
    let chartDiv = document.getElementById("mapparent");
    this.width = chartDiv.clientWidth;
    this.height = chartDiv.clientHeight;
    console.log(this.width);
    console.log(this.height);
  }
};
</script>
<style scoped>
#mapparent {
  display: contents;
}
</style>
