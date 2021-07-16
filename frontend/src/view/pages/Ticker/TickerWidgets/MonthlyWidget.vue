<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        گزارش ماهیانه
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          
        ></b-spinner>
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column" v-if="type == 'bank'">
      <v-tabs
        background-color="#1e1e2d"
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div class="card-body d-flex flex-column" v-if="type == 'insurance'">
      <v-tabs
        background-color="#1e1e2d"
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div class="card-body d-flex flex-column" v-if="type == 'production'">
      <v-tabs
        background-color="#1e1e2d"
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
                      >{{ numberWithCommas(item.status) }}
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>

    <div class="card-body d-flex flex-column" v-if="type == 'leasing'">
      <v-tabs
        background-color="#1e1e2d"
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
                <!-- <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش تولید و فروش
                  </h4>
                </div>
               
                <v-data-table
                  :headers="headersLeasingDelegated"
                  :items="filteredItems3"
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
                      >{{ numberWithCommas(item.status) }}
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
                </v-data-table> -->
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div class="card-body d-flex flex-column" v-if="type == 'service'">
      <v-tabs
        background-color="#1e1e2d"
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
                  <!-- <template
                    v-slot:[`item.RevenueUntilStartOfPeriod`]="{ item }"
                  >
                    <span class="cellItem"
                      >{{ numberWithCommas(item.RevenueUntilStartOfPeriod) }}
                    </span>
                  </template> -->
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div class="card-body d-flex flex-column" v-if="type == 'investment'">
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>

    <div class="card-body d-flex flex-column" v-if="type == 'construction'">
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
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == '' && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "MonthlyWidget",
  props: ["notices", "deposits", "portfos", "summaries", "typeOf"],
  data() {
    return {
      search: "",
      loading: true,
      type: "",
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      headersLeasingCost: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "عنوان",
          value: "itemTitle"
        },
        {
          text: "هزینه های دوره",
          value: "thisPeriod_Achievedcost"
        },
        {
          text: "هزینه ها از شروع سال مالی",
          value: "Total_Achievedcost"
        },
        {
          text: "تسهیلات اخذ شده دوره",
          value: "thisPeriod_TakenFacilityRemaind"
        },
        {
          text: "تهسیلات اخذ شده سال مالی",
          value: "Total_TakenFacilityRemained"
        }
      ],
      headersLeasingRevenue: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "عنوان",
          value: "itemTitle"
        },
        {
          text: "درآمد دوره",
          value: "thisPeriodAmount"
        },
        {
          text: "درآمد کل سال مالی",
          value: "TotalAmount"
        }
      ],
      headersfacility: [
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
          text: "مانده اول دوره تسهیلات",
          value: "StartPeriod_RemainingFacility"
        },
        {
          text: "اصلاحات",
          value: "StartPeriod_RemainingFacility_modifications"
        },
        {
          text: "مانده اول دوره تسهیلات- اصلاح شده",
          value: "StartPeriod_RemainingFacility_modified"
        },
        {
          text: "تسهیلات اعطایی طی دوره",
          value: "thisPeriod_IssuedFacilitiy"
        },
        {
          text: "تسهیلات وصولی طی دوره",
          value: "thisPeriod_SetteledFacility"
        },
        {
          text: "مانده تسهیلات اعطایی پایان دوره",
          value: "EnePeriod_RemainingFacility"
        },
        {
          text: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره",
          value: "PreviousPeriods_RevenueFromFacility"
        },
        {
          text: "اصلاحات",
          value: "PreviousPeriods_RevenueFromFacility_modification"
        },
        {
          text: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره -اصلاح شده",
          value: "PreviousPeriods_RevenueFromFacility_modified"
        },
        {
          text: " درآمد تسهیلات اعطایی در طی دوره گزارش",
          value: "thisPeriod_RevenueFromFacility"
        },
        {
          text: "جمع درآمد تسهیلات از ابتدای سال مالی تا پایان دوره گزارش",
          value: "thisYear_RevenueFromFacility"
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
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        // {
        //   text: "عنوان",
        //   value: "title"
        // },
        {
          text: "رشته بیمه ای",
          value: "InsuranceField"
        },
        {
          text: "حق بیمه صادره از ابتدای سال تا ابتدای دوره - مبلغ",
          value: "PreviousPeriods_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره از ابتدای سال تا ابتدای دوره- سهم (درصد)",
          value: "PreviousPeriods_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی از ابتدای سال تا ابتدای دوره - مبلغ",
          value: "PreviousPeriods_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی از ابتدای سال تا ابتدای دوره-سهم (درصد)",
          value: "PreviousPeriods_DamageRepaid_Amount"
        },
        {
          text: "اصلاحات حق بیمه صادره - تا ابتدای دوره - مبلغ",
          value: "Modification_IssuedInsurance_Amount"
        },
        {
          text: "اصلاحات خسارت پرداختی تا ابتدای دوره -مبلغ",
          value: "Modification_DamageRepaid_Amount"
        },
        {
          text: "حق بیمه صادره اصلاح شده -تا ابتدای دوره-مبلغ",
          value: "PreviousModified_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره اصلاح شده تا ابتدای دوره-درصد",
          value: "PreviousModified_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی اصلاح شده تا ابتدای دوره -مبلغ",
          value: "PreviousModified_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی اصلاح شده تا ابتدای دوره - سهم",
          value: "PreviousModified_DamageRepaid_Share"
        },
        {
          text: "حق بیمه صادره دوره - مبلغ",
          value: "ThisPeriod_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره دوره - سهم",
          value: "ThisPeriod_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی دوره -مبلغ",
          value: "ThisPeriod_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی دوره -درصد",
          value: "ThisPeriod_DamageRepaid_Share"
        },
        {
          text: "حق بیمه صادره کل سال - مبلغ",
          value: "Total_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره کل سال -سهم",
          value: "Total_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی کل سال -مبلغ",
          value: "Total_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی کل سال -درصد",
          value: "Total_DamageRepaid_Share"
        }
      ],
      headersconstructionSold: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "عنوان پروژه",
          value: "projectName"
        },
        {
          text: "موقعیت پروژه",
          value: "Location"
        },
        {
          text: "نوع پروژه",
          value: "typeOfProject"
        },
        {
          text: "واحد",
          value: "projectUnit"
        },
        {
          text: "بهای تمام شده فروش در ماه جاری",
          value: "thisMonth_Cost"
        },
        {
          text: "متراژ فروش ماه جاری",
          value: "thisMonth_MeterSold"
        },
        {
          text: "نرخ فروش در ماه جاری",
          value: "thisMonth_SaleRate"
        },
        {
          text: "مبلغ فروش ماه جاری",
          value: "thisMonth_SaleAmount"
        },
        {
          text: "بهای تمام شده شناسایی شده ",
          value: "FromBefore_Cost"
        },
        {
          text: "درآمد شناسایی شده",
          value: "FromBefore_Revenue"
        },
        {
          text: "بهای تمام شده از ابتدای سال مالی تا پایان دوره",
          value: "TotalYear_Cost"
        },
        {
          text: "متراژ فروش کل سال",
          value: "TotalYear_MeterSold"
        },
        {
          text: "نرخ فروش کل سال",
          value: "TotalYear_SaleRate"
        },
        {
          text: "مبلغ فروش",
          value: "TotalYear_SaleAmount"
        }
      ],
      headersconstructionOngoing: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "عنوان پروژه",
          value: "projectName"
        },
        {
          text: "موقعیت پروژه",
          value: "Location"
        },
        {
          text: "نوع پروژه",
          value: "typeOfProject"
        },
        {
          text: "درصد مالکیت",
          value: "Ownership"
        },
        {
          text: "واحد",
          value: "projectUnit"
        },
        {
          text: "زیر بنای مفید",
          value: "NetMeter"
        },
        {
          text: "درصد پیشرفت فیزیکی در انتهای ماه قبل",
          value: "lastMonth_physicalProgress"
        },
        {
          text: "مبلغ بهای تمام شده در انتهای ماه قبل",
          value: "lastMonth_Cost"
        },
        {
          text: "برآورد هزینه های مانده در انتهای ماه قبل",
          value: "lastMonth_EstimationOfRemainingCost"
        },
        {
          text: "مبلغ بهای تمام شده برآوردی در انتهای ماه قبل",
          value: "lastMonth_EstmiatedTotalCost"
        },
        {
          text: "متراژ پروژه های فروش رفته در طی ماه",
          value: "SoldProjectsDuringMonth_meter"
        },
        {
          text: "بهای تمام شده پروژه های فروش رفته طی ماه",
          value: "SoldProjectsDuringMonth_cost"
        },
        {
          text: "درصد پیشرفت فیزیکی در پایان ماه",
          value: "thisMonth_physicalProgress"
        },
        {
          text: "بهای تمام شده در پایان ماه",
          value: "thisMonth_cost"
        },
        {
          text: "برآورد هزینه های تکمیل در پایان ماه",
          value: "thisMonth_EstimationRemainingCost"
        },
        {
          text: "مبلغ بهای تمام شده برآوردی در پایان ماه",
          value: "thisMonth_EsitmatedTotalCost"
        }
      ],
      headesInvestTransIn: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "خریداری شده",
          value: "in_firm"
        },
        {
          text: "تعداد سهم خریداری شده",
          value: "in_shareCount"
        },
        {
          text: "بهای تمام شده هر سهم ",
          value: "in_shareCost"
        },
        {
          text: "کل مبلغ تمام شده پذیرفته شده در بورس",
          value: "in_TotalpublicCost"
        },
        {
          text: "کل مبلغ بهای تمام شده خارج از بورس",
          value: "in_TotalOtcCost"
        }
      ],
      headesInvestTransOut: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "واگذار شده",
          value: "out_firm"
        },
        {
          text: "تعداد سهم واگذار شده",
          value: "out_shareCount"
        },
        {
          text: "بهای تمام شده هر سهم ",
          value: "out_shareCost"
        },
        {
          text: "کل مبلغ تمام شده",
          value: "out_TotalCost"
        },
        {
          text: " قیمت واگذاری هر سهم",
          value: "out_shareSellValue"
        },
        {
          text: "کل مبلغ واگذاری",
          value: "out_TotalSellValue"
        },
        {
          text: "سود (زیان ) واگذاری",
          value: "Out_net"
        }
      ],
      headesInvestPortfo: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "نوع شرکت",
          value: "typeOfCompany"
        },
        {
          text: "شرکت",
          value: "company"
        },
        {
          text: "سرمایه ",
          value: "companyCapital"
        },
        {
          text: "ارزش اسمی هر سهم",
          value: "companyshare_NominalValue"
        },
        {
          text: " تعداد سهم ابتدای دوره",
          value: "start_companyShare"
        },
        {
          text: "بهای تمام شده ابتدای دوره",
          value: "start_cost"
        },
        {
          text: "ارزش بازار ابتدای دوره",
          value: "start_sharesMarketValue"
        },
        {
          text: "تغییرات تعداد سهام طی دوره",
          value: "changes_companyShare"
        },
        {
          text: "تغییرات بهای تمام شده طی دوره",
          value: "changes_cost"
        },
        {
          text: "تغییرات ارزش بازار طی دوره",
          value: "changes_sharesMarketValue"
        },
        {
          text: "درصد مالکیت انتهای دوره",
          value: "end_ownPercentage"
        },
        {
          text: "بهای تمام شده انتهای دوره",
          value: "end_costperShare"
        },
        {
          text: "کل مبلغ واگذاری",
          value: "end_costTotal"
        },
        {
          text: "ارزش بازار انتهای دوره",
          value: "end_MarketValue"
        },
        {
          text: "ارزش هر سهم انتهای دوره",
          value: "end_valueperShare"
        },
        {
          text: "افزایش (کاهش) انتهای دوره",
          value: "end_TotalChange"
        }
      ],
      headesInvestSummary: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        // {
        //   text: "شرکت گزارش دهنده",
        //   value: "reported_firm"
        // },
        {
          text: "صنعت",
          value: "industry"
        },
        {
          text: "تعداد شرکت های بورسی",
          value: "public_start_companyCount"
        },
        {
          text: "بهای تمام شده شرکت های بورسی ابتدای دوره ",
          value: "public_start_cost"
        },
        {
          text: "ارزش بازار شرکت های بورسی در ابتدای دوره",
          value: "public_start_marketValue"
        },
        {
          text: " تغییرات ارزش بازار شرکت های بورسی",
          value: "public_changes_marketValue"
        },
        {
          text: "تعداد شرکت های بورسی در انتهای دوره",
          value: "public_end_companyCount"
        },
        {
          text: "بهای تمام شده شرکتهای بورسی در انتهای دوره",
          value: "public_end_cost"
        },
        {
          text: "ارزش بازار شرکت های بورسی در انتهای دوره",
          value: "public_end_marketValue"
        },
        {
          text: "تعداد شرکتهای غیر بورسی در ابتدای دوره",
          value: "private_start_companyCount"
        },
        {
          text: "بهای تمام شده شرکتهای غیر بورسی در ابتدای دوره",
          value: "private_start_cost"
        },
        {
          text: "تغییرات بهای تمام شده شرکتهای غیر بورسی ",
          value: "private_changes_cost"
        },
        {
          text: "تعداد شرکتهای غیر بورسی در انتهای دوره",
          value: "private_end_companyCount"
        },
        {
          text: "بهای تمام شده شرکتهای غیر بورسی در انتهای دوره",
          value: "private_end_cost"
        }
      ],

      headersProduction: [
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
          value: "name"
        },
        {
          text: "واحد",
          value: "unit"
        },
        {
          text: "وضعیت",
          value: "status"
        },
        {
          text: "دسته بندی",
          value: "category"
        },
        {
          text: "مجموع تولیدات دوره",
          value: "totalProductionPeriod"
        },
        {
          text: "مجموع فروش دوره",
          value: "totalSalePeriod"
        },
        {
          text: "مبلغ فروش دوره",
          value: "saleAmountPeriod"
        },
        { text: "تولید کل دوره", value: "totalProductionYear" },
        { text: "فروش کل دوره", value: "totalSaleYear" },
        { text: "نرخ فروش کل دوره", value: "saleRateYear" },
        { text: "مبلغ فروش کل دوره", value: "saleAmountYear" },
        {
          text: "مجموع تولید تا ابتدای دوره",
          value: "prevTotalProductionYear"
        },
        { text: "مجموع فروش تا ابتدای دوره", value: "prevTotalSalesYear" },
        { text: "نرخ فروش تا ابتدای دوره", value: "prevTotalSalesRateYear" },
        {
          text: "مجموع مبلغ فروش تا ابتدای دوره",
          value: "prevTotalSalesAmountYear"
        },
        { text: "اصلاحات تولید", value: "modification_Production" },
        { text: "اصلاحات فروش", value: "modification_Sales" },
        { text: "اصلاحات مبلغ", value: "modification_SalesAmount" },
        {
          text: "مجموع تولید تا ابتدای دوره-اصلاح شده",
          value: "prev_modified_TotalProduction"
        },
        {
          text: "مجموع فروش تا ابتدای دوره- اصلاح شده",
          value: "prev_modified_TotalSales"
        },
        {
          text: "نرخ فروش تا ابتدای دوره- اصلاح شده",
          value: "prev_modified_TotalSalesRate"
        },
        {
          text: "مبلغ فروش تا ابتدای دوره- اصلاح شده",
          value: "prev_modified_TotalSalesAmount"
        },

        {
          text: "تولید سال مالی فبل",
          value: "lastyear_Production"
        },
        {
          text: "تعداد فروش سال مالی قبل",
          value: "lastyear_saleCount"
        },

        {
          text: "نرخ فروش سال مالی قبل",
          value: "lastyear_saleRate"
        },
        {
          text: "مبلغ فروش سال مالی قبل",
          value: "lastyear_saleAmount"
        }
      ],
      headersService: [
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
          value: "name"
        },
        {
          text: "تاریخ عقد قرارداد",
          value: "contractDate"
        },
        {
          text: "مدت قرارداد",
          value: "contract_Duration"
        },
        {
          text: "درآمد تا ابتدای دوره",
          value: "RevenueUntilStartOfPeriod"
        },
        {
          text: "اصلاحات تا ابتدای دوره",
          value: "ModificationToStart"
        },
        {
          text: "درآمد از ابتدای سال - اصلاح شده",
          value: "TotalYearToStartOfPeriodModified"
        },
        {
          text: "درآمد کل سال",
          value: "TotalYearIncludingThisPeriod"
        },
        { text: "درآمد کل سال مالی قبل", value: "TotalRevLastYear" },
        { text: "پیش بینی درآمد سال", value: "PredictionRevenueYear" },
        { text: "پیش بینی هزینه های سال", value: "PredictionCostYear" },
        {
          text: "توضیحات",
          value: "ItemDesc"
        }
      ],
      DataItems2: [],
      DataItems3: [],
      DataItems4: [],
      DataItems5: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      return this.DataItems2.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems2() {
      return this.DataItems3.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems3() {
      return this.DataItems4.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems4() {
      return this.DataItems5.filter(item => {
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

    populateData() {
      this.DataItems2 = this.notices;
      this.DataItems3 = this.deposits;
      this.DataItems4 = this.portfos;
      this.DataItems5 = this.summaries;
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
    },
    setType() {
      this.type = this.typeOf;
    }
  },
  mounted() {
    this.populateData();
    this.setType();
  },
  watch: {
    notices() {
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
    },
    deposits() {
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
    },
    portfos() {
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
    },
    summaries() {
      this.populateData();
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
.cellItem {
  font-family: "Vazir-Light-FD";
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
