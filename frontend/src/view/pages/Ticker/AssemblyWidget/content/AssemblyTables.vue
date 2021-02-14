<template>
  <div class="row">
    <div class="col-xxl-12 col-lg-12 " v-if="ICitems.length">
      <v-card>
        <v-card-title>افزایش سرمایه</v-card-title>
        <b-table
          class="ticker-assembly-table"
          thClass="ticker-assembly-table-head"
          striped
          bordered
          outlined
          small
          hover
          fixed
          :items="ICitems"
          :fields="stepThreeItemsTableHeaders.ICheaders"
        ></b-table>
      </v-card>
    </div>

    <div class="col-4">
      <!-- Chief Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="ChiefItems.length">
        <v-card>
          <v-card-title>هیئت رییسه</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="ChiefItems"
            :fields="stepThreeItemsTableHeaders.ChiefHeaders"
          ></b-table>
        </v-card>
      </div>

      <!-- CEO Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="CEOItems.length">
        <v-card>
          <v-card-title>مدیر عامل</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="CEOItems"
            :fields="stepThreeItemsTableHeaders.CEOheaders"
          ></b-table>
        </v-card>
      </div>

      <!-- NewBoard Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="NewBoardItems.length">
        <v-card>
          <v-card-title>هیئت مدیره جدید</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="NewBoardItems"
            :fields="stepThreeItemsTableHeaders.NewBoardHeaders"
          ></b-table>
        </v-card>
      </div>

      <!-- Wage Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="WageItems.length">
        <v-card>
          <v-card-title>حقوق و مزایای هیئت مدیره</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="WageItems"
            :fields="stepThreeItemsTableHeaders.WageHeaders"
          ></b-table>
        </v-card>
      </div>
    </div>
    <div class="col-4">
      <!-- Shareholders Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="ShareholdersItems.length">
        <v-card>
          <v-card-title>سهامداران</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="ShareholdersItems"
            :fields="stepThreeItemsTableHeaders.ShareholdersHeaders"
          ></b-table>
        </v-card>
      </div>

      <!-- Board Table -->

      <div class="col-xxl-12 col-lg-12 " v-if="BoardItems.length">
        <v-card>
          <v-card-title>هیئت مدیره</v-card-title>
          <b-table
            class="ticker-assembly-table"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="BoardItems"
            :fields="stepThreeItemsTableHeaders.BoardHeaders"
          ></b-table>
        </v-card>
      </div>
    </div>
    <div class="col-4">
      <!-- IC table  -->

      <!-- Statement Table -->
      <div class="col-xxl-12 col-lg-12 " v-if="StatementItems.length">
        <v-card>
          <v-card-title>صورت مصوب</v-card-title>
          <b-table
            class="ticker-assembly-table"
            thClass="ticker-assembly-table-head"
            striped
            bordered
            outlined
            small
            hover
            fixed
            :items="StatementItems"
            :fields="stepThreeItemsTableHeaders.StatementHeaders"
          >
            <!-- <template #cell(Nemad)="data">
                        <b class="ticker-assembly-table-cell-bold">{{ data.value }}</b>
                      </template> -->
          </b-table>
        </v-card>
      </div>
    </div>
    <!-- Summary Table -->

    <!-- <div class="col-xxl-12 col-lg-12" v-if="SummaryItems.length">
                    <v-card>
                      <v-card-title>خلاصه مجمع</v-card-title>
                      <b-table
                        class="ticker-assembly-table"
                        striped
                        bordered
                        outlined
                        small
                        hover
                        fixed
                        :items="SummaryItems"
                        :fields="stepThreeItemsTableHeaders.SummaryHeaders"
                      ></b-table>
                    </v-card>
                  </div> -->
  </div>
