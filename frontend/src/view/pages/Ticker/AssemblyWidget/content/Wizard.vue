<template>
  <div>
    <v-card>
      <div
        class="wizard wizard-3"
        id="kt_wizard_v3"
        data-wizard-state="step-first"
        data-wizard-clickable="false"
      >
        <!--begin: Wizard Nav -->
        <div class="wizard-nav border-bottom ">
          <div class="wizard-steps px-8 px-lg-15">
            <div
              class="wizard-step"
              data-wizard-type="step"
              data-wizard-state="current"
            >
              <div class="wizard-label">
                <h3 class="wizard-title">
                  <span class="step-text">۱</span>
                  <span class="step-text">انتخاب نوع مجمع شرکت</span>
                </h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title">
                  <span class="step-text">۲</span
                  ><span class="step-text">انتخاب مجمع</span>
                </h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title">
                  <span class="step-text">۳</span
                  ><span class="step-text">نمایش اطلاعات</span>
                </h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <!-- <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title"><span>۴</span>مرحله چهارم</h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title"><span>۵</span>مرحله پنجم</h3>
                <div class="wizard-bar"></div>
              </div>
            </div> -->
          </div>
        </div>
        <!--end: Wizard Nav -->

        <!--begin: Wizard Body-->
        <div class="row justify-content-center  px-8  px-lg-1">
          <div class="col-xl-12 col-xxl-7">
            <!--begin: Wizard Form-->
            <form class="form" id="kt_form">
              <!--begin: Wizard Step 1-->
              <div
                class="pb-5"
                data-wizard-type="step-content"
                data-wizard-state="current"
              >
                <!-- <h4 class="mb-10 font-weight-bold text-dark">
                  step 1
                </h4> -->
                <div class="row">
                  <div class="col-xl-4">
                    <date-picker
                      v-model="stepOneData.startDate"
                      color="#1e1e2d"
                      label="از"
                      placeholder="انتخاب کنید..."
                      :auto-submit="true"
                      view="year"
                    />
                  </div>
                  <div class="col-xl-4">
                    <date-picker
                      v-model="stepOneData.endDate"
                      color="#1e1e2d"
                      label="تا"
                      :auto-submit="true"
                      placeholder="انتخاب کنید..."
                    />
                  </div>
                  <div class="col-xl-4">
                    <b-form-select
                      v-model="stepOneData.TypeSelected"
                      :options="stepOneData.TypeOptions"
                    >
                      <template #first>
                        <b-form-select-option :value="null" disabled
                          >-- انتخاب کنید --</b-form-select-option
                        >
                      </template>
                    </b-form-select>
                  </div>
                </div>
              </div>
              <!--end: Wizard Step 1-->

              <!--begin: Wizard Step 2-->
              <div class="pb-1" data-wizard-type="step-content">
                <!-- <h4 class="mb-10 font-weight-bold text-dark">
                  step 2
                </h4> -->
                <!-- <div>
                  <b-table
                    class="ticker-assembly-table"
                    ref="selectableTable"
                    selectable
                    select-mode="single"
                    :items="items"
                    :fields="fields"
                    @row-selected="onRowSelected"
                    responsive="sm"
                  >

                    <template #cell(selected)="{ rowSelected }">
                      <template v-if="rowSelected">
                        <span aria-hidden="true">&check;</span>
                        <span class="sr-only">Selected</span>
                      </template>
                      <template v-else>
                        <span aria-hidden="true">&nbsp;</span>
                        <span class="sr-only">Not selected</span>
                      </template>
                    </template>
                  </b-table>

                  <p>
                    Selected Rows:<br />
                    {{ selectedRow }}
                  </p>
                </div> -->
                <v-data-table
                  v-model="stepTwoSelected"
                  :headers="stepTwoHeaders"
                  :items="stepTwoItems"
                  dense
                  :single-select="true"
                  :header-props="{ sortIcon: null }"
                  item-key="id"
                  show-select
                  hide-default-footer
                  class="elevation-1 selectionTable"
                >
                </v-data-table>
              </div>
              <!--end: Wizard Step 2-->

              <!--begin: Wizard Step 3-->
              <div class="pb-5" data-wizard-type="step-content">
                <!-- ******************** TABLE COMPONENT ********************* -->
                <AssemblyTables
                  :ShareholdersItems="ShareholdersData"
                  :ChiefItems="ChiefData"
                  :SummaryItems="SummaryData"
                  :ICitems="ICData"
                  :StatementItems="StatementData"
                  :CEOItems="CEOData"
                  :BoardItems="BoardData"
                  :NewBoardItems="NewBoardData"
                  :WageItems="WageData"
                >
                </AssemblyTables>

                <!-- ******************** TABLE COMPONENT ********************* -->
              </div>
              <!--end: Wizard Step 3-->

              <!--begin: Wizard Actions -->
              <div class="d-flex justify-content-between border-top pt-1">
                <div class="mr-2">
                  <button
                    class="btn btn-light-primary font-weight-bold text-uppercase px-9 py-2"
                    data-wizard-type="action-prev"
                  >
                    بازگشت
                  </button>
                </div>
                <div>
                  <!-- <button
                    v-on:click="submit"
                    class="btn btn-success font-weight-bold text-uppercase px-9 py-4"
                    data-wizard-type="action-submit"
                  >
                    Submit
                  </button> -->
                  <button
                    class="btn btn-primary font-weight-bold text-uppercase px-9 py-2"
                    data-wizard-type="action-next"
                    @click="submit"
                    :disabled="nextBtnDisable"
                  >
                    مرحله بعد
                  </button>
                </div>
              </div>

              <!--end: Wizard Actions -->
            </form>
            <!--end: Wizard Form-->
          </div>
        </div>
        <!--end: Wizard Body-->
      </div>
    </v-card>
  </div>
