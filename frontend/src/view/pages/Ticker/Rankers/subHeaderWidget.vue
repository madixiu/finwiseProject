<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        {{ this.Nemad }}<span class="small mr-5">{{ this.tickerfull }}</span>
      </h3>
    </div> -->
    <div class="row border-0 pb-4 pt-2">
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          نماد
        </v-chip>
        {{ DataItems.ticker }}
      </div>
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          نام شرکت
        </v-chip>
        {{ DataItems.name }}
      </div>
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          بازار
        </v-chip>
        {{ DataItems.market }}
      </div>
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          صنعت
        </v-chip>

        {{ DataItems.subIndustry }}
      </div>
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          تابلو
        </v-chip>
        {{ DataItems.board }}
      </div>
      <div class="col-xxl-2 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1A237E" text-color="#FAFAFA">
          گروه
        </v-chip>
        {{ DataItems.parentIndustry }}
      </div>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import axios from "axios";
export default {
  name: "SubHeaderWidget",
  props: ["tickerdata"],
  data() {
    return {
      search: "",
      DataItems: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems = this.tickerdata;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    tickerdata() {
      this.populateData();
      // console.log("WatcherSubHeader");
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
