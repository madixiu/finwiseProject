<template>
  <div>
    <div class="row mr-2 mb-2">
      <v-card width="100%">
        <div class="row">
          <div class="col-xxl-2 col-lg-2 mr-3 mt-3">
            <v-select
              height="8"
              label="بازار"
              v-model="filters.tableMarketSelected"
              :items="filters.tableMarketFilters"
              dense
              outlined
              color="#3dbff0"
              @input="test"
            >
            </v-select>
          </div>
          <!-- <div class="col-2">
            <v-checkbox
              v-model="yesterdayEnableTrigger"
              label="yes"
              color="red"
              hide-details
              @click="TriggerFilteredHeader"
            ></v-checkbox>
          </div>
          <div class="col-2">
            <v-checkbox
              v-model="filters.EPSEnableTrigger"
              label="EPS"
              color="green"
              hide-details
              @click="TriggerFilteredHeader"
            ></v-checkbox>
          </div>
          <div class="col-2">
            <v-checkbox
              v-model="filters.moreInfoTrigger"
              label="اطلاعات حقیقی/حقوقی"
              color="green"
              hide-details
              @click="TriggerFilteredHeader"
            ></v-checkbox>
          </div> -->
          <div class="mt-4">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <!-- type selctor -->
          <div class="col-xxl-5 col-lg-5 mr-2">
            <v-select
              class="motherfucker"
              label="نوع"
              v-model="filters.tableMarketTypeSelected"
              height="10"
              :items="filters.tableMarketTypeFilters"
              :menu-props="{ maxHeight: '200' }"
              deletable-chips
              color="#3dbff0"
              dense
              outlined
              multiple
              small-chips
              @input="test"
            >
            </v-select>
          </div>
          <!-- industry selector -->
          <div class="col-xxl-5 col-lg-5 mr-2 dropdown-rtl">
            <v-select
              class="motherfucker"
              label="صنعت"
              v-model="filters.tableMarketIndustrySelected"
              height="10"
              :items="filters.tableMarketIndustryFilters"
              deletable-chips
              outlined
              dense
              color="#3dbff0"
              small-chips
              multiple
              @input="test"
            >
            </v-select>
          </div>
        </div>
      </v-card>
    </div>

    <!-- table -->
    <div class="row mr-1 mt-1 ml-1">
      <v-card width="100%">
        <b-col lg="4" class="my-1">
          <b-input-group size="sm">
            <b-form-input
              v-model="Tablefilter"
              type="search"
              id="filterInput"
              placeholder="جستجو"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!Tablefilter" @click="Tablefilter = ''"
                >پاک کردن</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-col>
        <b-table
          thClass="marketwatch-table-head"
          class="marketwatch-table"
          tbody-tr-class="marketwatch-table-row"
          striped
          sticky-header
          dense
          :filter="Tablefilter"
          bordered
          outlined
          small
          hover
          responsive
          foot-clone
          :items="tableData"
          :fields="HD"
          @filtered="onFiltered"
        >
          <template #cell(TradeCount)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(TradeVolume)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(TradeValue)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(yesterday)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(last)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(close)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(first)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(low)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(high)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(MinRange)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(MaxRange)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountBuy_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountBuy_Hoguhgi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeBuy_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeBuy_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountSell_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountSell_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeSell_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeSell_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(closePercent)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="marketwatch-table-cell-red"
              >{{ data.value }}%</b
            >
          </template>
          <template #cell(lastPercent)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="marketwatch-table-cell-red"
              >{{ data.value }}%</b
            >
          </template>
        </b-table>
      </v-card>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "marketwatch",
  components: {},
  data() {
    return {
      filters: {
        tableMarketSelected: "همه",
        tableMarketFilters: ["همه", "بورس", "فرابورس"],
        // tableMarketFilters: [
        //   { item: 0, name: "همه" },
        //   { item: 1, name: "بورس" },
        //   { item: 2, name: "فرابورس" }
        // ],
        tableMarketTypeSelected: [],
        tableMarketTypeFilters: [],
        tableMarketIndustrySelected: [],
        tableMarketIndustryFilters: [],
        yesterdayEnableTrigger: false,
        EPSEnableTrigger: false,
        moreInfoTrigger: false
      },
      yesterdayEnableTrigger: false,
      EPSEnableTrigger: false,
      moreInfoTrigger: false,
      WebsocketRequest: false,
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "EPS", value: "EPS" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      Tablefilter: "",
      // tableData: [],
      TypeSearch: "",
      IndustrySearch: "",
      value: [],
      MarketTableHeader: [
        { label: "نماد", key: "ticker", thClass: "marketwatch-table-head" },
        {
          label: "بازار",
          key: "marketName",
          thClass: "marketwatch-table-head"
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "marketwatch-table-head"
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "marketwatch-table-head"
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "marketwatch-table-head"
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "marketwatch-table-head"
        },
        { label: "آخرین قیمت", key: "last", thClass: "marketwatch-table-head" },
        {
          label: "درصد تغییر آخرین قیمت",
          key: "lastPercent",
          thClass: "marketwatch-table-head"
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "marketwatch-table-head"
        },
        {
          label: "درصد تغییر قیمت پایانی",
          key: "closePercent",
          thClass: "marketwatch-table-head"
        },
        // { label: "نام", key: "name" },
        // { label: "صنعت", key: "industry" },
        // { label: "آخرین بروز رسانی", key: "updatedAt" },
        {
          label: "کف مجاز قیمت",
          key: "MinRange",
          thClass: "marketwatch-table-head"
        },
        {
          label: "سقف مجاز قیمت",
          key: "MaxRange",
          thClass: "marketwatch-table-head"
        },
        { label: "EPS", key: "EPS", thClass: "marketwatch-table-head" },
        {
          label: "بالاترین قیمت",
          key: "high",
          thClass: "marketwatch-table-head"
        },
        { label: "کمترین قیمت", key: "low", thClass: "marketwatch-table-head" },
        {
          label: "اولین قیمت",
          key: "first",
          thClass: "marketwatch-table-head"
        },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "marketwatch-table-head"
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "marketwatch-table-head"
        }
      ]
    };
  },
  watch: {
    selectedHeaderOptions() {
      console.log(this.selectedHeaderOptions);
      // this.TriggerFilteredHeader();
    }
  },
  computed: {
    HD() {
      return this.TriggerFilteredHeader();
    },
    //search for selectors
    // criteria() {
    //   // Compute the search criteria
    //   return this.search.trim().toLowerCase();
    // },
    ...mapState({
      tableData: state => state.marketwatch.marketWatchItems
    }),

    // TableFiltered() {
    //   if (
    //     this.filters.tableMarketTypeSelected.length == 0 &&
    //     this.filters.tableMarketIndustrySelected.length == 0
    //   ) {
    //     return this.tableData;
    //   } else if (this.filters.tableMarketIndustrySelected.length == 0) {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (this.filters.tableMarketTypeSelected.includes(obj["Type"])) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   } else if (this.filters.tableMarketTypeSelected.length == 0) {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (
    //         this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
    //       ) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   } else {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (
    //         this.filters.tableMarketTypeSelected.includes(obj["Type"]) &&
    //         this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
    //       ) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   }
    // },
    TypeAvailableOptions() {
      let criteria = this.TypeSearch;
      // Filter out already selected options
      let options = this.filters.tableMarketTypeFilters.filter(
        opt => this.value.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    },
    IndustryAvailableOptions() {
      let criteria = this.IndustrySearch;
      // Filter out already selected options
      let options = this.filters.tableMarketIndustryFilters.filter(
        opt => this.value.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    }

    // searchDesc() {
    //   if (this.criteria && this.availableOptions.length === 0) {
    //     return "There are no tags matching your search criteria";
    //   }
    //   return "";
    // }
  },
  mounted() {
    this.loadData();
    this.TriggerFilteredHeader();
    console.log(this.TableFilteredY());
  },
  methods: {
    setFilterSelected() {
      // this.selectedFilters = [
      //   this.filters.tableMarketSelected,
      //   this.filters.tableMarketTypeSelected,
      //   this.filters.tableMarketIndustrySelected
      // ];
      if (this.WebsocketRequest == true) {
        // this.WebsocketRequest = false
        // this.Stop();
        this.MarketWatchFilterPost();
        // this.liveChecker();
      } else {
        this.MarketWatchFilterPost();
        // this.liveChecker();
      }
    },
    test() {
      console.log("yeah fuck");
      console.log(this.filters.tableMarketSelected);
      this.MarketWatchFilterPost();
      // console.log(this.selectedHeaderOptions);
      // console.log(this.moreInfoTrigger);
    },
    TriggerFilteredHeader() {
      // console.log(this.MarketTableHeader);
      let header = JSON.parse(JSON.stringify(this.MarketTableHeader));
      // let options = [this.filters.yesterdayEnableTrigger,this.filters.EPSEnableTrigger,this.filters.moreInfoTrigger]
      // let options = {
      //   yesterday: this.filters.yesterdayEnableTrigger,
      //   EPS: this.filters.EPSEnableTrigger,
      //   moreInfo: this.filters.moreInfoTrigger
      // };
      let options = this.selectedHeaderOptions;

      let SwCase = 0;
      // if (
      //   this.yesterdayEnableTrigger != true &&
      //   this.filters.EPSEnableTrigger != true &&
      //   this.filters.moreInfoTrigger != true
      // )
      //   SwCase = 0;
      // else if (
      //   this.yesterdayEnableTrigger == true &&
      //   this.filters.EPSEnableTrigger != true &&
      //   this.filters.moreInfoTrigger != true
      // )
      //   SwCase = 1;
      // else if (
      //   this.yesterdayEnableTrigger != true &&
      //   this.filters.EPSEnableTrigger == true &&
      //   this.filters.moreInfoTrigger != true
      // )
      //   SwCase = 2;
      // else if (
      //   this.yesterdayEnableTrigger != true &&
      //   this.filters.EPSEnableTrigger != true &&
      //   this.filters.moreInfoTrigger == true
      // )
      //   SwCase = 3;
      // else if (
      //   this.yesterdayEnableTrigger == true &&
      //   this.filters.EPSEnableTrigger == true &&
      //   this.filters.moreInfoTrigger != true
      // )
      //   SwCase = 4;
      // else if (
      //   this.yesterdayEnableTrigger != true &&
      //   this.filters.EPSEnableTrigger == true &&
      //   this.filters.moreInfoTrigger == true
      // )
      //   SwCase = 5;
      // else if (
      //   this.yesterdayEnableTrigger == true &&
      //   this.filters.EPSEnableTrigger != true &&
      //   this.filters.moreInfoTrigger == true
      // )
      //   SwCase = 6;
      // else if (
      //   this.yesterdayEnableTrigger == true &&
      //   this.filters.EPSEnableTrigger == true &&
      //   this.filters.moreInfoTrigger == true
      // )
      //   SwCase = 7;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
        console.log(options);
        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "EPS") SwCase = 2;
        else if (options[0] == "HH") SwCase = 3;
      } else if (options.length == 2) {
        if (!options.includes("HH")) SwCase = 4;
        else if (!options.includes("yesterday")) SwCase = 5;
        else if (!options.includes("EPS")) SwCase = 6;
      } else if (options.length == 3) SwCase = 7;

      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          header.splice(11, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          header.splice(12, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;

        case 2:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 3:
          header.splice(5, 1);
          header.splice(11, 1);
          break;

        case 4:
          for (let i = 0; i < 8; i++) header.pop();
          break;

        case 5:
          header.splice(5, 1);
          break;

        case 6:
          header.splice(12, 1);
          break;

        case 7:
          break;
        default:
          header.splice(5, 1);
          header.splice(11, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      return header;
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    TableFilteredY() {
      if (
        this.filters.tableMarketTypeSelected.length == 0 &&
        this.filters.tableMarketIndustrySelected.length == 0
      ) {
        return this.tableData;
      } else if (this.filters.tableMarketIndustrySelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (this.filters.tableMarketTypeSelected.includes(obj["Type"])) {
            temp.push(obj);
          }
        }
        return temp;
      } else if (this.filters.tableMarketTypeSelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (
            this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
          ) {
            temp.push(obj);
          }
        }
        return temp;
      } else {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (
            this.filters.tableMarketTypeSelected.includes(obj["Type"]) &&
            this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
          ) {
            temp.push(obj);
          }
        }
        return temp;
      }
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.MarketWatchTableReq().then(response => {
        this.MarketWatchFilterListReq();
      });
    },
    async MarketWatchTableReq() {
      await this.axios
        .get("/api/marketwatch")
        .then(response => {
          // let data = response.data;
          // this.tableData = data;
          this.$store.dispatch("setMarketWatchItems", response.data);
          console.log(this.tableData);
        })
        .catch(error => {
          console.log(error);
        });
      // var cars = new Array();
    },
    async MarketWatchFilterListReq() {
      await this.axios.get("/api/marketwatchfilterlists").then(response => {
        this.filters.tableMarketTypeFilters = response.data[0];
        this.filters.tableMarketIndustryFilters = response.data[1];
        // console.log(response.data);
        // let data = response.data[0];
        // let test = this.tableData[0].includes(data[0]);
        // for (let obj of this.tableData) {
        //   if (obj["Type"] == data[0]) console.log(obj);
        // }
      });
    },
    MarketWatchFilterPost() {
      this.axios({
        method: "post",
        url: "/api/marketwatch",
        data: {
          marketName: this.filters.tableMarketSelected,
          marketType: this.filters.tableMarketTypeSelected,
          marketIndustry: this.filters.tableMarketIndustrySelected
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          // console.log(response.data);
          this.$store.dispatch("setMarketWatchItems", response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    onOptionClick({ option, addTag }) {
      addTag(option);
      this.search = "";
    }
  }
};
</script>
<style>
.form-input-class {
  direction: rtl;
}
.form-tag-class {
  direction: rtl !important;
}
.dropdown-rtl {
  text-align: right !important;
  direction: rtl;
}
.marketwatch-table-head {
  background-color: #f2f2f2;
  vertical-align: middle !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important ;
}
.marketwatch-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8rem !important;
  line-height: 1 !important;
}
.marketwatch-table-row:hover {
  background-color: #999999 !important;
}
.marketwatch-table-cell {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
}
.marketwatch-table-cell-green {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: green;
  font-weight: 400;
}
.marketwatch-table-cell-red {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: red;
  font-weight: 400;
}
.marketwatch-table-cell-bold {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 600;
}
.marketwatch-table-row {
  direction: ltr;
  vertical-align: middle !important;
}

.motherfucker .v-text-field--box .v-input__slot,
.v-text-field--outlined .v-input__slot {
  min-height: 25px !important;
  max-height: 50px;
  display: flex !important;
  align-items: center !important;
  font-size: 0.8rem !important;
}
.motherfucker .v-chip.v-size--small {
  border-radius: 19px !important;
  font-size: 0.8rem !important;
  height: 19px !important;
  background-color: "#3dbff0";
}
</style>
