<template>
  <!--begin::Mixed Widget 14-->
  <v-card rounded="lg" height="100%">
    <!--begin::Header-->
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        افزایش سرمایه ها
      </h3>
    </div> -->
    <!--end::Header-->
    <!--begin::Body-->
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em;"
        >افزایش سرمایه ها</v-toolbar-title
      >
    </v-toolbar>
    <v-skeleton-loader
      v-if="loading && !noData"
      type=" table-heading, table-thead, table-tbody"
    ></v-skeleton-loader>
    <b-table
      id="IncreaseCapitalsWidgetTable"
      class="IncreaseCapitalsWidget-table"
      thClass="IncreaseCapitalsWidget-tableHeader"
      tbody-tr-class="IncreaseCapitalsWidget-table-row"
      v-if="!loading && !noData"
      small
      hover
      :per-page="tablePaginationVisible"
      :current-page="tablePaginationNumber"
      :responsive="true"
      :items="notices"
      :fields="headersNew"
    >
      <template #cell(IncreasePercent)="data">
        <span v-if="data.value == null || data.value == ''">-</span>
        <span v-else>{{ roundTo(data.value, 2) }}%</span>
      </template>
      <template #cell(HtmlUrl)="data">
        <v-chip label small :disabled="data.value == '' ? true : false">
          <a v-bind:href="`http://codal.ir${data.value}`" target="_blank"
            >اطلاعیه
          </a>
        </v-chip>
      </template>
    </b-table>
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
    <!-- <v-data-table
      v-if="loading == false"
      :headers="headers"
      :items="notices"
      :items-per-page="13"
      class="elevation-1 FinancialStrength"
    >
      <template v-slot:[`item.IncreasePercent`]="{ item }">
        <span class="cellItem">{{ roundTo(item.IncreasePercent, 2) }}% </span>
      </template>
      <template v-slot:[`item.AttachmentUrl`]="{ item }">
        <v-chip label small :disabled="item.HtmlUrl == '' ? true : false">
          <a v-bind:href="`http://codal.ir${item.HtmlUrl}`" target="_blank"
            >اطلاعیه
          </a>
        </v-chip>
      </template>
    </v-data-table> -->
    <!--end::Body-->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
export default {
  name: "ICWidget",
  props: ["notices"],
  data() {
    return {
      tablePaginationNumber: 1,
      tablePaginationLength: 10,
      loading: true,
      noData: false,
      headersNew: [
        {
          label: "سهم",
          key: "ticker",
          sortable: false,
          thClass: "IncreaseCapitalsWidget-tableHeader"
        },
        {
          label: "زمان انتشار",
          key: "PublishTime",
          thClass: "IncreaseCapitalsWidget-tableHeader"
        },
        {
          label: "نوع اطلاعیه",
          key: "Title",
          sortable: false,
          thClass: "IncreaseCapitalsWidget-tableHeader"
        },
        {
          label: "درصد افزایش سرمایه",
          key: "IncreasePercent",
          thClass: "IncreaseCapitalsWidget-tableHeader"
        },
        {
          label: "محل افزایش سرمایه",
          key: "CapitalChangeType",
          sortable: false,
          thClass: "IncreaseCapitalsWidget-tableHeader"
        },
        {
          label: "لینک فایلها",
          key: "HtmlUrl",
          sortable: false,
          thClass: "IncreaseCapitalsWidget-tableHeader"
        }
      ],
      headers: [
        {
          text: "سهم",
          value: "ticker",
          sortable: false
        },
        {
          text: "زمان انتشار",
          value: "PublishTime"
        },
        {
          text: "نوع اطلاعیه",
          value: "Title",
          sortable: false
        },
        {
          text: "درصد افزایش سرمایه",
          value: "IncreasePercent"
        },
        {
          text: "محل افزایش سرمایه",
          value: "CapitalChangeType",
          sortable: false
        },
        {
          text: "لینک فایلها",
          value: "AttachmentUrl",
          sortable: false
        }
      ]
    };
  },
  computed: {
    tablePaginationVisible() {
      let screenHeight = window.innerHeight;
      let tableHeightWithoutHeader = screenHeight - 303;
      //? every row has 55 pixel
      let rowCount = parseInt(tableHeightWithoutHeader / 33);
      return rowCount;
    }
  },
  methods: {
    pagination(number) {
      if (number % this.tablePaginationVisible == 0)
        return number / this.tablePaginationVisible;
      else {
        return parseInt(number / this.tablePaginationVisible) + 1;
      }
    },
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
    }
  },
  mounted() {},
  watch: {
    notices() {
      this.loading = false;
    }
  }
};
</script>
<style scoped>
.IncreaseCapitalsWidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1.5;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.IncreaseCapitalsWidget-table /deep/ .IncreaseCapitalsWidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
  /* min-width: 200px; */
}
.IncreaseCapitalsWidget-table /deep/ .IncreaseCapitalsWidget-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
.IncreaseCapitalsWidget-table /deep/ .IncreaseCapitalsWidget-tableTD {
  vertical-align: middle;
}

.cellItem {
  font-family: "Vazir-Medium-FD";
  font-weight: 600;
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
</style>
