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
        <div class="wizard-nav border-bottom mb-1 mb-lg-5">
          <div class="wizard-steps px-8 py-8 px-lg-15 py-lg-3">
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
        <div class="row justify-content-center  px-8  px-lg-10">
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
                    class="bb-table"
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
                <!-- <h4 class="mb-10 font-weight-bold text-dark">
                  step3
                </h4> -->
                <div class="row">
                  <!-- IC table  -->

                  <div class="col-xxl-6 col-lg-6 mb-2" v-if="ICitems.length">
                    <v-card>
                      <v-card-title>IC table</v-card-title>
                      <b-table
                        class="bb-table"
                        thClass="bb-table-head"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="ICitems"
                        :fields="stepThreeItemsTableHeaders.ICheaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Statement Table -->

                  <div
                    class="col-xxl-12 col-lg-12 mb-2"
                    v-if="StatementItems.length"
                  >
                    <v-card>
                      <v-card-title>Statement Table</v-card-title>
                      <b-table
                        class="bb-table"
                        thClass="bb-table-head"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="StatementItems"
                        :fields="stepThreeItemsTableHeaders.StatementHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Chief Table -->

                  <div class="col-xxl-6 col-lg-6 mb-2" v-if="ChiefItems.length">
                    <v-card>
                      <v-card-title>Chief Table </v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="ChiefItems"
                        :fields="stepThreeItemsTableHeaders.ChiefHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Shareholders Table -->

                  <div
                    class="col-xxl-6 col-lg-6 mb-2"
                    v-if="ShareholdersItems.length"
                  >
                    <v-card>
                      <v-card-title>Shareholders Table</v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="ShareholdersItems"
                        :fields="stepThreeItemsTableHeaders.ShareholdersHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- CEO Table -->

                  <div class="col-xxl-6 col-lg-6 mb-2" v-if="CEOItems.length">
                    <v-card>
                      <v-card-title>CEO Table</v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="CEOItems"
                        :fields="stepThreeItemsTableHeaders.CEOheaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Board Table -->

                  <div class="col-xxl-6 col-lg-6 mb-2" v-if="BoardItems.length">
                    <v-card>
                      <v-card-title>Board Table</v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="BoardItems"
                        :fields="stepThreeItemsTableHeaders.BoardHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- NewBoard Table -->

                  <div
                    class="col-xxl-6 col-lg-6 mb-2"
                    v-if="NewBoardItems.length"
                  >
                    <v-card>
                      <v-card-title>NewBoard Table </v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="NewBoardItems"
                        :fields="stepThreeItemsTableHeaders.NewBoardHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Wage Table -->

                  <div class="col-xxl-6 col-lg-6 mb-2" v-if="WageItems.length">
                    <v-card>
                      <v-card-title>Wage Table</v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="WageItems"
                        :fields="stepThreeItemsTableHeaders.WageHeaders"
                      ></b-table>
                    </v-card>
                  </div>

                  <!-- Summary Table -->

                  <div class="col-xxl-12 col-lg-12" v-if="SummaryItems.length">
                    <v-card>
                      <v-card-title>Summary Table</v-card-title>
                      <b-table
                        class="bb-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="SummaryItems"
                        :fields="stepThreeItemsTableHeaders.SummaryHeaders"
                      ></b-table>
                    </v-card>
                  </div>
                </div>
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
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import KTUtil from "@/assets/js/components/util";
import KTWizard from "@/assets/js/components/wizard";
import Swal from "sweetalert2";
import datePicker from "vue-persian-datetime-picker";

