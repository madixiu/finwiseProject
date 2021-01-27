<template>
  <div>
    <div class="col-12">
      <!-- User Interface controls -->
      <v-card>
        <b-col lg="4" class="my-1">
          <b-input-group size="sm">
            <b-form-input
              id="filter-input"
              v-model="filter"
              type="search"
              placeholder="جستجو"
            ></b-form-input>

            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''"
                >پاک کردن</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-col>

        <!-- Main table element -->
        <b-table
          thClass="Descision-table-head"
          class="Descision-table"
          tbody-tr-class="Descision-table-row"
          striped
          :items="ListData"
          :fields="headersListData"
          :current-page="currentPage"
          :per-page="perPage"
          :filter="filter"
          :filter-debounce="1200"
          :busy.sync="isBusy"
          :no-provider-paging="true"
          no-border-collapse
          dense
          bordered
          outlined
          small
          hover
          responsive
          @filtered="onFiltered"
        >
          <template #table-busy>
            <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong>شکیبا باشید...</strong>
            </div>
          </template>
          <!-- <template #cell(name)="row">
            {{ row.value.first }} {{ row.value.last }}
          </template> -->

          <template #cell(HtmlUrl)="row">
            <!-- <b-button size="sm" @click="info(row.item)" class="mr-1">
              لینک
            </b-button> -->
            <v-icon
              size="15px"
              color="#4682B4"
              @click="info(row.item)"
              class="mr-1"
              >mdi-link-variant</v-icon
            >
          </template>
        </b-table>
        <b-col sm="7" md="6" class="my-1">
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            align="fill"
            size="sm"
            class="my-0"
          ></b-pagination>
        </b-col>
      </v-card>

      <!-- Info modal -->
      <!-- <b-modal
        :id="infoModal.id"
        :title="infoModal.title"
        ok-only
        @hide="resetInfoModal"
      >
        <pre>{{ infoModal.content }}</pre>
      </b-modal> -->
    </div>
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-6.vue";
// import Wizard from "@/view/pages/Saham/Majame/content/Wizard";
export default {
  name: "Decisions",
  components: {},
  data() {
    return {
      totalRows: 1,
      currentPage: 1,
      perPage: 15,
      isBusy: false,
      headersListData: [
        {
          label: "تاریخ انتشار",
          key: "PublishTime",
          thClass: "Descision-table-head"
        },
        {
          label: "سهم",
          key: "Ticker",
          width: "100",
          thClass: "Descision-table-head"
        },
        {
          label: "عنوان",
          key: "title",
          width: "100",
          thClass: "Descision-table-head"
        },
        {
          label: "لینک کدال",
          key: "HtmlUrl",
          width: "100",
          thClass: "Descision-table-head"
        }
      ],
      ListData: null,
      filter: null,
      // test DATA BELOW *******************************************
      items: [
        {
          isActive: true,
          age: 40,
          name: { first: "Dickerson", last: "Macdonald" }
        },
        { isActive: false, age: 21, name: { first: "Larsen", last: "Shaw" } },
        {
          isActive: false,
          age: 9,
          name: { first: "Mini", last: "Navarro" },
          _rowVariant: "success"
        },
        { isActive: false, age: 89, name: { first: "Geneva", last: "Wilson" } },
        { isActive: true, age: 38, name: { first: "Jami", last: "Carney" } },
        { isActive: false, age: 27, name: { first: "Essie", last: "Dunlap" } },
        { isActive: true, age: 40, name: { first: "Thor", last: "Macdonald" } },
        {
          isActive: true,
          age: 87,
          name: { first: "Larsen", last: "Shaw" },
          _cellVariants: { age: "danger", isActive: "warning" }
        },
        { isActive: false, age: 26, name: { first: "Mitzi", last: "Navarro" } },
        {
          isActive: false,
          age: 22,
          name: { first: "Genevieve", last: "Wilson" }
        },
        { isActive: true, age: 38, name: { first: "John", last: "Carney" } },
        { isActive: false, age: 29, name: { first: "Dick", last: "Dunlap" } }
      ],
      fields: [
        {
          key: "name",
          label: "Person full name",
          sortable: true,
          sortDirection: "desc"
        },
        {
          key: "age",
          label: "Person age",
          sortable: true,
          class: "text-center"
        },
        {
          key: "isActive",
          label: "Is Active",
          // eslint-disable-next-line no-unused-vars
          formatter: (value, key, item) => {
            return value ? "Yes" : "No";
          },
          sortable: true,
          sortByFormatted: true,
          filterByFormatted: true
        },
        { key: "actions", label: "Actions" }
      ],
      pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc"
      // filterOn: []
      // infoModal: {
      //   id: "info-modal",
      //   title: "",
      //   content: ","
      // }
    };
  },
  watch: {},
  computed: {
    // search() {
    //   this.isBusy = true;
    //   setTimeout(() => {  console.log("World!"); }, 2000);
    // },
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    }
  },
  mounted() {
    this.loadData();

    // Set the initial number of items temporary
    // this.totalRows = this.items.length;
  },
  methods: {
    loadData() {
      // this.ListReq().then(response => {
      //   this.OptionTableReq();
      // });
      this.ListReq();
    },
    // async ListReq() {
    //   try {
    //     this.isBusy = true;
    //     let response = await this.axios.get("/api/MainAssemblyDataList");
    //     this.isBusy = false;
    //     this.totalRows = response.data.length;
    //     console.log(response.data);
    //     return response.data;
    //   } catch (error) {
    //     this.isBusy = false;
    //     return [];
    //   }
    // },
    async ListReq() {
      this.isBusy = true;

      await this.axios
        .get("/api/MainAssemblyDataList")
        .then(response => {
          this.isBusy = false;
          this.totalRows = response.data.length;
          this.ListData = response.data;
        })
        .catch(error => {
          this.isBusy = false;

          console.log(error);
        });
    },
    info(item) {
      // this.infoModal.title = `Row index: ${index}`;
      // this.infoModal.content = JSON.stringify(item, null, 2);
      // this.$root.$emit("bv::show::modal", this.infoModal.id, button);
      console.log(item);
      window.open("https://codal.ir" + item.HtmlUrl, "_blank");
    },
    // resetInfoModal() {
    //   this.infoModal.title = "";
    //   this.infoModal.content = "";
    // },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    }
  }
};
</script>
<style>
.Descision-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.Descision-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
</style>
