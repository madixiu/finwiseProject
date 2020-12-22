<template>
  <div>
    <div class="row mr-2 mb-2">
      <v-card width="100%">
        <div class="row">
          <div class="col-xxl-2 col-lg-2 mr-2 mt-2">
            <b-form-select
              v-model="filters.tableMarketSelected"
              :options="filters.tableMarketFilters"
              value-field="item"
              text-field="name"
              @change="MarketWatchFilterPost()"
            >
              <!-- <template #first>
                <b-form-select-option :value="همه">همه</b-form-select-option>
              </template> -->
            </b-form-select>
          </div>
          <!-- <div class="col-xxl-2 col-lg-2 mr-2 mt-2"> -->
          <!-- <b-form-checkbox
              id="checkbox-1"
              v-model="yesterdayEnableTrigger"
              name="checkbox-1"
              value="true"
              unchecked-value="false"
              size="lg"
            >
              <span style="font-size: 1rem"> قیمت دیروز </span>
            </b-form-checkbox> -->
          <!-- </div> -->
          <!-- <div class="col-xxl-2 col-lg-2 mr-2 mt-2"> -->
          <!-- <b-form-checkbox
              id="checkbox-2"
              v-model="EPSEnableTrigger"
              name="checkbox-2"
              value="true"
              unchecked-value="false"
              size="lg"
            >
              <span style="font-size: 1rem">EPS</span>
            </b-form-checkbox> -->
          <!-- </div> -->
          <!-- <div class="col-xxl-2 col-lg-2 mr-2 mt-2">
            <b-form-checkbox
              id="checkbox-3"
              v-model="moreInfoTrigger"
              name="checkbox-3"
              value="true"
              unchecked-value="false"
              size="lg"
              @change="test"
            >
              <span style="font-size: 1rem"> اطلاعات حقیقی/حقوقی</span>
            </b-form-checkbox>
          </div> -->
          <div>
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
          <div class="col-xxl-5 col-lg-5 mr-2 dropdown-rtl">
            <b-form-group label="نوع" label-for="tags-with-dropdown">
              <b-form-tags
                id="tags-with-dropdown"
                tag-class="form-tag-class"
                v-model="filters.tableMarketTypeSelected"
                no-outer-focus
                class="mb-2"
                @change="MarketWatchFilterPost()"
              >
                <template v-slot="{ tags, disabled, addTag, removeTag }">
                  <ul
                    v-if="tags.length > 0"
                    class="list-inline d-inline-block mb-2"
                  >
                    <li v-for="tag in tags" :key="tag" class="list-inline-item">
                      <b-form-tag
                        @remove="removeTag(tag)"
                        :title="tag"
                        :disabled="disabled"
                        variant="info"
                        >{{ tag }}</b-form-tag
                      >
                    </li>
                  </ul>

                  <b-dropdown
                    size="sm"
                    variant="outline-secondary"
                    block
                    boundary="viewport"
                    menu-class="w-100 dropdown-rtl"
                  >
                    <template #button-content>
                      <b-icon icon="tag-fill"></b-icon>نوع
                    </template>
                    <b-dropdown-form @submit.stop.prevent="() => {}">
                      <b-form-group
                        label="Search tags"
                        label-for="tag-search-input"
                        label-cols-md="auto"
                        class="mb-0"
                        label-size="sm"
                        :disabled="disabled"
                      >
                        <b-form-input
                          v-model="TypeSearch"
                          id="tag-search-input"
                          input-class="form-input-class"
                          type="search"
                          size="sm"
                          autocomplete="off"
                        ></b-form-input>
                      </b-form-group>
                    </b-dropdown-form>
                    <b-dropdown-divider></b-dropdown-divider>
                    <b-dropdown-item-button
                      v-for="option in TypeAvailableOptions"
                      :key="option"
                      @click="
                        onOptionClick({ option, addTag });
                      "
                    >
                      {{ option }}
                    </b-dropdown-item-button>
                    <b-dropdown-text v-if="TypeAvailableOptions.length === 0">
                      There are no tags available to select
                    </b-dropdown-text>
                  </b-dropdown>
                </template>
              </b-form-tags>
            </b-form-group>
          </div>
          <!-- industry selector -->
          <div class="col-xxl-5 col-lg-5 mr-2 dropdown-rtl">
            <b-form-group label="صنعت" label-for="tags-with-dropdown">
              <b-form-tags
                id="tags-with-dropdown"
                tag-class="form-tag-class"
                v-model="filters.tableMarketIndustrySelected"
                no-outer-focus
                class="mb-2"
              >
                <template v-slot="{ tags, disabled, addTag, removeTag }">
                  <ul
                    v-if="tags.length > 0"
                    class="list-inline d-inline-block mb-2"
                  >
                    <li v-for="tag in tags" :key="tag" class="list-inline-item">
                      <b-form-tag
                        @remove="removeTag(tag)"
                        :title="tag"
                        :disabled="disabled"
                        variant="info"
                        >{{ tag }}</b-form-tag
                      >
                    </li>
                  </ul>
                  <b-dropdown
                    size="sm"
                    variant="outline-secondary"
                    block
                    menu-class="w-100 dropdown-rtl"
                  >
                    <template #button-content>
                      <b-icon icon="tag-fill"></b-icon>صنعت
                    </template>
                    <b-dropdown-form @submit.stop.prevent="() => {}">
                      <b-form-group
                        label="Search tags"
                        label-for="tag-search-input"
                        label-cols-md="auto"
                        class="mb-0"
                        label-size="sm"
                        :disabled="disabled"
                      >
                        <b-form-input
                          v-model="IndustrySearch"
                          id="tag-search-input"
                          input-class="form-input-class"
                          type="search"
                          size="sm"
                          autocomplete="off"
                        ></b-form-input>
                      </b-form-group>
                    </b-dropdown-form>
                    <b-dropdown-divider></b-dropdown-divider>
                    <b-dropdown-item-button
                      v-for="option in IndustryAvailableOptions"
                      :key="option"
                      @click="
                        onOptionClick({ option, addTag });
                        MarketWatchFilterPost();
                      "
                    >
                      {{ option }}
                    </b-dropdown-item-button>
                    <b-dropdown-text
                      v-if="IndustryAvailableOptions.length === 0"
                    >
                      There are no tags available to select
                    </b-dropdown-text>
                  </b-dropdown>
                </template>
              </b-form-tags>
            </b-form-group>
          </div>
        </div>
      </v-card>
    </div>
    <!-- <div class="row mt-2">
   
    </div> -->
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
          <!-- <template #cell(Nemad)="data">
            <b class="marketwatch-table-cell-bold">{{ data.value }}</b>
          </template>
          <template #cell(UnderLying)="data">
            <b class="marketwatch-table-cell-bold">{{ data.value }}</b>
          </template>
          <template #cell(StrikePrice)="data">
            <b class="marketwatch-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>

          <template #cell(AssetPrice)="data">
            <b class="marketwatch-table-cell">{{ data.value.toLocaleString() }}</b>
          </template>
          <template #cell(DifferenceToAverage)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green">{{
              data.value
            }}</b>
            <b v-if="data.value < 0" class="marketwatch-table-cell-red">{{
              data.value
            }}</b>
          </template>
          <template #cell(PPP)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green">{{
              data.value.toLocaleString()
            }}</b>
            <b v-if="data.value < 0" class="marketwatch-table-cell-red">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(ArzandegiLast)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green">{{
              data.value.toLocaleString()
            }}</b>
            <b v-if="data.value < 0" class="marketwatch-table-cell-red">{{
              data.value.toLocaleString()
            }}</b>
            <b v-if="data.value == 0" class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template> -->
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
        tableMarketSelected: 0,
        // tableMarketFilters: ["همه", "بورس", "فرابورس"],
        tableMarketFilters: [
          { item: 0, name: "همه" },
          { item: 1, name: "بورس" },
          { item: 2, name: "فرابورس" }
        ],
        tableMarketTypeSelected: [],
        tableMarketTypeFilters: [],
        tableMarketIndustrySelected: [],
        tableMarketIndustryFilters: []
      },
      yesterdayEnableTrigger: "false",
      EPSEnableTrigger: "false",
      moreInfoTrigger: "false",
      selectedHeaderOptions: [],
      HeaderOptionsPattern: [],
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
        { label: "نام", key: "name" },
        { label: "صنعت", key: "industry" },
        { label: "بازار", key: "marketName" },
        { label: "آخرین بروز رسانی", key: "updatedAt" },
        { label: "کف مجاز قیمت", key: "MinRange" },
        { label: "سقف مجاز قیمت", key: "MaxRange" },
        { label: "EPS", key: "EPS" },
        { label: "حجم معاملات", key: "TradeVolume" },
        { label: "ارزش معاملات", key: "TradeValue" },
        { label: "تعداد معاملات", key: "TradeCount" },
        { label: "قیمت دیروز", key: "yesterday" },
        { label: "بالاترین قیمت", key: "high" },
        { label: "کمترین قیمت", key: "low" },
        { label: "آخرین قیمت", key: "last" },
        { label: "قیمت پایانی", key: "close" },
        { label: "اولین قیمت", key: "first" },
        { label: "تعداد خرید حقیقی", key: "CountBuy_Haghighi" },
        { label: "تعداد خرید حقوقی", key: "CountBuy_Hoguhgi" },
        { label: "حجم خرید حقیقی", key: "VolumeBuy_Haghighi" },
        { label: "حجم خرید حقوقی", key: "VolumeBuy_Hoghughi" },
        { label: "تعداد فروش حقیقی", key: "CountSell_Haghighi" },
        { label: "تعداد فروش حقوقی", key: "CountSell_Hoghughi" },
        { label: "حجم فروش حقیقی", key: "VolumeSell_Haghighi" },
        { label: "حجم فروش حقوقی", key: "VolumeSell_Hoghughi" }
      ],
      filteredHeader: []
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

    TableFiltered() {
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
    test() {
      console.log("yeah fuck");
      console.log(this.filters);
      // console.log(this.selectedHeaderOptions);
      // console.log(this.moreInfoTrigger);
    },
    TriggerFilteredHeader() {
      console.log(this.MarketTableHeader);
      // console.log(this.filteredHeader);
      let header = JSON.parse(JSON.stringify(this.MarketTableHeader));
      let options = this.selectedHeaderOptions;
      console.log(options.length);

      // let header = this.MarketTableHeader;
      let SwCase = 0;
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
          header.splice(7, 1);
          header.splice(10, 1);
          for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
          break;
        case 1:
          header.splice(7, 1);
          for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
          break;

        case 2:
          header.splice(11, 1);
          for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
          break;
        case 3:
          header.splice(7, 1);
          header.splice(10, 1);
          //this.filteredHeader = header;
          break;

        case 4:
          for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
          break;

        case 5:
          header.splice(11, 1);
          // for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
          break;

        case 6:
          header.splice(7, 1);

          //this.filteredHeader = header;
          break;

        case 7:
          //this.filteredHeader = header;
          break;
        default:
          header.splice(7, 1);
          header.splice(10, 1);
          for (let i = 0; i < 8; i++) header.pop();
          //this.filteredHeader = header;
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
    async MarketWatchFilterPost() {
      await this.axios({
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
          console.log(response.data);
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
  vertical-align: middle !important;
  font-size: 0.8rem !important;
  font-weight: 500 !important ;
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
</style>
