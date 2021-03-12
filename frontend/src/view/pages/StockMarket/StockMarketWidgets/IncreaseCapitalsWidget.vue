<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        افزایش سرمایه ها
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
        <template v-slot:[`item.IncreasePercent`]="{ item }">
          <span class="cellItem">{{ roundTo(item.IncreasePercent, 2) }}% </span>
        </template>
        <template v-slot:[`item.AttachmentUrl`]="{ item }">
          <v-chip label small :disabled="item.HtmlUrl == '' ? true : false">
            <a v-bind:href="`http://codal.ir${item.HtmlUrl}`" target="_blank"
              >اطلاعیه
            </a>
          </v-chip>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "ICWidget",
  props: ["notices"],
  data() {
    return {
      search: "",
      loading: true,
      headers: [
        {
          text: "سهم",
          value: "ticker"
        },
        {
          text: "زمان انتشار",
          value: "PublishTime"
        },
        {
          text: "نوع اطلاعیه",
          value: "Title"
        },
        {
          text: "درصد افزایش سرمایه",
          value: "IncreasePercent"
        },
        {
          text: "محل افزایش سرمایه",
          value: "CapitalChangeType"
        },
        {
          text: "لینک فایلها",
          value: "AttachmentUrl"
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
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
    },
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
.cellItem {
  font-family: "Dirooz FD";
  font-weight: 600;
}
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
