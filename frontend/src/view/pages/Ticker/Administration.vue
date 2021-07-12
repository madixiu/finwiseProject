<template>
  <div>
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <AdminNoticeWidget :notices="notice"></AdminNoticeWidget>
      </div>
    </div>
  </div>
</template>
<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import AdminNoticeWidget from "@/view/pages/Ticker/TickerWidgets/AdministrationNoticeWidget.vue";
export default {
  name: "AdminNotice",
  components: {
    SubHeaderWidget,
    AdminNoticeWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - پیام ناظر";
  },

  mounted() {
    // this.loadData2();
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "پیام ناظر" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response2 => {
        this.getTwo();
      });
    },
    // async getAllowed() {
    //   await this.axios
    //     .get("/api/tickerallnames")
    //     .then(response3 => {
    //       this.allowed = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
    async getTwo() {
      await this.axios
        .get("/api/AdminNotice/" + this.$route.params.id + "/")
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
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
