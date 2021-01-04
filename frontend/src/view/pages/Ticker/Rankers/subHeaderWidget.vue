<template>
  <!--begin::Mixed Widget 14-->
  <div>
    <v-card width="100%">
      <!-- <div class="row border-0 pb-4 pt-2"> -->
      <div class="row pb-2 pt-4">
        <div class="col-xxl-2 col-lg-2 FinancialStrength pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
          نماد
        </v-chip> -->
          <div class="text-center">
            <b-button class="testB" variant="primary">
              نماد
              <br /><b-badge variant="light">{{ DataItems.ticker }}</b-badge>
            </b-button>
          </div>
          <!-- {{ DataItems.ticker }} -->
        </div>
        <div class="col-xxl-2 col-lg-2 FinancialStrength pr-5 pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            نام شرکت
          </v-chip>
          {{ DataItems.name }} -->
          <div class="text-center">
            <b-button variant="primary">
              نام شرکت <br /><b-badge variant="light">{{
                DataItems.name
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div class="col-xxl-2 col-lg-2 FinancialStrength pr-5 pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            بازار
          </v-chip>
          {{ DataItems.market }} -->
          <div class="text-center">
            <b-button variant="primary">
              بازار <br /><b-badge variant="light">{{
                DataItems.market
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div class="col-xxl-2 col-lg-2 FinancialStrength pr-5 pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            صنعت
          </v-chip>
          {{ DataItems.subIndustry }} -->
          <div class="text-center">
            <b-button variant="primary">
              صنعت <br /><b-badge variant="light">{{
                DataItems.subIndustry
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div class="col-xxl-2 col-lg-2 FinancialStrength pr-5 pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            تابلو
          </v-chip>
          {{ DataItems.board }} -->
          <div class="text-center">
            <b-button variant="primary">
              تابلو <br /><b-badge variant="light">{{
                DataItems.board
              }}</b-badge>
            </b-button>
          </div>
        </div>
        <div class="col-xxl-2 col-lg-2 FinancialStrength pr-5 pb-2 pt-2">
          <!-- <v-chip class="ma-2" color="#1A237E" text-color="#FAFAFA">
            گروه
          </v-chip>
          {{ DataItems.parentIndustry }} -->
          <div class="text-center">
            <b-button variant="primary">
              گروه <br /><b-badge variant="light">{{
                DataItems.parentIndustry
              }}</b-badge>
            </b-button>
          </div>
        </div>
      </div>
    </v-card>
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        {{ this.Nemad }}<span class="small mr-5">{{ this.tickerfull }}</span>
      </h3>
    </div> -->
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
  font-size: 0.8em;
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
