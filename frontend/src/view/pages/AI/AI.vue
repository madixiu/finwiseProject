<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      BBBBBB
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import axios from "axios";
export default {
  name: "AI",
  components: {},
  data() {
    return {};
  },
  mounted() {
    // this.loadData2();
    // this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "بازار رمز ارز" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {}
};
</script>
