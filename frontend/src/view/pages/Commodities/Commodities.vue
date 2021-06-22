<template>
  <div>
    <v-sheet elevation="6">
      <v-tabs background-color="#f0efeb" color="deep-purple accent-4" centered>
        <v-tab>نگاه کلی</v-tab>
        <v-tab :disabled="premiumAccountLock">
          <span
            >طلا و ارز
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>
        <v-tab :disabled="premiumAccountLock">
          <span
            >شاخص های جهانی
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>
        <v-tab :disabled="premiumAccountLock">
          <span
            >فلزات اساسی
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>
        <v-tab :disabled="premiumAccountLock">
          <span
            >پتروشیمی
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>
        <v-tab :disabled="premiumAccountLock">
          <span
            >پالایشی
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>

        <v-tab :disabled="premiumAccountLock">
          <span
            >فارکس
            <v-icon v-if="premiumAccountLock" size="15px" color="#4682B4"
              >mdi-lock</v-icon
            >
          </span>
        </v-tab>

        <v-tab-item>
          <v-row no-gutters class="pb-2 mt-1">
            <v-col class="ml-1 mr-2">
              <v-card>
                <v-toolbar dense color="#f2cc8f">
                  <v-toolbar-title>دلار و طلا</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>دلار و طلا</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    id="dollargoldTable"
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material dollargoldTable"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="dollargoldHeader"
                    :enableRtl="true"
                    :gridOptions="gridOptions"
                    @grid-ready="onGridReady"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in dollargold"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card>
            </v-col>

            <v-col class="mr-1 ml-2">
              <v-card>
                <v-toolbar dense color="#3d405b">
                  <v-toolbar-title>فلزات</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>فلزات</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="MetalHeader"
                    :enableRtl="true"
                    :gridOptions="MetalGridOptions"
                    @grid-ready="onMetalGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in metal1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card></v-col
            >
          </v-row>
          <v-row no-gutters class="pb-2">
            <v-col class="mr-2 ml-1"
              ><v-card>
                <v-toolbar dense color="#81b29a">
                  <v-toolbar-title>انرژی</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>انرژی</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height: 150px; font-family: 'Vazir-Light-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="EnergyHeader"
                    :enableRtl="true"
                    :gridOptions="EnergyGridOptions"
                    @grid-ready="onEnergyGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in energy1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card></v-col
            >
            <v-col class="ml-2 mr-1">
              <v-card>
                <v-toolbar dense color="#e07a5f">
                  <v-toolbar-title>فارکس</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>فارکس</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  150px; font-family: 'Vazir-Light-FD'"
                    class="ag-theme-material dollargoldTable"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="ForexHeader"
                    :enableRtl="true"
                    :gridOptions="ForexGridOptions"
                    @grid-ready="onForexGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      <span style="text-align:center;">قیمت</span>
                    </v-col>
                    <v-col>
                      <span style="text-align:center">تاریخ</span>
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in forex1"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>
                      <span class="comItems">{{ item.persianName }}</span>
                    </v-col>
                    <v-col>
                      {{ numberWithCommas(item.lastPrice) }}
                      <v-chip small class="chips"
                        >{{ item.changeperc }}
                      </v-chip>
                    </v-col>
                    <v-col>
                      <span class="comDates">{{ item.persianDate }}</span>
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card></v-col
            >
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row no-gutters class="pb-2 mt-1">
            <v-col class="mr-2 ml-1">
              <v-card>
                <v-toolbar dense color="#f2cc8f">
                  <v-toolbar-title>طلا</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>طلا</v-card-title> -->
                <!-- <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="GoldHeader"
                    :enableRtl="true"
                    :gridOptions="GoldGridOptions"
                    @grid-ready="onGoldGridReady"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in gold"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card>
            </v-col>
            <v-col class="ml-2 mr-1">
              <v-card>
                <v-toolbar dense color="#118ab2">
                  <v-toolbar-title>ارز</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>ارز</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="CurrenciesHeader"
                    :enableRtl="true"
                    :gridOptions="CurrenciesGridOptions"
                    @grid-ready="onCurrenciesGridReady"
                  ></ag-grid-vue>
                  <!-- <v-row no-gutters class="pb-2">
                    <v-col> </v-col>
                    <v-col>
                      قیمت
                    </v-col>
                    <v-col>
                      تاریخ
                    </v-col>
                  </v-row>
                  <v-row
                    v-for="item in currencies"
                    :key="item.persianName"
                    no-gutters
                    class="pb-2"
                  >
                    <v-col>{{ item.persianName }} </v-col>
                    <v-col> {{ numberWithCommas(item.price) }} ریال </v-col>
                    <v-col>
                      {{ item.Date }}
                    </v-col>
                  </v-row> -->
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row class="pb-2 pt-1">
            <v-col class="ml-2 mr-2">
              <v-card>
                <v-toolbar dense color="#00afb9">
                  <v-toolbar-title>شاخص جهانی</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  280px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="IndicesHeader"
                    :enableRtl="true"
                    :gridOptions="IndicesGridOptions"
                    @grid-ready="onIndicesGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row no-gutters class="pb-2 pt-1 ">
            <v-col class="mr-2 ml-1">
              <v-card>
                <v-toolbar dense color="#3d405b">
                  <v-toolbar-title>فلزات</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="MetalHeader"
                    :enableRtl="true"
                    :gridOptions="MetalGridOptions"
                    @grid-ready="onMetalGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col class="mr-1 ml-2">
              <v-card>
                <v-toolbar dense color="#5D2A42">
                  <v-toolbar-title>متال بولتن</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  400px; font-family: 'Vazir-Medium-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="MBHeader"
                    :enableRtl="true"
                    :gridOptions="MBGridOptions"
                    @grid-ready="onMBGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row class="pb-2 pt-1">
            <v-col class="mr-2 ml-2"
              ><v-card>
                <v-toolbar dense color="#023e8a">
                  <v-toolbar-title>پتروشیمی</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height: 250px; font-family: 'Vazir-Light-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="PetroHeader"
                    :enableRtl="true"
                    :gridOptions="PetroGridOptions"
                    @grid-ready="onPetroGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text> </v-card
            ></v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row class="pb-2 pt-1">
            <v-col class="mr-2 ml-2"
              ><v-card>
                <v-toolbar dense color="#81b29a">
                  <v-toolbar-title>انرژی</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>انرژی</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height: 150px; font-family: 'Vazir-Light-FD'"
                    class="ag-theme-material"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="EnergyHeader"
                    :enableRtl="true"
                    :gridOptions="EnergyGridOptions"
                    @grid-ready="onEnergyGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text> </v-card
            ></v-col>
          </v-row>
        </v-tab-item>
        <v-tab-item>
          <v-row class="pb-2 pt-1">
            <v-col class="ml-2 mr-2">
              <v-card>
                <v-toolbar dense color="#e07a5f">
                  <v-toolbar-title>فارکس</v-toolbar-title>
                </v-toolbar>
                <!-- <v-card-title>فارکس</v-card-title>
                <v-divider></v-divider> -->
                <v-card-text>
                  <ag-grid-vue
                    style="width: 100%; height:  150px; font-family: 'Vazir-Light-FD'"
                    class="ag-theme-material dollargoldTable"
                    :localeText="localeText"
                    :defaultColDef="defaultColDef"
                    :columnDefs="ForexHeader"
                    :enableRtl="true"
                    :gridOptions="ForexGridOptions"
                    @grid-ready="onForexGridReady"
                    :asyncTransactionWaitMillis="asyncTransactionWaitMillis"
                  ></ag-grid-vue>
                </v-card-text> </v-card
            ></v-col>
          </v-row>
        </v-tab-item>
      </v-tabs>
    </v-sheet>
  </div>
