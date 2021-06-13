<template>
  <div>
    <!-- <div class="row mr-2 mb-1">
      <v-card width="100%">
 
      </v-card>
    </div> -->

    <!-- table -->
    <div class="row mr-1 ml-1">
      <v-card width="100%">
        <!-- <v-toolbar dense>
          <v-col></v-col>
          <v-spacer></v-spacer>
          <v-col cols="1">
            <span>بازار</span>
          </v-col>
          <v-col cols="2">
            <b-form-select
              class=""
              label="بازار"
              v-model="tableMarketSelected"
              :options="tableMarketFilters"
              @input="test"
            ></b-form-select>
          </v-col>
          <v-col cols="1">
            <span>صنعت</span>
          </v-col>
          <v-col cols="6" class="">
            <v-select
              style="height: 30px !important;font: size 0.8em;"
              v-model="valuesss"
              :items="itemsss"
              label="صنعت"
              multiple
              outlined
              dense
              clearable
              deletable-chips
              chips
            >
              <template v-slot:selection="{ item, index }">
                <v-chip v-if="index === 0" color="#1867c0" label outlined small>
                  <span>{{ item }}</span>
                </v-chip>
                <span
                  v-if="index === 1"
                  class="grey--text text-caption"
                  style="font-family:'Vazir-Medium-FD'"
                >
                  (+{{ valuesss.length - 1 }} صنعت دیگر)
                </span>
              </template>
            </v-select>
          </v-col>
        </v-toolbar> -->
        <!-- <div id="marketwatchFilterRow1" class="row">
          <div
            class="col-xxl-1 col-lg-1 col-md-6 col-sm-12 mr-1 mt-1 dropdown-rtl"
          >
            <span style="font-size:0.9em">بازار</span>
            <b-form-select
              label="بازار"
              v-model="tableMarketSelected"
              :options="tableMarketFilters"
              @input="test"
            ></b-form-select>
          </div> -->
        <!-- <div class="row"> -->
        <!-- type selctor -->
        <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
        <!-- <div class="col-xxl-3 col-lg-3  dropdown-rtl">
            <div>
              <b-form-group label="نوع" label-for="tags-with-dropdown">
                <b-form-tags
                  id="tags-with-dropdown"
                  v-model="tableMarketTypeSelected"
                  no-outer-focus
                  class=""
                  @input="test"
                >
                  <template v-slot="{ tags, disabled, addTag, removeTag }">
                    <ul
                      v-if="tags.length > 0"
                      class="list-inline d-inline-block mb-2"
                    >
                      <li
                        v-for="tag in tags"
                        :key="tag"
                        class="list-inline-item"
                      >
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
                      menu-class="w-100"
                    >
                      <template #button-content>
                        <b-icon icon="tag-fill"></b-icon> انتخاب
                      </template>
                      <b-dropdown-form @submit.stop.prevent="() => {}">
                        <b-form-group
                          label="جستجو"
                          label-for="tag-search-input"
                          label-cols-md="auto"
                          class="mb-0"
                          label-size="sm"
                          :description="searchDescType"
                          :disabled="disabled"
                        >
                          <b-form-input
                            v-model="TypeSearch"
                            id="tag-search-input"
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
                        @click="TypeonOptionClick({ option, addTag })"
                      >
                        {{ option }}
                      </b-dropdown-item-button>
                      <b-dropdown-text v-if="TypeAvailableOptions.length === 0">
                        موردی یافت نشد
                      </b-dropdown-text>
                    </b-dropdown>
                  </template>
                </b-form-tags>
              </b-form-group>
            </div>
          </div> -->
        <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
        <!-- industry selector -->
        <!-- <div class="col-xxl-3 col-lg-3 col-md-6 col-sm-12 dropdown-rtl">
            <div>
              <b-form-group label="صنعت" label-for="tags-with-dropdown">
                <b-form-tags
                  id="tags-with-dropdown"
                  v-model="tableMarketIndustrySelected"
                  no-outer-focus
                  class=""
                  @input="test"
                >
                  <template v-slot="{ tags, disabled, addTag, removeTag }">
                    <ul
                      v-if="tags.length > 0"
                      class="list-inline d-inline-block mb-2"
                    >
                      <li
                        v-for="tag in tags"
                        :key="tag"
                        class="list-inline-item"
                      >
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
                      menu-class="w-100"
                    >
                      <template #button-content>
                        <b-icon icon="tag-fill"></b-icon> انتخاب
                      </template>
                      <b-dropdown-form @submit.stop.prevent="() => {}">
                        <b-form-group
                          label="جستجو"
                          label-for="tag-search-input"
                          label-cols-md="auto"
                          class="mb-0"
                          label-size="sm"
                          :description="searchDescIndustry"
                          :disabled="disabled"
                        >
                          <b-form-input
                            v-model="IndustrySearch"
                            id="tag-search-input"
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
                        @click="IndustryonOptionClick({ option, addTag })"
                      >
                        {{ option }}
                      </b-dropdown-item-button>
                      <b-dropdown-text
                        v-if="IndustryAvailableOptions.length === 0"
                      >
                        موردی یافت نشد
                      </b-dropdown-text>
                    </b-dropdown>
                  </template>
                </b-form-tags>
              </b-form-group>
            </div>
          </div> -->
        <!-- END OF SANNNAT  -->
        <!-- </div> -->
        <div id="marketwatchFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-3 col-lg-3 col-md-6 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-form-input
                v-model="Tablefilter"
                type="search"
                id="filterInput"
                placeholder="فیلتر"
                @keyup="onQuickFilterChanged"
              ></b-form-input>
              <b-input-group-append>
                <b-button :disabled="!Tablefilter" @click="Tablefilter = ''"
                  >پاک کردن</b-button
                >
              </b-input-group-append>
            </b-input-group>
          </div>
          <!-- <div class="col-xxl-4 col-lg-4 col-md-8 col-sm-12 mt-1">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div> -->
        </div>
        <ag-grid-vue
          :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
          :columnDefs="MarketWatchHeader"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
          :cacheQuickFilter="true"
          :sideBar="sideBar"
          :enableRtl="true"
          :gridOptions="gridOptions"
          @grid-ready="onReady"
          @gridColumnsChanged="gridColumnsChanged"
          :localeText="localeText"
          :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
        >
        </ag-grid-vue>
        <!-- <b-table
          thClass="marketwatch-table-head"
          head-variant="secondary"
          class="marketwatch-table"
          tbody-tr-class="marketwatch-table-row"
          striped
          :busy.sync="isBusy"
          :sticky-header="height"
          dense
          :filter="Tablefilter"
          :filter-debounce="100"
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
            <b class="marketwatch-table-ticker" @click="tickerClick(data)">{{
              data.value
            }}</b>
          </template>
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
          <template #cell(EPS)="data">
            <b v-if="data.value == 'NaN'" class="marketwatch-table-cell">
              {{ "-" }}</b
            >
            <b v-else class="marketwatch-table-cell">
              {{ data.value.toLocaleString() }}</b
            >
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
            <b v-if="data.value == 0" class="marketwatch-table-cell"
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
            <b v-if="data.value == 0" class="marketwatch-table-cell"
              >{{ data.value }}%</b
            >
          </template>
        </b-table> -->
      </v-card>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "marketwatch",
  components: {
    AgGridVue
  },
  data() {
    return {
      // AGgrid
      modules: AllModules,
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      MarketWatchHeader: [],
      sideBar: null,
      allColumnIds: [],
      gridColumnApi: null,
      localeText: null,
      dataFetch: false,
      tableData: null,
      asyncTransactionWaitMillis: 4000,
      interval: null,
      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      itemsss: ["foo", "bar", "fizz", "buzz", "fizzbuzz", "foobar"],
      valuesss: [],
      height: "370px",
      filterOn: ["ticker"],
      isBusy: true,
      sortDesc: false,
      sortBy: "ticker",
      tableMarketSelected: "همه",
      tableMarketFilters: ["همه", "بورس", "فرابورس"],
      tableMarketTypeSelected: [],
      tableMarketTypeFilters: [],
      tableMarketIndustrySelected: [],
      tableMarketIndustryFilters: [],
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
        {
          label: "نماد",
          key: "ticker",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "بازار",
          key: "marketName",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "درصد آخرین قیمت",
          key: "lastPercent",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "درصد قیمت پایانی",
          key: "closePercent",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "کف مجاز قیمت",
          key: "MinRange",
          thClass: "marketwatch-table-head",
          sortable: true
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
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "کمترین قیمت",
          key: "low",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "اولین قیمت",
          key: "first",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        }
      ]
    };
  },

  computed: {
    // %%%%%%%%%%%% type data %%%%%%%%%%%%
    Industrycriteria() {
      // Compute the search criteria
      return this.TypeSearch.trim().toLowerCase();
    },
    IndustryAvailableOptions() {
      let criteria = this.IndustrySearch;
      // Filter out already selected options
      let options = this.tableMarketIndustryFilters.filter(
        opt => this.tableMarketIndustrySelected.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    },
    searchDescIndustry() {
      if (this.Industrycriteria && this.IndustryAvailableOptions.length === 0) {
        return "There are no tags matching your search criteria";
      }
      return "";
    },

    HD() {
      return this.TriggerFilteredHeader();
    },

    ...mapState({
      // tableData: state => state.marketwatch.marketWatchItems
    })
  },
  watch: {
    $route() {
      if (this.$route.name != "marketwatch") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    },
    tableData(newValue, oldValue) {
      if (oldValue == null && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }

      if (oldValue != null)
        if (this.dataFetch == true && oldValue.length != 0)
          for (let i = 0; i < this.tableData.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.lastPercent != newValue[i].lastPercent) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.lastPercent = itemUpdate.lastPercent;
              newItem.closePercent = itemUpdate.closePercent;
              newItem.last = itemUpdate.last;
              newItem.last = itemUpdate.close;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.gridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
    }
  },
  created() {
    document.title = "Finwise - دیده‌بان";
    // GRID LOCALE FILE LOAD
    this.localeText = AG_GRID_LOCALE_FA;

    // GRID OPTIONS
    this.gridOptions = {
      suppressColumnVirtualisation: true,
      rowDragManaged: true,
      animateRows: true,
      rowClass: "ag-grid-row-class",

      // headerHeight: 20,
      rowHeight: 22,
      getRowNodeId: data => data.ID
    };
    this.defaultColDef = {
      flex: 1,
      minWidth: 100,
      filter: true,
      // sortable: true,
      // headerHeight: 12,
      enablePivot: false,
      suppressMenu: true,
      cellStyle: {
        display: "flex",
        "justify-content": "center",
        "border-left-color": "#e2e2e2",
        "align-items": "center",
        direction: "ltr"
      }
    };

    // AG Sidebar
    this.sideBar = {
      toolPanels: [
        {
          id: "columns",
          labelDefault: "Columns",
          labelKey: "columns",
          iconKey: "columns",
          toolPanel: "agColumnsToolPanel",
          toolPanelParams: {
            suppressRowGroups: true,
            suppressValues: true,
            suppressPivots: true,
            suppressPivotMode: true,
            suppressSideButtons: false,
            suppressColumnFilter: false,
            suppressColumnSelectAll: false,
            suppressColumnExpandAll: false
          }
        },

        {
          id: "filters",
          labelDefault: "Filters",
          labelKey: "filters",
          iconKey: "filter",
          toolPanel: "agFiltersToolPanel"
        }
      ],
      defaultToolPanel: ""
    };

    this.MarketWatchHeader = [
      {
        headerName: "نماد",
        field: "ticker",

        sortable: true,

        pinned: "right",
        rowDrag: true,
        cellStyle: {
          direction: "rtl",
          display: "inline-block"
          // // "justify-content": "center",
          // "align-items": "center !important",
          // "height": "100%"
        }
      },
      {
        headerName: "بازار",
        field: "marketName",
        sortable: true,
        minWidth: 150
      },
      {
        headerName: "صنعت",
        field: "industry",
        sortable: true,
        minWidth: 250,
        hide: true
      },
      {
        headerName: "تعداد معاملات",
        field: "TradeCount",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم معاملات",
        field: "TradeVolume",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "ارزش معاملات",
        field: "TradeValue",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت دیروز",
        field: "yesterday",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "آخرین قیمت",
        field: "last",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          return params.value.toLocaleString();
        },
        cellRenderer: "agAnimateSlideCellRenderer"
      },
      {
        headerName: "درصد آخرین قیمت",
        field: "lastPercent",
        filter: "agNumberColumnFilter",

        // cellStyle: {
        //   display: "flex",
        // color: "green",
        //   "justify-content": "center",
        //   "border-left-color": "#e2e2e2",

        //   "align-items": "center",
        //   direction: "ltr"
        // },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
          } else if (params.value < 0) {
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
          } else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",
              "align-items": "center",
              direction: "ltr"
            };
        },
        sortable: true,
        valueFormatter: function(params) {
          let percent = params.value;
          if (percent < 0) percent = "(" + Math.abs(percent) + ")";

          return "%" + percent.toLocaleString();
        },
        cellRenderer: "agAnimateShowChangeCellRenderer"
        // cellRenderer: function(params) {
        //   let Class = "";
        //   let percent = params.value;
        //   if (percent > 0) Class = "greenCell";
        //   else if (percent < 0) {
        //     Class = "redCell";
        //     percent = "(" + Math.abs(percent) + ")";
        //   }
        //   return `<span class="${Class}"><span class="${Class}" style="font-size:0.9em">%</span>${percent}</span>`;
        // }
      },
      {
        headerName: "قیمت پایانی",
        field: "close",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          return params.value.toLocaleString();
        },
        cellRenderer: "agAnimateSlideCellRenderer"
      },
      {
        headerName: "درصد قیمت پایانی",
        filter: "agNumberColumnFilter",
        field: "closePercent",
        sortable: true,
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          } else if (params.value < 0) {
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          } else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        valueFormatter: function(params) {
          let percent = params.value;
          if (percent < 0) percent = "(" + Math.abs(percent) + ")";

          return "%" + percent.toLocaleString();
        },
        cellRenderer: "agAnimateShowChangeCellRenderer"
      },
      {
        headerName: "کف مجاز قیمت",
        field: "MinRange",
        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "سقف مجاز قیمت",
        field: "MaxRange",
        sortable: true,
        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "EPS",
        field: "EPS",
        hide: true,
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "بالاترین قیمت",
        field: "high",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "کمترین قیمت",
        field: "low",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "اولین قیمت",
        field: "first",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد خرید حقیقی",
        field: "CountBuy_Haghighi",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد خرید حقوقی",
        field: "CountBuy_Hoguhgi",
        filter: "agNumberColumnFilter",

        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "border-left-color": "#e2e2e2",

          "align-items": "center"
        },
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم خرید حقیقی",
        field: "VolumeBuy_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم خرید حقوقی",
        field: "VolumeBuy_Hoghughi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد فروش حقیقی",
        field: "CountSell_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "تعداد فروش حقوقی",
        field: "CountSell_Hoghughi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم فروش حقیقی",
        field: "VolumeSell_Haghighi",
        filter: "agNumberColumnFilter",

        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم فروش حقوقی",
        field: "VolumeSell_Hoghughi",
        filter: "agNumberColumnFilter",
        sortable: true,
        hide: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      }
    ];
  },
  mounted() {
    this.height = this.getHeight();
    // let container = document.getElementById("kt_content");
    // this.width = window.screen.width;
    // this.height = (window.screen.height * 72) / 100;
    // let height = container.offsetHeight;
    this.loadData();
    this.TriggerFilteredHeader();
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // this.$socketMarketWatch.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    this.$socketMarketWatch.onmessage = data => {
      // this.DataItems = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
        this.$store.dispatch("setMarketWatchItems", JSON.parse(data.data));
    };
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    onQuickFilterChanged(event) {
      this.gridOptions.api.setQuickFilter(event.target.value);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        console.log("chaange");
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
    },
    onReady(params) {
      console.log("onReady");
      let allColumnIds = [];
      // this.gridOptions.api.closeToolPanel();
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;

      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      console.log(allColumnIds);
      // this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
      this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    tickerClick(data) {
      this.$router.push({ path: `/ticker/Overview/Overall/${data.item.ID}` });
    },
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
      this.MarketWatchFilterPost();
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.MarketTableHeader));
      let options = this.selectedHeaderOptions;

      let SwCase = 0;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
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
        this.tableMarketTypeSelected.length == 0 &&
        this.tableMarketIndustrySelected.length == 0
      ) {
        return this.tableData;
      } else if (this.tableMarketIndustrySelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (this.tableMarketTypeSelected.includes(obj["Type"])) {
            temp.push(obj);
          }
        }
        return temp;
      } else if (this.tableMarketTypeSelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (this.tableMarketIndustrySelected.includes(obj["Industry"])) {
            temp.push(obj);
          }
        }
        return temp;
      } else {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (
            this.tableMarketTypeSelected.includes(obj["Type"]) &&
            this.tableMarketIndustrySelected.includes(obj["Industry"])
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
      this.isBusy = true;

      await this.axios
        .get("/api/marketwatch")
        .then(response => {
          this.isBusy = false;
          this.$store.dispatch("setMarketWatchItems", response.data);
          this.tableData = response.data;
        })
        .catch(error => {
          this.isBusy = false;

          console.error(error);
        });
    },
    async MarketWatchFilterListReq() {
      await this.axios.get("/api/marketwatchfilterlists").then(response => {
        this.tableMarketIndustryFilters = response.data;
        this.itemsss = response.data;
      });
    },
    MarketWatchFilterPost() {
      this.axios({
        method: "post",
        url: "/api/marketwatch",
        data: {
          marketName: this.tableMarketSelected,
          // marketType: this.tableMarketTypeSelected,
          marketIndustry: this.tableMarketIndustrySelected
        },
        headers: { "Content-Type": "application/json" },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response2 => {
          // this.$store.dispatch("setMarketWatchItems", response2.data);
          this.tableData = response2.data;
          this.gridApi.setRowData(this.tableData);
        })
        .catch(error => {
          console.error(error);
        });
    },

    TypeonOptionClick({ option, addTag }) {
      addTag(option);
      this.TypeSearch = "";
      this.MarketWatchFilterPost();
    },
    IndustryonOptionClick({ option, addTag }) {
      addTag(option);
      this.IndustrySearch = "";
      this.MarketWatchFilterPost();
    },
    getHeight() {
      // let filterRow = document.getElementById("marketwatchFilterRow1")
      //   .offsetHeight;
      // let filterRow2 = document.getElementById("marketwatchFilterRow2")
      //   .offsetHeight;

      return (window.innerHeight - 100).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval._id);
          return;
        }
        // let barier = {
        //   request: "get",
        //   data: {
        //     marketName: this.tableMarketSelected,
        //     marketIndustry: this.tableMarketIndustrySelected
        //   }
        // };
        // this.$socketMarketWatch.send(JSON.stringify(barier));
        this.MarketWatchTableReq();
      }, 10000);
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
  beforeDestroy() {
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  }
};
</script>
<style>
/* ag Grid */
.ag-theme-balham .ag-header {
  background-color: #f5f7f7;
  background-color: var(--ag-header-background-color, #f5f7f7);
  border-top: solid 1px;
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-top-color: #bdc3c7;
  border-top-color: var(--ag-border-color, #bdc3c7);
  border-radius: 10px 10px 0px 0px;
}

.ag-theme-balham .ag-rtl .ag-cell {
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
  overflow: hidden;
}
/* header */
.ag-header-cell-label {
  color: black;
  font-size: 1em;
  font-weight: 300;
  align-items: center;
  text-align: center;
  margin-right: 2px !important;
  display: flex;
  justify-content: center;
  align-content: center;
}
.ag-grid-row-class {
  /* background-color: red !important; */
  display: flex;
  align-items: center !important;
}
/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */

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
  font-size: 1.1em !important;
  font-weight: 700 !important ;
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
  font-size: 1em;
  /* line-height: 1; */
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.marketwatch-table-ticker {
  /* color: #4682b4; */
  color: #000;
  font-size: 1.2em;
  cursor: pointer;
  vertical-align: middle !important;
}
.marketwatch-table-ticker:hover {
  color: #4682b4;
  cursor: pointer;
  vertical-align: middle !important;
}
.marketwatch-table-cell-green {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.marketwatch-table-cell-red {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  vertical-align: middle !important;
  font-family: "Vazir-Medium-FD";
}
.marketwatch-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
  vertical-align: middle !important;
}
.marketwatch-table-row {
  direction: ltr;
  vertical-align: middle !important;
}

/* .selector .v-text-field--box .v-input__slot,
.v-text-field--outlined .v-input__slot {
  min-height: 25px !important;
  max-height: 50px;
  display: flex !important;
  align-items: center !important;
  font-size: 0.8rem !important;
}
.selector .v-chip.v-size--small {
  border-radius: 19px !important;
  font-size: 0.8rem !important;
  height: 19px !important;
  background-color: "#3dbff0";
} */
</style>
