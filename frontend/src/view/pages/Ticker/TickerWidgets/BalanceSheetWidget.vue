<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        ترازنامه
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading"
        ></b-spinner>
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div
      class="card-body d-flex flex-column"
      v-if="this.notices != '' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
        color="#FFF"
        dark
        prev-icon="mdi-arrow-right-bold-box-outline"
        next-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
        <v-tab
          v-for="item in this.todatesyears"
          :key="item.key"
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-tabs
            vertical
            background-color="#1A237E"
            color="#FFF"
            dark
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
          >
            <v-tab
              v-for="item in todates"
              :key="item.key"
              @click="GetFiltered(item.value)"
            >
              {{ item.value }}
            </v-tab>
            <v-tab-item v-for="itemR in todates" :key="itemR.key">
              <div class="card-header border-0">
                <h3 class="card-title font-weight-bolder FinancialStrength">
                  ترازنامه دوره {{ itemR.period }} ماه منتهی به
                  {{ itemR.value }} - سال مالی {{ itemR.fiscalYear }}
                </h3>
              </div>
              <div class="row">
                <div class="col-xxl-6">
                  <div class="card-body d-flex flex-column">
                    <div class="card-header border-0">
                      <h4
                        class="card-title font-weight-bolder FinancialStrength"
                      >
                        دارایی
                      </h4>
                    </div>
                    <v-data-table
                      :headers="headersfacility"
                      :items="filteredItems"
                      class="elevation-1 FinancialStrength"
                      :header-props="{ sortIcon: null }"
                      :disable-sort="true"
                      hide-default-footer
                      disable-pagination
                    >
                    </v-data-table>
                  </div>
                </div>
                <div class="col-xxl-6">
                  <div class="card-body d-flex flex-column">
                    <div class="card-header border-0">
                      <h4
                        class="card-title font-weight-bolder FinancialStrength"
                      >
                        بدهی
                      </h4>
                    </div>
                    <v-data-table
                      :headers="headersfacility"
                      :items="filteredItems2"
                      class="elevation-1 FinancialStrength"
                      :header-props="{ sortIcon: null }"
                      :disable-sort="true"
                      hide-default-footer
                      disable-pagination
                    >
                    </v-data-table>
                  </div>
                  <div class="card-body d-flex flex-column">
                    <div class="card-header border-0">
                      <h4
                        class="card-title font-weight-bolder FinancialStrength"
                      >
                        حقوق صاحبان سهام
                      </h4>
                    </div>
                    <v-data-table
                      :headers="headersfacility"
                      :items="filteredItems3"
                      class="elevation-1 FinancialStrength"
                      :header-props="{ sortIcon: null }"
                      :disable-sort="true"
                      hide-default-footer
                      disable-pagination
                    >
                    </v-data-table>
                  </div>
                </div>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="this.notices == '' && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "BalanceSheetWidget",
  props: ["notices"],
  data() {
    return {
      search: "",
      loading: true,
      type: "",
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      headersfacility: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "عنوان",
          value: "Translated"
        },
        {
          text: "دوره (میلیون ریال) ",
          value: "thisPeriod"
        },
        {
          text: "دوره مشابه سال مالی گذشته(میلیون ریال) ",
          value: "lastYear"
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      return this.DataItems2.filter(item => {
        return (item.toDate == this.selectedMonth) & (item.type == "Asset");
      });
    },
    filteredItems2() {
      return this.DataItems2.filter(item => {
        return (item.toDate == this.selectedMonth) & (item.type == "Liability");
      });
    },
    filteredItems3() {
      return this.DataItems2.filter(item => {
        return (item.toDate == this.selectedMonth) & (item.type == "Equity");
      });
    }
  },
  methods: {
    populateData() {
      this.DataItems2 = this.notices;
      //   console.log(this.DataItems2);
    },
    gettabs() {
      var lookup = {};
      var lookup2 = {};
      var items = this.DataItems2;
      var result = [];
      var result2 = [];
      var counter = 0;
      for (var item, i = 0; (item = items[i++]); ) {
        var name = item.toDate;
        if (!(name in lookup)) {
          lookup[name] = 1;
          var itemOne = {};
          itemOne["key"] = counter;
          itemOne["value"] = name;
          itemOne["period"] = item.period;
          itemOne["fiscalYear"] = item.fiscalYear;
          result.push(itemOne);
          counter += 1;
        }
        if (!(name.split("/")[0] in lookup2)) {
          lookup2[name.split("/")[0]] = 1;
          var itemTwo = {};
          itemTwo["key"] = counter;
          itemTwo["value"] = name.split("/")[0];
          itemOne["period"] = item.period;
          itemOne["fiscalYear"] = item.fiscalYear;
          result2.push(itemTwo);
          counter += 1;
        }
      }

      this.todates = result;
      console.log(this.todates);
      this.todatesyears = result2;
      this.fillNewestMonth();
    },
    getOnesfromthisyear() {
      var lookup = {};
      var items = this.DataItems2;
      var result = [];
      var counter = 0;
      for (var item, i = 0; (item = items[i++]); ) {
        var name = item.toDate;
        if (name.split("/")[0] == this.selectedYear && !(name in lookup)) {
          lookup[name] = 1;
          var itemOne = {};
          itemOne["key"] = counter;
          itemOne["value"] = name;
          itemOne["period"] = item.period;
          itemOne["fiscalYear"] = item.fiscalYear;
          result.push(itemOne);
          counter += 1;
        }
      }
      this.todates = result;
      // console.log(result);
      // console.log(this.selectedYear);
    },
    GetFiltered(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.selectedMonth = selectedItem;
    },
    GetFilteredYearly(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });

      this.selectedYear = selectedItem;
    },
    fillNewestMonth() {
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      this.selectedYear = this.todatesyears[0].value;
    },
    SetNewPagefirstMonth() {
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      // this.selectedYear = this.todatesyears[0].value;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      //   console.log("Watcher");
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
      //   console.log(this.notices);
    },
    selectedYear: function() {
      this.getOnesfromthisyear();
      this.SetNewPagefirstMonth();
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
.itemFilters {
  font-family: "Dirooz FD";
  font-weight: 700;
  font-size: 1em;
}
table.v-table tbody td {
  font-family: "Dirooz FD" !important;
}
</style>
