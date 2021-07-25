<template>
  <v-app id="app">
    <router-view></router-view>
  </v-app>
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

// Main style scss
// @import "assets/sass/style.vue";

// Check documentation for RTL css
// Update HTML with RTL attribute at public/index.html
// @import "assets/css/style.vue.rtl";
@import "assets/css/MainCSS.min.css";

.v-toolbar__content {
  height: 36px !important;
}
</style>

<script>
// import { OVERRIDE_LAYOUT_CONFIG } from "@/core/services/store/config.module";
import { VERIFY_ACCESS_TOKEN, REFRESH_ACCESS_TOKEN } from "@/graphql/mutations";
import { GET_USER } from "@/graphql/queries";
import JwtService from "@/core/services/jwt.service";
export default {
  name: "Finwise",
  watch: {
    $route: {
      handler(newValue, oldValue) {
        if (newValue != oldValue && oldValue != undefined) {
          this.checkRole();
        }
      },
      immediate: true
    }
  },
  created() {
    //****************CheckStorage ***********************************/
    if (JwtService.getToken()) {
      let refreshToken = this.CryptoJS.AES.decrypt(
        JwtService.getToken(),
        "key"
      ).toString(this.CryptoJS.enc.Utf8);
      this.getAccessTokenAndUser(refreshToken);
    }

    // ***************************************************************/
    this.loadData();
  },
  methods: {
    checkRole() {
      this.$router.beforeEach((to, from, next) => {
        let user = this.$store.getters.currentUser;
        if (
          (to.name == "Industries" ||
            to.name == "IndustriesDetail" ||
            to.name == "Taghadom" ||
            to.name == "TickerAssemblyDPSAndIC") &&
          Object.keys(user).length === 0
        )
          next({ name: "login" });
        if (
          (to.name == "AssemblyIC" || to.name == "TechnicalMoreInfo") &&
          (user.role < 2 || Object.keys(user).length === 0)
        )
          next({ name: "login" });
        if (
          (to.name == "Option" ||
            to.name == "commodities" ||
            to.name == "Monthly" ||
            to.name == "BalanceSheet" ||
            to.name == "IncomeStatement" ||
            to.name == "CashFlow" ||
            to.name == "AdjustedPrices") &&
          (user.role < 3 || Object.keys(user).length === 0)
        )
          next({ name: "login" });

        if (
          to.name == "CommoditiesDetail" &&
          (user.role < 4 || Object.keys(user).length === 0)
        )
          next({ name: "login" });
        else next();
      });
    },
    loadData() {
      this.axios
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
          this.$store.dispatch("LOGIN", data.data.users.edges[0].node);
          this.checkRole();
          this.LockCheck();
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
};
</script>
