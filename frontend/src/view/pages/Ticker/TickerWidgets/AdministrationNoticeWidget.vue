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
    <div class="row">
      <div class="col-xxl-2 FinancialStrength" v-if="loading">
        <v-skeleton-loader
          v-bind="attrs"
          type=" list-item, card-heading, divider, date-picker-options, date-picker-days, actions"
        ></v-skeleton-loader>
      </div>
      <div class="col-xxl-2 FinancialStrength" v-if="loading == false">
        <p>فیلتر بر اساس تاریخ</p>
        <p class="FinancialStrength">تاریخ شروع :</p>
        <date-picker v-model="date"></date-picker>
        <hr />
        <p class="FinancialStrength">تاریخ پایان :</p>
        <date-picker v-model="date"></date-picker>
        <hr />
        <v-btn small color="primary" dark>
          اعمال فیلتر
        </v-btn>

        <v-btn small color="primary" dark>
          حذف فیلتر x
        </v-btn>
      </div>
      <div class="col-xxl-10 FinancialStrength">
        <div class="card-body d-flex flex-column" v-if="loading">
          <v-skeleton-loader
            v-bind="attrs"
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
      </div>
    </div>

    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
import Vue from "vue";
import VuePersianDatetimePicker from "vue-persian-datetime-picker";
Vue.component("date-picker", VuePersianDatetimePicker);
export default {
  name: "AdministrationWidget",
  props: ["notices"],
  data() {
    return {
      filtered: false,
      loading: true,
      search: "",
      headers: [
        {
          text: "تاریخ ارسال",
          value: "Submited"
        },
        {
          text: "عنوان",
          value: "Title"
        },
        {
          text: "متن پیام ناظر",
          value: "Text"
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  components: {
    datePicker: VuePersianDatetimePicker
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
      // console.log("Watcher");
      this.populateData();
      this.loading = false;
      // console.log(this.notices);
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl !important;
  text-align: right !important;
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
  vertical-align: baseline !important;
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
input {
  display: inline-block !important;
}
</style>
