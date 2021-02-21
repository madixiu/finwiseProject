<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        سابقه قیمت
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <v-text-field
        v-model="search"
        append-icon="search"
        label="جستجوی تاریخ"
        single-line
        hide-details
        :search="search"
        class="mt-0 pt-0"
      ></v-text-field>
      <v-data-table
        :headers="headers"
        :items="DataItems2"
        class="elevation-1 FinancialStrength"
        dense
        :options.sync="options"
        :search="search"
      >
        <template v-slot:[`item.persiandate`]="{ item }">
          <span class="FinancialStrength"
            >{{
              item.persiandate.substring(0, 4) +
                "/" +
                item.persiandate.substring(4, 6) +
                "/" +
                item.persiandate.substring(6, 8)
            }}
          </span>
        </template>
        <template v-slot:[`item.high`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.high) }}
          </span>
        </template>
        <template v-slot:[`item.low`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.low) }}
          </span>
        </template>
        <template v-slot:[`item.closing`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.closing) }}
          </span>
        </template>
        <template v-slot:[`item.adjustedclosing`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.adjustedclosing) }}
          </span>
        </template>
        <template v-slot:[`item.last`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.last) }}
          </span>
        </template>
        <template v-slot:[`item.first`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(item.first) }}
          </span>
        </template>
        <template v-slot:[`item.value`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(roundTo(item.value / 1000000000, 2)) }} میلیارد
            ریال</span
          >
        </template>
        <template v-slot:[`item.volume`]="{ item }">
          <span class="FinancialStrength"
            >{{ numberWithCommas(roundTo(item.volume / 1000000, 2)) }} میلیون
            سهم
          </span>
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
  name: "adjustedWidget",
  props: ["adjusted"],
  data() {
    return {
      search: "",
      options: {
        itemsPerPage: 20
      },
      headers: [
        {
          text: "تاریخ شمسی",
          value: "persiandate"
        },
        {
          text: "قیمت پایانی",
          value: "closing",
          filterable: false
        },
        {
          text: "قیمت تعدیلی",
          value: "adjustedclosing",
          filterable: false
        },

        {
          text: "آخرین قیمت",
          value: "last",
          filterable: false
        },
        {
          text: " اولین قیمت",
          value: "first",
          filterable: false
        },
        {
          text: "بالاترین قیمت",
          value: "high",
          filterable: false
        },
        {
          text: "پایین ترین قیمت",
          value: "low",
          filterable: false
        },
        {
          text: "ارزش معاملات",
          value: "value",
          filterable: false
        },
        {
          text: "حجم معاملات",
          value: "volume",
          filterable: false
        }
      ],
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems2 = this.adjusted;
    },
    numberWithCommas(x) {
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
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
    },
    filterItems(items, search, filter) {
      items.filter(r => filter((r.persiandate = search)));
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    adjusted() {
      console.log("Watcher");
      this.populateData();
      // console.log(this.notices);
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
  font-family: "Dirooz FD" !important;
  font-size: 1.1em;
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
