<template>
  <div>
    <v-sheet rounded="lg" elevation="6" height="100%">
      <v-tabs
        background-color="#f0efeb"
        color="#4682B4"
        centered
        slider-size="3"
        height="30"
        prev-icon="mdi-arrow-left-bold-box-outline"
        next-icon="mdi-arrow-right-bold-box-outline"
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
          <v-card rounded="lg">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                صورت جریان وجوه نقدی دوره {{ itemPeriod }} ماه منتهی به
                {{ selectedMonth }} - سال مالی {{ itemfiscalYear }}-
                {{ itemReportStatus }}
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-col class="d-flex justify-content-end" cols="3">
                <v-select
                  class="vuetifySelectCustom flex-grow-1"
                  :items="selectedDatesList"
                  v-model="selectedMonth"
                  solo-inverted
                  dense
                ></v-select>
              </v-col>
            </v-toolbar>
            <v-card-text>
              <b-table
                class="CashFlowWidget-table"
                thClass="CashFlowWidget-tableHeader"
                tbody-tr-class="CashFlowWidget-table-row"
                small
                hover
                :items="filteredItems"
                :fields="headersfacility"
              >
                <template #cell(thisPeriod)="data">
                  <span v-if="data.value < 0" style="color:red" dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                  <span v-else-if="data.value === null || data.value == ''"
                    >-</span
                  >
                  <span v-else dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                </template>
                <template #cell(LastYear)="data">
                  <span v-if="data.value < 0" style="color:red" dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                  <span v-else-if="data.value === null || data.value == ''"
                    >-</span
                  >
                  <span v-else dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                </template>
                <template #cell(LastYearThisPeriod)="data">
                  <span v-if="data.value < 0" style="color:red" dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                  <span v-else-if="data.value === null || data.value == ''"
                    >-</span
                  >
                  <span v-else dir="ltr">{{
                    data.value.toLocaleString()
                  }}</span>
                </template>
              </b-table>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-sheet>
  </div>
</template>

<script>
export default {
  props: ["notices"],
  data() {
    return {
      loading: true,
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      headersfacility: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "CashFlowWidget-tableHeader"
        },
        {
          label: "عنوان",
          key: "Item",
          thClass: "CashFlowWidget-tableHeader"
        },
        {
          label: "دوره (میلیون ریال) ",
          key: "thisPeriod",
          thClass: "CashFlowWidget-tableHeader"
        },
        {
          label: " سال مالی گذشته(میلیون ریال) ",
          key: "LastYear",
          thClass: "CashFlowWidget-tableHeader"
        },
        {
          label: "دوره مشابه سال مالی گذشته(میلیون ریال) ",
          key: "LastYearThisPeriod",
          thClass: "CashFlowWidget-tableHeader"
        }
      ]
    };
  },
  computed: {
    itemPeriod() {
      let period = null;
      this.todates.filter(d => {
        if (d.value == this.selectedMonth) period = d.period;
      });
      return period;
    },
    itemfiscalYear() {
      let fiscalYear = null;
      this.todates.filter(d => {
        if (d.value == this.selectedMonth) fiscalYear = d.fiscalYear;
      });
      return fiscalYear;
    },
    itemReportStatus() {
      let reportStatus = null;
      this.todates.filter(d => {
        if (d.value == this.selectedMonth) reportStatus = d.reportStatus;
      });
      return reportStatus;
    },
    selectedDatesList() {
      let items = [];
      for (let item of this.todates) items.push(item.value);

      return items;
    },
    filteredItems() {
      return this.notices.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    }
  },
  methods: {
    gettabs() {
      var lookup = {};
      var lookup2 = {};
      var items = this.notices;
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
      var items = this.notices;
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
      this.selectedMonth = selectedItem;
    },
    GetFilteredYearly(selectedItem) {
      this.selectedYear = selectedItem;
    },
    fillNewestMonth() {
      this.selectedMonth = this.todates[0].value;
      this.selectedYear = this.todatesyears[0].value;
    },
    SetNewPagefirstMonth() {
      this.selectedMonth = this.todates[0].value;
    }
  },

  watch: {
    notices() {
      // this.populateData();
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
.CashFlowWidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-family: "Vazir-Medium-FD";
}
.CashFlowWidget-table /deep/ .CashFlowWidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
}
.CashFlowWidget-table /deep/ .ticker-assembly-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
.vuetifySelectCustom /deep/ .v-input__control {
  min-height: 25px !important;
  height: 25px !important;
}
.vuetifySelectCustom /deep/ .v-input__control {
  font-size: 0.7em !important;
}
.vuetifySelectCustom /deep/ .v-chip.v-size--small {
  border-radius: 3px;
  font-size: 10px;
  height: 17px;
}
.vuetifySelectCustom /deep/ .v-chip .v-chip__close.v-icon {
  font-size: 12px !important;
}
</style>