export default {
  name: "Wizard",
  component: { datePicker },
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
      DecisionsHeaders: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name"
        },
        { text: "Calories", value: "calories" },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" }
      ],
      DecisionsDesserts: [
        {
          name: "Frozen Yogurt",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%"
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%"
        },
        {
          name: "Eclair",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%"
        },
        {
          name: "Cupcake",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%"
        },
        {
          name: "Gingerbread",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%"
        },
        {
          name: "Jelly bean",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%"
        },
        {
          name: "Lollipop",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%"
        },
        {
          name: "Honeycomb",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%"
        },
        {
          name: "Donut",
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%"
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%"
        }
      ],
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
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "LastShareCount", key: "LastShareCount" },
          { label: "LastShareNominalValue", key: "LastShareNominalValue" },
          { label: "LastCapital", key: "LastCapital" },
          { label: "CashIncoming_Final", key: "CashIncoming_Final" },
          { label: "CashIncoming_Ceo", key: "CashIncoming_Ceo" },
          { label: "CashIncoming_Total", key: "CashIncoming_Total" },
          { label: "RetainedEarning_Final", key: "RetainedEarning_Final" },
          { label: "RetainedEarning_Ceo", key: "RetainedEarning_Ceo" },
          { label: "RetainedEarning_Sum", key: "RetainedEarning_Sum" },
          { label: "Reserves_Final", key: "Reserves_Final" },
          { label: "Reserves_Ceo", key: "Reserves_Ceo" },
          { label: "Reserves_Sum", key: "Reserves_Sum" },
          { label: "Reevaluation_Final", key: "Reevaluation_Final" },
          { label: "Reevaluation_Ceo", key: "Reevaluation_Ceo" },
          { label: "Reevaluation_Sum", key: "Reevaluation_Sum" },
          { label: "SarfSaham_Final", key: "SarfSaham_Final" },
          { label: "SarfSaham_Ceo", key: "SarfSaham_Ceo" },
          { label: "SarfSaham_Sum", key: "SarfSaham_Sum" },
          { label: "IncreaseValue_Final", key: "IncreaseValue_Final" },
          { label: "IncreaseValue_Ceo", key: "IncreaseValue_Ceo" },
          { label: "IncreaseValue_Sum", key: "IncreaseValue_Sum" },
          { label: "IncreasePercent_Final", key: "IncreasePercent_Final" },
          { label: "IncreasePercent_Ceo", key: "IncreasePercent_Ceo" },
          { label: "IncreasePercent_Sum", key: "IncreasePercent_Sum" }
        ],
        StatementHeaders: [
          { label: "ID", key: "ID", thClass: "bb-table-head" },
          {
            label: "SummaryID",
            key: "SummaryID"
          },
          {
            label: "Title",
            key: "Title"
          },
          {
            label: "Value",
            key: "Value"
          }
        ],
        ChiefHeaders: [
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "Name", key: "Name" },
          { label: "Position", key: "Position" }
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
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "FullName", key: "FullName" },
          { label: "SSID", key: "SSID" },
          { label: "Degree", key: "Degree" }
        ],
        BoardHeaders: [
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "FullName", key: "FullName" },
          { label: "SSID", key: "SSID" },
          { label: "typeOfCompany", key: "typeOfCompany" },
          { label: "Membership", key: "Membership" },
          { label: "AgentName", key: "AgentName" },
          { label: "AgentSSID", key: "AgentSSID" },
          { label: "Position", key: "Position" },
          { label: "Duty", key: "Duty" },
          { label: "Degree", key: "Degree" }
        ],
        NewBoardHeaders: [
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "Name", key: "Name" },
          { label: "Type", key: "Type" },
          { label: "SSID", key: "SSID" },
          { label: "Duty", key: "Duty" }
        ],
        WageHeaders: [
          { label: "ID", key: "ID" },
          { label: "SummaryID", key: "SummaryID" },
          { label: "Title", key: "Title" },
          { label: "LastYear", key: "LastYear" },
          { label: "CurrentYear", key: "CurrentYear" },
          { label: "MoreDetails", key: "MoreDetails" }
        ],
        SummaryHeaders: [
          { label: "ID", key: "ID" },
          { label: "firm", key: "firm" },
          { label: "report_id", key: "report_id" },
          { label: "ToDate", key: "ToDate" },
          { label: "Correction", key: "Correction" },
          { label: "CorrectionDetails", key: "CorrectionDetails" },
          { label: "NewsPaper", key: "NewsPaper" },

          { label: "Inspector", key: "Inspector" },

          { label: "OtherDesc", key: "OtherDesc" },

          {
            label: "IsListenedBoardMemberReport",
            key: "IsListenedBoardMemberReport"
          },
          { label: "IsSelectInspector", key: "IsSelectInspector" },
          { label: "IsSelectNewspaper", key: "IsSelectNewspaper" },
          { label: "IsBoardMemberGift", key: "IsBoardMemberGift" },
          { label: "IsOther", key: "IsOther" },
          { label: "IsBoardMemberWage", key: "IsBoardMemberWage" },
          { label: "IsSelectBoardMember", key: "IsSelectBoardMember" },
          { label: "IsPublishSecurity", key: "IsPublishSecurity" },
          { label: "IsLocationChange", key: "IsLocationChange" },
          { label: "IsNameChange", key: "IsNameChange" },
          { label: "IsActivitySubjectChange", key: "IsActivitySubjectChange" },
          {
            label: "IsConvertSecurityToShare",
            key: "IsConvertSecurityToShare"
          },
          { label: "IsFinancialYearChange", key: "IsFinancialYearChange" },
          { label: "IsCapitalIncrease", key: "IsCapitalIncrease" }
        ]
      },
      ShareholdersItems: [],
      ChiefItems: [],
      SummaryItems: [],
      ICitems: [],
      StatementItems: [],
      CEOItems: [],
      BoardItems: [],
      NewBoardItems: [],
      WageItems: [],

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
          },
          { value: "d", text: "آگهی دعوت به مجمع" }
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
    this.$store.dispatch(SET_BREADCRUMB, [
      { title: "Wizard", route: "wizard-1" },
      { title: "Wizard-3" }
    ]);

    // Initialize form wizard
    const wizard = new KTWizard("kt_wizard_v3", {
      startStep: 1, // initial active step number
      clickableSteps: false // allow step clicking
    });
    this.wizard = wizard;
    console.log(wizard.isFirstStep());
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
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
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
          console.log(data);
          if (this.stepOneData.TypeSelected == "AssemblyGeneral") {
            this.StatementItems = data[0];
            this.ChiefItems = data[1];
            this.ShareholdersItems = data[2];
            this.CEOItems = data[3];
            this.BoardItems = data[4];
            this.NewBoardItems = data[5];
            this.WageItems = data[6];
            this.SummaryItems = data[7];
          } else if (this.stepOneData.TypeSelected == "AssemblyExtra") {
            this.ICitems = data[0];
            this.ChiefItems = data[1];
            this.ShareholdersItems = data[2];
            this.SummaryItems = data[3];
          } else if (this.stepOneData.TypeSelected == "AssemblyGeneralExtra") {
            this.StatementItems = data[0];
            this.ChiefItems = data[1];
            this.ShareholdersItems = data[2];
            this.CEOItems = data[3];
            this.BoardItems = data[4];
            this.NewBoardItems = data[5];
            this.WageItems = data[6];
            this.SummaryItems = data[7];
          }

          // console.log((data.ShareHolders));
          // console.log((data.Chief));
          // console.log((data.Summary));
          // console.log((data.IC));
          // console.log(JSON.parse(data.ShareHolders));
          // console.log(JSON.parse(data.Chief));
          // console.log(JSON.parse(data.Summary));
          // console.log(JSON.parse(data.IC));
          // this.ShareholdersItems = JSON.parse(data.ShareHolders);
          // this.ChiefItems = JSON.parse(data.Chief);
          // this.SummaryItems = JSON.parse(data.Summary);
          // this.ICitems = JSON.parse(data.IC);
          // this.stepThreeItems.Shareholders = JSON.parse(data.ShareHolders);
          // this.stepThreeItems.Chief = JSON.parse(data.Chief)
          // this.stepThreeItems.Summary = JSON.parse(data.Summary)
          // this.stepThreeItems.IC = JSON.parse(data.IC)

          // console.log(this.stepThreeItems);
        })
        .catch(error => {
          console.log(error);
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
          console.log("ok");
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
/* .bb-table {
  text-align: right;
} */
.bb-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.bb-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.selectionTable {
  direction: rtl;
  text-align: right;
}
</style>
