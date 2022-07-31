<template>
  <v-card rounded="lg" height="100%">
    <v-toolbar elevation="1" dense style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em;"
        >افزایش سرمایه</v-toolbar-title
      >
    </v-toolbar>
    <v-skeleton-loader
      v-if="loading"
      height="200px"
      type=" table-heading, table-thead, table-tbody"
    ></v-skeleton-loader>
    <b-table
      v-if="!loading"
      class="AssemblyICwidget-table"
      thClass="AssemblyICwidget-tableHeader"
      tbody-tr-class="AssemblyICwidget-table-row"
      small
      hover
      :items="notices"
      :fields="headers"
    >
      <template #cell(PublishTime)="data">
        <span v-if="data.value === null || data.value == ''">-</span>
        <span v-else dir="ltr">{{ data.value.split(" ")[0] }}</span>
      </template>
      <template #cell(IncreasePercent)="data">
        <span v-if="data.value === null || data.value == ''">-</span>
        <span v-else dir="ltr">{{ roundTo(data.value, 2) }}%</span>
      </template>
    </b-table>
    <!--end::Body-->
  </v-card>
</template>

<script>
export default {
  name: "AssemblyIC",
  props: ["notices"],
  data() {
    return {
      loading: true,
      headers: [
        {
          label: "تاریخ",
          key: "PublishTime",
          thClass: "AssemblyICwidget-tableHeader"
        },
        {
          label: "درصد افزایش",
          key: "IncreasePercent",
          thClass: "AssemblyICwidget-tableHeader"
        },
        {
          label: "محل افزایش سرمایه",
          key: "CapitalChangeType",
          thClass: "AssemblyICwidget-tableHeader"
        }
      ]
    };
  },
  computed: {},
  methods: {
    roundTo(n, digits) {
      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    }
  },
  mounted() {},
  watch: {
    // eslint-disable-next-line no-unused-vars
    notices(newValue, oldValue) {
      if (newValue.length || oldValue.length) this.loading = false;
    }
  }
};
</script>
<style scoped>
.AssemblyICwidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.AssemblyICwidget-table /deep/ .AssemblyICwidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
}
.AssemblyICwidget-table /deep/ .AssemblyICwidget-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
</style>
