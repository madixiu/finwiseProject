<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        صورت جریان وجوه نقد
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
        background-color="#212529"
        color="#FFF"
        dark
        prev-icon="mdi-arrow-right-bold-box-outline"
        next-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
        <v-tab
          v-for="item in this.todatesyears"
          :key="item.key"
          class="itemFilters"
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-tabs
            vertical
            background-color="#212529"
            color="#FFF"
            dark
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
          >
            <v-tab
              v-for="item in todates"
              :key="item.key"
              class="itemFilters"
              @click="GetFiltered(item.value)"
            >
              {{ item.value }}
            </v-tab>
            <v-tab-item v-for="itemR in todates" :key="itemR.key">
              <div class="card-header border-0">
                <h4 class="card-title cellItem FinancialStrength">
                  صورت جریان وجوه نقدی دوره {{ itemR.period }} ماه منتهی به
                  {{ itemR.value }} - سال مالی {{ itemR.fiscalYear }}-
                  {{ itemR.reportStatus }}
                </h4>
              </div>
              <div class="row">
                <div class="col-xxl-12">
                  <div class="card-body d-flex flex-column">
                    <v-data-table
                      :headers="headersfacility"
                      :items="filteredItems"
                      class="elevation-1 FinancialStrength"
                      :header-props="{ sortIcon: null }"
                      :disable-sort="true"
                      hide-default-footer
                      disable-pagination
                    >
                      <template v-slot:[`item.toDate`]="{ item }">
                        <span class="cellItem">{{ item.toDate }} </span>
                      </template>
                      <template v-slot:[`item.Item`]="{ item }">
                        <span class="cellItem">{{ item.Item }} </span>
                      </template>
                      <template v-slot:[`item.lastYear`]="{ item }">
                        <span
                          class="cellItem"
                          v-bind:class="[
                            item.lastYear > 0
                              ? 'ltr_aligned'
                              : 'redItem ltr_aligned'
                          ]"
                          >{{ numberWithCommas(item.lastYear) }}
                        </span>
                      </template>
                      <template v-slot:[`item.thisPeriod`]="{ item }">
                        <span
                          class="cellItem"
                          v-bind:class="[
                            item.thisPeriod > 0
                              ? 'ltr_aligned'
                              : 'redItem ltr_aligned'
                          ]"
                          >{{ numberWithCommas(item.thisPeriod) }}
                        </span>
                      </template>
                      <template v-slot:[`item.LastYear`]="{ item }">
                        <span
                          class="cellItem"
                          v-bind:class="[
                            item.LastYear > 0
                              ? 'ltr_aligned'
                              : 'redItem ltr_aligned'
                          ]"
                          >{{ numberWithCommas(item.LastYear) }}
                        </span>
                      </template>
                      <template v-slot:[`item.LastYearThisPeriod`]="{ item }">
                        <span
                          class="cellItem"
                          v-bind:class="[
                            item.LastYearThisPeriod > 0
                              ? 'ltr_aligned'
                              : 'redItem ltr_aligned'
                          ]"
                          >{{ numberWithCommas(item.LastYearThisPeriod) }}
                        </span>
                      </template>
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
          value: "Item"
        },
        {
          text: "دوره (میلیون ریال) ",
          value: "thisPeriod"
        },
        {
          text: " سال مالی گذشته(میلیون ریال) ",
          value: "LastYear"
        },
        {
          text: "دوره مشابه سال مالی گذشته(میلیون ریال) ",
          value: "LastYearThisPeriod"
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      return this.DataItems2.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    }
  },
  methods: {
    numberWithCommas(x) {
      if (x === null) {
        return "-";
      }
      if (x == 0) {
        return "-";
      }
      if (x == "") {
        return "-";
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    },
    populateData() {
      this.DataItems2 = this.notices;

      this.loading = false;
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
          itemOne["reportStatus"] = item.reportStatus;
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
          itemOne["reportStatus"] = item.reportStatus;
          result2.push(itemTwo);
          counter += 1;
        }
      }

      this.todates = result;
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
          itemOne["reportStatus"] = item.reportStatus;
          result.push(itemOne);
          counter += 1;
        }
      }
      this.todates = result;
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
      this.selectedMonth = this.todates[0].value;
      this.selectedYear = this.todatesyears[0].value;
    },
    SetNewPagefirstMonth() {
      this.selectedMonth = this.todates[0].value;
      // this.selectedYear = this.todatesyears[0].value;
    }
  },
  mounted() {
    // this.populateData();
  },
  watch: {
    notices() {
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
    },
    selectedYear: function() {
      this.getOnesfromthisyear();
      this.SetNewPagefirstMonth();
    }
  }
};
</script>
<style scoped>
.cellItem {
  font-family: "Vazir-Light-FD";
  font-weight: 700;
}
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
  font-family: "Vazir-Light-FD";
  font-weight: 700;
  font-size: 1em;
}
table.v-table tbody td {
  font-family: "Vazir-Light-FD" !important;
}
</style>
