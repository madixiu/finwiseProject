<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <ICWidget :notices="notice"></ICWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import ICWidget from "@/view/pages/Ticker/AssemblyWidget/AssemblyICwidget.vue";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    ICWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعیه های کدال" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getAllowed().then(response => {
        // eslint-disable-next-line no-unused-vars
        this.getOne().then(response2 => {
          this.getTwo().then(function() {});
        });
      });
    },
    async getAllowed() {
      await this.axios
        .get("/api/tickerallnames")
        .then(response3 => {
          this.allowed = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTwo() {
      await this.axios
        .get("/api/CodalNotices/" + this.$route.params.id)
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/SubHeaderW/" + this.$route.params.id)
        .then(response1 => {
          this.subheaders = response1.data[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