</template>
<script>
import { AllModules } from "@ag-grid-enterprise/all-modules/dist/ag-grid-enterprise.js";
import { AG_GRID_LOCALE_FA } from "@/view/content/ag-grid/local.fa.js";
import { AgGridVue } from "ag-grid-vue";
export default {
  name: "Commodities",
  components: {
    AgGridVue
  },
  data() {
    return {
      //***TEMPORARY */
      rowData: [],

      //***TEMPORARY */
      gridApi: null,
      defaultColDef: null,
      gridOptions: null,
      dollargoldHeader: [],
      // Specified Data ****
      // METAL ****
      MetalGridApi: null,
      MetalDefaultColDef: null,
      MetalGridOptions: null,
      MetalHeader: [],
      MetalDataFetch: false,
      //******
      // METAL ****
      MBGridApi: null,
      MBDefaultColDef: null,
      MBGridOptions: null,
      MBHeader: [],
      MBDataFetch: false,
      //******

      // ENERGY ****
      EnergyGridApi: null,
      EnergyDefaultColDef: null,
      EnergyGridOptions: null,
      EnergyHeader: [],
      EnergyDataFetch: false,
      //******
      // FOREX ****
      ForexGridApi: null,
      ForexDefaultColDef: null,
      ForexGridOptions: null,
      ForexHeader: [],
      ForexDataFetch: false,
      //******
      // GOLD ****
      GoldGridApi: null,
      GoldDefaultColDef: null,
      GoldGridOptions: null,
      GoldHeader: [],
      GoldDataFetch: false,
      //******
      // CURRENCIES ****
      CurrenciesGridApi: null,
      CurrenciesDefaultColDef: null,
      CurrenciesGridOptions: null,
      CurrenciesHeader: [],
      CurrenciesDataFetch: false,
      //******
      // INDICES ****
      IndicesGridApi: null,
      IndicesDefaultColDef: null,
      IndicesGridOptions: null,
      IndicesHeader: [],
      IndicesDataFetch: false,
      //******
      // PETRO ****
      PetroGridApi: null,
      PetroDefaultColDef: null,
      PetroGridOptions: null,
      PetroHeader: [],
      PetroDataFetch: false,
      //******
      localeText: null,
      asyncTransactionWaitMillis: 4000,

      modules: AllModules,
      premiumAccountLock: true,
      premiumPlusAccountLock: true,
      WebsocketRequest: true,
      role: 0,
      BasicAccount: false,
      isBusy: true,
      tableData: null,
      tableData2: null,
      dollargold: [],
      energy1: [],
      metal1: [],
      forex1: [],
      currencies: [],
      gold: [],
      indices: [],
      petro: [],
      MB: []
    };
  },
  watch: {
    //%%%%%%%%%%%%%%%%%%%% Main %%%%%%%%%%%%%%%%%%%%%%%%
    dollargold(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0);
      this.gridApi.setRowData(newValue);
    },
    energy1(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        this.EnergyGridApi.setRowData(newValue);
        this.EnergyDataFetch = true;
      }

      if (oldValue != undefined)
        if (this.EnergyDataFetch == true && oldValue.length != 0) {
          for (let i = 0; i < this.energy1.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.lastPrice != newValue[i].lastPrice) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.lastPrice = itemUpdate.lastPrice;
              newItem.changeperc = itemUpdate.changeperc;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.EnergyGridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
        }
    },
    forex1(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        this.ForexGridApi.setRowData(newValue);
        this.ForexDataFetch = true;
      }

      if (oldValue != undefined)
        if (this.ForexDataFetch == true && oldValue.length != 0) {
          for (let i = 0; i < this.forex1.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.lastPrice != newValue[i].lastPrice) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.lastPrice = itemUpdate.lastPrice;
              newItem.changeperc = itemUpdate.changeperc;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.ForexGridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
        }
    },
    metal1(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.MetalGridApi.setRowData(newValue);
        this.MetalDataFetch = true;
      }
      if (oldValue != undefined)
        if (this.MetalDataFetch == true && oldValue.length != 0) {
          for (let i = 0; i < this.metal1.length; i++) {
            let newItem = JSON.parse(JSON.stringify(oldValue[i]));
            if (newItem.lastPrice != newValue[i].lastPrice) {
              let itemUpdate = JSON.parse(JSON.stringify(newValue[i]));
              newItem.lastPrice = itemUpdate.lastPrice;
              newItem.changeperc = itemUpdate.changeperc;
              // let rowNode = that.MetalGridApi.getRowNode(itemUpdate.id);
              this.MetalGridApi.applyTransactionAsync({ update: [newItem] });
            }
          }
        }
    },
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    //%%%%%%%%%%%%%%%%%%%% Gold & Currency %%%%%%%%%%%%%
    gold(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.GoldGridApi.setRowData(newValue);
        this.GoldDataFetch = true;
      }
    },
    currencies(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.CurrenciesGridApi.setRowData(newValue);
        this.CurrenciesDataFetch = true;
      }
    },
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    //%%%%%%%%%%%%%%%%%%%% Indices %%%%%%%%%%%%%%%%%%%%%
    indices(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.IndicesGridApi.setRowData(newValue);
        this.IndicesDataFetch = true;
      }
    },
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    //%%%%%%%%%%%%%%%%%%%% Petro %%%%%%%%%%%%%%%%%%%%%
    petro(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.PetroGridApi.setRowData(newValue);
        this.PetroDataFetch = true;
      }
    },
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    //%%%%%%%%%%%%%%%%%%%% Petro %%%%%%%%%%%%%%%%%%%%%
    MB(newValue, oldValue) {
      if (oldValue.length == 0 && newValue.length != 0) {
        // this.MetalGridApi = this.MetalGridOptions.api;
        this.MBGridApi.setRowData(newValue);
        this.MBDataFetch = true;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  created() {
    document.title = "Finwise - بازار جهانی";

    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    let user = this.$store.getters.currentUser;
    this.role = user.role;
    if (this.role == 2) this.premiumAccountLock = false;
    if (this.role > 2) {
      this.premiumAccountLock = false;
      this.premiumPlusAccountLock = false;
    }
    console.log(user.role);

    // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    (this.localeText = AG_GRID_LOCALE_FA),
      (this.defaultColDef = {
        flex: 1,
        minWidth: 100,
        // sortable: true,
        // headerHeight: 12,
        enablePivot: false,
        cellStyle: {
          display: "flex",
          "justify-content": "center",
          "align-items": "center",
          direction: "ltr"
        }
      });
    // GRID OPTIONS
    this.gridOptions = {
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.MetalGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.EnergyGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.ForexGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.GoldGridOptions = {
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.CurrenciesGridOptions = {
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.IndicesGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.PetroGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };
    this.MBGridOptions = {
      asyncTransactionWaitMillis: 4000,
      headerHeight: 20,
      rowHeight: 30,
      getRowNodeId: data => data.id
    };

    // GRID HEADERS
    this.dollargoldHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.ID, request: "IR" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: " قیمت(ریال)",
        sortable: true,
        field: "price",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
          // return `<div><span>${params.value.toLocaleString()}</span> <span>ریال</span></div>`;
        }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "Date"
      }
    ];
    this.MetalHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.id, request: "IN" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: " قیمت(دلار)",
        sortable: true,
        field: "lastPrice",
        cellRenderer: "agAnimateShowChangeCellRenderer",

        valueFormatter: function(params) {
          return params.value.toLocaleString();
          // return `<span>${params.value.toLocaleString()}</span> <span style=color:black>دلار</span>`;
        }
      },
      {
        headerName: "تغییر قیمت",
        sortable: true,
        field: "changeperc",
        cellRenderer: "agAnimateShowChangeCellRenderer",
        valueFormatter: function(params) {
          // let Color = "black";
          let perc = parseFloat(params.value);
          // if (perc > 0) Color = "green";
          // else if (perc < 0) Color = "red";
          return "%" + perc.toLocaleString();
          // return `<span style=color:${Color}>${perc.toString()}</span>`;
        },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              color: "green",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else if (params.value < 0) {
            return {
              color: "red",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else
            return {
              color: "black",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
        }
        // cellRenderer: "agAnimateShowChangeCellRenderer"
        // cellRenderer: function(params) {
        //   let Color = "black";
        //   let perc = parseFloat(params.value);
        //   if (perc > 0) Color = "green";
        //   else if (perc < 0) Color = "red";
        //   return `<div><span style=color:${Color}>${perc.toString()}</span>`;
        // }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "persianDate"
      }
    ];
    this.EnergyHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.id, request: "IN" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: " قیمت(دلار)",
        sortable: true,
        field: "lastPrice",
        cellRenderer: "agAnimateShowChangeCellRenderer",

        valueFormatter: function(params) {
          return params.value.toLocaleString();
          // return `<span>${params.value.toLocaleString()}</span> <span style=color:black>دلار</span>`;
        }
      },
      {
        headerName: "تغییر قیمت",
        sortable: true,
        field: "changeperc",
        cellRenderer: "agAnimateShowChangeCellRenderer",
        valueFormatter: function(params) {
          // let Color = "black";
          let perc = parseFloat(params.value);
          // if (perc > 0) Color = "green";
          // else if (perc < 0) Color = "red";
          return "%" + perc.toLocaleString();
          // return `<span style=color:${Color}>${perc.toString()}</span>`;
        },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              color: "green",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else if (params.value < 0) {
            return {
              color: "red",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else
            return {
              color: "black",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
        }
        // cellRenderer: "agAnimateShowChangeCellRenderer"
        // cellRenderer: function(params) {
        //   let Color = "black";
        //   let perc = parseFloat(params.value);
        //   if (perc > 0) Color = "green";
        //   else if (perc < 0) Color = "red";
        //   return `<div><span style=color:${Color}>${perc.toString()}</span>`;
        // }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "persianDate"
      }
    ];
    this.ForexHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.id, request: "IN" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: " قیمت(دلار)",
        sortable: true,
        field: "lastPrice",
        cellRenderer: "agAnimateShowChangeCellRenderer",

        valueFormatter: function(params) {
          return params.value.toLocaleString();
          // return `<span>${params.value.toLocaleString()}</span> <span style=color:black>دلار</span>`;
        }
      },
      {
        headerName: "تغییر قیمت",
        sortable: true,
        field: "changeperc",
        cellRenderer: "agAnimateShowChangeCellRenderer",
        valueFormatter: function(params) {
          // let Color = "black";
          let perc = parseFloat(params.value);
          // if (perc > 0) Color = "green";
          // else if (perc < 0) Color = "red";
          return "%" + perc.toLocaleString();
          // return `<span style=color:${Color}>${perc.toString()}</span>`;
        },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              color: "green",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else if (params.value < 0) {
            return {
              color: "red",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else
            return {
              color: "black",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
        }
        // cellRenderer: "agAnimateShowChangeCellRenderer"
        // cellRenderer: function(params) {
        //   let Color = "black";
        //   let perc = parseFloat(params.value);
        //   if (perc > 0) Color = "green";
        //   else if (perc < 0) Color = "red";
        //   return `<div><span style=color:${Color}>${perc.toString()}</span>`;
        // }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "persianDate"
      }
    ];
    this.GoldHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.ID, request: "IR" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: "قیمت",
        sortable: true,
        field: "price",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
          // return `<div><span>${params.value.toLocaleString()}</span> <span>ریال</span></div>`;
        }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "Date"
      }
    ];
    this.CurrenciesHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.ID, request: "IR" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: "قیمت",
        sortable: true,
        field: "price",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
          // return `<div><span>${params.value.toLocaleString()}</span> <span>ریال</span></div>`;
        }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "Date"
      }
    ];
    this.IndicesHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.id, request: "IN" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: " قیمت(دلار)",
        sortable: true,
        field: "lastPrice",
        cellRenderer: "agAnimateShowChangeCellRenderer",

        valueFormatter: function(params) {
          return params.value.toLocaleString();
          // return `<span>${params.value.toLocaleString()}</span> <span style=color:black>دلار</span>`;
        }
      },
      {
        headerName: "تغییر قیمت",
        sortable: true,
        field: "changeperc",
        cellRenderer: "agAnimateShowChangeCellRenderer",
        valueFormatter: function(params) {
          // let Color = "black";
          let perc = parseFloat(params.value);
          // if (perc > 0) Color = "green";
          // else if (perc < 0) Color = "red";
          return "%" + perc.toLocaleString();
          // return `<span style=color:${Color}>${perc.toString()}</span>`;
        },
        cellStyle: params => {
          if (params.value > 0) {
            //mark police cells as red
            return {
              color: "green",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else if (params.value < 0) {
            return {
              color: "red",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
          } else
            return {
              color: "black",
              display: "flex",
              "justify-content": "center",
              direction: "ltr",
              "align-items": "center"
            };
        }
        // cellRenderer: "agAnimateShowChangeCellRenderer"
        // cellRenderer: function(params) {
        //   let Color = "black";
        //   let perc = parseFloat(params.value);
        //   if (perc > 0) Color = "green";
        //   else if (perc < 0) Color = "red";
        //   return `<div><span style=color:${Color}>${perc.toString()}</span>`;
        // }
      },
      {
        headerName: "تاریخ",
        sortable: true,
        field: "persianDate"
      }
    ];
    this.PetroHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName",
        cellRenderer: params => {
          const route = {
            name: "CommoditiesDetail",
            params: { id: params.data.id, request: "PL" }
          };
          const link = document.createElement("a");
          link.href = this.$router.resolve(route).href;
          link.innerText = params.value;
          link.addEventListener("click", e => {
            e.preventDefault();
            this.$router.push(route);
          });
          return link;
        }
      },
      {
        headerName: "دسته",
        sortable: true,
        field: "persianCategory"
      },
      {
        headerName: "لوکیشن",
        sortable: true,
        field: "location"
      },
      {
        headerName: "قیمت",
        sortable: true,
        field: "price",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
          // return `<div><span>${params.value.toLocaleString()}</span> <span>ریال</span></div>`;
        }
      },
      {
        headerName: "تاریخ",
        sortable: false,
        field: "persianDate"
      }
    ];
    this.MBHeader = [
      {
        headerName: "",
        sortable: false,

        field: "persianName"
      },
      {
        headerName: "لوکیشن",
        sortable: true,
        field: "location"
      },
      {
        headerName: "قیمت",
        sortable: true,
        field: "price",
        cellRenderer: function(params) {
          return params.value.toLocaleString();
          // return `<div><span>${params.value.toLocaleString()}</span> <span>ریال</span></div>`;
        }
      },
      {
        headerName: "تاریخ",
        sortable: false,
        field: "persianDate"
      }
    ];
  },
  mounted() {
    this.loadData();
    // this.loadIRData();
    // this.loadInvestingData();

    this.apiLiveData();

    // this.liveData();
    // this.$socketIRCommodities.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) {
    //     this.tableData = JSON.parse(data.data);
    //     this.prepareData();
    //   }
    // };
    // this.$socketInvCommodities.onmessage = data => {
    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) {
    //     this.tableData2 = JSON.parse(data.data);
    //     this.prepareData2();
    //   }
    // };
  },
  methods: {
    onMBGridReady(params) {
      this.MBGridApi = params.api;
      params.api.setRowData(this.MB);
    },
    onPetroGridReady(params) {
      this.PetroGridApi = params.api;
      params.api.setRowData(this.petro);
    },
    onIndicesGridReady(params) {
      this.IndicesGridApi = params.api;
      params.api.setRowData(this.indices);
    },
    onCurrenciesGridReady(params) {
      this.CurrenciesGridApi = params.api;
      params.api.setRowData(this.currencies);
    },
    onGoldGridReady(params) {
      this.GoldGridApi = params.api;
      params.api.setRowData(this.gold);
    },
    onForexGridReady(params) {
      this.ForexGridApi = params.api;
      params.api.setRowData(this.forex1);
    },
    onEnergyGridReady(params) {
      this.EnergyGridApi = params.api;
      params.api.setRowData(this.energy1);
    },
    onMetalGridReady(params) {
      this.MetalGridApi = params.api;
      console.log("metal:", this.metal1);
      params.api.setRowData(this.metal1);
    },
    onGridReady(params) {
      this.gridApi = params.api;
      // if (this.dollargold != null)
      console.log(params.api);
      console.log(this.dollargold);
      params.api.setRowData(this.dollargold);
    },
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },

    async loadIRData() {
      this.isBusy = true;
      await this.axios
        .get("/api/Commodities/IR", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(responseIR => {
          this.isBusy = false;

          let data = responseIR.data;
          if (data != "noData") {
            this.dollargold = data[1];
            this.gold = data[2];
            this.currencies = data[3];
            // this.tableData = data;
            // this.prepareData();
          }
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    async loadInvestingData() {
      this.isBusy = true;
      await this.axios
        .get("/api/Commodities/Investing", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          // this.tableData2 = data;
          this.metal1 = data[1];
          this.energy1 = data[2];
          this.forex1 = data[3];
          this.indices = data[4];
          // this.prepareData2();
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    async loadPetroData() {
      await this.axios
        .get("/api/Commodities/Petro", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(PetroResponse => {
          this.petro = PetroResponse.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async loadMBData() {
      await this.axios
        .get("/api/Commodities/MB", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(MBResponse => {
          this.MB = MBResponse.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.loadIRData().then(resp0 => {
        // eslint-disable-next-line no-unused-vars
        this.loadInvestingData().then(resp1 => {
          // eslint-disable-next-line no-unused-vars
          this.loadPetroData().then(resp2 => {
            this.loadMBData();
          });
        });
      });
    },
    apiLiveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        this.loadInvestingData();
      }, 10000);
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketIRCommodities.send(JSON.stringify(barier));
      }, 3000);
      let interval2 = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval2);
          return;
        }
        let barier = { request: "get" };
        this.$socketInvCommodities.send(JSON.stringify(barier));
      }, 3000);
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketIRCommodities.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.cardColor {
  background-color: rgba(226, 194, 194, 0.61) !important;
  border-color: black !important;
  max-height: 100vh;
  min-width: 312px;
}
.chips {
  font-family: "Vazir-Medium-FD" !important;
  font: size 0.6em;
  text-align: right;
}
.comItems {
  font-family: "Vazir-Medium-FD" !important;
  font: size 1em;
  text-align: right;
}
.comDates {
  font-family: "Vazir-Medium-FD" !important;
  font: size 0.7em;
  text-align: right;
}
.ag-header-cell-label .ag-header-cell-text {
  color: black;
  padding-right: 2px;
  padding-left: 2px;
  /* Force the width corresponding at how much width
    we need once the text is laid out vertically */
  /* width: 30px; */
  /* transform: rotate(90deg); */
  /* margin-top: 50px; */
  /* Since we are rotating a span */
  display: inline-block;
}
.ag-header-cell-label {
  justify-content: center;
}
</style>
