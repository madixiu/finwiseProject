<template>
  <ErrorMine></ErrorMine>
</template>
<script>
import ErrorMine from "@/view/pages/error/Error-6.vue";
export default {
  name: "AI",
  components: {
    // Error,
    ErrorMine
  }
  , created() {
    document.title = "Finwise - هوش مصنوعی";
  },
};
</script>
