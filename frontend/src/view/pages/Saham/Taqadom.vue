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
        <b-col lg="4" xxl="4" class="mt-2">
          <b-form-group>
            <b-form-checkbox-group
              v-model="selectedHeaderOptions"
              :options="HeaderOptions"
              @change="TriggerFilteredHeader"
            ></b-form-checkbox-group>
          </b-form-group>
        </b-col>
      </b-row>

      <b-table
        thClass="taghadom-table-head"
        class="taghadom-table"
        tbody-tr-class="taghadom-table-row"
        striped
        :sticky-header="height"
        :busy.sync="isBusy"
        :no-provider-paging="true"
        dense
        :filter="Tablefilter"
        :sort-desc.sync="sortDesc"
        :filter-included-fields="filterOn"
        :sort-by.sync="sortBy"
        sort-direction="desc"
        sort-icon-left
        bordered
        no-border-collapse
        outlined
        small
        hover
        responsive
        :items="tableData"
        :fields="HD"
        @filtered="onFiltered"
      >
        <template #cell(ticker)="data">
          <b class="taghadom-table-cell-bold">{{ data.value }}</b>
        </template>
        <template #cell(TradeCount)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(TradeVolume)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(TradeValue)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(yesterday)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(last)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(close)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(first)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(low)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(high)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(MinRange)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(MaxRange)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountBuy_Haghighi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountBuy_Hoguhgi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeBuy_Haghighi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeBuy_Hoghughi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountSell_Haghighi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountSell_Hoghughi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeSell_Haghighi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeSell_Hoghughi)="data">
          <b class="taghadom-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(closePercent)="data">
          <b v-if="data.value > 0" class="taghadom-table-cell-green"
            >{{ data.value }}%</b
          >
          <b v-if="data.value < 0" class="taghadom-table-cell-red"
            >{{ data.value }}%</b
          >
          <b v-if="data.value == 0" class="taghadom-table-cell"
            >{{ data.value }}%</b
          >
        </template>
        <template #cell(lastPercent)="data">
          <b v-if="data.value > 0" class="taghadom-table-cell-green"
            >{{ data.value }}%</b
          >
          <b v-if="data.value < 0" class="taghadom-table-cell-red"
            >{{ data.value }}%</b
          >
          <b v-if="data.value == 0" class="taghadom-table-cell"
            >{{ data.value }}%</b
          >
        </template>
      </b-table>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "Taghadom",
  components: {},
  data() {
    return {
      WebsocketRequest: false,
      height: "470px",
      filterOn: ["ticker"],
      sortDesc: false,
      sortBy: "ticker",
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      isBusy: true,
      tableData: null,
      Tablefilter: "",
      TaghadomTableHeader: [
        {
          label: "نماد",
          key: "ticker",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "بازار",
          key: "marketName",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "درصد تغییر آخرین قیمت",
          key: "lastPercent",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "درصد تغییر قیمت پایانی",
          key: "closePercent",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "کف مجاز قیمت",
          key: "MinRange",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "سقف مجاز قیمت",
          key: "MaxRange",
          thClass: "taghadom-table-head",
          sortable: true
        },
        // { label: "EPS", key: "EPS", thClass: "taghadom-table-head" },
        {
          label: "بالاترین قیمت",
          key: "high",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "کمترین قیمت",
          key: "low",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "اولین قیمت",
          key: "first",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "taghadom-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "taghadom-table-head",
          sortable: true
        }
      ]
    };
  },
  computed: {
    HD() {
      return this.TriggerFilteredHeader();
    }
  },
  mounted() {
    this.loadData();
    this.height = this.getHeight();
       this.$socketTaqadom.onmessage = data => {
      // this.tableData = JSON.parse(data.data);
      // console.log(!!this.tableData.length);
      if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length)
        // this.$store.dispatch("setSahm", JSON.parse(data.data));
        this.tableData = JSON.parse(data.data);
    };
  },
  methods: {
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/HaghTaghadom")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData = data;
          console.log(data);
        })
        .catch(error => {
          this.isBusy = false;
          console.log(error);
        });
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.TaghadomTableHeader));
      let options = this.selectedHeaderOptions;
      let SwCase = 0;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "HH") SwCase = 2;
      } else if (options.length == 2) SwCase = 3;

      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 2:
          header.splice(5, 1);
          break;
        case 3:
          break;
        default:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      console.log(header);
      return header;
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
        this.$socketTaqadom.send(JSON.stringify(barier));
        // console.log(this.WebsocketRequest);
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getHours() > 8 && date.getHours() < 15) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketTaqadom.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style>
.taghadom-table-head {
  /* background-color: #e01313; */
  vertical-align: middle !important;
  font-size: 1.1em !important;
  font-weight: 600 !important ;
}
.taghadom-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8em !important;
  line-height: 1 !important;
  font-family: "Vazir-Medium-FD";
}
.taghadom-table-row:hover {
  background-color: #999999 !important;
}
.taghadom-table-cell {
  text-align: center;
  vertical-align: middle !important;
  font-size: 1em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.taghadom-table-cell-green {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: green;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.taghadom-table-cell-red {
  vertical-align: middle !important;
  text-align: center;
  font-size: 1em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.taghadom-table-cell-bold {
  text-align: center;
  font-size: 1em;
  line-height: 1;
  font-weight: 600;
}
.taghadom-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
</style>
