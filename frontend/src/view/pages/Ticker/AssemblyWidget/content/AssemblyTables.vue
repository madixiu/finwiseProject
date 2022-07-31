<template>
  <v-row>
    <div class="col-xxl-12 col-lg-12 " v-if="ICitems.length">
      <v-card elevation="14" style="margin-top:5px">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >افزایش سرمایه</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          thClass="ICheader"
          tbody-tr-class="ticker-assembly-table-row"
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

    <div class="col-4" style="padding-left:5px;padding-right:20px">
      <!-- Chief Table -->
      <v-card elevation="14" style="margin-top:5px" v-if="ChiefItems.length">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >هیئت رییسه</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
          striped
          bordered
          outlined
          small
          hover
          fixed
          :items="ChiefItems"
          :fields="stepThreeItemsTableHeaders.ChiefHeaders"
        >
          <template #cell(Position)="data">
            <b v-if="data.value == 'Cheif'" class="ticker-assembly-table-cell"
              >رییس مجمع</b
            >
            <b
              v-if="data.value == 'Supervisor1' || data.value == 'Supervisor2'"
              class="ticker-assembly-table-cell"
              >ناظر مجمع</b
            >
            <b
              v-if="data.value == 'Secretary'"
              class="ticker-assembly-table-cell"
              >منشی مجمع</b
            >
          </template>
        </b-table>
      </v-card>
      <!-- </div> -->

      <!-- CEO Table -->
      <v-card elevation="14" style="margin-top:5px" v-if="CEOItems.length">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >مدیر عامل</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
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
      <!-- </div> -->

      <!-- NewBoard Table -->
      <v-card elevation="14" style="margin-top:5px" v-if="NewBoardItems.length">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >هیئت مدیره جدید</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
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
      <!-- </div> -->

      <!-- Wage Table -->
      <v-card elevation="14" style="margin-top:5px" v-if="WageItems.length">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >حقوق و مزایای هیئت مدیره</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
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
      <!-- </div> -->
    </div>
    <div class="col-4" style="padding-right:0px;padding-left:0px;">
      <!-- Shareholders Table -->
      <v-card
        elevation="14"
        style="margin-top:5px"
        v-if="ShareholdersItems.length"
      >
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >حاضرین</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
          striped
          bordered
          outlined
          small
          hover
          fixed
          :items="ShareholdersItems"
          :fields="stepThreeItemsTableHeaders.ShareholdersHeaders"
        >
          <template #cell(ShareCount)="data">
            <span class="ticker-assembly-table-cell-number">{{
              parseInt(data.value).toLocaleString()
            }}</span>
          </template>
          <template #cell(OwnerPercentage)="data">
            <b class="ticker-assembly-table-cell-number">{{ data.value }}</b>
          </template>
        </b-table>
      </v-card>
      <!-- </div> -->

      <!-- Board Table -->
      <v-card elevation="14" style="margin-top:5px" v-if="BoardItems.length">
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >هیئت مدیره</v-toolbar-title
          >
        </v-toolbar>
        <!-- <v-card-title>هیئت مدیره</v-card-title> -->
        <b-table
          class="ticker-assembly-table"
          tbody-tr-class="ticker-assembly-table-row"
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
    <!-- </div> -->
    <div class="col-4" style="padding-right:5px;padding-left:20px">
      <!-- IC table  -->
      <!-- Statement Table -->
      <v-card
        elevation="14"
        style="margin-top:5px"
        v-if="StatementItems.length"
      >
        <v-toolbar
          dense
          color="#f4f1de"
          class="AssemblyTablesTableToolbars"
          style="height:30px"
        >
          <v-toolbar-title style="height:30px;font-size:0.9em"
            >صورت مصوب</v-toolbar-title
          >
        </v-toolbar>
        <b-table
          class="ticker-assembly-table"
          thClass="ticker-assembly-table-head"
          tbody-tr-class="ticker-assembly-table-row"
          striped
          bordered
          outlined
          small
          hover
          fixed
          :items="StatementItems"
          :fields="stepThreeItemsTableHeaders.StatementHeaders"
        >
          <template #cell(Value)="data">
            <b class="ticker-assembly-table-cell-number">{{
              parseInt(data.value).toLocaleString()
            }}</b>
          </template>
        </b-table>
      </v-card>
      <!-- </div> -->
    </div>
    <!-- Summary Table -->
    <!-- <div class="col-xxl-12 col-lg-12" v-if="SummaryItems.length">
                    <v-card elevation="14" style="margin-top:5px">
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
    <!-- </div> -->
  </v-row>
