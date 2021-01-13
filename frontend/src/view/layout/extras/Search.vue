<template>
  <div>
    <div>
      <autocomplete
        :search="searchA"
        placeholder="جستجو"
        :get-result-value="getResultValue"
        @submit="handleSubmit"
      >
        <template #result="{ result, props }">
          <li v-bind="props">
            <div class="search-title">
              {{ result.ticker }}
            </div>
            <div class="search-snippet">{{ result.Type }}</div>
          </li>
        </template>
      </autocomplete>
    </div>

    <!-- <div class="topbar-item">
      <div class="w-auto btn-clean d-flex align-items-center btn-lg">
        <v-autocomplete
          v-model="select"
          :loading="loading"
          :items="items"
          :search-input.sync="search"
          no-filter
          prepend-inner-icon="mdi-magnify"
          append-icon=""
          cache-items
          class="mx-1"
          flat
          solo
          dark
          dense
          hide-no-data
          hide-details
          placeholder="جستجو"
        >
          <template v-slot:item="{ item }">
            <v-list-item-content>
              <v-list-item-title v-text="item.ticker"></v-list-item-title>
              <v-list-item-subtitle v-text="item.Type"></v-list-item-subtitle>
            </v-list-item-content> -->
    <!-- <v-list-item-action>
            <v-icon>mdi-bitcoin</v-icon>
          </v-list-item-action> -->
    <!-- </template>
        </v-autocomplete>
      </div>
    </div> -->
  </div>
