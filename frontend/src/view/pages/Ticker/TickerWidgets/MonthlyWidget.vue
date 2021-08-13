<template>
  <div>
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        گزارش ماهیانه
        <b-spinner class="titleHeaders" type="grow" small></b-spinner>
      </h3>
    </div> -->

    <!--//? گزارش تسهیلات -->
    <v-sheet rounded="lg" elevation="6" height="100%" v-if="type == 'bank'">
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                گزارش تسهیلات
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
            <b-table
              class="MonthlyWidget-table"
              thClass="MonthlyWidget-tableHeader"
              tbody-tr-class="MonthlyWidget-table-row"
              small
              hover
              :responsive="true"
              :items="filteredItems"
              :fields="headersfacility"
            ></b-table>
          </v-card>

          <!-- <v-tabs
            vertical
            background-color="#212529 "
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش تسهیلات
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
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template
                    v-slot:[`item.StartPeriod_RemainingFacility`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.StartPeriod_RemainingFacility)
                      }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.StartPeriod_RemainingFacility_modifications`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.StartPeriod_RemainingFacility_modifications
                        )
                      }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.StartPeriod_RemainingFacility_modified`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.StartPeriod_RemainingFacility_modified
                        )
                      }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.thisPeriod_IssuedFacilitiy`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriod_IssuedFacilitiy) }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.thisPeriod_SetteledFacility`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriod_SetteledFacility) }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.EnePeriod_RemainingFacility`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.EnePeriod_RemainingFacility) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_RevenueFromFacility`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_RevenueFromFacility
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_RevenueFromFacility_modification`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_RevenueFromFacility_modification
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_RevenueFromFacility_modified`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_RevenueFromFacility_modified
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisPeriod_RevenueFromFacility`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.thisPeriod_RevenueFromFacility)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisYear_RevenueFromFacility`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisYear_RevenueFromFacility) }}
                    </span>
                  </template>
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش سپرده ها
                  </h4>
                </div>
                <v-data-table
                  :headers="headersdeposit"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template v-slot:[`item.StartPeriod_Deposits`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.StartPeriod_Deposits) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.StartPeriod_Deposits_modifications`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.StartPeriod_Deposits_modifications
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.StartPeriod_Deposits_modified`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.StartPeriod_Deposits_modified)
                      }}
                    </span>
                  </template>

                  <template
                    v-slot:[`item.thisPeriod_IncomingDeposit`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriod_IncomingDeposit) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisPeriod_setteledDeposits`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriod_setteledDeposits) }}
                    </span>
                  </template>
                  <template v-slot:[`item.EndPeriod_Deposits`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.EndPeriod_Deposits) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_InterestOnDeposits`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_InterestOnDeposits
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_InterestOnDeposits_modifications`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_InterestOnDeposits_modifications
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_InterestOnDeposits_modified`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_InterestOnDeposits_modified
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisPeriod_InterestOnDeposits`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.thisPeriod_InterestOnDeposits)
                      }}
                    </span>
                  </template>
                  <template v-slot:[`item.Total_InterestOnDeposits`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_InterestOnDeposits) }}
                    </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? گزارش فعالیت بیمه -->
    <!-- <div class="card-body d-flex flex-column" v-if="type == 'insurance'"> -->
    <v-sheet
      rounded="lg"
      elevation="6"
      height="100%"
      v-if="type == 'insurance'"
    >
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                گزارش فعالیت بیمه
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
            <b-table
              class="MonthlyWidget-table"
              thClass="MonthlyWidget-tableHeader"
              tbody-tr-class="MonthlyWidget-table-row"
              small
              hover
              :responsive="true"
              :items="filteredItems"
              :fields="heaadersInsurance"
            >
              <template #cell(PreviousPeriods_IssuedInsurance_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousPeriods_IssuedInusrance_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousPeriods_DamageRepaid_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Modification_IssuedInsurance_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Modification_DamageRepaid_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousModified_IssuedInsurance_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousModified_IssuedInusrance_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousModified_DamageRepaid_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PreviousModified_DamageRepaid_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(ThisPeriod_IssuedInsurance_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(ThisPeriod_IssuedInusrance_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(ThisPeriod_DamageRepaid_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(ThisPeriod_DamageRepaid_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Total_IssuedInsurance_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Total_IssuedInusrance_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Total_DamageRepaid_Amount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(Total_DamageRepaid_Share)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
            </b-table>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش فعالیت بیمه
                  </h4>
                </div>
                <v-data-table
                  :headers="heaadersInsurance"
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
                  <template
                    v-slot:[`item.PreviousPeriods_IssuedInsurance_Amount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_IssuedInsurance_Amount
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_IssuedInusrance_Share`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_IssuedInusrance_Share
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousPeriods_DamageRepaid_Amount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousPeriods_DamageRepaid_Amount
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Modification_IssuedInsurance_Amount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.Modification_IssuedInsurance_Amount
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Modification_DamageRepaid_Amount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.Modification_DamageRepaid_Amount)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousModified_IssuedInsurance_Amount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousModified_IssuedInsurance_Amount
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousModified_IssuedInusrance_Share`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousModified_IssuedInusrance_Share
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousModified_DamageRepaid_Amount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousModified_DamageRepaid_Amount
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.PreviousModified_DamageRepaid_Share`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.PreviousModified_DamageRepaid_Share
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.ThisPeriod_IssuedInsurance_Amount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.ThisPeriod_IssuedInsurance_Amount)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.ThisPeriod_IssuedInusrance_Share`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.ThisPeriod_IssuedInusrance_Share)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.ThisPeriod_DamageRepaid_Amount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.ThisPeriod_DamageRepaid_Amount)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.ThisPeriod_DamageRepaid_Share`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.ThisPeriod_DamageRepaid_Share)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Total_IssuedInsurance_Amount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_IssuedInsurance_Amount) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Total_IssuedInusrance_Share`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_IssuedInusrance_Share) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Total_DamageRepaid_Amount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_DamageRepaid_Amount) }}
                    </span>
                  </template>
                  <template v-slot:[`item.Total_DamageRepaid_Share`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_DamageRepaid_Share) }}
                    </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? گزارش تولید و فروش -->
    <!-- <div class="card-body d-flex flex-column" v-if="type == 'production'"> -->
    <v-sheet
      rounded="lg"
      elevation="6"
      height="100%"
      v-if="type == 'production'"
    >
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                گزارش تولید و فروش
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
            <b-table
              class="MonthlyWidget-table"
              thClass="MonthlyWidget-tableHeader"
              tbody-tr-class="MonthlyWidget-table-row"
              small
              hover
              :responsive="true"
              :items="filteredItems"
              :fields="headersProduction"
            >
              <template #cell(category)="data">
                <span>{{ categoryProduct(data.value) }} </span>
              </template>
              <template #cell(totalProductionPeriod)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(totalSalePeriod)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(saleAmountPeriod)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(totalProductionYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(totalSaleYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(saleRateYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(saleAmountYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prevTotalProductionYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prevTotalSalesYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prevTotalSalesRateYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prevTotalSalesAmountYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(modification_Production)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(modification_Sales)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(modification_SalesAmount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prev_modified_TotalProduction)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prev_modified_TotalSales)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prev_modified_TotalSalesRate)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(prev_modified_TotalSalesAmount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(lastyear_Production)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(lastyear_saleCount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(lastyear_saleRate)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(lastyear_saleAmount)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
            </b-table>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش تولید و فروش
                  </h4>
                </div>
                <v-data-table
                  :headers="headersProduction"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength itemFilters"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                  loading
                  loading-text="در حال بارگزاری"
                >
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template v-slot:[`item.status`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.statusdata.value.toLocaleString()}}
                    </span>
                  </template>
                  <template v-slot:[`item.unit`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.unit) }}
                    </span>
                  </template>
                  <template v-slot:[`item.category`]="{ item }">
                    <span class="FinancialStrength"
                      >{{ categoryProduct(item.category) }}
                    </span>
                  </template>
                  <template v-slot:[`item.totalProductionPeriod`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.totalProductionPeriod) }}
                    </span>
                  </template>
                  <template v-slot:[`item.totalSalePeriod`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.totalSalePeriod) }}
                    </span>
                  </template>
                  <template v-slot:[`item.saleAmountPeriod`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.saleAmountPeriod) }}
                    </span>
                  </template>
                  <template v-slot:[`item.totalProductionYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.totalProductionYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.totalSaleYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.totalSaleYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.saleRateYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.saleRateYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.saleAmountYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.saleAmountYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.prevTotalProductionYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prevTotalProductionYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.prevTotalSalesYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prevTotalSalesYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.prevTotalSalesRateYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prevTotalSalesRateYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.prevTotalSalesAmountYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prevTotalSalesAmountYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.modification_Production`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.modification_Production) }}
                    </span>
                  </template>
                  <template v-slot:[`item.modification_Sales`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.modification_Sales) }}
                    </span>
                  </template>
                  <template v-slot:[`item.modification_SalesAmount`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.modification_SalesAmount) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.prev_modified_TotalProduction`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.prev_modified_TotalProduction)
                      }}
                    </span>
                  </template>
                  <template v-slot:[`item.prev_modified_TotalSales`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prev_modified_TotalSales) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.prev_modified_TotalSalesRate`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.prev_modified_TotalSalesRate) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.prev_modified_TotalSalesAmount`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.prev_modified_TotalSalesAmount)
                      }}
                    </span>
                  </template>
                  <template v-slot:[`item.lastyear_Production`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastyear_Production) }}
                    </span>
                  </template>
                  <template v-slot:[`item.lastyear_saleCount`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastyear_saleCount) }}
                    </span>
                  </template>
                  <template v-slot:[`item.lastyear_saleRate`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastyear_saleRate) }}
                    </span>
                  </template>
                  <template v-slot:[`item.lastyear_saleAmount`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastyear_saleAmount) }}
                    </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? هزینه ها -->
    <!-- <div class="card-body d-flex flex-column" v-if="type == 'leasing'"> -->
    <v-sheet rounded="lg" elevation="6" height="100%" v-if="type == 'leasing'">
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                هزینه و درآمد
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
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  هزینه ها
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems"
                :fields="headersLeasingCost"
              ></b-table>
            </v-card>
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  درآمدها
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems2"
                :fields="headersLeasingRevenue"
              ></b-table>
            </v-card>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    هزینه ها
                  </h4>
                </div>
                <v-data-table
                  :headers="headersLeasingCost"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength itemFilters"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                  loading
                  loading-text="در حال بارگزاری"
                >
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template v-slot:[`item.thisPeriod_Achievedcost`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriod_Achievedcost) }}
                    </span>
                  </template>
                  <template v-slot:[`item.Total_Achievedcost`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_Achievedcost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisPeriod_TakenFacilityRemaind`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.thisPeriod_TakenFacilityRemaind)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.Total_TakenFacilityRemained`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.Total_TakenFacilityRemained) }}
                    </span>
                  </template>
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    درآمدها
                  </h4>
                </div>
                <v-data-table
                  :headers="headersLeasingRevenue"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength itemFilters"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                  loading
                  loading-text="در حال بارگزاری"
                >
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template v-slot:[`item.thisPeriodAmount`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisPeriodAmount) }}
                    </span>
                  </template>
                  <template v-slot:[`item.TotalAmount`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalAmount) }}
                    </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? گزارش درآمد خدمات -->

    <!-- <div class="card-body d-flex flex-column" v-if="type == 'service'"> -->

    <v-sheet rounded="lg" elevation="6" height="100%" v-if="type == 'service'">
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                گزارش درآمد خدمات
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
            <b-table
              class="MonthlyWidget-table"
              thClass="MonthlyWidget-tableHeader"
              tbody-tr-class="MonthlyWidget-table-row"
              small
              hover
              :responsive="true"
              :items="filteredItems"
              :fields="headersService"
            >
              <template #cell(RevenueUntilStartOfPeriod)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(ModificationToStart)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(TotalYearToStartOfPeriodModified)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(TotalYearIncludingThisPeriod)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(TotalRevLastYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PredictionRevenueYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
              <template #cell(PredictionCostYear)="data">
                <span v-if="data.value != null || data.value != ''"
                  >{{ data.value.toLocaleString() }}
                </span>
                <span v-else>-</span>
              </template>
            </b-table>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش درآمد خدمات
                  </h4>
                </div>
                <v-data-table
                  :headers="headersService"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength itemFilters"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                  loading
                  loading-text="در حال بارگزاری"
                >
                  <template v-slot:[`item.toDate`]="{ item }">
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template v-slot:[`item.contractDate`]="{ item }">
                    <span class="cellItem">{{ item.contractDate }} </span>
                  </template>
                  <template v-slot:[`item.contract_Duration`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.contract_Duration) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.RevenueUntilStartOfPeriod`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.RevenueUntilStartOfPeriod) }}
                    </span>
                  </template>
                  <template v-slot:[`item.ModificationToStart`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.ModificationToStart) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYearToStartOfPeriodModified`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.TotalYearToStartOfPeriodModified)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYearIncludingThisPeriod`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalYearIncludingThisPeriod) }}
                    </span>
                  </template>
                  <template v-slot:[`item.TotalRevLastYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalRevLastYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.PredictionRevenueYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.PredictionRevenueYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.PredictionCostYear`]="{ item }">
                    <span class="cellItem"
                      >{{ numberWithCommas(item.PredictionCostYear) }}
                    </span>
                  </template>
                  <template v-slot:[`item.ItemDesc`]="{ item }">
                    <span class="cellItem">{{ item.ItemDesc }} </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? سهام تحصیل شده -->

    <!-- <div class="card-body d-flex flex-column" v-if="type == 'investment'"> -->
    <v-sheet
      rounded="lg"
      elevation="6"
      height="100%"
      v-if="type == 'investment'"
    >
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
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                پورتفوی
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

            <!--//! here -->
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  سهام تحصیل شده
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems"
                :fields="headesInvestTransIn"
              >
                <template #cell(in_TotalOtcCost)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(in_shareCount)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(in_shareCost)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(in_TotalpublicCost)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
              </b-table>
            </v-card>
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  سهام واگذار شده
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems2"
                :fields="headesInvestTransOut"
              >
                <template #cell(out_shareCount)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(out_shareCost)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(out_TotalCost)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(out_shareSellValue)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(out_TotalSellValue)="data">
                  <span v-if="data.value != null || data.value != ''"
                    >{{ data.value.toLocaleString() }}
                  </span>
                  <span v-else>-</span>
                </template>
                <template #cell(Out_net)="data">
                  <span v-if="data.value == null || data.value == ''">- </span>
                  <span
                    v-else-if="data.value < 0"
                    style="color:red"
                    dir="ltr"
                    >{{ data.value.toLocaleString() }}</span
                  >
                  <span v-else>{{ data.value.toLocaleString() }}</span>
                </template>
              </b-table>
            </v-card>
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  خلاصه
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems3"
                :fields="headesInvestPortfo"
              ></b-table>
            </v-card>
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  پورتفوی سرمایه گذاری
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems4"
                :fields="headesInvestSummary"
              ></b-table>
            </v-card>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    سهام تحصیل شده
                  </h4>
                </div>
                <v-data-table
                  :headers="headesInvestTransIn"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    سهام واگذار شده
                  </h4>
                </div>
                <v-data-table
                  :headers="headesInvestTransOut"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    خلاصه
                  </h4>
                </div>
                <v-data-table
                  :headers="headesInvestPortfo"
                  :items="filteredItems3"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    پورتفوی سرمایه گذاری
                  </h4>
                </div>
                <v-data-table
                  :headers="headesInvestSummary"
                  :items="filteredItems4"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>

    <!--//? گزارش پروژه های فروخته -->
    <!-- <div class="card-body d-flex flex-column" v-if="type == 'construction'"> -->

    <v-sheet
      rounded="lg"
      elevation="6"
      height="100%"
      v-if="type == 'construction'"
    >
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
          <v-card rounded="lg" color="#f0efeb" elevation="7">
            <v-toolbar dense style="height:36px;">
              <v-toolbar-title style="height:20px;font-size:0.95em">
                گزارش های پروژه
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
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  گزارش پروژه های فروخته
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems"
                :fields="headersconstructionSold"
              ></b-table>
            </v-card>
            <v-card rounded="lg" class="mt-2" color="#f0efeb" elevation="0">
              <v-toolbar elevation="1" width="15%" dense style="height:36px;">
                <v-toolbar-title style="height:20px;font-size:0.95em">
                  گزارش پروژه های جاری
                </v-toolbar-title>
              </v-toolbar>
              <b-table
                class="MonthlyWidget-table"
                thClass="MonthlyWidget-tableHeader"
                tbody-tr-class="MonthlyWidget-table-row"
                small
                hover
                :items="filteredItems2"
                :fields="headersconstructionOngoing"
              ></b-table>
            </v-card>
          </v-card>
          <!-- <v-tabs
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
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش پروژه های فروخته
                  </h4>
                </div>
                <v-data-table
                  :headers="headersconstructionSold"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                  loading
                  loading-text="در حال بارگزاری"
                >
                  <template
                    v-slot:[`item.toDate`]="{
                      item
                    }"
                  >
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_Cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_Cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_MeterSold`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_MeterSold) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_SaleAmount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_SaleAmount) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.FromBefore_Cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.FromBefore_Cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_SaleRate`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_SaleRate) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.FromBefore_Revenue`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.FromBefore_Revenue) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYear_Cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalYear_Cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYear_MeterSold`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalYear_MeterSold) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYear_SaleRate`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalYear_SaleRate) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.TotalYear_SaleAmount`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.TotalYear_SaleAmount) }}
                    </span>
                  </template>
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش پروژه های جاری
                  </h4>
                </div>
                <v-data-table
                  :headers="headersconstructionOngoing"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                  <template
                    v-slot:[`item.toDate`]="{
                      item
                    }"
                  >
                    <span class="cellItem">{{ item.toDate }} </span>
                  </template>
                  <template
                    v-slot:[`item.NetMeter`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.NetMeter) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.lastMonth_physicalProgress`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastMonth_physicalProgress) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.lastMonth_Cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastMonth_Cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.lastMonth_EstimationOfRemainingCost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(
                          item.lastMonth_EstimationOfRemainingCost
                        )
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.lastMonth_EstmiatedTotalCost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.lastMonth_EstmiatedTotalCost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.SoldProjectsDuringMonth_meter`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.SoldProjectsDuringMonth_meter)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.SoldProjectsDuringMonth_cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.SoldProjectsDuringMonth_cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_physicalProgress`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_physicalProgress) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_cost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_cost) }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_EstimationRemainingCost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{
                        numberWithCommas(item.thisMonth_EstimationRemainingCost)
                      }}
                    </span>
                  </template>
                  <template
                    v-slot:[`item.thisMonth_EsitmatedTotalCost`]="{
                      item
                    }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.thisMonth_EsitmatedTotalCost) }}
                    </span>
                  </template>
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs> -->
        </v-tab-item>
      </v-tabs>
    </v-sheet>
    <!-- <div
      class="card-body d-flex flex-column"
      v-if="type == '' && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div> -->
  </div>
</template>

<script>
export default {
  name: "MonthlyWidget",
  props: ["notices", "deposits", "portfos", "summaries", "typeOf"],
  data() {
    return {
      loading: true,
      type: "",
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      headersLeasingCost: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "عنوان",
          key: "itemTitle",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "هزینه های دوره",
          key: "thisPeriod_Achievedcost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "هزینه ها از شروع سال مالی",
          key: "Total_Achievedcost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تسهیلات اخذ شده دوره",
          key: "thisPeriod_TakenFacilityRemaind",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تهسیلات اخذ شده سال مالی",
          key: "Total_TakenFacilityRemained",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headersLeasingRevenue: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "عنوان",
          key: "itemTitle",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درآمد دوره",
          key: "thisPeriodAmount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درآمد کل سال مالی",
          key: "TotalAmount",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headersfacility: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "عنوان",
          key: "title",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مانده اول دوره تسهیلات",
          key: "StartPeriod_RemainingFacility",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "اصلاحات",
          key: "StartPeriod_RemainingFacility_modifications",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مانده اول دوره تسهیلات- اصلاح شده",
          key: "StartPeriod_RemainingFacility_modified",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تسهیلات اعطایی طی دوره",
          key: "thisPeriod_IssuedFacilitiy",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تسهیلات وصولی طی دوره",
          key: "thisPeriod_SetteledFacility",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مانده تسهیلات اعطایی پایان دوره",
          key: "EnePeriod_RemainingFacility",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره",
          key: "PreviousPeriods_RevenueFromFacility",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "اصلاحات",
          key: "PreviousPeriods_RevenueFromFacility_modification",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره -اصلاح شده",
          key: "PreviousPeriods_RevenueFromFacility_modified",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: " درآمد تسهیلات اعطایی در طی دوره گزارش",
          key: "thisPeriod_RevenueFromFacility",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "جمع درآمد تسهیلات از ابتدای سال مالی تا پایان دوره گزارش",
          key: "thisYear_RevenueFromFacility",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],
      headersdeposit: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "عنوان",
          value: "title"
        },
        {
          text: "مانده اول دوره سپرده های سرمایه گذاری",
          value: "StartPeriod_Deposits"
        },
        {
          text: "اصلاحات",
          value: "StartPeriod_Deposits_modifications"
        },
        {
          text: "مانده اول دوره سپرده های سرمایه گذاری- اصلاح شده",
          value: "StartPeriod_Deposits_modified"
        },
        {
          text: "سپرده های دریافتی طی دوره",
          value: "thisPeriod_IncomingDeposit"
        },
        {
          text: "سپرده های تسویه شده طی دوره",
          value: "thisPeriod_setteledDeposits"
        },
        {
          text: "مانده سپرده های سرمایه گذاری پایان دوره",
          value: "EndPeriod_Deposits"
        },
        {
          text: "سود سپرده های سرمایه گذاری از ابتدای سال تا ابتدای دوره",
          value: "PreviousPeriods_InterestOnDeposits"
        },
        {
          text: "اصلاحات",
          value: "PreviousPeriods_InterestOnDeposits_modifications"
        },
        {
          text:
            "سود سپرده های سرمایه گذاری از ابتدای سال تا ابتدای دوره -اصلاح شده",
          value: "PreviousPeriods_InterestOnDeposits_modified"
        },
        {
          text: " سود سپرده های سرمایه گذاری طی دوره گزارش",
          value: "thisPeriod_InterestOnDeposits"
        },
        {
          text:
            "جمع سود سپرده سرمایه گذاری از ابتدای سال مالی تا پایان دوره گزارش",
          value: "Total_InterestOnDeposits"
        }
      ],
      heaadersInsurance: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "رشته بیمه ای",
          key: "InsuranceField",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "حق بیمه صادره از ابتدای سال تا ابتدای دوره - مبلغ",
          key: "PreviousPeriods_IssuedInsurance_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "حق بیمه صادره از ابتدای سال تا ابتدای دوره- سهم (درصد)",
          key: "PreviousPeriods_IssuedInusrance_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "خسارت پرداختی از ابتدای سال تا ابتدای دوره - مبلغ",
          key: "PreviousPeriods_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "خسارت پرداختی از ابتدای سال تا ابتدای دوره-سهم (درصد)",
          key: "PreviousPeriods_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "اصلاحات حق بیمه صادره - تا ابتدای دوره - مبلغ",
          key: "Modification_IssuedInsurance_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "اصلاحات خسارت پرداختی تا ابتدای دوره -مبلغ",
          key: "Modification_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "حق بیمه صادره اصلاح شده -تا ابتدای دوره-مبلغ",
          key: "PreviousModified_IssuedInsurance_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "حق بیمه صادره اصلاح شده تا ابتدای دوره-درصد",
          key: "PreviousModified_IssuedInusrance_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "خسارت پرداختی اصلاح شده تا ابتدای دوره -مبلغ",
          key: "PreviousModified_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "خسارت پرداختی اصلاح شده تا ابتدای دوره - سهم",
          key: "PreviousModified_DamageRepaid_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "200px" }
        },
        {
          label: "حق بیمه صادره دوره - مبلغ",
          key: "ThisPeriod_IssuedInsurance_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "حق بیمه صادره دوره - سهم",
          key: "ThisPeriod_IssuedInusrance_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "خسارت پرداختی دوره -مبلغ",
          key: "ThisPeriod_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "خسارت پرداختی دوره -درصد",
          key: "ThisPeriod_DamageRepaid_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "حق بیمه صادره کل سال - مبلغ",
          key: "Total_IssuedInsurance_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "حق بیمه صادره کل سال -سهم",
          key: "Total_IssuedInusrance_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "خسارت پرداختی کل سال -مبلغ",
          key: "Total_DamageRepaid_Amount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "خسارت پرداختی کل سال -درصد",
          key: "Total_DamageRepaid_Share",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        }
      ],

      headersconstructionSold: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm"
        // },
        {
          label: "عنوان پروژه",
          key: "projectName",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "موقعیت پروژه",
          key: "Location",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "نوع پروژه",
          key: "typeOfProject",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "واحد",
          key: "projectUnit",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده فروش در ماه جاری",
          key: "thisMonth_Cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "متراژ فروش ماه جاری",
          key: "thisMonth_MeterSold",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "نرخ فروش در ماه جاری",
          key: "thisMonth_SaleRate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مبلغ فروش ماه جاری",
          key: "thisMonth_SaleAmount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده شناسایی شده ",
          key: "FromBefore_Cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درآمد شناسایی شده",
          key: "FromBefore_Revenue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده از ابتدای سال مالی تا پایان دوره",
          key: "TotalYear_Cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "متراژ فروش کل سال",
          key: "TotalYear_MeterSold",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "نرخ فروش کل سال",
          key: "TotalYear_SaleRate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مبلغ فروش",
          key: "TotalYear_SaleAmount",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headersconstructionOngoing: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm"
        // },
        {
          label: "عنوان پروژه",
          key: "projectName",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "موقعیت پروژه",
          key: "Location",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "نوع پروژه",
          key: "typeOfProject",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درصد مالکیت",
          key: "Ownership",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "واحد",
          key: "projectUnit",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "زیر بنای مفید",
          key: "NetMeter",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درصد پیشرفت فیزیکی در انتهای ماه قبل",
          key: "lastMonth_physicalProgress",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مبلغ بهای تمام شده در انتهای ماه قبل",
          key: "lastMonth_Cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "برآورد هزینه های مانده در انتهای ماه قبل",
          key: "lastMonth_EstimationOfRemainingCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مبلغ بهای تمام شده برآوردی در انتهای ماه قبل",
          key: "lastMonth_EstmiatedTotalCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "متراژ پروژه های فروش رفته در طی ماه",
          key: "SoldProjectsDuringMonth_meter",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده پروژه های فروش رفته طی ماه",
          key: "SoldProjectsDuringMonth_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درصد پیشرفت فیزیکی در پایان ماه",
          key: "thisMonth_physicalProgress",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده در پایان ماه",
          key: "thisMonth_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "برآورد هزینه های تکمیل در پایان ماه",
          key: "thisMonth_EstimationRemainingCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مبلغ بهای تمام شده برآوردی در پایان ماه",
          key: "thisMonth_EsitmatedTotalCost",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headesInvestTransIn: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "خریداری شده",
          key: "in_firm",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد سهم خریداری شده",
          key: "in_shareCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده هر سهم ",
          key: "in_shareCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "کل مبلغ تمام شده پذیرفته شده در بورس",
          key: "in_TotalpublicCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "کل مبلغ بهای تمام شده خارج از بورس",
          key: "in_TotalOtcCost",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headesInvestTransOut: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "واگذار شده",
          key: "out_firm",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد سهم واگذار شده",
          key: "out_shareCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده هر سهم ",
          key: "out_shareCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "کل مبلغ تمام شده",
          key: "out_TotalCost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: " قیمت واگذاری هر سهم",
          key: "out_shareSellValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "کل مبلغ واگذاری",
          key: "out_TotalSellValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "سود (زیان ) واگذاری",
          key: "Out_net",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headesInvestPortfo: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm"
        // },
        {
          label: "نوع شرکت",
          key: "typeOfCompany",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "شرکت",
          key: "company",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "سرمایه ",
          key: "companyCapital",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش اسمی هر سهم",
          key: "companyshare_NominalValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: " تعداد سهم ابتدای دوره",
          key: "start_companyShare",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده ابتدای دوره",
          key: "start_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش بازار ابتدای دوره",
          key: "start_sharesMarketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تغییرات تعداد سهام طی دوره",
          key: "changes_companyShare",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تغییرات بهای تمام شده طی دوره",
          key: "changes_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تغییرات ارزش بازار طی دوره",
          key: "changes_sharesMarketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "درصد مالکیت انتهای دوره",
          key: "end_ownPercentage",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده انتهای دوره",
          key: "end_costperShare",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "کل مبلغ واگذاری",
          key: "end_costTotal",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش بازار انتهای دوره",
          key: "end_MarketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش هر سهم انتهای دوره",
          key: "end_valueperShare",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "افزایش (کاهش) انتهای دوره",
          key: "end_TotalChange",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headesInvestSummary: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm"
        // },
        {
          label: "صنعت",
          key: "industry",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد شرکت های بورسی",
          key: "public_start_companyCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده شرکت های بورسی ابتدای دوره ",
          key: "public_start_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش بازار شرکت های بورسی در ابتدای دوره",
          key: "public_start_marketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: " تغییرات ارزش بازار شرکت های بورسی",
          key: "public_changes_marketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد شرکت های بورسی در انتهای دوره",
          key: "public_end_companyCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده شرکتهای بورسی در انتهای دوره",
          key: "public_end_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "ارزش بازار شرکت های بورسی در انتهای دوره",
          key: "public_end_marketValue",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد شرکتهای غیر بورسی در ابتدای دوره",
          key: "private_start_companyCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده شرکتهای غیر بورسی در ابتدای دوره",
          key: "private_start_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تغییرات بهای تمام شده شرکتهای غیر بورسی ",
          key: "private_changes_cost",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "تعداد شرکتهای غیر بورسی در انتهای دوره",
          key: "private_end_companyCount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "بهای تمام شده شرکتهای غیر بورسی در انتهای دوره",
          key: "private_end_cost",
          thClass: "MonthlyWidget-tableHeader"
        }
      ],

      headersProduction: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "20px" }
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm",
        // thClass:"MonthlyWidget-tableHeader"
        // },
        {
          label: "عنوان",
          key: "name",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "واحد",
          key: "unit",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "50px" }
        },
        {
          label: "وضعیت",
          key: "status",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "دسته بندی",
          key: "category",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "90px" }
        },
        {
          label: "مجموع تولیدات دوره",
          key: "totalProductionPeriod",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مجموع فروش دوره",
          key: "totalSalePeriod",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مبلغ فروش دوره",
          key: "saleAmountPeriod",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "تولید کل دوره",
          key: "totalProductionYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "فروش کل دوره",
          key: "totalSaleYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "نرخ فروش کل دوره",
          key: "saleRateYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مبلغ فروش کل دوره",
          key: "saleAmountYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مجموع تولید تا ابتدای دوره",
          key: "prevTotalProductionYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "مجموع فروش تا ابتدای دوره",
          key: "prevTotalSalesYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "120px" }
        },
        {
          label: "نرخ فروش تا ابتدای دوره",
          key: "prevTotalSalesRateYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مجموع مبلغ فروش تا ابتدای دوره",
          key: "prevTotalSalesAmountYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "اصلاحات تولید",
          key: "modification_Production",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "اصلاحات فروش",
          key: "modification_Sales",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "اصلاحات مبلغ",
          key: "modification_SalesAmount",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مجموع تولید تا ابتدای دوره-اصلاح شده",
          key: "prev_modified_TotalProduction",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "مجموع فروش تا ابتدای دوره- اصلاح شده",
          key: "prev_modified_TotalSales",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "نرخ فروش تا ابتدای دوره- اصلاح شده",
          key: "prev_modified_TotalSalesRate",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "مبلغ فروش تا ابتدای دوره- اصلاح شده",
          key: "prev_modified_TotalSalesAmount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },

        {
          label: "تولید سال مالی فبل",
          key: "lastyear_Production",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "تعداد فروش سال مالی قبل",
          key: "lastyear_saleCount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },

        {
          label: "نرخ فروش سال مالی قبل",
          key: "lastyear_saleRate",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        {
          label: "مبلغ فروش سال مالی قبل",
          key: "lastyear_saleAmount",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        }
      ],

      headersService: [
        {
          label: "منتهی به",
          key: "toDate",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "100px" }
        },
        // {
        //   label: "شرکت گزارش دهنده",
        //   key: "reported_firm"
        // },
        {
          label: "عنوان",
          key: "name",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "350px" }
        },
        {
          label: "تاریخ عقد قرارداد",
          key: "contractDate",
          thClass: "MonthlyWidget-tableHeader"
        },
        {
          label: "مدت قرارداد",
          key: "contract_Duration",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "درآمد تا ابتدای دوره",
          key: "RevenueUntilStartOfPeriod",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "اصلاحات تا ابتدای دوره",
          key: "ModificationToStart",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "درآمد از ابتدای سال - اصلاح شده",
          key: "TotalYearToStartOfPeriodModified",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "درآمد کل سال",
          key: "TotalYearIncludingThisPeriod",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "درآمد کل سال مالی قبل",
          key: "TotalRevLastYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "پیش بینی درآمد سال",
          key: "PredictionRevenueYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "پیش بینی هزینه های سال",
          key: "PredictionCostYear",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "150px" }
        },
        {
          label: "توضیحات",
          key: "ItemDesc",
          thClass: "MonthlyWidget-tableHeader",
          thStyle: { "min-width": "350px" }
        }
      ]
    };
  },
  computed: {
    selectedDatesList() {
      let items = [];
      for (let item of this.todates) items.push(item.value);

      return items;
    },
    filteredItems() {
      return this.notices.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems2() {
      return this.deposits.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems3() {
      return this.portfos.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems4() {
      return this.summaries.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    }
  },
  methods: {
    categoryProduct(x) {
      if (x === null) {
        return "";
      }
      if (x == "Domestic_Sale") {
        return "فروش داخلی";
      }
      if (x == "Export_Sale") {
        return "فروش صادراتی";
      }
      if (x == "Whole") {
        return "عمده";
      }
      if (x == "Discount") {
        return "تخفیف";
      }
      if (x == "Refund") {
        return "بازگشت از فروش";
      }
      if (x == "Service_revenue") {
        return "خدمات";
      }
      return "";
    },
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
          result.push(itemOne);
          counter += 1;
        }
        if (!(name.split("/")[0] in lookup2)) {
          lookup2[name.split("/")[0]] = 1;
          var itemTwo = {};
          itemTwo["key"] = counter;
          itemTwo["value"] = name.split("/")[0];
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
      // this.selectedYear = this.todatesyears[0].value;
    },
    setType() {
      this.type = this.typeOf;
    }
  },
  mounted() {
    // this.populateData();
    this.setType();
  },
  watch: {
    notices() {
      // this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
    },
    deposits() {
      // this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
    },
    portfos() {
      // this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
    },
    summaries() {
      // this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
    },
    selectedYear: function() {
      this.getOnesfromthisyear();
      this.SetNewPagefirstMonth();
    },
    typeOf() {
      this.setType();
    }
  }
};
</script>
<style scoped>
.MonthlyWidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.MonthlyWidget-table /deep/ .MonthlyWidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
  /* min-width: 200px; */
}
.MonthlyWidget-table /deep/ .ticker-assembly-table-row {
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

.cellItem {
  font-family: "Vazir-Light-FD";
}

.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
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