</template>
<script>
export default {
  name: "AssemblyTables",
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
        ICheaders: [
          // { label: "ID", key: "ID" },
          // { label: "SummaryID", key: "SummaryID" },
          { label: "تعداد سهام", key: "LastShareCount", thClass: "ICheader" },
          {
            label: "ارزش اسمی هر سهم",
            key: "LastShareNominalValue",
            thClass: "ICheader"
          },
          {
            label: "آخرین سرمایه ثبتی",
            key: "LastCapital",
            thClass: "ICheader"
          },
          {
            label: "مطالبات و آورده نقدی-قطعی",
            key: "CashIncoming_Final",
            thClass: "ICheader"
          },
          {
            label: "مطالبات و آورده نقدی-در اختیار هیئت مدیره",
            key: "CashIncoming_Ceo",
            thClass: "ICheader"
          },
          {
            label: "مطالبات و آورده نقدی-کل",
            key: "CashIncoming_Total",
            thClass: "ICheader"
          },
          {
            label: "سود انباشته-قطعی",
            key: "RetainedEarning_Final",
            thClass: "ICheader"
          },
          {
            label: "سود انباشته-قطعی در اختیار هیئت مدیره",
            key: "RetainedEarning_Ceo",
            thClass: "ICheader"
          },
          {
            label: "سود انباشته-کل",
            key: "RetainedEarning_Sum",
            thClass: "ICheader"
          },
          { label: "اندوخته-قطعی", key: "Reserves_Final", thClass: "ICheader" },
          {
            label: "اندوخته-در اختیار هیئت مدیره",
            key: "Reserves_Ceo",
            thClass: "ICheader"
          },
          { label: "اندوخته-کل", key: "Reserves_Sum", thClass: "ICheader" },
          {
            label: "مازاد تجدید ارزیابی-قطعی",
            key: "Reevaluation_Final",
            thClass: "ICheader"
          },
          {
            label: "مازاد تجدید ارزیابی-در اختیار هیئت مدیره",
            key: "Reevaluation_Ceo",
            thClass: "ICheader"
          },
          {
            label: "مازاد تجدید ارزیابی-کل",
            key: "Reevaluation_Sum",
            thClass: "ICheader"
          },
          {
            label: "صرف سهام-قطعی",
            key: "SarfSaham_Final",
            thClass: "ICheader"
          },
          {
            label: "صرف سهام در اختیار هیئت مدیره",
            key: "SarfSaham_Ceo",
            thClass: "ICheader"
          },
          { label: "صرف سهام-کل", key: "SarfSaham_Sum", thClass: "ICheader" },
          {
            label: "مبلغ افزایش سرمایه-قطعی",
            key: "IncreaseValue_Final",
            thClass: "ICheader"
          },
          {
            label: "مبلغ افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreaseValue_Ceo",
            thClass: "ICheader"
          },
          {
            label: "مبلغ افزایش سرمایه-کل",
            key: "IncreaseValue_Sum",
            thClass: "ICheader"
          },
          {
            label: "درصد افزایش سرمایه-قطعی",
            key: "IncreasePercent_Final",
            thClass: "ICheader"
          },
          {
            label: "درصد افزایش سرمایه-در اختیار هیئت مدیره",
            key: "IncreasePercent_Ceo",
            thClass: "ICheader"
          },
          {
            label: "درصد افزایش سرمایه-کل",
            key: "IncreasePercent_Sum",
            thClass: "ICheader"
          }
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
  text-align: center;
}
.ticker-assembly-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-family: "Vazir-Medium-FD";
}
.ticker-assembly-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
.ticker-assembly-table-cell {
  text-align: center;
  direction: ltr !important;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.ticker-assembly-table-cell-number {
  text-align: center;
  direction: ltr !important;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.ICheader {
  font-size: 0.8em !important;
  font-weight: 300;
  text-align: center;
}
.AssemblyTablesTableToolbars /deep/ .v-toolbar__content {
  height: 30px !important;
}
</style>