</template>
<script>
import Autocomplete from "@trevoreyre/autocomplete-vue";
// import "@trevoreyre/autocomplete-vue/dist/style.css";
export default {
  components: {
    Autocomplete
  },
  data() {
    return {
      searchClosed: true,
      searchData: [],
      loading: false,
      items: [],
      search: null,
      select: null,
      states: [
        "Alabama",
        "Alaska",
        "American Samoa",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "District of Columbia",
        "Federated States of Micronesia",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Marshall Islands",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Northern Mariana Islands",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Palau",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virgin Island",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming"
      ]
    };
  },
  watch: {
    search(val) {
      val !== this.select && this.querySelections(val);
      // if (this.items.length > 0) return;

      // this.isLoading = true;
      // setTimeout(() => {
      //   if (!this.searchData.length) this.loadData();

      //   // this.items = this.states.filter(e => {
      //   //   return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
      //   // });
      //   this.loading = false;
      // }, 1500);
      // console.log(val);
      // val && val !== this.select && this.querySelections(val);
    }
  },
  computed: {
    SearchIcon() {
      return process.env.BASE_URL + "media/svg/icons/General/Search.svg";
    }
  },
  mounted() {
    console.log("search mount");
    this.loadData();
  },
  methods: {
    //----------------------------------
    searchA(input) {
      if (input.length < 1) {
        return [];
      }
      return this.searchData.filter(e => {
        return e.ticker.toLowerCase().startsWith(input.toLowerCase());
      });
    },
    getResultValue(result) {
      return result.ticker;
    },
    //----------------------------------
    handleSubmit(result) {
      if (result.TypeID == 1 || result.TypeID == 25)
        // this.$router.push({ name: "TickerOverall", params: { id: result.ID } });
        this.$router.push({ path: `/ticker/Overview/Overall/${result.ID}` });
      else {
        alert(`You selected ${result.ID} which is oraq and not created`);
      }
    },
    async loadData() {
      await this.axios
        .get("/api/MainSearchBar")
        .then(response => {
          let data = response.data;
          // let tickerNames = [];
          if (data != "noData") this.searchData = data;
          // for (let item of data) {
          //   tickerNames.append(item.ticker);
          // }
          // console.log(tickerNames);
          // this.states = tickerNames;
        })
        .catch(error => {
          console.log(error);
        });
    },
    querySelections(v) {
      this.loading = true;

      // Simulated ajax query
      setTimeout(() => {
        // this.items = this.states.filter(e => {
        //   return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
        // });
        // let res = users.filter(it => it.name.includes("oli"));
        this.items = this.searchData.filter(e => {
          // console.log(e.ticker);
          return e.ticker.indexOf(v) > -1;
        });
        this.loading = false;
      }, 100);
    }
  }
};
// export default {
//   data() {
//     return {
//       search: ""
//     };
//   },
//   watch: {
//     // search(val) {
//     //   val && val !== this.select && this.querySelections(val);
//     // }
//   },
//   methods: {
//     querySelections(v) {
//       this.loading = true;
//       // Simulated ajax query
//       setTimeout(() => {
//         this.items = this.states.filter(e => {
//           return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
//         });
//         this.loading = false;
//       }, 500);
//     }
//   }
// };
</script>
<style>
.search-title {
  font-size: 0.9rem;
  direction: rtl;
}
.search-snippet {
  color: #929292;
  font-size: 0.8;
}
.autocomplete-input {
  border: 1px solid #eee;
  border-radius: 8px;
  width: 100%;
  padding: 12px 25px 12px 48px;
  box-sizing: border-box;
  position: relative;
  font-size: 14px;
  line-height: 1.5;
  flex: 1;
  background-color: #eee;
  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjNjY2IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTEiIGN5PSIxMSIgcj0iOCIvPjxwYXRoIGQ9Ik0yMSAyMWwtNC00Ii8+PC9zdmc+");
  background-repeat: no-repeat;
  background-position: 12px;
  direction: rtl;
}
.autocomplete-input:focus,
.autocomplete-input[aria-expanded="true"] {
  border-color: rgba(0, 0, 0, 0.12);
  background-color: #fff;
  outline: none;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16);
}
[data-position="below"] .autocomplete-input[aria-expanded="true"] {
  border-bottom-color: transparent;
  border-radius: 8px 8px 0 0;
  direction: rtl;
}
[data-position="above"] .autocomplete-input[aria-expanded="true"] {
  border-top-color: transparent;
  border-radius: 0 0 8px 8px;
  z-index: 2;
  direction: rtl;
}
.autocomplete[data-loading="true"]:after {
  content: "";
  border: 3px solid rgba(0, 0, 0, 0.12);
  border-right-color: rgba(0, 0, 0, 0.48);
  border-radius: 100%;
  width: 20px;
  height: 20px;
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  animation: rotate 1s linear infinite;
  direction: rtl;
}
.autocomplete-result-list {
  margin: 0;
  border: 1px solid rgba(0, 0, 0, 0.12);
  padding: 0;
  box-sizing: border-box;
  max-height: 296px;
  overflow-y: auto;
  background: #fff;
  list-style: none;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16);
  direction: rtl !important;
}
[data-position="below"] .autocomplete-result-list {
  margin-top: -1px;
  border-top-color: transparent;
  border-radius: 0 0 8px 8px;
  padding-bottom: 8px;
  direction: rtl;
}
[data-position="above"] .autocomplete-result-list {
  margin-bottom: -1px;
  border-bottom-color: transparent;
  border-radius: 8px 8px 0 0;
  padding-top: 8px;
}
.autocomplete-result {
  cursor: default;
  padding: 12px 12px 12px 48px;
  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjY2NjIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTEiIGN5PSIxMSIgcj0iOCIvPjxwYXRoIGQ9Ik0yMSAyMWwtNC00Ii8+PC9zdmc+");
  background-repeat: no-repeat;
  background-position: 12px;
  direction: inherit !important;
}
.autocomplete-result:hover,
.autocomplete-result[aria-selected="true"] {
  background-color: rgba(0, 0, 0, 0.06);
}
@keyframes rotate {
  0% {
    transform: translateY(-50%) rotate(0deg);
  }
  to {
    transform: translateY(-50%) rotate(359deg);
  }
}

/* ------------------------------------------------------- */
/* .autocomplete-input {
  padding: 12px 25px 12px 48px;
  background-color: #626280;
  font-size: 1rem;
}
.autocomplete-input:focus {
  background-color: #8f8fad;
  color: white;
}
.autocomplete-input::placeholder {
  color: white;
} */

/* ----------------------------------------------------------------------------- */
/* .v-list v-select-list v-sheet theme--light v-list--dense theme--light {
  direction: "rtl";
}
.v-menu__content .theme--light .v-menu__content--fixed .menuable__content__active .v-autocomplete__content {
    max-height: 34px;
    min-width: 251px;
    top: 12px;
    left: 267px;
    transform-origin: right top;
    z-index: 99;
    margin-top: 1rem;
} */
</style>
