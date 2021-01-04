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
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
                  </div>
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
                  </div>
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
                  </div>
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
                  </div>
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
                  </div>
                  <div class="col-xxl-6 col-lg-6">
                    <b-table
                      class="bb-table"
                      striped
                      bordered
                      outlined
                      small
                      hover
                      fixed
                      foot-clone
                      :items="items"
                      :fields="fields"
                    ></b-table>
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
      // items: [
      //   { تاریخ: "Dickerson" },
      //   { تاریخ: "Larsen" },
      //   { تاریخ: "Geneva" },
      //   { تاریخ: "Jami" }
      // ],
      stepTwoSelected: [],
      stepTwoHeaders: [
        { text: "مجمع", align: "end", sortable: false, value: "title" },
        {
          text: "تاریخ",
          align: "end",
          sortable: false,
          value: "PublishTime"
        }
      ],
      stepTwoItems: [
        // {
        //   name: "Frozen Yogurt",
        //   calories: 159,
        //   fat: 6.0,
        //   carbs: 24,
        //   protein: 4.0,
        //   iron: "1%"
        // },
        // {
        //   name: "Ice cream sandwich",
        //   calories: 237,
        //   fat: 9.0,
        //   carbs: 37,
        //   protein: 4.3,
        //   iron: "1%"
        // },
        // {
        //   name: "Eclair",
        //   calories: 262,
        //   fat: 16.0,
        //   carbs: 23,
        //   protein: 6.0,
        //   iron: "7%"
        // }
      ],
      stepOneData: {
        startDate: "",
        endDate: "",
        TypeSelected: null,
        TypeOptions: [
          { value: "a", text: "مجمع عادی" },
          { value: "b", text: "مجمع فوق العاده" },
          { value: "c", text: "مجمع عادی به طور فوق العاده" },
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
.bb-table {
  text-align: right;
}
.selectionTable {
  direction: rtl;
  text-align: right;
}
</style>
