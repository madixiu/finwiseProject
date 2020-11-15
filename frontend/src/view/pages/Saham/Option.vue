<template>
  <div>
    <v-card class="mr-1 ml-1" outlined>
      <vxe-toolbar class="table-toolbar">
        <template v-slot:buttons>
          <vxe-input
            v-model="filterName"
            type="search"
            placeholder="جستجو"
          ></vxe-input>
        </template>
      </vxe-toolbar>
      <vxe-table
        border
        :height="height"
        :scroll-x="{ gt: 40 }"
        class="optionTable-style"
        align="center"
        :data="list"
        round
        ref="xTable1"
        :export-config="{}"
        size="mini"
        show-header-overflow
        show-overflow
        highlight-hover-row
      >
        <!-- <vxe-table-column type="seq" width="60"></vxe-table-column> -->
        <!-- <vxe-table-column field="get" title="Name"></vxe-table-column>
          <vxe-table-column field="sex" title="Sex"></vxe-table-column>
          <vxe-table-column field="age" title="Age"></vxe-table-column> -->
        <vxe-table-column
          v-for="item in this.headers"
          :key="item.label"
          :field="item.field"
          :title="item.label"
          :width="item.width"
          sortable
          type="html"
        >
        </vxe-table-column>
      </vxe-table>
      <!-- <v-data-table
      :height="height"
      :headers="headers"
      :items="getSahm"
      :search="search"
      fixed-header
      disable-pagination
      hide-default-footer
      dark
      class="elevation-1 test"
      
    >
  
    <template v-slot:[`item.DifferenceToAverage`]="{ item }">
      <v-chip :color="getColor(item.DifferenceToAverage)" dark>{{ item.DifferenceToAverage }}</v-chip>
    </template>
   
    </v-data-table> -->
    </v-card>
  </div>
</template>

<script>
import axioso from "axios";
import { mapGetters } from "vuex";
import XEUtils from "xe-utils";

