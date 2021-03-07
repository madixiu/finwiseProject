<template>
  <div>
    <!--begin::Header -->
    <div
      class="d-flex flex-column flex-center py-10 bgi-size-cover bgi-no-repeat rounded-top"
      :style="{ backgroundImage: `url(${backgroundImage})` }"
    >
      <h4 class="text-white font-weight-bold">
        حساب کاربری
      </h4>
      <!-- <span class="btn btn-success btn-sm font-weight-bold font-size-sm mt-2">
        23 tasks pending
      </span> -->
    </div>
    <!--end::Header -->

    <!--begin::Nav -->
    <div class="row row-paddingless">
      <div class="col-6 item"  @click="ToProfile">
        <span class="svg-icon svg-icon-3x svg-icon-success">
          <!--begin::Svg Icon-->
          <inline-svg :src="list[0].svg" />
          <!--end::Svg Icon-->
        </span>
        <span
          class="d-block text-dark-75 font-weight-bold font-size-h6 mt-2 mb-1"
        >
          {{ list[0].title }}
        </span>
        <span class="d-block text-dark-50 font-size-lg">
          {{ list[0].desc }}
        </span>
      </div>
      <div
        v-if="!this.$store.getters.isAuthenticated"
        class="col-6 item"
        @click="LogIn"
      >
        <span class="svg-icon svg-icon-3x svg-icon-success">
          <!--begin::Svg Icon-->
          <inline-svg :src="list[1].svg" />
          <!--end::Svg Icon-->
        </span>
        <span
          class="d-block text-dark-75 font-weight-bold font-size-h6 mt-2 mb-1"
        >
          {{ list[1].title }}
        </span>
        <span class="d-block text-dark-50 font-size-lg">
          {{ list[1].desc }}
        </span>
      </div>
      <div
        v-if="this.$store.getters.isAuthenticated"
        class="col-6 item"
        @click="LogOut"
      >
        <span class="svg-icon svg-icon-3x svg-icon-success">
          <!--begin::Svg Icon-->
          <inline-svg :src="list[2].svg" />
          <!--end::Svg Icon-->
        </span>
        <span
          class="d-block text-dark-75 font-weight-bold font-size-h6 mt-2 mb-1"
        >
          {{ list[2].title }}
        </span>
        <span class="d-block text-dark-50 font-size-lg">
          {{ list[2].desc }}
        </span>
      </div>
      <!--begin:Item-->
      <!--end:Item-->
    </div>
    <!--end::Nav -->
  </div>
</template>

<script>
export default {
  name: "KTDropdownQuickAction",
  data() {
    return {
      list: [
        {
          title: "تنظیمات",
          desc: "",
          svg:
            process.env.BASE_URL +
            "media/svg/icons/Communication/Mail-attachment.svg"
        },
        {
          title: "ورود",
          desc: "",
          svg: process.env.BASE_URL + "media/svg/icons/Navigation/Sign-in.svg"
        },
        {
          title: "خروج",
          desc: "",
          svg: process.env.BASE_URL + "media/svg/icons/Navigation/Sign-out.svg"
        }
        // {
        //   title: "Projects",
        //   desc: "Pending Tasks",
        //   svg: process.env.BASE_URL + "media/svg/icons/Shopping/Box2.svg"
        // },
        // {
        //   title: "Customers",
        //   desc: "Latest Cases",
        //   svg: process.env.BASE_URL + "media/svg/icons/Communication/Group.svg"
        // }
      ]
    };
  },
  methods: {
    LogOut() {
      this.$store
        .dispatch("LOGOUT")
        .then(() => this.$router.push({ name: "login" }));
    },
    LogIn() {
      this.$router.push({ name: "login" });
    },
    ToProfile() {
      this.$router.push({ name: "profile" });
    }
  },

  computed: {
    backgroundImage() {
      return process.env.BASE_URL + "media/misc/bg-1.jpg";
    }
  }
};
</script>
<style scoped>
.item {
  text-align: center;
  cursor: pointer;
}
</style>
