<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        گزارش مجامع
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <!-- <div class="card-body d-flex flex-column">
      <v-skeleton-loader
        type=" table-heading, table-thead, table-tbody"
      ></v-skeleton-loader>
    </div> -->
    <div class="card-body d-flex flex-column">
      <div class="row FinancialStrength">
        <div class="col-xxl-4">
          <span>انتخاب نوع مجمع :</span>
          <b-dropdown
            id="ddCommodity"
            name="ddCommodity"
            v-model="ddTestSelectedOption"
            :text="parentDrop"
            variant="primary"
            class="m-md-2"
          >
            <b-dropdown-item disabled value="0">انتخاب کنید</b-dropdown-item>
            <b-dropdown-item
              v-for="option in options"
              :key="option.value"
              :value="option.value"
              @click="ParentChanged(option)"
            >
              {{ option.text }}
            </b-dropdown-item>
          </b-dropdown>
        </div>
        <div class="col-xxl-4">
          <span>انتخاب تاریخ مجمع :</span>
          <b-dropdown id="dropdown-1" text="تاریخ مجمع" class="m-md-2">
            <b-dropdown-item>مجمع عادی</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item>مجمع عادی به طور فوق العاده</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item>مجمع فوق العاده</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item active>Active action</b-dropdown-item>
            <b-dropdown-item disabled>Disabled action</b-dropdown-item>
          </b-dropdown>
        </div>
        <div class="col-xxl-4">
          <v-btn depressed color="#1A237E">
            نمایش اطلاعات مجمع
          </v-btn>
        </div>
      </div>
    </div>
    <v-divider></v-divider>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "AssemblyDPS",
  props: ["notices"],
  data() {
    return {
      search: "",
      parentDrop: "نوع مجمع",
      DataItems2: [],
      years: [],
      options: [
        {
          text: "مجمع عادی",
          value: "General"
        },
        {
          text: "مجمع عادی به طور فوق العاده",
          value: "GeneralExtra"
        },
        {
          text: "مجمع فوق العاده",
          value: "Extra"
        }
      ],
      ddTestSelectedOption: ""
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    ParentChanged(option) {
      this.ddTestSelectedOption = option.value;
      console.log(this.ddTestSelectedOption);
      this.parentDrop = option.text;
    },
    changeItem: async function() {
      console.log(this.ddTestSelectedOption);
    },
    filteredItems(value) {
      return this.DataItems2.filter(item => {
        // console.log("Value");
        // console.log(value);
        // console.log("Item");
        // console.log(item.ToDate);
        // console.log("Equality");
        // console.log(item.ToDate == value);
        return item.ToDate.normalize("NFC") == value.normalize("NFC");
      });
    },
    populateData() {
      this.DataItems2 = this.notices;
    },
    setYears() {
      let lookup = {};
      let items = this.DataItems2;
      let result = [];
      for (let item, i = 0; (item = items[i++]); ) {
        let name = item.ToDate;

        if (!(name in lookup)) {
          lookup[name] = 1;
          result.push(name);
        }
      }
      result.sort();
      result.reverse();
      let result2 = {};
      let items2 = result;
      let counter = 0;
      for (let item, i = 0; (item = items2[i++]); ) {
        let name = item;
        result2[counter] = name;
        counter += 1;
      }
      this.years = result2;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      // console.log("Watcher");
      this.populateData();
      this.setYears();
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
