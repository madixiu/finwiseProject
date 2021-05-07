<template>
  <div class="row" style="padding-top:5px">
    <div class="col-xxl-6 col-lg-6 col-md-12 col-sm-12">
      <div class="row">
        <TechnicalCharts
          :inpuDataTechnical="TechnicalData"
          class="mb-4"
        ></TechnicalCharts>
      </div>
    </div>
    <div class="col-xxl-6 col-lg-6 col-md-12 col-sm-12">
      <div class="row">
        <CorrMatrix :inpuDataCorr="CorrData" class="mb-4"></CorrMatrix>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import TechnicalCharts from "@/view/pages/Crypto/Widgets/TechnicalChart.vue";
import CorrMatrix from "@/view/pages/Crypto/Widgets/CorrMatrix.vue";
export default {
  name: "CryptoDashboard",
  components: {
    TechnicalCharts,
    CorrMatrix
  },
  data() {
    return {
      dataFetched: false,
      TechnicalData: [],
      CorrData: [],
      ResponeseTimeout: {
        getTechnicalData: true,
        getCorrData: true
      }
    };
  },
  created() {
    document.title = "FinWise - رمز ارز";
  },
  mounted() {
    // this.test();
    this.ResponeseTimeout = {
      getTechnicalData: true,
      getCorrData: true
    };
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "داشبورد رمز ارز" }]);
    this.loadData();

    // this.make_requests_handler();
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getTechnical().then(resp0 => {
        // eslint-disable-next-line no-unused-vars
        this.getCorrelationM().then(resp1 => {});
        // eslint-disable-next-line no-unused-vars
        // this.getTradesAll().then(resp1 => {
        // eslint-disable-next-line no-unused-vars
        // });
      });
    },
    async getTechnical() {
      await this.axios
        .get("/api/CryptoTechincalAll")
        .then(getHighestQResp => {
          this.ResponeseTimeout.getTechnicalData = false;
          this.TechnicalData = getHighestQResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            this.ResponeseTimeout.getTechnicalData = true;
          // setTimeout(this.getHighestQ(), 1000);
          else console.error(error);
        });
    }
    ,
    async getCorrelationM() {
      await this.axios
      .get("/api/CryptoHistoricCorr")
        .then(getHighestQResp => {
          this.ResponeseTimeout.getCorrData = false;
          this.CorrData = getHighestQResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            this.ResponeseTimeout.getCorrData = true;
          // setTimeout(this.getHighestQ(), 1000);
          else console.error(error);
        });
    }
  },

  setActiveTab1(event) {
    this.tabIndex = this.setActiveTab(event);
  },
  setActiveTab2(event) {
    this.tabIndex2 = this.setActiveTab(event);
  },
  /**
   * Set current active on click
   * @param event
   */
  setActiveTab(event) {
    // get all tab links
    const tab = event.target.closest('[role="tablist"]');
    const links = tab.querySelectorAll(".nav-link");
    // remove active tab links
    for (let i = 0; i < links.length; i++) {
      links[i].classList.remove("active");
    }

    // set current active tab
    event.target.classList.add("active");

    // set clicked tab index to bootstrap tab
    return parseInt(event.target.getAttribute("data-tab"));
  }
};
</script>
