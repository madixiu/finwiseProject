<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <StatusChangesWidget :notices="notice"></StatusChangesWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import StatusChangesWidget from "@/view/pages/Ticker/TickerWidgets/StatusChangeWidget.vue";
import axios from "axios";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    StatusChangesWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  mounted() {
    // this.loadData2();
    this.loadData3();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "تغییر وضعیت سهم" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
      // console.log(this.notices);
    },
    allowed() {
      var flag = false;
      for (var i = 0; i < this.allowed.length; i++) {
        var obj = this.allowed[i];
        if (obj.ID == this.$route.params.id) {
          flag = true;
        }
      }
      if (!flag) {
        this.$router.push({ name: "wizard" });
      }
    }
  },
  methods: {
    loadData3() {
      this.getAllowed().then(response => {
        console.log(response);
        //add this to package.json in developement
        //         "eslintConfig": {
        //     "rules": {
        //       "no-console": "off",
        //       "no-unused-vars": "off"
        //     }
        // },
        this.getOne().then(response2 => {
          console.log(response2);
          this.getTwo().then(function() {});
          // console.log("ChainDone");
        });
      });
    },
    async getAllowed() {
      await axios
        .get("http://localhost:8000/api/tickerallnames")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.allowed = response3.data;
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getTwo() {
      await axios
        .get(
          "http://localhost:8000/api/StatusChanges/" +
            this.$route.params.id +
            "/"
        )
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.notice = response2.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getOne() {
      await axios
        .get(
          "http://localhost:8000/api/SubHeaderW/" + this.$route.params.id + "/"
        )
        .then(response1 => {
          // console.log("firstDone");
          this.subheaders = response1.data[0];
          // console.log(response1.data);
        })
        .catch(error => {
          // console.log("GetOneCatch");
          console.log(error);
        });
    }
  }
};
</script>
