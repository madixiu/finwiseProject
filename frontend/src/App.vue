<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
// 3rd party plugins css
@import "assets/sass/custom.scss";
@import "~bootstrap-vue/dist/bootstrap-vue.css";
@import "~perfect-scrollbar/css/perfect-scrollbar.css";
@import "~socicon/css/socicon.css";
@import "~@fortawesome/fontawesome-free/css/all.css";
@import "~line-awesome/dist/line-awesome/css/line-awesome.css";
@import "assets/plugins/flaticon/flaticon.css";
@import "assets/plugins/flaticon2/flaticon.css";
@import "assets/plugins/keenthemes-icons/font/ki.css";
@import "assets/font/MainFont.css";

// Main demo style scss
// @import "assets/sass/style.vue";

// Check documentation for RTL css
// Update HTML with RTL attribute at public/index.html
// @import "assets/css/style.vue.rtl";
@import "assets/css/unminifyCss";

// @import "assets/css/Unminified.style.vue.rtl";

// @font-face {
//   font-family: "Vazir";
//   src: local("Vazir.ttf "), url("assets/font/Vazir.ttf") format("truetype");
// }
/* * {
  font-family: "Vazir";
} */
</style>

<script>
// import { OVERRIDE_LAYOUT_CONFIG } from "@/core/services/store/config.module";
import { VERIFY_ACCESS_TOKEN, REFRESH_ACCESS_TOKEN } from "@/graphql/mutations";
import { GET_USER } from "@/graphql/queries";
import JwtService from "@/core/services/jwt.service";
export default {
  name: "Finwise",
  mounted() {
    this.loadData();
    //****************NEW CODE ***********************************/
    if (JwtService.getToken) {
      let refreshToken = this.CryptoJS.AES.decrypt(
        JwtService.getToken(),
        "key"
      ).toString(this.CryptoJS.enc.Utf8);
      this.getAccessTokenAndUser(refreshToken);
    }
    // ***************OLD CODE************************************/
    // if (
    //   this.$route.name !== "login" &&
    //   !this.$store.getters.isAuthenticated &&
    //   !JwtService.getToken()
    // ) {
    //   // next({ name: "login" });
    //   this.$router.push({ name: "login" });
    //   // this.$router.push({ name: "verify" });
    // } else if (JwtService.getToken() && !this.$store.getters.isAuthenticated) {
    //   console.log(!!this.$store.getters.currentUser.length);
    //   let hasUser = !!this.$store.getters.currentUser.length;
    //   if (hasUser) {
    //     // var LoginData;
    //     this.verifyAccessToken(this.$store.getters.currentUserAccessToken);
    //   } else if (this.$store.isAuthenticated) {
    //     this.$router.push({ path: "/" });
    //     // return;
    //     // this.$router.beforeEach((to, from, next) => {
    //     //   // reset config to initial state
    //     //   // store.dispatch(RESET_LAYOUT_CONFIG);
    //     //   next();
    //     //   // router.push({ name: "dashboard" });
    //     //   // Scroll page to top on every route change
    //     //   setTimeout(() => {
    //     //     window.scrollTo(0, 0);
    //     //   }, 100);
    //     // });
    //   } else if (!hasUser) {
    //     let refreshToken = this.CryptoJS.AES.decrypt(
    //       JwtService.getToken(),
    //       "key"
    //     ).toString(this.CryptoJS.enc.Utf8);
    //     console.log(refreshToken);
    //     this.getAccessTokenAndUser(refreshToken);
    //     // let token = this.$store.getters.currentUserAccessToken;
    //     // this.getQueryUser();
    //     console.log(this.$store.getters.currentUserAccessToken);
    //   }
    //   // else {
    //   //   this.$router.push({ name: "login" });
    //   //   return;
    //   // }
    // }
    /**
     * this is to override the layout config using saved data from localStorage
     * remove this to use config only from static json (@/core/config/layout.config.json)
     */
    // this.$store.dispatch(OVERRIDE_LAYOUT_CONFIG);
  },
  methods: {
    async loadData() {
      await this.axios
        .get("/api/MainSearchBar")
        .then(SearchResponse => {
          let data = SearchResponse.data;
          // console.log(data);
          if (data != "noData") this.$store.dispatch("setSearch", data);
        })
        .catch(error => {
          console.error(error);
        });
    },
    getQueryUser(UserName) {
      // let token = this.$store.getters.currentUserAccessToken;
      this.$apollo
        .query({
          query: GET_USER,
          // headers: {
          // authorization: token ? `JWT ${token}` : ""
          // }
          variables: {
            username: UserName
          }
        })
        .then(data => {
          // console.log("query");
          // console.log(data);
          // console.log(data.data.me);
          this.$store.dispatch("LOGIN", data.data.users.edges[0].node);
          this.LockCheck();

          // this.$router.push({ path: "/" });
        });
    },
    verifyAccessToken(AccessToken) {
      this.$apollo
        .mutate({
          mutation: VERIFY_ACCESS_TOKEN,
          variables: {
            token: AccessToken
          }
        })
        .then(data => {
          // console.log(data);
          let LoginData = data.data.verifyToken;
          // console.log(LoginData.success);
          if (LoginData.success) {
            // this.$router.push({ name: "Dashboard" });
          } else if (LoginData == false) {
            let Rtoken = this.CryptoJS.AES.decrypt(
              JwtService.getToken(),
              "key"
            ).toString(this.CryptoJS.enc.Utf8);
            this.getAccessTokenAndUser(Rtoken);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    getAccessTokenAndUser(RefreshToken) {
      // console.log(RefreshToken);
      // console.log("we are in");
      this.$apollo
        .mutate({
          mutation: REFRESH_ACCESS_TOKEN,
          variables: {
            refreshToken: RefreshToken
          }
        })
        .then(data => {
          // console.log(data);
          let LoginData = data.data.refreshToken;
          // console.log(LoginData);
          if (!data.data.errors) {
            // console.log(LoginData.success);
            if (LoginData.success) {
              // store new acc token to vuex

              this.$store.dispatch("RenewAccessToken", LoginData.token);
              this.getQueryUser(LoginData.payload.username);
              // this.$router.push({ name: "Dashboard" });
            } else {
              // console.log(LoginData.errors.nonFieldErrors[0].message);
              this.$store.dispatch("LOGOUT");
              // this.$router.push({ name: "login" });
              // this.$router.push({ name: "verify" });
            }
          } else {
            // console.log(LoginData.errors.nonFieldErrors[0].message);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    LockCheck() {
      let user = this.$store.getters.currentUser;

      if (this.$store.getters.isAuthenticated && user.role == 2)
        this.$store.dispatch("setOptionStatus", false);
    }
    // checkVerify() {
    //   if (!JwtService.getToken()) {
    //     // push to login
    //   } else {
    //     // do refresh the access token
    //   }
    //   if (this.$store.getters.isAuthenticated == false) {
    //   }
    // }
  }
  // updated() {
  //  console.log(this.$route.path)
  // }
};
</script>