</template>

<style lang="scss">
@import "@/assets/sass/pages/wizard/wizard-3.scss";

.step-text {
  font-size: 1rem !important;
  margin-right: 0.5rem !important;
}
</style>

<script>
// import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import AssemblyTables from "@/view/pages/Ticker/AssemblyWidget/content/AssemblyTables.vue";
import KTUtil from "@/assets/js/components/util";
import KTWizard from "@/assets/js/components/wizard";
import Swal from "sweetalert2";
import datePicker from "vue-persian-datetime-picker";

export default {
  name: "Wizard",
  components: { datePicker, AssemblyTables },
  data() {
    return {
      wizard: null,
      nextBtnDisable: true,
      fields: ["first_name", "last_name", "age"],
      items: [
        { age: 40, first_name: "Dickerson", last_name: "Macdonald" },
        { age: 21, first_name: "Larsen", last_name: "Shaw" },
        { age: 89, first_name: "Geneva", last_name: "Wilson" }
      ],
      selectMode: "multi",
      selectedRow: [],
      stepTwoSelected: null,
      stepTwoHeaders: [
        { text: "مجمع", align: "end", sortable: false, value: "title" },
        {
          text: "تاریخ",
          align: "end",
          sortable: false,
          value: "PublishTime"
        }
      ],
      stepThreeItemsTableHeaders: {
        // ShareholdersHeaders: ["درصد مالکیت","تعداد سهام","سهامدار"],

        ICheaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "تعداد سهام", key: "LastShareCount" },
          { label: "ارزش اسمی هر سهم", key: "LastShareNominalValue" },
          { label: "آخرین سرمایه ثبتی", key: "LastCapital" },
          { label: "مطالبات و آورده نقدی-قطعی", key: "CashIncoming_Final" },
          {
            label: "مطالبات و آورده نقدی-در اختیار هیئت مدیره",
            key: "CashIncoming_Ceo"
          },
          { label: "مطالبات و آورده نقدی-کل", key: "CashIncoming_Total" },
          { label: "سود انباشته-قطعی", key: "RetainedEarning_Final" },
          {
            label: "سود انباشته-قطعی در اختیار هیئت مدیره",
            key: "RetainedEarning_Ceo"
          },
          { label: "سود انباشته-کل", key: "RetainedEarning_Sum" },
          { label: "اندوخته-قطعی", key: "Reserves_Final" },
          { label: "اندوخته-در اختیار هیئت مدیره", key: "Reserves_Ceo" },
          { label: "اندوخته-کل", key: "Reserves_Sum" },
          { label: "مازاد تجدید ارزیابی-قطعی", key: "Reevaluation_Final" },
          {
            label: "مازاد تجدید ارزیابی-در اختیار هیئت مدیره",
            key: "Reevaluation_Ceo"
          },
          { label: "مازاد تجدید ارزیابی-کل", key: "Reevaluation_Sum" },
          { label: "صرف سهام-قطعی", key: "SarfSaham_Final" },
          { label: "صرف سهام در اختیار هیئت مدیره", key: "SarfSaham_Ceo" },
          { label: "صرف سهام-کل", key: "SarfSaham_Sum" },
          { label: "مبلغ افزایش سرمایه-قطعی", key: "IncreaseValue_Final" },
          {
            label: "مبلغ افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreaseValue_Ceo"
          },
          { label: "مبلغ افزایش سرمایه-کل", key: "IncreaseValue_Sum" },
          { label: "درصد افزایش سرمایه-قطعی", key: "IncreasePercent_Final" },
          {
            label: "درصد افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreasePercent_Ceo"
          },
          { label: "درصد افزایش سرمایه-کل", key: "IncreasePercent_Sum" }
        ],
        StatementHeaders: [
          // { label: "ID", key: "ID", thClass: "ticker-assembly-table-head" },
          // {
          //   label: "SummaryID",
          //   key: "SummaryID"
          // },
          {
            label: "عنوان",
            key: "Title"
          },
          {
            label: "مقدار",
            key: "Value"
          }
        ],
        ChiefHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "Name" },
          { label: "سمت", key: "Position" }
        ],
        ShareholdersHeaders: [
          { label: "سهامدار", key: "Shareholders" },
          {
            label: "تعداد سهام",
            key: "ShareCount"
          },
          {
            label: "درصد مالکیت",
            key: "OwnerPercentage"
          }
        ],
        CEOheaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "FullName" },
          // { label: "SSID", key: "SSID" },
          { label: "مدرک تحصیلی", key: "Degree" }
        ],
        BoardHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "FullName" },
          // { label: "SSID", key: "SSID" },
          { label: "نوع شرکت", key: "typeOfCompany" },
          { label: "عضویت", key: "Membership" },
          { label: "نام نماینده", key: "AgentName" },
          // { label: "AgentSSID", key: "AgentSSID" },
          { label: "سمت", key: "Position" },
          // { label: "Duty", key: "Duty" },
          { label: "مدرک تحصیلی", key: "Degree" }
        ],
        NewBoardHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "Name" },
          { label: "نوع", key: "Type" },
          // { label: "SSID", key: "SSID" },
          { label: "وظیفه", key: "Duty" }
        ],
        WageHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "عنوان", key: "Title" },
          { label: "سال گذشته", key: "LastYear" },
          { label: "سال جاری", key: "CurrentYear" },
          { label: "اطلاعات بیشتر", key: "MoreDetails" }
        ],
        SummaryHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "firm", key: "firm" },
          // { label: "report_id", key: "report_id" },
          { label: "منتهی به", key: "ToDate" },
          { label: "اصلاحات", key: "Correction" },
          { label: "توضیحات اصلاحی", key: "CorrectionDetails" },
          { label: "روزنامه", key: "NewsPaper" },

          { label: "حسابرس", key: "Inspector" },

          { label: "سایر توضیحات", key: "OtherDesc" },

          {
            label: "استماع گزارش هیئت مدیره",
            key: "IsListenedBoardMemberReport"
          },
          { label: "انتخاب حسابرس", key: "IsSelectInspector" },
          { label: "انتخاب روزنامه", key: "IsSelectNewspaper" },
          { label: "تصمیم گیری پاداش هیئت مدیره", key: "IsBoardMemberGift" },
          { label: "دارای توضیحات اضافی", key: "IsOther" },
          { label: "تصمیم گیری حقوق هیئت مدیره", key: "IsBoardMemberWage" },
          { label: "انتخاب اعضای هیئت مدیره", key: "IsSelectBoardMember" },
          { label: "انتشار اوراق بهادار", key: "IsPublishSecurity" },
          { label: "تغییر محل فعالیت شرکت", key: "IsLocationChange" },
          { label: "تغییر نام شرکت", key: "IsNameChange" },
          { label: "تغییر فعالیت شرکت", key: "IsActivitySubjectChange" },
          // {
          //   label: "IsConvertSecurityToShare",
          //   key: "IsConvertSecurityToShare"
          // },
          { label: "تغییر سال مالی", key: "IsFinancialYearChange" },
          { label: "افزایش سرمایه", key: "IsCapitalIncrease" }
        ]
      },
      ShareholdersData: [],
      ChiefData: [],
      SummaryData: [],
      ICData: [],
      StatementData: [],
      CEOData: [],
      BoardData: [],
      NewBoardData: [],
      WageData: [],

      stepTwoItems: [],
      stepOneData: {
        startDate: "1360/01/01",
        endDate: "1399/10/10",
        TypeSelected: null,
        TypeOptions: [
          { value: "AssemblyGeneral", text: "مجمع عادی" },
          { value: "AssemblyExtra", text: "مجمع فوق العاده" },
          {
            value: "AssemblyGeneralExtra",
            text: "مجمع عادی به طور فوق العاده"
          }
          // { value: "d", text: "آگهی دعوت به مجمع" }
        ]
      }
    };
  },
  watch: {
    stepOneData: {
      handler() {
        if (
          this.stepOneData.TypeSelected != null &&
          this.stepOneData.endDate.length &&
          this.stepOneData.startDate.length
        )
          this.nextBtnDisable = false;
        else this.nextBtnDisable = true;
      },
      deep: true
    }
    // stepTwoSelected() {
    //   if (this.stepTwoSelected.length) this.nextBtnDisable = false;
    //   else this.nextBtnDisable = true;
    // }
  },
  mounted() {
    // this.$store.dispatch(SET_BREADCRUMB, [
    //   { title: "Wizard", route: "wizard-1" },
    //   { title: "Wizard-3" }
    // ]);

    // Initialize form wizard
    const wizard = new KTWizard("kt_wizard_v3", {
      startStep: 1, // initial active step number
      clickableSteps: false // allow step clicking
    });
    this.wizard = wizard;
    // Validation before going to next page
    wizard.on("beforeNext", function(/*wizardObj*/) {
      // validate the form and use below function to stop the wizard's step
      // wizardObj.stop();
    });

    // Change event
    wizard.on("change", function(/*wizardObj*/) {
      setTimeout(() => {
        KTUtil.scrollTop();
      }, 500);
    });
  },
  methods: {
    stepOneDataPostReq() {
      this.axios({
        method: "post",
        url: "/api/tickerAssemblyStepOne",
        data: {
          tickerID: this.$route.params.id,
          startDate: this.stepOneData.startDate,
          endDate: this.stepOneData.endDate,
          Type: this.stepOneData.TypeSelected
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          this.stepTwoItems = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    stepTwoDataPostReq() {
      this.axios({
        method: "post",
        url: "/api/tickerAssemblyStepTwo",
        data: {
          SummaryID: this.stepTwoSelected[0].id,
          Type: this.stepOneData.TypeSelected
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          let data = response.data;
          if (this.stepOneData.TypeSelected == "AssemblyGeneral") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
          } else if (this.stepOneData.TypeSelected == "AssemblyExtra") {
            this.StatementData = [];
            this.CEOData = [];
            this.BoardData = [];
            this.NewBoardData = [];
            this.WageData = [];
            this.ICData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.SummaryData = data[3];
          } else if (this.stepOneData.TypeSelected == "AssemblyGeneralExtra") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    submit: function(e) {
      e.preventDefault();
      if (this.wizard.isFirstStep()) {
        this.stepOneDataPostReq();
      } else if (
        !!this.wizard.isFirstStep() == false &&
        !!this.wizard.isLastStep() == false
      ) {
        if (this.stepTwoSelected.length) {
          this.stepTwoDataPostReq();
        } else {
          this.wizard.stop();
          Swal.fire({
            icon: "error",
            title: "خطا...",
            text: "لطفا یک گزینه انتخاب کنید",
            confirmButtonText: "باشه",
            showConfirmButton: false,
            timer: 1500
          });
        }
      }
      // if (wizard)
      // Swal.fire({
      //   title: "",
      //   text: "The application has been successfully submitted!",
      //   icon: "success",
      //   confirmButtonClass: "btn btn-secondary"
      // });
    },
    onRowSelected(items) {
      this.selectedRow = items;
    },
    getColor(calories) {
      if (calories > 400) return "red";
      else if (calories > 200) return "orange";
      else return "green";
    }
  }
};
</script>
<style scoped>
/* .ticker-assembly-table {
  text-align: right;
} */
.ticker-assembly-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.ticker-assembly-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.selectionTable {
  direction: rtl;
  text-align: right;
}
</style>
