<template>
  <div>
    <v-card>
      <v-card-title>تکنیکال بدترین</v-card-title>
      <v-subheader class="ltr_aligned" v-if="loading == false">
        <!-- آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }} -->
        آخرین به روز رسانی
      </v-subheader>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      loading: false
    };
  },
  mounted() {}
};
</script>
<style scoped>
.ltr_aligned {
  direction: ltr !important;
  text-align: left !important;
}
</style>
