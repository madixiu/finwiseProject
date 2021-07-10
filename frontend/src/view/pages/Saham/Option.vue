/* eslint-disable no-unused-vars */
<template>
  <div>
    <div class="row mr-1 ml-1">
      <!-- OPTION TABLE *************************************************** -->
      <v-card width="100%">
        <div id="marketwatchFilterRow2" class="row pb-1 pt-1">
          <div class="col-xxl-2 col-lg-2 col-md-6 col-sm-12 mr-1">
            <b-input-group size="sm">
              <b-input-group-prepend is-text>
                <!-- <b-icon v-if="filter != ''" icon="x-circle" @click="filter=''"></b-icon>
                <b-icon v-else icon="search"></b-icon> -->
                <b-icon icon="search"></b-icon>
              </b-input-group-prepend>
              <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="جستجو"
                @keyup="onQuickFilterChanged"
              ></b-form-input>
              <!-- <b-input-group-append>
                <b-button :disabled="!filter" @click="onQuickFilterChanged; filter=''">
                  <b-icon
                    icon="x-circle"
                    variant="danger"
                    font-scale="1"
                  ></b-icon
                ></b-button>
              </b-input-group-append> -->
            </b-input-group>
          </div>
        </div>
        <ag-grid-vue
          :style="`width: 100%; height:${height}; font-family: Vazir-Medium-FD`"
          class="ag-theme-balham"
          :columnDefs="OptionHeader"
          :defaultColDef="defaultColDef"
          rowSelection="multiple"
          :cacheQuickFilter="true"
          :sideBar="sideBar"
          :enableRtl="true"
          :gridOptions="gridOptions"
          @grid-ready="onReady"
          @gridColumnsChanged="gridColumnsChanged"
          :localeText="localeText"
        >
        </ag-grid-vue>
        <!-- <b-table
            thClass="option-table-head"
            class="option-table"
            tbody-tr-class="option-table-row"
            :sticky-header="height"
            dense
            striped
            :busy.sync="isBusy"
            :filter="filter"
            :filter-included-fields="filterOn"
            :filter-debounce="100"
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
            :items="getSahm"
            :fields="headersBoot"
            @filtered="onFiltered"
          >
            <template #table-busy>
              <div class="text-center text-danger my-2">
                <b-spinner class="align-middle mr-2"></b-spinner>
                <strong>شکیبا باشید</strong>
              </div>
            </template>
            <template #cell(Nemad)="data">
              <b class="option-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(UnderLying)="data">
              <b class="option-table-cell-bold">{{ data.value }}</b>
            </template>
            <template #cell(StrikePrice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(TTM)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(averageFairprice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(priceseller)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(volumeseller)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(AssetPrice)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(DifferenceToAverage)="data">
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value
              }}</b>
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -10001 && data.value != -10000
                "
                class="option-table-cell-red"
                >{{ data.value }}</b
              >
              <b v-if="data.value == -10001" class="option-table-cell-s">{{
                "سفارش فروش ندارد"
              }}</b>
              <b v-if="data.value == -10000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(PPP)="data">
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value.toLocaleString() }}</b
              >
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "سفارش فروش ندارد"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value.toLocaleString()
              }}</b>
            </template>
            <template #cell(TotalValue)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(FinalPayment)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(LastTrade)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
            <template #cell(DifferenceToLast)="data">
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value }}</b
              >
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value
              }}</b>
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "بدون معامله"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(ArzandegiLast)="data">
              <b v-if="data.value > 0" class="option-table-cell-green">{{
                data.value.toLocaleString()
              }}</b>
              <b
                v-if="
                  data.value < 0 && data.value != -1001 && data.value != -1000
                "
                class="option-table-cell-red"
                >{{ data.value.toLocaleString() }}</b
              >
              <b v-if="data.value == 0" class="option-table-cell">{{
                data.value.toLocaleString()
              }}</b>
              <b v-if="data.value == -1001" class="option-table-cell-s">{{
                "بدون معامله"
              }}</b>
              <b v-if="data.value == -1000" class="option-table-cell-r">{{
                "ارزنده نیست"
              }}</b>
            </template>
            <template #cell(TradeVolume)="data">
              <b class="option-table-cell">{{ data.value.toLocaleString() }}</b>
            </template>
          </b-table> -->
      </v-card>

      <!-- <div class="col-12">
        <div class="row">

          <div
            class="px-sm-2 pb-2 pb-sm-6 px-xs-0 col-sm-4 col-md-4 col-lg-4 col-12"
          >
            <v-card round elevation="15">
              <v-toolbar dense flat>
                <v-toolbar-title v-if="card2Key">تلاطم</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-btn v-if="card2Key" icon @click="card2Key = !card2Key">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
                <v-btn v-if="!card2Key" icon @click="card2Key = !card2Key">
                  <v-icon>mdi-arrow-left</v-icon>
                </v-btn>
              </v-toolbar>
              <div class="filterBox">
                <transition name="fade">
                  <div v-if="card2Key" key="1">
                    <v-data-table
                      thClass="option-table-head"
                      fixed-header
                      height="196"
                      :headers="card1Header"
                      :items="OptionAsset"
                      item-key="name"
                      class="elevation-1 cardTable"
                      :hide-default-footer="true"
                    ></v-data-table>
                  </div>

                  <div
                    v-if="!card2Key"
                    class="cardExplanation ml-4 mr-4"
                    key="2"
                  >
                    <p>
                      در این جدول مقدار تلاطم (Volatility) یک ساله برای دارایی
                      های پایه قابل مشاهده است. محاسبه این مقادیر به کمک قیمت
                      تعدیل شده انجام گرفته است.
                    </p>
                  </div>
                </transition>
              </div>
              <v-card-actions>
                <span class="cardFooter">{{ OptionAsset.length }}</span>
                <span v-if="OptionAsset.length" class="cardFooter mr-2"
                  >نتیجه</span
                >
              </v-card-actions>
            </v-card>
          </div>
          <div class="col-8">
            <v-card height="280">
              <v-card-title>
                <i class="flaticon2-pen text-danger"></i>

                <span>نحوه محاسبه</span>
              </v-card-title>
              <div style="direction:rtl;text-align:right" class="mr-5 ml-5">
                <span
                  >در این قسمت محاسباتی برای معامله بهتر اختیارات خرید به
                  کاربران ارائه شده است. قیمت های عادلانه با استفاده از مدل بلک
                  شولز محاسبه شده اند. نرخ بهره با ۴ سناریوی مختلف و تلاطم در ۵
                  بازه زمانی کوتاه مدت تا بلند مدت محاسبه و نهایتا ۲۰ سناریو
                  متفاوت برای قیمت اختیار در نظر گرفته می شود. میانگین وزنی این
                  ۲۰ سناریو به عنوان خروجی نهایی قیمت عادلانه معرفی شده است.
                  برای اطلاعات بیشتر نشانگر را روی نام هر ستون قرار دهید.</span
                >
              </div>
            </v-card>
          </div>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "Option",
  components: {
    AgGridVue
  },

  data: () => ({
    // * AGgrid base data
    modules: AllModules,
    gridApi: null,
    defaultColDef: null,
    gridOptions: null,
    OptionHeader: [],
    sideBar: null,
    allColumnIds: [],
    gridColumnApi: null,
    localeText: null,
    dataFetch: false,
    tableData: null,

    // * %%%%%%%%%%%%%%%
    WebsocketRequest: false,
    isBusy: true,
    filterOn: ["Nemad", "UnderLying"],
    sortDesc: true,
    sortBy: "DifferenceToAverage",
    OptionAsset: [],
    card1Key: true,
    card2Key: true,
    card1Header: [
      { text: "اسم سهم", align: "center", value: "ticker", sortable: false },
      {
        text: "مقدار تلاطم",
        align: "center",
        value: "round",
        sortable: false
      }
    ],
    filter: null,
    height: "450px",
    search: "",
    headersBoot: [
      {
        label: "نماد",
        key: "Nemad",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "دارایی پایه",
        key: "UnderLying",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "قیمت اعمال",
        key: "StrikePrice",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "فاصله تا سر رسید",
        key: "TTM",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "قیمت دارایی پایه",
        key: "AssetPrice",
        width: "120",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "قیمت عادلانه",
        key: "averageFairprice",
        width: "230",
        thClass: "option-table-head",
        sortable: true,
        headerTitle: "قیمت به دست آمده از مدل بلک شولز"
      },
      {
        label: "قیمت بهترین سفارش فروش",
        key: "priceseller",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },
      {
        label: "حجم بهترین سفارش فروش",
        key: "volumeseller",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "ارزندگی بهترین سفارش فروش",
        key: "DifferenceToAverage",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },

      {
        label: "پوشش قیمت سهام با بهترین سفارش فروش",
        key: "PPP",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "پرداخت کنونی بهترین سفارش(میلیون ریال)",
        key: "TotalValue",
        width: "120",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، امروز باید پرداخت شود"
      },
      {
        label: "پرداخت نهایی بهترین سفارش(میلیون ریال)",
        key: "FinalPayment",
        width: "100",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، در روز اعمال باید پرداخت شود"
      },
      {
        label: "قیمت آخرین معامله",
        key: "LastTrade",
        width: "130",
        thClass: "option-table-head",
        sortable: true
      },

      {
        label: "ارزندگی آخرین معامله",
        key: "DifferenceToLast",
        width: "200",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },
      {
        label: "پوشش قیمت سهام با آخرین معامله",
        key: "ArzandegiLast",
        width: "130",
        thClass: "option-table-head",
        sortable: true,
        headerTitle:
          "قیمت تمام شده سهام با توجه به قیمت آخرین معامله آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        label: "حجم",
        key: "TradeVolume",
        width: "100",
        thClass: "option-table-head",
        sortable: true
      }
    ]
  }),

  computed: {
    ...mapGetters(["getSahm"])
  },
  watch: {
    tableData(newValue, oldValue) {
      if (oldValue == null && newValue.length != 0) {
        this.gridApi.setRowData(newValue);
        this.dataFetch = true;
      }
    }
  },
  created() {
    document.title = "Finwise - آپشن";
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
      getRowNodeId: data => data.id
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

    this.OptionHeader = [
      {
        headerName: "نماد",
        field: "Nemad",

        sortable: true,
        minWidth: 120,
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
        headerName: "دارایی پایه",
        field: "UnderLying",
        sortable: true
      },

      {
        headerName: "قیمت اعمال",
        field: "StrikePrice",

        sortable: true,
        filter: "agNumberColumnFilter",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "فاصله تا سر رسید",
        field: "TTM",
        width: "130",
        filter: "agNumberColumnFilter",
        sortable: true
      },
      {
        headerName: "قیمت دارایی پایه",
        field: "AssetPrice",
        filter: "agNumberColumnFilter",
        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "قیمت عادلانه",
        field: "averageFairprice",

        sortable: true,
        filter: "agNumberColumnFilter",

        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip: "قیمت به دست آمده از مدل بلک شولز"
      },
      {
        headerName: "قیمت بهترین سفارش فروش",
        field: "priceseller",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },
      {
        headerName: "حجم بهترین سفارش فروش",
        field: "volumeseller",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },

      {
        headerName: "ارزندگی بهترین سفارش فروش",
        field: "DifferenceToAverage",
        filter: "agNumberColumnFilter",
        sortable: true,
        headerTooltip:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است",
        valueFormatter: function(params) {
          if (params.value == -10001) return "سفارش فروش ندارد";
          else if (params.value == -10000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (
            (params.value < 0 || params.value == -10000) &&
            params.value != -10001
          )
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        }
      },

      {
        headerName: "پوشش قیمت سهام با بهترین سفارش فروش",
        field: "PPP",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "سفارش فروش ندارد";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          "قیمت تمام شده سهام با توجه به قیمت بهترین سفارش فروش آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        headerName: "پرداخت کنونی بهترین سفارش(میلیون ریال)",
        field: "TotalValue",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، امروز باید پرداخت شود"
      },
      {
        headerName: "پرداخت نهایی بهترین سفارش(میلیون ریال)",
        field: "FinalPayment",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        headerTooltip:
          "مبلغی که در صورت خرید کامل بهترین سفارش فروش، در روز اعمال باید پرداخت شود"
      },
      {
        headerName: "قیمت آخرین معامله",
        field: "LastTrade",
        filter: "agNumberColumnFilter",

        sortable: true,
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        }
      },

      {
        headerName: "ارزندگی آخرین معامله",
        field: "DifferenceToLast",
        filter: "agNumberColumnFilter",

        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "بدون معامله";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          " هر چه این مقدار بزرگتر و نزدیکتر به عدد 1 باشد یعنی خرید در این قیمت ارزنده تر است"
      },
      {
        headerName: "پوشش قیمت سهام با آخرین معامله",
        field: "ArzandegiLast",
        filter: "agNumberColumnFilter",
        sortable: true,
        valueFormatter: function(params) {
          if (params.value == -1001) return "بدون معامله";
          else if (params.value == -1000) return "ارزنده نیست";
          else return params.value;
        },
        cellStyle: params => {
          if (params.value > 0)
            return {
              display: "flex",
              color: "green",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else if (params.value < 0 && params.value != -1001)
            return {
              display: "flex",
              color: "red",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
          else
            return {
              display: "flex",
              color: "black",
              "justify-content": "center",
              "border-left-color": "#e2e2e2",

              "align-items": "center",
              direction: "ltr"
            };
        },
        headerTooltip:
          "قیمت تمام شده سهام با توجه به قیمت آخرین معامله آپشن است و این نسبت به طوری اصلاح شده که هر چه بزرگتر و نزدیکتر به عدد 1 باشد قرارداد ارزنده تر است"
      },

      {
        headerName: "حجم",
        field: "TradeVolume",
        filter: "agNumberColumnFilter",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
        },
        sortable: true
      }
      // &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&
      // &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&
    ];
  },
  mounted() {
    this.loadData();

    this.height = this.getHeight();

    this.liveChecker();
    // this.$socketOptions.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
    //     this.$store.dispatch("setSahm", JSON.parse(data.data));
    // };
  },
  methods: {
    // AG GRID METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // eslint-disable-next-line no-unused-vars
    onQuickFilterChanged(event) {
      // this.gridOptions.api.setQuickFilter(event.target.value);
      this.gridOptions.api.setQuickFilter(this.filter);
    },
    gridColumnsChanged() {
      if (this.allColumnIds.length) {
        this.gridColumnApi.autoSizeColumns(this.allColumnIds, false);
      }
    },
    onReady(params) {
      let allColumnIds = [];
      // this.gridOptions.api.closeToolPanel();
      this.gridColumnApi = this.gridOptions.columnApi;
      this.gridApi = params.api;

      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      // this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
      this.gridColumnApi.autoSizeColumns(allColumnIds, false);
      this.allColumnIds = allColumnIds;
      this.gridApi = params.api;
      if (this.tableData != null) params.api.setRowData(this.tableData);
    },
    // * %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    loadData() {
      // eslint-disable-next-line no-unused-vars
      // this.OptionAssetReq().then(response => {
      //   this.OptionTableReq();
      // });
      this.OptionTableReq();
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    async OptionAssetReq() {
      await this.axios
        .get("/api/ViewOptionAssetVolatility")
        .then(response => {
          let data = response.data;
          if (data != "noData") {
            this.OptionAsset = data;
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    async OptionTableReq() {
      this.isBusy = true;
      await this.axios
        .get("/api/options", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response => {
          let data = response.data;
          this.isBusy = false;
          if (data != "noData" && data != "AccessDenied") {
            this.tableData = data;
            // this.$store.dispatch("setSahm", data);
          } else if (data == "AccessDenied") {
            this.$store.dispatch("AutoRenewAccessToken");
            this.OptionTableReq();
          }
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    getHeight() {
      return (window.innerHeight - 100).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketOptions.send(JSON.stringify(barier));
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
    this.$$socketOptions.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
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

.cardFooter {
  color: #7c6f68;
  font-size: 0.9rem;
}
/* .v-toolbar__content,
.v-toolbar__extension {
  padding: 0px 4px !important;
} */
.filterBox {
  height: 196px;
  overflow: hidden;
  position: relative;
}
.cardExplanation {
  height: 196px;
  font-size: 0.8rem;
  text-align: right;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
/* always present */
.expand-transition {
  transition: all 0.6s ease;
  height: 30px;
  padding: 10px;
  background-color: #eee;
  overflow: hidden;
}
/* .expand-enter defines the starting state for entering */
/* .expand-leave defines the ending state for leaving */
.expand-enter,
.expand-leave {
  height: 0;
  padding: 0 10px;
  opacity: 0;
}
.list-enter,
.list-leave-to {
  visibility: hidden;
  height: 0;
  margin: 0;
  padding: 0;
  opacity: 0;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.3s;
}
.theme--light.v-data-table
  > .v-data-table__wrapper
  > table
  > thead
  > tr:last-child
  > th {
  border-bottom-width: 0px !important;
}
.cardTable {
  direction: rtl;
  text-align: right;
}
.Mychips {
  text-align: center;
}
.option-table-head {
  font-size: 1.1em !important;
  font-weight: 500;
}
.option-table {
  text-align: center;
  font-size: 0.8rem;
  vertical-align: middle !important;
  line-height: 1;
  font-family: "Vazir-Medium-FD";
}
.option-table-row:hover {
  background-color: #999999 !important;
}
@media screen and (max-width: 1366px) {
  .option-table-cell-s {
    vertical-align: middle !important;
    text-align: center;
    font-size: 0.9em;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (min-width: 1600px) {
  .option-table-cell-s {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (max-width: 1366px) {
  .option-table-cell-r {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    color: red;
    line-height: 1;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
@media screen and (min-width: 1600px) {
  .option-table-cell-r {
    vertical-align: middle !important;
    text-align: center;
    font-size: 1em;
    line-height: 1;
    color: red;
    font-weight: 400;
    font-family: "Vazir-Medium-FD";
  }
}
.option-table-cell {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
/* .option-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
} */
.option-table-cell-green {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.option-table-cell-red {
  text-align: center;
  vertical-align: middle !important;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.option-table-cell-bold {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
  /* font-family: "Vazir-Medium-FD";  */
  font-family: "Vazir-Medium-FD";
}
.option-table-row {
  direction: ltr;
  vertical-align: middle !important;
}

/* .vxe-toolbar .vxe-button--wrapper {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  text-align: right !important;
}
.vxe-input--inner {
  border: 1px solid black !important;
}
.vxe-input {
  display: inline-block;
  position: relative;
  width: 300px !important;
  height: 30px !important;
  margin-right: 10px;
} */
</style>
