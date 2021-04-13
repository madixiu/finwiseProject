<template>
  <!--begin::Mixed Widget 14-->
  <div class="col-xxl-12 col-lg-12 col-md-12 col-sm 12">
    <v-card>
      <!--begin::Header-->
      <!-- <div class="card-header border-0 pt-2"> -->
      <!-- <h3 class="card-title font-weight-bolder FinancialStrength">
        بیشترین تقاضا
      </h3> -->
      <v-card-title>
        آخرین اخبار
      </v-card-title>
      <v-divider class="mt-0"></v-divider>

      <!-- </div> -->
      <!--end::Header-->
      <!--begin::Body-->
      <div class="card-body d-flex flex-column">
        <div class="FinancialStrength" v-if="loading">
          <b-spinner small></b-spinner>
          در حال بارگزاری
        </div>

        <v-data-table
          v-if="loading == false"
          :headers="mvheaders"
          :items="DataItems"
          :hide-default-footer="true"
          class="elevation-1 FinancialStrength"
          :header-props="{ sortIcon: null }"
          :items-per-page="10"
        >
          <template v-slot:[`item.title`]="{ item }">
            <a :href="item.href" target="_blank">
              {{ item.title }}
            </a>
          </template>
          <template v-slot:[`item.source`]="{ item }">
            <v-chip small label>{{ item.source }}</v-chip>
          </template>
        </v-data-table>
      </div>
      <!--end::Body-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
// import axios from "axios";
export default {
  name: "News",
  props: { inputDataNews: Array },
  //   props: ["mostviewed"],
  data() {
    return {
      loading: true,
      DataItems: [],
      mvheaders: [
        { text: "عنوان", value: "title", sortabale: false },
        { text: "منبع", value: "source", sortabale: false }
      ]
    };
  },
  computed: {},
  methods: {
    renderData() {
      this.DataItems = this.inputDataNews;
      if (this.DataItems.length > 0) {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.renderData();
  },
  watch: {
    inputDataNews() {
      this.renderData();
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
  text-align: left !important;
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
