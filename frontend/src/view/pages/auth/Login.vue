<template>
  <div>
    <!--begin::Content header-->
    <!-- 
    <div class="container">
      <v-container>
        <v-row>

        </v-row>
      </v-container>
    </div> -->
    <v-card class="cardColor">
      <v-container>
        <!-- <v-divider></v-divider> -->
        <!-- <div class=" justify-content-center position-absolute top-0 right-0">
    
          <router-link
            class="font-weight-bold font-size-3 ml-2"
            :to="{ name: 'register' }"
          >
            ثبت نام
          </router-link>
        </div> -->
        <!--end::Content header-->

        <!--begin::Signin-->
        <!-- MAY REMOVE THIS DIV (REDUNDANT) -->
        <div class="">
          <div class="text-center">
            <v-chip class="chip-top">
              <span style="color:white" class="pr-2 pl-2">ورود</span>
            </v-chip>
          </div>
          <v-divider></v-divider>

          <!--begin::Form-->

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
            <div
              class="form-group d-flex flex-wrap justify-content-center align-items-center"
            >
              <v-btn
                block
                color="#4CAF50"
                class="submit-button"
                :loading="buttonLoading"
                @click="onSubmit"
                >ورود</v-btn
              >
              <!-- <button
                ref="kt_login_signin_submit"
                class="btn btn-primary font-weight-bold px-9 py-4 my-3 font-size-3"
              >
                ورود
              </button> -->
              <router-link
                class="text-dark-60 text-hover-primary mt-2"
                id="kt_login_forgot"
                :to="{ name: 'passwordReset' }"
              >
                فراموشی رمز عبور
              </router-link>
            </div>
            <v-divider></v-divider>
            <div class=" justify-content-center ">
              <!-- <span class="font-weight-bold font-size-3 text-dark-60">
            ثبت نام نکرده اید؟
          </span> -->
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
  mixins: [validationMixin],
  name: "login",
  // eslint-disable-next-line no-unused-vars
  beforeRouteEnter: (to, from, next) => {
    next(vm => {
      vm.NextRoutePath = from.path;
    });
    // next();
  },
  data() {
    return {
      NextRoutePath: "",
      buttonLoading: false,
      verified: true,
      ErrorMsgflag: false,
      ErrorMsgText: "",
      ErrorMsg: [
        "خطایی رخ داده است",
        "مشخصات وارد شده صحیح نمی باشد",
        "اکانت شما تایید نشده است"
      ],
      form: {
        // email: "",
        phonenumber: "",
        password: ""
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
  methods: {
    LockCheck() {
      // console.log(this.$store.getters.currentUser.role);
      let user = this.$store.getters.currentUser;
      // console.log(user.role);

      if (user.role == 2) this.$store.dispatch("setOptionStatus", false);
    },
    checkError() {
      let errors = this.$store.getters.errors;
      // console.log(errors);
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
      if (this.$v.form.$anyError) {
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

            // this.LockCheck();

            // if (user.verified == true) {
            //   console.log("verified");
            //   this.$store.dispatch("LOGIN", user);
            // }
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

          // console.log(LoginData);

          // JwtService.destroyToken();
          // JwtService.saveToken(LoginData.token)
          // this.$store.dispatch(SET_AUTH, data);
        })

        .catch(error => {
          console.error(error);
          // console.log(LOGIN_USER);
          // console.log(email + " " + password);
          // this.$store.dispatch(SET_ERROR, error.data.errors);
        });

      // clear existing errors
      // this.$store.dispatch(LOGOUT);

      // set spinner to submit button
      // const submitButton = this.$refs["kt_login_signin_submit"];
      // submitButton.classList.add("spinner", "spinner-light", "spinner-right");
      this.buttonLoading = true;
      // dummy delay
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
  background-color: rgba(226, 194, 194, 0.61) !important;
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
