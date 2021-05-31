<template>
  <div>
    <div class="col-12">
      <!-- User Interface controls -->
      <v-card>
        <v-toolbar dense flat>
          <v-toolbar-title v-if="cardKey">لیست مجامع</v-toolbar-title>
          <v-toolbar-title v-if="!cardKey">{{ AssemblyName }}</v-toolbar-title>

          <!-- <v-card-title v-if="cardKey">لیست مجامع</v-card-title> -->
          <!-- <v-card-title v-if="!cardKey">{{ AssemblyName }}</v-card-title> -->
          <v-card-subtitle style="textalign:right" v-if="!cardKey">
            <span> {{ subTitle }}</span>
          </v-card-subtitle>
          <v-spacer></v-spacer>

          <v-btn v-if="!cardKey" icon @click="cardKey = !cardKey">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
        </v-toolbar>
        <transition-group name="slide-fade" tag="div">
          <div v-show="cardKey" key="1">
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
                  <b-spinner class="align-middle mr-2"></b-spinner>
                  <strong>شکیبا باشید</strong>
                </div>
              </template>
              <template #cell(title)="row">
                <b class="AssemblyTitle" @click="titleClick(row)">{{
                  row.value
                }}</b>
              </template>

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
                class="my-0 paginationClass"
              ></b-pagination>
            </b-col>
          </div>
          <div v-if="!cardKey" key="2">
            <!-- ******************** TABLE COMPONENT ********************* -->
            <AssemblyTables
              :ShareholdersItems="ShareholdersData"
              :ChiefItems="ChiefData"
              :SummaryItems="SummaryData"
              :ICitems="ICData"
              :StatementItems="StatementData"
              :CEOItems="CEOData"
              :BoardItems="BoardData"
              :NewBoardItems="NewBoardData"
              :WageItems="WageData"
            >
            </AssemblyTables>
            <!-- ******************** TABLE COMPONENT ********************* -->
          </div>
        </transition-group>
      </v-card>
    </div>
  </div>
</template>
<script>
// import Wizard from "@/view/pages/Saham/Majame/content/Wizard";
import AssemblyTables from "@/view/pages/Ticker/AssemblyWidget/content/AssemblyTables.vue";
export default {
  name: "Decisions",
  components: { AssemblyTables },
  data() {
    return {
      cardKey: true,
      AssemblyName: "",
      subTitle: "",
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

      pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      ShareholdersData: [],
      ChiefData: [],
      SummaryData: [],
      ICData: [],
      StatementData: [],
      CEOData: [],
      BoardData: [],
      NewBoardData: [],
      WageData: []
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
  created() {
    document.title = "Finwise - تصمیمات مجامع";
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

          console.error(error);
        });
    },
    TablesReq(ID, type) {
      this.axios({
        method: "post",
        url: "/api/tickerAssemblyStepTwo",
        data: {
          SummaryID: ID,
          Type: "Assembly" + type
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          let data = response.data;
          if (type == "General") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
          } else if (type == "Extra") {
            this.StatementData = [];
            this.CEOData = [];
            this.BoardData = [];
            this.NewBoardData = [];
            this.WageData = [];
            this.ICData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.SummaryData = data[3];
          } else if (type == "GeneralExtra") {
            this.ICData = [];
            this.StatementData = data[0];
            this.ChiefData = data[1];
            this.ShareholdersData = data[2];
            this.CEOData = data[3];
            this.BoardData = data[4];
            this.NewBoardData = data[5];
            this.WageData = data[6];
            this.SummaryData = data[7];
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    titleClick(item) {
      this.TablesReq(item.item.ID, item.item.Type);
      // console.log(item.item);
      this.subTitle = item.item.title;
      this.AssemblyName = item.item.Ticker;
      this.cardKey = false;
    },
    info(item) {
      // this.infoModal.title = `Row index: ${index}`;
      // this.infoModal.content = JSON.stringify(item, null, 2);
      // this.$root.$emit("bv::show::modal", this.infoModal.id, button);
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
/* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
.AssemblyTitle {
  color: #4682b4;
  cursor: pointer;
}
.Descision-table-head {
  font-size: 0.8rem;
  font-weight: 500;
}
.Descision-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
}
.Descision-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
.paginationClass {
  font-family: "Vazir-Medium-FD" !important;
}
</style>