</template>
<script>
export default {
  props: {
    ShareholdersItems: Array,
    ChiefItems: Array,
    SummaryItems: Array,
    ICitems: Array,
    StatementItems: Array,
    CEOItems: Array,
    BoardItems: Array,
    NewBoardItems: Array,
    WageItems: Array
  },
  data() {
    return {
      stepThreeItemsTableHeaders: {
        // ShareholdersHeaders: ["درصد مالکیت","تعداد سهام","سهامدار"],

        ICheaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "تعداد سهام", key: "LastShareCount" },
          { label: "ارزش اسمی هر سهم", key: "LastShareNominalValue" },
          { label: "آخرین سرمایه ثبتی", key: "LastCapital" },
          { label: "مطالبات و آورده نقدی-قطعی", key: "CashIncoming_Final" },
          {
            label: "مطالبات و آورده نقدی-در اختیار هیئت مدیره",
            key: "CashIncoming_Ceo"
          },
          { label: "مطالبات و آورده نقدی-کل", key: "CashIncoming_Total" },
          { label: "سود انباشته-قطعی", key: "RetainedEarning_Final" },
          {
            label: "سود انباشته-قطعی در اختیار هیئت مدیره",
            key: "RetainedEarning_Ceo"
          },
          { label: "سود انباشته-کل", key: "RetainedEarning_Sum" },
          { label: "اندوخته-قطعی", key: "Reserves_Final" },
          { label: "اندوخته-در اختیار هیئت مدیره", key: "Reserves_Ceo" },
          { label: "اندوخته-کل", key: "Reserves_Sum" },
          { label: "مازاد تجدید ارزیابی-قطعی", key: "Reevaluation_Final" },
          {
            label: "مازاد تجدید ارزیابی-در اختیار هیئت مدیره",
            key: "Reevaluation_Ceo"
          },
          { label: "مازاد تجدید ارزیابی-کل", key: "Reevaluation_Sum" },
          { label: "صرف سهام-قطعی", key: "SarfSaham_Final" },
          { label: "صرف سهام در اختیار هیئت مدیره", key: "SarfSaham_Ceo" },
          { label: "صرف سهام-کل", key: "SarfSaham_Sum" },
          { label: "مبلغ افزایش سرمایه-قطعی", key: "IncreaseValue_Final" },
          {
            label: "مبلغ افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreaseValue_Ceo"
          },
          { label: "مبلغ افزایش سرمایه-کل", key: "IncreaseValue_Sum" },
          { label: "درصد افزایش سرمایه-قطعی", key: "IncreasePercent_Final" },
          {
            label: "درصد افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreasePercent_Ceo"
          },
          { label: "درصد افزایش سرمایه-کل", key: "IncreasePercent_Sum" }
        ],
        StatementHeaders: [
          // { label: "ID", key: "ID", thClass: "ticker-assembly-table-head" },
          // {
          //   label: "SummaryID",
          //   key: "SummaryID"
          // },
          {
            label: "عنوان",
            key: "Title"
          },
          {
            label: "مقدار",
            key: "Value"
          }
        ],
        ChiefHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "Name" },
          { label: "سمت", key: "Position" }
        ],
        ShareholdersHeaders: [
          { label: "سهامدار", key: "Shareholders" },
          {
            label: "تعداد سهام",
            key: "ShareCount"
          },
          {
            label: "درصد مالکیت",
            key: "OwnerPercentage"
          }
        ],
        CEOheaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "FullName" },
          // { label: "SSID", key: "SSID" },
          { label: "مدرک تحصیلی", key: "Degree" }
        ],
        BoardHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "FullName" },
          // { label: "SSID", key: "SSID" },
          { label: "نوع شرکت", key: "typeOfCompany" },
          { label: "عضویت", key: "Membership" },
          { label: "نام نماینده", key: "AgentName" },
          // { label: "AgentSSID", key: "AgentSSID" },
          { label: "سمت", key: "Position" },
          // { label: "Duty", key: "Duty" },
          { label: "مدرک تحصیلی", key: "Degree" }
        ],
        NewBoardHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "نام", key: "Name" },
          { label: "نوع", key: "Type" },
          // { label: "SSID", key: "SSID" },
          { label: "وظیفه", key: "Duty" }
        ],
        WageHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "عنوان", key: "Title" },
          { label: "سال گذشته", key: "LastYear" },
          { label: "سال جاری", key: "CurrentYear" },
          { label: "اطلاعات بیشتر", key: "MoreDetails" }
        ],
        SummaryHeaders: [
          // { label: "ID", key: "ID" },
          // { label: "firm", key: "firm" },
          // { label: "report_id", key: "report_id" },
          { label: "منتهی به", key: "ToDate" },
          { label: "اصلاحات", key: "Correction" },
          { label: "توضیحات اصلاحی", key: "CorrectionDetails" },
          { label: "روزنامه", key: "NewsPaper" },

          { label: "حسابرس", key: "Inspector" },

          { label: "سایر توضیحات", key: "OtherDesc" },

          {
            label: "استماع گزارش هیئت مدیره",
            key: "IsListenedBoardMemberReport"
          },
          { label: "انتخاب حسابرس", key: "IsSelectInspector" },
          { label: "انتخاب روزنامه", key: "IsSelectNewspaper" },
          { label: "تصمیم گیری پاداش هیئت مدیره", key: "IsBoardMemberGift" },
          { label: "دارای توضیحات اضافی", key: "IsOther" },
          { label: "تصمیم گیری حقوق هیئت مدیره", key: "IsBoardMemberWage" },
          { label: "انتخاب اعضای هیئت مدیره", key: "IsSelectBoardMember" },
          { label: "انتشار اوراق بهادار", key: "IsPublishSecurity" },
          { label: "تغییر محل فعالیت شرکت", key: "IsLocationChange" },
          { label: "تغییر نام شرکت", key: "IsNameChange" },
          { label: "تغییر فعالیت شرکت", key: "IsActivitySubjectChange" },
          // {
          //   label: "IsConvertSecurityToShare",
          //   key: "IsConvertSecurityToShare"
          // },
          { label: "تغییر سال مالی", key: "IsFinancialYearChange" },
          { label: "افزایش سرمایه", key: "IsCapitalIncrease" }
        ]
      }
    };
  }
};
</script>
<style>
.ticker-assembly-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.ticker-assembly-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.selectionTable {
  direction: rtl;
  text-align: right;
}
</style>
