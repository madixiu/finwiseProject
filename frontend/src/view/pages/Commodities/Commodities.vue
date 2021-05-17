<template>
  <div class="row mt-1 mr-1">
    <div class="col-xxl-2 col-lg-2 col-md-4 col-sm-4">
      <div class="row">
        <v-card class="mx-auto rtl_ mb-2" color="#388E3C" dark max-width="100%" min-width="100%">
          <v-card-title>
            <v-icon large left>
              mdi-currency-usd
            </v-icon>
            <span class="title font-weight-light">دلار</span>
          </v-card-title>

          <v-card-text class="headline font-weight-bold">
            دلار آزاد :
            <br>
            دلار نیما: }{}{}
          </v-card-text>

          <v-card-actions>
            <v-list-item class="grow">
              <v-row align="center" justify="end">
                <v-icon class="mr-1">mdi-clock</v-icon>
                <span class="subheading mr-2">به روز رسانی:{}</span>
              </v-row>
            </v-list-item>
          </v-card-actions>
        </v-card>
         <v-card class="mx-auto rtl_ mb-2" color="#FFA000" dark max-width="100%" min-width="100%">
          <v-card-title>
            <v-icon large left>
              mdi-currency-usd
            </v-icon>
            <span class="title font-weight-light">طلا</span>
          </v-card-title>

          <v-card-text class="headline font-weight-bold">
            دلار آزاد :{{}}
            <br>
            دلار نیما: }{}{}
          </v-card-text>

          <v-card-actions>
            <v-list-item class="grow">
              <v-row align="center" justify="end">
                <v-icon class="mr-1">mdi-clock</v-icon>
                <span class="subheading mr-2">به روز رسانی:{}</span>
              </v-row>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </div>
    </div>
    <div class="col-xxl-6 col-lg-6 col-md-12 col-sm-12">
      <div class="row"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Commodities",
  components: {
    // Error,
  },
  created() {
    document.title = "Finwise - بازار جهانی";
  }
};
</script>
<style>
.rtl_ {
  direction: rtl;
  text-align: center;
}
</style>