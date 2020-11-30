<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        سابقه قیمت
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <v-data-table
        :headers="headers"
        :items="DataItems2"
        class="elevation-1 FinancialStrength"
        :header-props="{ sortIcon: null }"
        :disable-sort="true"
      >
        <!-- <template v-slot:[`item.HtmlUrl`]="{ item }">
          <v-chip label small :disabled="item.HtmlUrl == '' ? true : false">
            <a v-bind:href="`http://codal.ir${item.HtmlUrl}%`">گزارش </a>
          </v-chip>
        </template>
        <template v-slot:[`item.AttachmentUrl`]="{ item }">
          <v-chip
            label
            small
            :disabled="item.AttachmentUrl == '' ? true : false"
          >
            <a v-bind:href="`http://codal.ir${item.AttachmentUrl}%`">فایل </a>
          </v-chip>
        </template>
        <template v-slot:[`item.ExcelUrl`]="{ item }">
          <v-chip label small :disabled="item.ExcelUrl == '' ? true : false">
            <a v-bind:href="`${item.ExcelUrl}%`">اکسل </a>
          </v-chip>
        </template>
        <template v-slot:[`item.PdfUrl`]="{ item }">
          <v-chip label small :disabled="item.PdfUrl == '' ? true : false">
            <a v-bind:href="`http://codal.ir/${item.PdfUrl}%`">پی دی اف </a>
          </v-chip>
        </template> -->
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "adjustedWidget",
  props: ["adjusted"],
  data() {
    return {
      search: "",
      headers: [
        {
          text: "تاریخ میلادی",
          value: "engdate"
        },
        {
          text: "تاریخ شمسی",
          value: "persiandate"
        },
        {
          text: "بالاترین قیمت",
          value: "high"
        },
        {
          text: "پایین ترین قیمت",
          value: "low"
        },
        {
          text: "قیمت پایانی",
          value: "closing"
        },
        {
          text: "آخرین قیمت",
          value: "last"
        },
        {
          text: " اولین قیمت",
          value: "first"
        },
        {
          text: "ارزش معاملات",
          value: "value"
        },
        {
          text: "حجم معاملات",
          value: "volume"
        },
        {
          text: "قیمت تعدیلی",
          value: "adjustedclosing"
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
      this.DataItems2 = this.adjusted;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    adjusted() {
      console.log("Watcher");
      this.populateData();
      // console.log(this.notices);
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