export default {
  name: "Option",

  data: () => ({
    filterName: "",
    temp: [],
    flag: 0,
    height: 400,
    search: "",
    headers: [
      { label: "نماد", field: "Nemad", width: "100" },
      { label: "دارایی پایه", field: "UnderLying", width: "100" },
      { label: "پرداخت نهایی", field: "FinalPayment", width: "100" },
      { label: "مبلغ کل اردر اول", field: "TotalValue", width: "120" },
      { label: "StrikePrice", field: "StrikePrice", width: "100" },
      { label: "قیمت دارایی پایه", field: "AssetPrice", width: "120" },
      {
        label: "فاصله تا قیمت عادلانه",
        field: "DifferenceToAverage",
        width: "200"
      },
      {
        label: "میانگین قیمت عادلانه",
        field: "averageFairprice",
        width: "130"
      },
      { label: "قیمت اردر فروش", field: "priceseller", width: "130" },
      { label: "حجم اردر فروش", field: "volumeseller", width: "130" },
      { label: "فاصله تا سر رسید", field: "TTM", width: "130" },
      {
        label: "قیمت فروش+قیمت قرارداد / قیمت دارایی پایه",
        field: "PPP",
        width: "200"
      },
      { label: "حجم قرارداد", field: "TradeVolume", width: "100" },
      { label: "قیمت آخرین معامله", field: "LastTrade", width: "130" },
      { label: "ارزندگی آخرین معامله", field: "ArzandegiLast", width: "130" },
      {
        label: "فاصله آخرین معامله تا قیمت عادلانه",
        field: "DifferenceToLast",
        width: "200"
      }
    ]
  }),

  computed: {
    list() {
      let data = this.$store.getters.getSahm;
      let filterName = XEUtils.toString(this.filterName).trim();
      console.log("filterName: " + filterName);
      if (filterName) {
        let filterRE = new RegExp(filterName, "gi");
        console.log("filteRE: " + filterRE);

        let searchProps = [
          "Nemad",
          "UnderLying",
          "FinalPayment",
          "TotalValue",
          "StrikePrice",
          "AssetPrice",
          "DifferenceToAverage",
          "averageFairprice",
          "priceseller",
          "volumeseller",
          "TTM",
          "PPP",
          "TradeVolume",
          "LastTrade",
          "ArzandegiLast",
          "DifferenceToLast"
        ];
        let rest = data.filter(item =>
          searchProps.some(
            key => XEUtils.toString(item[key]).indexOf(filterName) > -1
          )
        );
        // console.log('rest: '+ rest);
        return rest.map(row => {
          let item = Object.assign({}, row);
          searchProps.forEach(key => {
            item[key] = XEUtils.toString(item[key]).replace(
              filterRE,
              match => `<span class="keyword-lighten">${match}</span>`
            );
          });
          return item;
        });
      }
      return data;
    },

    ...mapGetters(["getSahm"])
  },
  mounted() {
    // websocket//////////////////////////
    // this.$socket.onopen = (data) => console.log('fucker' + data);
    // this.$socket.onmessage = (data) => {
    // // console.log("data firm live is: " +data.data)
    // let obj = new Array()
    // obj = JSON.parse(data.data)
    // this.$store.dispatch('setSocketMessage',obj)
    this.Req();

    // setInterval(() => {

    //       this.Req()

    // }, 5000)

    this.height = this.getHeight();
    // console.log(window.innerHeight);
    // defer the execution of anonymous function for
    // 3 seconds and go to next line of code.
    // sleep(2000).then(() => { console.log("World!"); });
  },
  methods: {
    makeToast(item) {
      // console.log(this.$store.getters.getSahm[0].DifferenceToLast);
      // console.log(this.$store.getters.getSahm.length);
      this.$bvToast.toast(item.DifferenceToLast, {
        title: item.Nemad,
        variant: "success",
        solid: false,
        noAutoHide: true,
        toaster: "b-toaster-bottom-left",
        enableSounds: true,
        sounds: {
          info:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233294/info.mp3",
          // path to sound for successfull message:
          success:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233524/success.mp3",
          // path to sound for warn message:
          warning:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233563/warning.mp3",
          // path to sound for error message:
          error:
            "https://res.cloudinary.com/dxfq3iotg/video/upload/v1557233574/error.mp3"
        }
      });
    },
    Req() {
      let vm = this;
      //  axios.get('http://45.82.136.21/api/options')
      axioso
        .get("http://localhost:8000/api/options")
        .then(response => {
          let data = response.data;
          // var cars = new Array();
          // cars = response.data
          // var json = JSON.parse(update);
          console.log(data);
          if (data != "noData") {
            this.$store.dispatch("setSahm", data);
            let items = data;

            for (const item of items) {
              if (item.TradeVolume != 0 && item.DifferenceToLast > 0.2) {
                if (this.flag == 0) {
                  vm.makeToast(item);
                  this.temp.push(item);
                  this.flag++;
                } else {
                  for (let tempItem of this.temp) {
                    if (
                      tempItem.Nemad == item.Nemad &&
                      tempItem.DifferenceToLast != item.DifferenceToLast
                    ) {
                      vm.makeToast(item);
                      this.temp.pop();
                      this.temp.push(item);
                    }
                  }
                }
              }
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    getColor(DefferenceToAverage) {
      if (DefferenceToAverage < 0) return "red";
      else if (DefferenceToAverage < 0.1 && DefferenceToAverage > 0)
        return "orange";
      else return "green";
    },

    getHeight() {
      //  return (window.innerHeight * 75)/100
      return window.innerHeight - 77;
    }
  }
};
</script>
<style>
.optionTable-style {
  direction: rtl;
}
/* .optionTable-style .vxe-table.size--mini {
    font-size: 9px;
} */

.optionTable-style .vxe-body--row {
  /* background-color: #000; */
  color: #000;
  direction: ltr;
  /* direction: rtl; */
}

.optionTable-style .vxe-header--column {
  background-color: #003941;
  color: #fff;

  font-size: smaller;
}

/*  */

.keyword-lighten {
  color: #000;
  background-color: #ffff00;
}

.vxe-toolbar .vxe-button--wrapper {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  text-align: right !important;
}
.vxe-input--inner {
  border: 1px solid black !important;
}
.vxe-input {
  display: inline-block;
  position: relative;
  width: 300px !important;
  height: 30px !important;
  margin-right: 10px;
}
</style>
