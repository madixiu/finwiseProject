<template>
  <div class="row mr-1  ml-1">
    <v-card width="100%">
      <b-row>
        <b-col lg="4" class="my-1 mr-3">
          <b-input-group size="sm">
            <b-form-input
              v-model="Tablefilter"
              type="search"
              id="filterInput"
              placeholder="فیلتر"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!Tablefilter" @click="Tablefilter = ''"
                >پاک کردن</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-col>
      </b-row>

      <b-table
        v-bind:thClass="{
          crypto_table_head: smallFontHeader,
          crypto_table_head_small: smallFontHeader
        }"
        class="crypto-table"
        tbody-tr-class="crypto-table-row"
        striped
        :sticky-header="height"
        :busy.sync="isBusy"
        :no-provider-paging="true"
        :sort-desc.sync="sortDesc"
        :sort-by.sync="sortBy"
        sort-direction="desc"
        sort-icon-left
        dense
        :filter="Tablefilter"
        :filter-included-fields="filterOn"
        :filter-debounce="100"
        bordered
        no-border-collapse
        outlined
        small
        hover
        responsive
        :items="tableData"
        :fields="CryptoTableHeader"
        @filtered="onFiltered"
      >
        <template #cell(symbol)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b> 
        </template>
        <template #cell(persianDate)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b> 
        </template>
        <template #cell(regularMarketDayRange)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(regularMarketPrice)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(regularMarketVolume)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(fiftyTwoWeekRange)="data">
          <b class="crypto-table-cell-bold">{{ data.value.toLocaleString() }}</b>
        </template>
        <!-- <template #cell(logoUrl)="data">
          <img :src="data.value" width="55px" height="55px" />
        </template> -->
        <template #cell(regularMarketChange)="data">
          <b v-if="data.value > 0" class="crypto-table-cell-green"
            >{{ data.value.toLocaleString() }}%</b
          >
          <b v-if="data.value < 0" class="crypto-table-cell-red"
            >{{ data.value.toLocaleString() }}%</b
          >
          <b v-if="data.value == 0" class="crypto-table-cell"
            >{{ data.value.toLocaleString() }}%</b
          >
        </template>
      </b-table>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "Crypto",
  components: {},
  data() {
    return {
      WebsocketRequest: true,
      height: "470px",
      sortDesc: false,
      filterOn: ["ticker"],
      sortBy: "ticker",
      selectedHeaderOptions: [],
      smallFontHeader: false,
      isBusy: true,
      tableData: null,
      Tablefilter: "",
      CryptoTableHeader: [
          {
          label: "نماد",
          key: "symbol",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "نام",
          key: "name",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "تاریخ آخرین به روز رسانی",
          key: "persianDate",
          thClass: "crypto_table_head",
          sortable: true
        },
        
        // {
        //   label: "لوگو",
        //   key: "logoUrl",
        //   thClass: "crypto_table_head",
        //   sortable: true
        // },
      
        {
          label: "بازار",
          key: "exchange",
          thClass: "crypto_table_head",
          sortable: true
        },
        
        {
          label: "تغییرات قیمت",
          key: "regularMarketChange",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "قیمت (دلار)",
          key: "regularMarketPrice",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "regularMarketVolume",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "بازه قیمت روز",
          key: "regularMarketDayRange",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "حجم معاملات در بازار",
          key: "regularMarketVolume",
          thClass: "crypto_table_head",
          sortable: true
        },
        {
          label: "بازه ۵۲ هفته ای",
          key: "fiftyTwoWeekRange",
          thClass: "crypto_table_head",
          sortable: true
        }
      ]
    };
  },

  mounted() {
    this.loadData();
    this.liveChecker();
    this.height = this.getHeight();
    this.$socketCrypto.onmessage = data => {
      if (JSON.parse(data.data) != "noData")
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData = JSON.parse(data.data);
    };
  },
  methods: {
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/CryptoMarket")
        .then(response => {
          this.isBusy = false;
          let data = response.data;
          this.tableData = data;
        })
        .catch(error => {
          this.isBusy = false;
          console.error(error);
        });
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },

    getHeight() {
      return (window.innerHeight - 150).toString() + "px";
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketCrypto.send(JSON.stringify(barier));
      }, 3000);
    },
    liveChecker() {
      // let date = new Date();
      // if (
      //   date.getHours() > 8 &&
      //   date.getHours() < 23 &&
      //   date.getDay() != 5 &&
      //   date.getDay() != 4
      // ) {
      //   this.WebsocketRequest = true;
      this.liveData();
      // } else {
      //   this.WebsocketRequest = false;
      // }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketCrypto.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.crypto_table_head {
  vertical-align: middle !important;
  font-size: 1.1em !important;
  font-weight: 600 !important ;
}
.crypto_table_head_small {
  vertical-align: middle !important;
  font-size: 0.9em !important;
  font-weight: 600 !important ;
}
.crypto-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8em !important;
  line-height: 1 !important;
}
.crypto-table-row:hover {
  background-color: #999999 !important;
}
.crypto-table-cell {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.crypto-table-cell-green {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.crypto-table-cell-red {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.crypto-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 700;
  font-family: "Vazir-Medium-FD";
}
.crypto-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
</style>
