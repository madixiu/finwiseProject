<template>
  <div>
    <!--begin::Content header-->
    <v-card class="cardColor">
      <v-container>
        <!-- //? title -->
        <div class="">
          <div class="text-center">
            <v-chip class="chip-top">
              <span style="color:white" class="pr-2 pl-2">ورود</span>
            </v-chip>
          </div>
          <v-divider></v-divider>

          <!-- //? begin::Form-->
          <b-form
            class="form"
            autocomplete="off"
            @submit.stop.prevent="onSubmit"
          >
            <!-- <div role="alert" class="alert alert-info">
              <div class="alert-text">
                <strong>شماره موبایل</strong> و <strong>رمز عبور</strong>خود را
                وارد کنید
              </div>
            </div> -->
            <div
              v-if="errors.length"
              role="alert"
              v-bind:class="{ show: errors.length }"
              class="alert fade alert-danger"
            >
              <div class="alert-text" v-for="(error, i) in errors" :key="i">
                {{ error }}
              </div>
            </div>
            <!--//? email input -->
            <b-form-group
              id="login-input-group-1"
              label=""
              label-for="login-input-1"
            >
              <b-form-input
                class="input-form"
                id="login-input-1"
                name="login-input-1"
                placeholder="شماره موبایل"
                v-model="$v.form.phonenumber.$model"
                :state="validateState('phonenumber')"
                aria-describedby="phone-live-feedback"
              ></b-form-input>

              <b-form-invalid-feedback id="phone-live-feedback">
                شماره موبایل خود را وارد کنید
              </b-form-invalid-feedback>
            </b-form-group>
            <!--//? password input -->
            <b-form-group
              id="login-input-group-2"
              label=""
              label-for="login-input-2"
            >
              <b-form-input
                class="input-form"
                type="password"
                id="login-input-2"
                name="login-input-2"
                placeholder="رمز عبور"
                v-model="$v.form.password.$model"
                :state="validateState('password')"
                aria-describedby="password-live-feedback"
              ></b-form-input>

              <b-form-invalid-feedback id="password-live-feedback">
                رمز عبور خود را صحیح وارد کنید
              </b-form-invalid-feedback>
            </b-form-group>
            <!--begin::Action-->
            <div
              class="form-group d-flex flex-wrap justify-content-between align-items-center"
            >
              <p class="WrongCredMsg" v-if="ErrorMsgflag">
                شماره موبایل و رمز عبور صحیح نمی باشد
              </p>
            </div>
            <!-- //? captcha section  -->
            <v-row no-gutters>
              <v-col class="d-flex align-center" cols="6">
                <b-form-group
                  style="margin-bottom:0px !important"
                  id="login-input-group-3"
                  label=""
                  label-for="login-input-3"
                >
                  <b-form-input
                    id="login-input-3"
                    name="login-input-3"
                    placeholder="عبارت امنیتی"
                    v-model="form.captcha"
                    aria-describedby="captcha-live-feedbackLogin"
                  ></b-form-input>

                  <b-form-invalid-feedback id="captcha-live-feedbackLogin">
                    عبارت امنیتی
                  </b-form-invalid-feedback>
                </b-form-group>
              </v-col>
              <v-col class="d-flex justify-end">
                <i
                  id="LoginRefreshIcon"
                  @click="refresh"
                  aria-hidden="true"
                  class="v-icon notranslate mdi mdi-refresh theme--light"
                ></i>
                <vue-captcha
                  ref="captcha"
                  :captcha.sync="code"
                  :fontSize="19"
                  textFillColor="#ff0000"
                  :width="120"
                >
                </vue-captcha>
              </v-col>
            </v-row>
            <div
              class="form-group d-flex flex-wrap justify-content-between align-items-center"
            >
              <p class="WrongCredMsg" v-if="CaptchaErrorMsgflag">
                عبارت امنیتی به درستی وارد نشده است
              </p>
            </div>

            <!--//? submit button -->
            <div
              class="form-group d-flex flex-wrap justify-content-center align-items-center mt-2"
            >
              <v-btn
                block
                color="#4CAF50"
                class="submit-button"
                :loading="buttonLoading"
                @click="onSubmit"
                >ورود</v-btn
              >
              <router-link
                class="text-dark-60 text-hover-primary mt-2"
                id="kt_login_forgot"
                :to="{ name: 'passwordReset' }"
              >
                فراموشی رمز عبور
              </router-link>
            </div>
            <v-divider></v-divider>
            <div class="justify-content-center">
              <router-link
                class="font-weight-bold font-size-3 ml-2"
                :to="{ name: 'register' }"
              >
                ثبت نام
              </router-link>
            </div>
            <!--end::Action-->
            <!--end::Form-->
          </b-form>
        </div></v-container
      >
    </v-card>

    <!--end::Signin-->
  </div>
