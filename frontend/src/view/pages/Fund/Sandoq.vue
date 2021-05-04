<template>
  <!-- <ErrorMine></ErrorMine> -->
  <div>
    <!-- table -->
    <div class="row mr-1 ml-1">
      <v-card width="100%">
        <div id="FundsFilterRow2" class="row">
          <div class="col-xxl-4 col-lg-4  col-md-8 col-sm-12 mr-3 mt-1">
            <b-input-group size="sm">
              <b-form-input
                v-model="Tablefilter"
                type="search"
                id="filterInput"
                placeholder="فیلتر"
              ></b-form-input>
              <b-input-group-append>
                <b-button :disabled="!Tablefilter" @click="Tablefilter = ''"
                  >پاک کردن</b-button
                >
              </b-input-group-append>
            </b-input-group>
          </div>
          <div class="col-xxl-4 col-lg-4 col-md-8 col-sm-12 mt-1">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div>
        </div>

        <b-table
          thClass="Funds-table-head"
          class="Funds-table"
          tbody-tr-class="Funds-table-row"
          striped
          :busy.sync="isBusy"
          :sticky-header="height"
          dense
          :filter="Tablefilter"
          :filter-included-fields="filterOn"
          :sort-desc.sync="sortDesc"
          :sort-by.sync="sortBy"
          sort-direction="desc"
          sort-icon-left
          bordered
          no-border-collapse
          outlined
          small
          hover
          responsive
          :items="tableData"
          :fields="HD"
          @filtered="onFiltered"
        >
          <template #table-busy>
            <div class="text-center text-danger my-2">
              <b-spinner class="align-middle mr-2"></b-spinner>
              <strong>شکیبا باشید</strong>
            </div>
          </template>
          <template #cell(ticker)="data">
            <b class="Funds-table-cell-bold" @click="tickerClick(data)">{{
              data.value
            }}</b>
          </template>
          <template #cell(TradeCount)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(TradeVolume)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(TradeValue)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(yesterday)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(last)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(close)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(first)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(low)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(high)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(MinRange)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(MaxRange)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(EPS)="data">
            <b v-if="data.value == 'NaN'" class="Funds-table-cell">
              {{ "-" }}</b
            >
            <b v-else class="Funds-table-cell">
              {{ data.value.toLocaleString() }}</b
            >
          </template>
          <template #cell(CountBuy_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountBuy_Hoguhgi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeBuy_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeBuy_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountSell_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(CountSell_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeSell_Haghighi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(VolumeSell_Hoghughi)="data">
            <b class="Funds-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(closePercent)="data">
            <b v-if="data.value > 0" class="Funds-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="Funds-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="Funds-table-cell"
              >{{ data.value }}%</b
            >
          </template>
          <template #cell(lastPercent)="data">
            <b v-if="data.value > 0" class="Funds-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="Funds-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="Funds-table-cell"
              >{{ data.value }}%</b
            >
          </template>
        </b-table>
      </v-card>
    </div>
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-//6.vue";
export default {
  name: "Funds",
  data() {
    return {
      height: "470px",
      WebsocketRequest: false,
      isBusy: true,
      sortDesc: false,
      filterOn: ["ticker"],
      tableData: null,
      sortBy: "ticker",
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      Tablefilter: "",
      TypeSearch: "",
      FundsTableHeader: [
        {
          label: "نماد",
          key: "ticker",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "بازار",
          key: "marketName",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "درصد آخرین قیمت",
          key: "lastPercent",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "درصد قیمت پایانی",
          key: "closePercent",
          thClass: "Funds-table-head",
          sortable: true
        },
        // { label: "نام", key: "name" },
        // { label: "صنعت", key: "industry" },
        // { label: "آخرین بروز رسانی", key: "updatedAt" },
        // {
        //   label: "کف مجاز قیمت",
        //   key: "MinRange",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "سقف مجاز قیمت",
        //   key: "MaxRange",
        //   thClass: "Funds-table-head"
        // },
        // // { label: "EPS", key: "EPS", thClass: "Funds-table-head" },
        // {
        //   label: "بالاترین قیمت",
        //   key: "high",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "کمترین قیمت",
        //   key: "low",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        // {
        //   label: "اولین قیمت",
        //   key: "first",
        //   thClass: "Funds-table-head",
        //   sortable: true
        // },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "Funds-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "Funds-table-head",
          sortable: true
        }
      ]
    };
  }, created() {
    document.title = "Finwise - صندوق";
  },
  mounted() {
    this.loadData();
    this.height = this.getHeight();
    this.liveChecker();
    this.$socketSandoq.onmessage = data => {
      // this.tableData = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData = JSON.parse(data.data);
    };
  },
  computed: {
    HD() {
      return this.TriggerFilteredHeader();
    }
  },
  methods: {
    getHeight() {
      return (window.innerHeight - 150).toString() + "px";
    },
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/Funds")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData = data;
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.FundsTableHeader));
      let options = this.selectedHeaderOptions;
      let SwCase = 0;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "HH") SwCase = 2;
      } else if (options.length == 2) SwCase = 3;

      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 2:
          header.splice(5, 1);
          break;
        case 3:
          break;
        default:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      return header;
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketSandoq.send(JSON.stringify(barier));
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (
        date.getHours() > 8 &&
        date.getHours() < 14 &&
        date.getDay() != 5 &&
        date.getDay() != 4
      ) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketSandoq.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.Funds-table-head {
  /* background-color: #e01313; */
  vertical-align: middle !important;
  font-size: 1.1em !important;
  font-weight: 600 !important ;
}
.Funds-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8em !important;
  line-height: 1 !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-row:hover {
  background-color: #999999 !important;
}
.Funds-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-cell-green {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-cell-red {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
  vertical-align: middle !important;
}
.Funds-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.Funds-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
</style>
