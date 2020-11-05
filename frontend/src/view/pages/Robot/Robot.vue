<template>
  <div>
    <div>
      <ErrorMine class="error"></ErrorMine>
    </div>
  </div>
</template>
<script>
import ErrorMine from "@/view/content/Error-mine.vue";
// import ListWidget3 from "@/view/content/widgets/list/Widget3.vue";
// import Error from "../error/Error-mine"
export default {
  name: "robot",
  components: {
    // Error,
    ErrorMine
  }
};
</script>
<style scoped>
.error{ 
  height: 100%;
}
</style>
