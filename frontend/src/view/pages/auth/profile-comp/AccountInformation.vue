<template>
  <!--begin::Card-->
  <b-card>
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <b-card-title style="text-align:right"
          >اطلاعات حساب کاربری</b-card-title
        >
        <b-card-sub-title style="text-align:right"
          >تغییرات اطلاعات کاربری
        </b-card-sub-title>
      </div>
      <div class="card-toolbar">
        <button
          type="reset"
          class="btn btn-success mr-2"
          @click="save()"
          ref="kt_save_changes"
        >
          ذخیره
        </button>
        <button type="reset" class="btn btn-secondary" @click="cancel()">
          لغو
        </button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
    <form class="form">
      <div class="card-body">
        <!--begin::Heading-->
        <div class="row">
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mb-6 text-right">حساب کاربری:</h5>
          </div>
        </div>
        <!--begin::Form Group-->
        <div class="form-group row">
          <label class="col-xl-1 col-lg-1 col-form-label profile-labels"
            >نام کاربری</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class=" spinner-sm spinner-success spinner-right">
              <input
                class="form-control form-control-lg form-control-solid"
                type="text"
                ref="username"
                :value="currentUser.username"
              />
            </div>
          </div>
        </div>
        <!--begin::Form Group-->
        <div class="form-group row">
          <label
            class="col-xl-1 col-lg-1 col-form-label profile-labels"
            style="text-align:right"
            >ایمیل</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="la la-at"></i>
                </span>
              </div>
              <input
                type="text"
                class="form-control form-control-lg form-control-solid"
                ref="email"
                :value="currentUser.email"
                placeholder="Email"
              />
            </div>
          </div>
        </div>

        <!--begin::Form Group-->
        <div class="separator separator-dashed my-5"></div>
        <!--begin::Form Group-->
        <!-- <div class="row">
          <label class="col-xl-3"></label>
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mb-6">Security:</h5>
          </div>
        </div> -->
        <!--begin::Form Group-->
        <!-- <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label"
            >Login verification</label
          >
          <div class="col-lg-9 col-xl-6">
            <button
              type="button"
              class="btn btn-light-primary font-weight-bold btn-sm"
            >
              Setup login verification
            </button>
            <p class="form-text text-muted pt-2">
              After you log in, you will be asked for additional information to
              confirm your identity and protect your account from being
              compromised. <a href="#" class="font-weight-bold">Learn more</a>.
            </p>
          </div>
        </div> -->
      </div>
    </form>
    <!--end::Form-->
  </b-card>

  <!--end::Card-->
</template>

<script>
import {
  VERIFY_ACCESS_TOKEN,
  REFRESH_ACCESS_TOKEN,
  UPDATE_USER
} from "@/graphql/mutations";
import JwtService from "@/core/services/jwt.service";
import { mapGetters } from "vuex";

export default {
  name: "AccountInformation",
  data() {
    return {};
  },
  methods: {
    verifyAccessToken() {
      this.$apollo
        .mutate({
          mutation: VERIFY_ACCESS_TOKEN,
          variables: {
            token: this.$store.getters.currentUserAccessToken
          }
        })
        .then(data => {
          // console.log(data);
          let LoginData = data.data.verifyToken;
          if (LoginData.success) {
            // this.$store.dispatch("RenewAccessToken", LoginData.token);
            this.UpdateAccount();
          } else if (LoginData == false) {
            let Rtoken = this.CryptoJS.AES.decrypt(
              JwtService.getToken(),
              "key"
            ).toString(this.CryptoJS.enc.Utf8);
            this.refreshAccessToken(Rtoken);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    refreshAccessToken(RefreshToken) {
      this.$apollo
        .mutate({
          mutation: REFRESH_ACCESS_TOKEN,
          variables: {
            refreshToken: RefreshToken
          }
        })
        .then(data => {
          let LoginData = data.data.refreshToken;
          if (!data.data.errors) {
            if (LoginData.success) {
              // store new acc token to vuex

              this.$store.dispatch("RenewAccessToken", LoginData.token);
              this.UpdateAccount();
              // this.getQueryUser(LoginData.payload.username);
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
    UpdateAccount() {
      this.$apollo
        .mutate({
          mutation: UPDATE_USER,
          variables: {
            firstName: this.$store.getters.currentUser.firstName,
            lastName: this.$store.getters.currentUser.lastName,
            age: this.$store.getters.currentUser.age,
            degree: this.$store.getters.currentUser.degree,

            username: this.$refs.username.value,
            email: this.$refs.email.value,
            gender: ""
          }
        })
        .then(data => {
          if (data.data.updateAccount.success) {
            // console.log(data);
            // console.log("Success");
            let user = this.currentUser;
            // console.log(user);
            (user.firstName = this.$refs.firstName.value),
              (user.lastName = this.$refs.lastName.value),
              (user.age = this.currentUser.age),
              (user.degree = this.currentUser.degree),
              (user.gender = "");
            this.$store.dispatch("updateUser", user);
          } else console.error("error");
        })
        .catch(error => {
          console.error(error);
        });
    },
    save() {
      // var username = this.$refs.username.value;
      // var email = this.$refs.email.value;

      // set spinner to submit button
      const submitButton = this.$refs["kt_save_changes"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        if (this.$store.getters.currentUserAccessToken)
          this.verifyAccessToken();
        else
          this.refreshAccessToken(
            this.CryptoJS.AES.decrypt(JwtService.getToken(), "key").toString(
              this.CryptoJS.enc.Utf8
            )
          );
        // send update request
        // this.$store.dispatch(UPDATE_ACCOUNT_INFO, {
        //   username,
        //   email

        // });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    },
    cancel() {
      this.$refs.username.value = this.currentUser.username;
      this.$refs.email.value = this.currentUser.email;
    }
  },
  computed: {
    ...mapGetters(["currentUser"])
  }
};
</script>

<style scoped>
.profile-labels {
  text-align: right;
  margin-top: auto;
  margin-bottom: auto;
}
</style>
