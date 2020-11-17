<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        اطلاعیه های کدال
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <v-data-table
        :headers="headers"
        :items="DataItems"
        class="elevation-1 FinancialStrength"
      >
        <template v-slot:[`item.HtmlUrl`]="{ item }">
          <v-chip label small :disabled="item.HtmlUrl == '' ? true : false">
            <a v-bind:href="`http://codal.ir${item.HtmlUrl}%`">گزارش </a>
          </v-chip>
        </template>
        <template v-slot:[`item.AttachmentUrl`]="{ item }">
          <v-chip
            label
            small
            :disabled="item.AttachmentUrl == '' ? true : false"
          >
            <a v-bind:href="`http://codal.ir${item.AttachmentUrl}%`">فایل </a>
          </v-chip>
        </template>
        <template v-slot:[`item.ExcelUrl`]="{ item }">
          <v-chip label small :disabled="item.ExcelUrl == '' ? true : false">
            <a v-bind:href="`${item.ExcelUrl}%`">اکسل </a>
          </v-chip>
        </template>
        <template v-slot:[`item.PdfUrl`]="{ item }">
          <v-chip label small :disabled="item.PdfUrl == '' ? true : false">
            <a v-bind:href="`http://codal.ir/${item.PdfUrl}%`">پی دی اف </a>
          </v-chip>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NotificationWidget",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "متن اطلاعیه",
          value: "title"
        },
        {
          text: "زمان ارسال",
          value: "SentTime"
        },
        {
          text: "زمان انتشار",
          value: "PublishTime"
        },
        {
          text: "لینک گزارش",
          value: "HtmlUrl"
        },
        {
          text: "لینک فایلها",
          value: "AttachmentUrl"
        },
        {
          text: "لینک پی دی اف",
          value: "PdfUrl"
        },
        {
          text: "لینک اکسل",
          value: "ExcelUrl"
        }
      ],
      DataItems: [
        {
          reported_firm: "سرمایه گذاری تامین اجتماعی",
          title: "درخواست تکمیل مشخصات سهامداران",
          SentTime: "۱۳۹۹/۰۸/۰۶ ۱۳:۳۱:۱۳",
          PublishTime: "۱۳۹۹/۰۸/۰۶ ۱۳:۳۱:۱۳",
          HtmlUrl:
            "/Reports/Attachment.aspx?LetterSerial=1B4EvSUdTXIm0isEX161zA%3d%3d",
          AttachmentUrl:
            "/Reports/Attachment.aspx?LetterSerial=1B4EvSUdTXIm0isEX161zA%3d%3d",
          PdfUrl:
            "DownloadFile.aspx?hs=mS9cutqC35p2GltZkKm7vQ%3d%3d&ft=1005&let=2020",
          ExcelUrl: "",
          TedanUrl: "http://www.tedan.ir"
        },
        {
          reported_firm: "سرمایه گذاری تامین اجتماعی",
          title: "گزارش فعالیت ماهانه دوره ۱ ماهه منتهی به ۱۳۹۹/۰۷/۳۰",
          SentTime: "۱۳۹۹/۰۸/۰۵ ۱۹:۲۵:۰۵",
          PublishTime: "۱۳۹۹/۰۸/۰۵ ۱۹:۲۵:۰۵",
          HtmlUrl:
            "/Reports/Decision.aspx?LetterSerial=gg8OzYI12khGfUR9Anj1Zw%3D%3D&rt=2&let=8&ct=0&ft=-1",
          AttachmentUrl: "",
          PdfUrl:
            "DownloadFile.aspx?hs=QQQaQQQgPI8XhMtrdzZ67%2bfchL6Q%3d%3d&ft=1005&let=11",
          ExcelUrl:
            "https://excel.codal.ir/service/Excel/GetAll/gg8OzYI12khGfUR9Anj1Zw%3d%3d/0",
          TedanUrl: "http://www.tedan.ir"
        }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {},
  mounted() {
    // this.setFinancialStrengthPercent();
    // reference; kt_stats_widget_7_chart
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
</style>
