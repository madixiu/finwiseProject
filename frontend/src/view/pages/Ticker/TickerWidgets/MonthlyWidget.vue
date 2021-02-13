<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        گزارش ماهیانه
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
      v-if="type == 'bank' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
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
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'insurance' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
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
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'production' && loading == false"
    >
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
                >
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>

    <div
      class="card-body d-flex flex-column"
      v-if="type == 'leasing' && loading == false"
    >
      <span class="rtl_centerd">leasing</span>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'service' && loading == false"
    >
      <span class="rtl_centerd">service</span>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'investment' && loading == false"
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
                    پورتفوی سرمایه گذاری
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
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>

    <div
      class="card-body d-flex flex-column"
      v-if="type == 'construction' && loading == false"
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
                >
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
      headersfacility: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان",
          value: "title"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
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
        }
        ,
        {
          text: "ارزش هر سهم انتهای دوره",
          value: "end_valueperShare"
        }
        ,
        {
          text: "افزایش (کاهش) انتهای دوره",
          value: "end_TotalChange"
        }
        
      ],
      headesInvestSummary: [],
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
          value: "product"
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

        { text: "تولید سال مالی فبل", value: "lastyear_Production" },
        { text: "تعداد فروش سال مالی قبل", value: "lastyear_saleCount" },

        { text: "نرخ فروش سال مالی قبل", value: "lastyear_saleRate" },
        { text: "مبلغ فروش سال مالی قبل", value: "lastyear_saleAmount" }
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
      // console.log(result);
      // console.log(this.selectedYear);
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
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      this.selectedYear = this.todatesyears[0].value;
    },
    SetNewPagefirstMonth() {
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      // this.selectedYear = this.todatesyears[0].value;
    },
    setType() {
      this.type = this.typeOf;
      console.log(this.type);
      console.log(this.deposits);
    }
  },
  mounted() {
    this.populateData();
    this.setType();
  },
  watch: {
    notices() {
      console.log("Watcher");
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
      console.log(this.notices);
    },
    deposits() {
      console.log("Watcher");
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();

      console.log(this.notices);
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
  font-family: "Dirooz FD";
  font-weight: 700;
  font-size: 1em;
}
table.v-table tbody td {
  font-family: "Dirooz FD" !important;
}
</style>