</template>
<script>
// import { mapState } from "vuex";
import VueCaptcha from "vue-captcha-code";
import { mapGetters } from "vuex";
// import gql from "graphql-tag";
// import { LOGIN, LOGOUT } from "@/core/services/store/auth2.module";
// import { LOGIN } from "@/core/services/store/auth";
import { validationMixin } from "vuelidate";
import {
  // email,
  minLength,
  required,
  maxLength,
  integer
} from "vuelidate/lib/validators";
import { LOGIN_USER } from "@/graphql/mutations";
import JwtService from "@/core/services/jwt.service";

export default {
  components: { VueCaptcha },
  mixins: [validationMixin],
  name: "login",
  // eslint-disable-next-line no-unused-vars
  beforeRouteEnter: (to, from, next) => {
    next(vm => {
      if (from.path != "/passReset" && from.path != "/register")
        vm.NextRoutePath = from.path;
      else vm.NextRoutePath = "/StockMarket/Dashboard/";
    });
    // next();
  },
  data() {
    return {
      code: "",
      NextRoutePath: "",
      buttonLoading: false,
      verified: true,
      ErrorMsgflag: false,
      CaptchaErrorMsgflag: false,
      ErrorMsgText: "",
      ErrorMsg: [
        "خطایی رخ داده است",
        "مشخصات وارد شده صحیح نمی باشد",
        "اکانت شما تایید نشده است"
      ],
      form: {
        // email: "",
        phonenumber: "",
        password: "",
        captcha: ""
      }
    };
  },
  validations: {
    form: {
      // email: {
      //   required,
      //   email
      // },
      phonenumber: {
        integer,
        required,
        minLength: minLength(11),
        maxLength: maxLength(11)
      },
      password: {
        required,
        minLength: minLength(8)
      }
    }
  },
  watch: {
    "form.captcha"(newValue, oldValue) {
      if (oldValue != "" && newValue == "") this.CaptchaErrorMsgflag = false;
    }
  },
  methods: {
    //* Captcha code handler NOT using it for now
    // handleChange(code) {
    // },
    refresh() {
      this.$refs.captcha.refreshCaptcha();
    },
    LockCheck() {
      let user = this.$store.getters.currentUser;
      if (user.role == 2) this.$store.dispatch("setOptionStatus", false);
    },
    checkError() {
      let errors = this.$store.getters.errors;
      if (errors.code == "invalid_credentials") {
        this.ErrorMsgflag = true;
        this.ErrorMsgText = this.ErrorMsg[1];
      } else if (errors.code == "not_verified") {
        this.ErrorMsgflag = true;
        this.ErrorMsgText = this.ErrorMsg[2];
        this.verified = false;
      } else {
        this.ErrorMsgflag = true;
        this.ErrorMsgText = this.ErrorMsg[0];
      }
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        phonenumber: null,
        // email: null,
        password: null
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },
    encryption(input, key) {
      let encrypted = this.CryptoJS.AES.encrypt(input, key).toString();
      return encrypted;
    },
    decryption(input, key) {
      let decrypted = this.CryptoJS.AES.decrypt(input, key).toString(
        this.CryptoJS.enc.Utf8
      );
      return decrypted;
    },
    onSubmit() {
      this.$v.form.$touch();
      //! here you write the captcha check function
      if (this.$v.form.$anyError || this.form.captcha == "") {
        return;
      }
      if (this.form.captcha != this.code) {
        this.CaptchaErrorMsgflag = true;
        this.refresh();
        return;
      }
      const phonenumber = this.$v.form.phonenumber.$model;
      const password = this.$v.form.password.$model;

      // add apollo
      this.$apollo
        .mutate({
          mutation: LOGIN_USER,
          variables: {
            phoneNumber: phonenumber,
            // email: email,
            password: password
          }
        })
        .then(data => {
          let LoginData = data.data.tokenAuth;
          if (LoginData.success == true) {
            this.ErrorMsgflag = false;
            let encryptedRefreshToken = this.encryption(
              LoginData.refreshToken,
              "key"
            );

            JwtService.destroyToken();
            JwtService.saveToken(encryptedRefreshToken);
            let user = LoginData.user;

            user.token = LoginData.token;
            this.$store.dispatch("LOGIN", user);
            this.$store.dispatch("RenewAccessToken", LoginData.token);
          } else if (LoginData.success == false) {
            this.$store.dispatch(
              "SET_ERROR",
              LoginData.errors.nonFieldErrors[0]
            );
            let user = { phoneNumber: this.form.phonenumber };
            this.$store.dispatch("SET_USER", user);
            // console.log(LoginData.errors.nonFieldErrors[0]);
            this.checkError();
          }
        })

        .catch(error => {
          console.error(error);
        });

      // clear existing errors

      this.buttonLoading = true;
      //* dummy delay
      setTimeout(() => {
        // send login request
        // this.$store
        //   .dispatch(LOGIN, { email, password })
        // go to which page after successfully login
        // .then(() => this.$router.push({ name: "dashboard" }));
        if (this.$store.getters.isAuthenticated)
          this.$router.push({ path: this.NextRoutePath });

        // this.$router.push({ name: "Dashboard" });
        // if (this.verified == false) this.$router.push({ name: "verify" });
        this.buttonLoading = false;
      }, 2000);
    }
  },
  computed: {
    // height() {
    //   console.log(document.getElementById("loginFormID"));
    //   return document.getElementById("loginFormID").clientHeight * 0.98;
    // },
    // ...mapState({
    //   errors: state => state.auth.errors
    // })
    // width() {
    //   return document.getElementsByClassName("login-form-page").width / 2;
    // },
    ...mapGetters(["errors"])
  }

  // mounted() {
  //   this.$router.beforeEnter((to, from, next) => {
  //     // next(vm => {
  //     //   vm.prevRoute = from;
  //     // });
  //     console.log(to, from, next);
  //   });
  // }
};
</script>
<style scoped>
#LoginRefreshIcon {
  color: rgb(77, 68, 68);
  caret-color: rgb(77, 68, 68);
}
#LoginRefreshIcon:hover {
  cursor: pointer;
  color: black;
}
.WrongCredMsg {
  color: red;
}
.submit-button {
  color: antiquewhite;
  font-size: 1em;
  font-weight: 600;
}
.submit-button:hover {
  color: rgb(29, 7, 7);
}
.input-form {
  background-color: rgba(82, 70, 70, 0.281) !important;
  color: white;
}
.chip-top {
  background-color: rgba(0, 0, 0, 0.212) !important;
  color: white;
}
.form-control {
  background-color: rgba(82, 70, 70, 0.281) !important;
  color: white;
  border-radius: 0.75rem;
}
input:-internal-autofill-selected {
  color: white !important;
  background-color: rgba(82, 70, 70, 0.281) !important;
  background-image: none;
}
input:-webkit-autofill {
  color: white !important;
  background-color: rgba(82, 70, 70, 0.281) !important;
  -webkit-background-clip: text;
  -webkit-box-shadow: 0 0 0 30px rgba(82, 70, 70, 0.281) inset !important;
}

/*Change text in autofill textbox*/
input:-webkit-autofill {
  -webkit-text-fill-color: rgb(252, 252, 252) !important;
}
/* Change the white to any color */
/* input:-webkit-autofill,
input:-webkit-autofill:hover, 
input:-webkit-autofill:focus, 
input:-webkit-autofill:active
{
 -webkit-box-shadow: 0 0 0 30px rgba(82, 70, 70, 0.281) inset !important;
} */

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  background-color: rgba(82, 70, 70, 0.281) !important;
}

.input-form .form-control .is-valid {
  background-color: rgba(82, 70, 70, 0.281) !important;
  color: white;
}
.cardColor {
  background-color: rgba(209, 209, 209, 0.938) !important;
  border-color: black !important;
  max-height: 100vh;
  min-width: 312px;
}

/* placeholder css */
.form-control::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: rgb(233, 233, 233);
  opacity: 1; /* Firefox */
  /* font-size: 0.9em; */
}
.form-control:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: rgb(214, 197, 197);
  /* font-size: 0.9em; */
}
.form-control::-ms-input-placeholder {
  /* Microsoft Edge */
  /* font-size: 0.9em; */
  color: rgb(214, 197, 197);
}
/* placeholder css end */
</style>
