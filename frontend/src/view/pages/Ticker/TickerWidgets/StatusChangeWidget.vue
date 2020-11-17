<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder">
        تغییر وضعیت
      </h3>
    </div>
    <!--end::Header-->
    <template>
      <v-timeline>
        <v-timeline-item>timeline item</v-timeline-item>
        <v-timeline-item>timeline item</v-timeline-item>
        <v-timeline-item>timeline item</v-timeline-item>
      </v-timeline>
    </template>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "SC",
  data() {
    return {
      search: ""
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {},
  mounted() {
    // this.setFinancialStrengthPercent();
    // reference; kt_stats_widget_7_chart
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
