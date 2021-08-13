<template>
  <v-card rounded="lg" height="100%">
    <!--begin::Header-->
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        اطلاعیه های کدال
      </h3>
    </div> -->
    <!--end::Header-->
    <!--begin::Body-->
    <v-skeleton-loader
      v-if="loading && !noData"
      type=" table-heading, table-thead, table-tbody"
    ></v-skeleton-loader>
    <b-table
      v-if="!loading && !noData"
      class="NotificationWidget-table"
      thClass="NotificationWidget-tableHeader"
      tbody-tr-class="NotificationWidget-table-row"
      small
      hover
      :responsive="true"
      :per-page="tablePaginationVisible"
      :current-page="tablePaginationNumber"
      :items="notices"
      :fields="headers"
    >
      <template #cell(Submited)="data">
        <span v-if="data.value == null || data.value == ''">- </span>
        <span v-else>{{ data.value }}</span>
      </template>

      <template #cell(HtmlUrl)="data">
        <v-chip label small :disabled="data.value == '' ? true : false">
          <a v-bind:href="`http://codal.ir${data.value}`" target="_blank"
            >گزارش
          </a>
        </v-chip>
      </template>
      <template #cell(AttachmentUrl)="data">
        <v-chip label small :disabled="data.value == '' ? true : false">
          <a v-bind:href="`http://codal.ir${data.value}`" target="_blank"
            >فایل
          </a>
        </v-chip>
      </template>
      <template #cell(ExcelUrl)="data">
        <v-chip label small :disabled="data.value == '' ? true : false">
          <a v-bind:href="`${data.value}`" target="_blank">اکسل </a>
        </v-chip>
      </template>
      <template #cell(PdfUrl)="data">
        <v-chip label small :disabled="data.value == '' ? true : false">
          <a v-bind:href="`http://codal.ir/${data.value}`" target="_blank"
            >پی دی اف
          </a>
        </v-chip>
      </template>
    </b-table>

    <!-- //? no Data  -->
    <div v-if="noData && !loading" class="d-flex justify-content-center py-5">
      <span style="font-size:0.9em">اطلاعات موجود نیست</span>
    </div>

    <!--//? pagination -->
    <div
      v-if="!loading && !noData"
      style="
              display: flex;
              justify-content: center;width:100%"
    >
      <div class="col-6">
        <v-pagination
          color="#4682B4"
          v-model="tablePaginationNumber"
          :length="tablePaginationLength"
          :total-visible="tablePaginationVisible"
        ></v-pagination>
      </div>
    </div>
  </v-card>
</template>
<script>
export default {
  name: "NotificationWidget",
  // props: ["notices"],
  props: {
    notices: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      tablePaginationNumber: 1,
      tablePaginationLength: 10,
      //// tablePaginationVisible: 15,
      loading: true,
      noData: false,
      headers: [
        {
          label: "شرکت گزارش دهنده",
          key: "reported_firm",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "متن اطلاعیه",
          key: "title",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "زمان ارسال",
          key: "SentTime",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "زمان انتشار",
          key: "PublishTime",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "لینک گزارش",
          key: "HtmlUrl",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "لینک فایلها",
          key: "AttachmentUrl",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "لینک پی دی اف",
          key: "PdfUrl",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        },
        {
          label: "لینک اکسل",
          key: "ExcelUrl",
          thClass: "NotificationWidget-tableHeader",
          tdClass: "NotificationWidget-tableTD"
        }
      ]
    };
  },
  computed: {
    tablePaginationVisible() {
      let screenHeight = window.innerHeight;
      let tableHeightWithoutHeader = screenHeight - 303;
      //? every row has 33 pixel
      let rowCount = parseInt(tableHeightWithoutHeader / 33);
      return rowCount;
    }
  },

  watch: {
    notices(newValue, oldValue) {
      if (
        newValue != oldValue &&
        newValue.length == 0 &&
        oldValue.length == 0
      ) {
        this.noData = true;
        this.loading = false;
      } else {
        this.tablePaginationLength = this.pagination(this.notices.length);
        this.loading = false;
      }
    }
  },
  methods: {
    pagination(number) {
      if (number % this.tablePaginationVisible == 0)
        return number / this.tablePaginationVisible;
      else {
        return parseInt(number / this.tablePaginationVisible) + 1;
      }
    }
  }
};
</script>
<style scoped>
.NotificationWidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1.5;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.NotificationWidget-table /deep/ .NotificationWidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
  /* min-width: 200px; */
}
.NotificationWidget-table /deep/ .NotificationWidget-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
.NotificationWidget-table /deep/ .NotificationWidget-tableTD {
  vertical-align: middle;
}
</style>
