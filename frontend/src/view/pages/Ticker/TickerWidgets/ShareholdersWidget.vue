<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        سهامداران عمده
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading"
        ></b-spinner>
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="row">
      <div class="col-xxl-9 FinancialStrength">
        <div class="card-body d-flex flex-column" v-if="loading == false">
          <v-chip v-if="notices.length != 0" label
            >اطلاعات سهامداران عمده</v-chip
          >
          <v-data-table
            v-if="notices.length != 0"
            :headers="boardheaders"
            :items="DataItems2"
            class="elevation-1 FinancialStrength "
            :header-props="{ sortIcon: null }"
            :disable-sort="true"
            hide-default-footer
            disable-pagination
          >
          </v-data-table>
        </div>
      </div>
      <div class="col-xxl-3 FinancialStrength">
        <div class="card-body d-flex flex-column" v-if="loading == false">
          <v-chip v-if="notices.length != 0" label>اطلاعات سهم</v-chip>
          <v-data-table
            v-if="notices.length != 0"
            :headers="Infoheaders"
            :items="DataItems3"
            class="elevation-1 FinancialStrength"
            :header-props="{ sortIcon: null }"
            :disable-sort="true"
            hide-default-footer
            disable-pagination
          >
            <template v-slot:[`item.Ownership`]="{ item }">
              <v-tooltip left>
                <template v-slot:activator="{ on }">
                  <v-chip label small v-on="on"
                    >{{ this.roundTo(item.Ownership,2) }} درصد</v-chip
                  >
                </template>
                <span class="small">{{ item.persianDate }}</span>
              </v-tooltip>
            </template>
          </v-data-table>
        </div>
      </div>
    </div>

    <div
      class="card-body d-flex flex-column"
      v-if="notices.length == 0 && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "ShareholdersWidget",
  props: ["notices"],
  data() {
    return {
      search: "",
      loading: true,
      DataItems2: [],
      DataItems3: [],
      Infoheaders: [
        { text: "درصد شناوری", value: "Shenavari" },
        { text: "تاریخ", value: "persianDate" },
        { text: "تعداد سهم", value: "ShareCount" }
      ],
      boardheaders: [
        { text: "سهامدار", value: "name" },
        { text: "تعداد سهام", value: "count" },
        { text: "درصد مالکیت", value: "Ownership" }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems2 = this.notices;
    },
    populatesubData() {
      var dd = {
        persianDate: this.notices[0]["persianDate"],
        Shenavari: this.notices[0]["Shenavari"],
        ShareCount: this.notices[0]["ShareCount"]
      };
      this.DataItems3 = [dd];
    },
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      if (n == "-") {
        return n;
      }

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
  mounted() {
      this.DataItems2=[]
      this.DataItems3=[]
    this.populateData();
    this.populatesubData();
  },
  watch: {
    notices() {
      //   console.log("Watcher");
      this.populateData();
      this.loading = false;
      this.populatesubData();
      //   console.log(this.notices);
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
th {
  font-size: 8em !important;
}
</style>
