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
                  <span>۱</span>انتخاب تاریخ و نوع مجمع شرکت
                </h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title"><span>۲</span>انتخاب مجمع</h3>
                <div class="wizard-bar"></div>
              </div>
            </div>
            <div class="wizard-step" data-wizard-type="step">
              <div class="wizard-label">
                <h3 class="wizard-title"><span>۳</span>نمایش اطلاعات</h3>
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
        <div class="row justify-content-center py-12 px-8 py-lg-15 px-lg-10">
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
                  <div class="col-xl-3">
                    <date-picker
                      v-model="stepOneData.startDate"
                      label="از"
                      placeholder="انتخاب کنید..."
                    />
                  </div>
                  <div class="col-xl-3">
                    <date-picker
                      v-model="stepOneData.endDate"
                      label="تا"
                      placeholder="انتخاب کنید..."
                    />
                  </div>
                  <div class="col-xl-3">
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
                  <div class="col-xl-3">
                    <b-form-select
                      v-model="stepOneData.FirmSelected"
                      :options="stepOneData.FirmOptions"
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
              <div class="pb-5" data-wizard-type="step-content">
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
                  v-model="selected"
                  :headers="headers"
                  :items="desserts"
                  dense
                  single-select="true"
                  :header-props="{ sortIcon: null }"
                  item-key="name"
                  show-select
                  hide-default-footer
                  class="elevation-1 selectionTable"
                  items-per-page="30"
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

              <!--begin: Wizard Step 4-->
              <!-- <div class="pb-5" data-wizard-type="step-content">
                <h4 class="mb-10 font-weight-bold text-dark">
                  step 4
                </h4>
              </div> -->
              <!--end: Wizard Step 4-->

              <!--begin: Wizard Step 5-->
              <!-- <div class="pb-5" data-wizard-type="step-content">
                <h4 class="mb-10 font-weight-bold text-dark">
                  step 5
                </h4>
              </div> -->
              <!--end: Wizard Step 5-->

              <!--begin: Wizard Actions -->
              <div class="d-flex justify-content-between border-top pt-10">
                <div class="mr-2">
                  <button
                    class="btn btn-light-primary font-weight-bold text-uppercase px-9 py-4"
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
                    class="btn btn-primary font-weight-bold text-uppercase px-9 py-4"
                    data-wizard-type="action-next"
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
</style>

<script>
// import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import KTUtil from "@/assets/js/components/util";
import KTWizard from "@/assets/js/components/wizard";
import Swal from "sweetalert2";
import datePicker from "vue-persian-datetime-picker";

export default {
  name: "Wizard",
  component: { datePicker },
  data() {
    return {
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
      selected: [],
      headers: [
        {
          text: "تاریخ",
          align: "end",
          sortable: false,
          value: "name"
        }
      ],
      desserts: [
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
        }
      ],
      stepOneData: {
        startDate: "",
        endDate: "",
        TypeSelected: null,
        TypeOptions: [
          { value: "a", text: "مجمع عادی" },
          { value: "b", text: "مجمع فوق العاده" },
          { value: { C: "3PO" }, text: "مجمع عادی به طور فوق العاده" }
        ],
        FirmSelected: null,
        FirmOptions: []
      }
    };
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
    submit: function(e) {
      e.preventDefault();
      Swal.fire({
        title: "",
        text: "The application has been successfully submitted!",
        icon: "success",
        confirmButtonClass: "btn btn-secondary"
      });
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
