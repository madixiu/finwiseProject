<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        پیام ناظر
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column" v-if="loading">
      <v-skeleton-loader
        type=" table-heading, table-thead, table-tbody"
      ></v-skeleton-loader>
    </div>
    <div class="card-body d-flex flex-column">
      <v-data-table
        v-if="loading == false"
        :headers="headers"
        :items="DataItems2"
        class="elevation-1 FinancialStrength"
      >
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "AdminNoticeWidget",
  props: ["notices"],
  data() {
    return {
      search: "",
      loading: true,
      headers: [
        {
          text: "تاریخ ارسال",
          value: "Submited"
        },
        {
          text: "تاریخ انتشار",
          value: "persianDate"
        },

        {
          text: "عنوان",
          value: "Title"
        },
        {
          text: "توضیحات",
          value: "Text"
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems2 = this.notices;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      this.populateData();
      this.loading = false;
    }
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
