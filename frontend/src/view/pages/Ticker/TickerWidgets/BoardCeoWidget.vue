<template>
  <div>
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        اطلاعات هیئت مدیره
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading"
        ></b-spinner>
      </h3>
    </div> -->
    <!--end::Header-->
    <!--begin::Body-->
    <div class="row">
      <div class="col-xxl-3 FinancialStrength">
        <div class="card-body d-flex flex-column" v-if="loading == false">
          <v-chip v-if="deposits.length != 0" label>مدیر عامل</v-chip>
          <v-data-table
            v-if="deposits.length != 0"
            :headers="ceoheaders"
            :items="deposits"
            class="elevation-1 FinancialStrength"
            :header-props="{ sortIcon: null }"
            :disable-sort="true"
            hide-default-footer
            disable-pagination
          >
          </v-data-table>
        </div>
      </div>
      <div class="col-xxl-9 FinancialStrength">
        <div class="card-body d-flex flex-column" v-if="loading == false">
          <v-chip v-if="notices.length != 0" label>هیئت مدیره</v-chip>
          <v-data-table
            v-if="notices.length != 0"
            :headers="boardheaders"
            :items="notices"
            class="elevation-1 FinancialStrength "
            :header-props="{ sortIcon: null }"
            :disable-sort="true"
            hide-default-footer
            disable-pagination
          >
          </v-data-table>
        </div>
      </div>
    </div>

    <div
      class="card-body d-flex flex-column"
      v-if="notices.length == 0 && deposits.length == 0 && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "BoardWidget",
  props: ["notices", "deposits"],
  data() {
    return {
      search: "",
      loading: true,
      ceoheaders: [
        { text: "نام مدیر عامل", value: "CEOName" },
        { text: "مدرک", value: "CEODegree" }
      ],
      boardheaders: [
        { text: "نام عضو", value: "newBoardName" },
        { text: "کد/شناسه ملی", value: "NationalCode" },
        { text: "نماینده", value: "NewAgentName" },
        { text: "سمت", value: "Posistion" },
        { text: "موظف", value: "Duty" },
        { text: "مدرک تحصیلی", value: "Degree" },
        { text: "تاریخ جلسه", value: "SessionDate" }
      ]
    };
  },



  watch: {
    notices() {
      this.loading = false;
    },
    deposits() {
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
th {
  font-size: 8em !important;
}
</style>
