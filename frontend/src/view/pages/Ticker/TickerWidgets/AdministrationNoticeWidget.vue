<template>
  <v-card rounded="lg" height="100%">
    <v-skeleton-loader
      v-if="loading && !noData"
      type=" table-heading, table-thead, table-tbody"
    ></v-skeleton-loader>

    <!-- <v-data-table
      v-if="loading == false"
      :headers="headers"
      :items="notices"
      class="elevation-1 FinancialStrength"
    >
    </v-data-table> -->
    <b-table
      id="AdministrationWidgetTable"
      class="AdministrationWidget-table"
      thClass="AdministrationWidget-tableHeader"
      tbody-tr-class="AdministrationWidget-table-row"
      v-if="!loading && !noData"
      small
      hover
      :per-page="tablePaginationVisible"
      :current-page="tablePaginationNumber"
      :responsive="true"
      :items="notices"
      :fields="headers"
    >
      <template #cell(Submited)="data">
        <span v-if="data.value == null || data.value == ''">- </span>
        <span v-else>{{ data.value }}</span>
      </template>
      <template #cell(persianDate)="data">
        <span v-if="data.value == null || data.value == ''">- </span>
        <span v-else>{{ data.value }}</span>
      </template>
      <template #cell(Title)="data">
        <span v-if="data.value == null || data.value == ''">- </span>
        <span v-else>{{ data.value }}</span>
      </template>
      <template #cell(Text)="data">
        <span v-if="data.value == null || data.value == ''">- </span>
        <span v-else>{{ data.value }}</span>
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
  name: "AdminNoticeWidget",
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
      loading: true,
      noData: false,
      headers: [
        {
          label: "تاریخ ارسال",
          key: "Submited",
          tdClass: "AdministrationWidget-tableTD",
          thStyle: { "min-width": "200px" },
          thClass: "AdministrationWidget-tableHeader"
        },
        {
          label: "تاریخ انتشار",
          key: "persianDate",
          tdClass: "AdministrationWidget-tableTD",
          thClass: "AdministrationWidget-tableHeader"
        },

        {
          label: "عنوان",
          key: "Title",
          tdClass: "AdministrationWidget-tableTD",
          thClass: "AdministrationWidget-tableHeader"
        },
        {
          label: "توضیحات",
          key: "Text",
          thClass: "AdministrationWidget-tableHeader"
        }
      ]
    };
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

  computed: {
    tablePaginationVisible() {
      let screenHeight = window.innerHeight;
      let tableHeightWithoutHeader = screenHeight - 303;
      //? every row has 55 pixel
      let rowCount = parseInt(tableHeightWithoutHeader / 55);
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
    }
  }

};
</script>
<style scoped>
.AdministrationWidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1.5;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.AdministrationWidget-table /deep/ .AdministrationWidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
  /* min-width: 200px; */
}
.AdministrationWidget-table /deep/ .AdministrationWidget-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
.AdministrationWidget-table /deep/ .AdministrationWidget-tableTD {
  vertical-align: middle;
}
</style>
