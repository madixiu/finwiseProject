<template>
  <!--begin::Card-->
  <b-card>
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <b-card-title style="text-align:right">رمز عبور</b-card-title>
        <b-card-sub-title style="text-align:right"
          >تغییر رمز عبور</b-card-sub-title
        >
      </div>
      <div class="card-toolbar">
        <button
          type="submit"
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
      <b-card-body>
        <div class="form-group row">
          <span class="profile-labels">رمز عبور فعلی</span>
          <div class="mt-7 mr-2">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid mb-2"
              value=""
              placeholder="رمز عبور فعلی"
              name="current_password"
              ref="current_password"
            />
            <a href="#" class="">فراموشی رمز عبور</a>
          </div>
          <!-- <div class="" style="direction:rtl;padding:0px">
            <a href="#"  class="">فراموشی رمز عبور</a>

          </div> -->
        </div>
        <div class="form-group row">
          <span class="profile-labels">رمز عبور جدید</span>
          <div class="mr-2">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid"
              value=""
              placeholder="رمز عبور جدید"
              name="new_password"
              ref="new_password"
            />
          </div>
        </div>
        <div class="form-group row">
          <span class="profile-labels">تکرار رمز عبور</span>
          <div class="mr-2">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid"
              value=""
              placeholder="تکرار رمز عبور"
              name="verify_password"
              ref="verify_password"
            />
          </div>
        </div>
      </b-card-body>
    </form>
    <!--end::Form-->
  </b-card>
</template>

<script>
import { mapGetters } from "vuex";
// import { UPDATE_PASSWORD } from "@/core/services/store/auth.module";
// import KTUtil from "@/assets/js/components/util";

// import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
// import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
// import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
// import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";
// import Swal from "sweetalert2";
import {
  VERIFY_ACCESS_TOKEN,
  REFRESH_ACCESS_TOKEN,
  PASS_CHANGE
} from "@/graphql/mutations";
import JwtService from "@/core/services/jwt.service";

export default {
  name: "ChangePassword",
  data() {
    return {
      password: "",
      status: "",
      valid: true
    };
  },
  mounted() {
    // const password_change_form = KTUtil.getById("kt_password_change_form");
    // var curr_password = this.currentUser.password;
    // this.fv = formValidation(password_change_form, {
    //   fields: {
    //     current_password: {
    //       validators: {
    //         notEmpty: {
    //           message: "Current password is required"
    //         },
    //         identical: {
    //           compare: function() {
    //             return curr_password;
    //           },
    //           message: "Wrong password"
    //         }
    //       }
    //     },
    //     new_password: {
    //       validators: {
    //         notEmpty: {
    //           message: "New password is required"
    //         }
    //       }
    //     },
    //     verify_password: {
    //       validators: {
    //         notEmpty: {
    //           message: "Confirm password is required"
    //         },
    //         identical: {
    //           compare: function() {
    //             return password_change_form.querySelector(
    //               '[name="new_password"]'
    //             ).value;
    //           },
    //           message: "The password and its confirm are not the same"
    //         }
    //       }
    //     }
    //   },
    //   plugins: {
    //     trigger: new Trigger(),
    //     bootstrap: new Bootstrap(),
    //     submitButton: new SubmitButton()
    //   }
    // });
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
          let LoginData = data.data.verifyToken;
          if (LoginData.success) {
            // this.$store.dispatch("RenewAccessToken", LoginData.token);
            this.ChangePass();
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
              this.ChangePass();
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
    ChangePass() {
      this.$apollo
        .mutate({
          mutation: PASS_CHANGE,
          variables: {
            oldPassword: this.$refs.current_password.value,
            newPassword1: this.$refs.new_password.value,
            newPassword2: this.$refs.verify_password.value
          }
        })
        .then(data => {
          if (data.data.passwordChange.success) {
            let encryptedRefreshToken = this.encryption(
              data.data.passwordChange.refreshToken,
              "key"
            );

            JwtService.destroyToken();
            JwtService.saveToken(encryptedRefreshToken);
            this.$store.dispatch(
              "RenewAccessToken",
              data.data.passwordChange.token
            );
          }
        });
    },
    save() {
      // this.fv.validate();

      // this.fv.on("core.form.valid", () => {
      // var password = this.$refs.new_password.value;
      const submitButton = this.$refs["kt_save_changes"];

      // set spinner to submit button
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send update request
        // this.$store
        // .dispatch(UPDATE_PASSWORD, { password })
        // go to which page after successfully update
        // .then(() => this.$router.push({ name: "dashboard" }));

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
      // });

      // this.fv.on("core.form.invalid", () => {
      //   Swal.fire({
      //     title: "",
      //     text: "Please, provide correct data!",
      //     icon: "error",
      //     confirmButtonClass: "btn btn-secondary"
      //   });
      // });
    },
    cancel() {
      // this.fv.resetForm();
      this.$refs.current_password.value = "";
      this.$refs.new_password.value = "";
      this.$refs.verify_password.value = "";
    }
  },
  computed: {
    ...mapGetters(["currentUser"])
  }
};
</script>

<style scoped>
.profile-labels {
  text-align: right !important;
  margin-top: auto !important;
  margin-bottom: auto !important;
}
</style>
