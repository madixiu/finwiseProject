<template>
  <!-- begin::Scrolltop -->
  <div id="kt_scrolltop" ref="kt_scrolltop" class="scrolltop">
    <span class="svg-icon">
      <inline-svg :src="ScrollIcon" />
    </span>
  </div>
  <!-- end::Scrolltop -->
</template>

<script>
import KTLayoutScrolltop from "@/assets/js/layout/extended/scrolltop.js";

export default {
  name: "KTScrollTop",
  mounted() {
    // Init Scrolltop
    KTLayoutScrolltop.init(this.$refs["kt_scrolltop"]);
  },
  computed: {
    ScrollIcon() {
      return process.env.BASE_URL + "media/svg/icons/Navigation/Up-2.svg";
    }
  }
};
</script>
