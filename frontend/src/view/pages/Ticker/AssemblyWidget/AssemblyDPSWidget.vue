<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        سود نقدی
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column" v-if="loading">
      <v-skeleton-loader
        type=" table-heading, table-thead, table-tbody"
      ></v-skeleton-loader>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="this.DataItems2.length != 0 && loading == false"
    >
      <div v-for="year in years" :key="year.key">
        <v-subheader>
          {{ year }}
        </v-subheader>
        <v-data-table
          v-if="loading == false"
          :headers="headers"
          :items="filteredItems(year)"
          class="elevation-1 FinancialStrength"
          :header-props="{ sortIcon: null }"
          :disable-sort="true"
          hide-default-footer
          disable-pagination
        >
        </v-data-table>
      </div>
    </div>
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
      loading: true,
      inset: true,
      items: [
        {
          action: "mdi-label",
          title: "List item 1"
        },
        {
          divider: true
        },
        {
          action: "mdi-label",
          title: "List item 2"
        },
        {
          divider: true
        },
        {
          action: "mdi-label",
          title: "List item 3"
        }
      ],
      headers: [
        {
          text: "منتهی به",
          value: "ToDate"
        },
        {
          text: "عنوان",
          value: "Title"
        },
        {
          text: "مقدار ریالی",
          value: "Value"
        }
      ],
      DataItems2: [],
      years: [],
      filtered: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    filteredItems(value) {
      return this.DataItems2.filter(item => {
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
      this.populateData();
      this.loading = false;
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
