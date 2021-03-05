<template>
  <div>
    <!--begin::Content header-->
    <div
      class="position-absolute top-0 left-0 text-right mt-5 mb-15 mb-lg-0 flex-column-auto justify-content-center py-5 px-10"
    >
      <span class="font-weight-bold font-size-3 text-dark-60">
        ثبت نام نکرده اید؟
      </span>
      <router-link
        class="font-weight-bold font-size-3 ml-2"
        :to="{ name: 'register' }"
      >
        ثبت نام
      </router-link>
    </div>
    <!--end::Content header-->

    <!--begin::Signin-->
    <div class="login-form login-signin">
      <div class="text-center mb-10 mb-lg-20">
        <h3 class="font-size-h1">ورود</h3>
        <p class="text-muted font-weight-semi-bold"></p>
      </div>
      <!--begin::Form-->
      <b-form class="form" @submit.stop.prevent="onSubmit">
        <div role="alert" class="alert alert-info">
          <div class="alert-text">
            <strong>نام کاربری</strong> و <strong>رمز عبور</strong>خود را وارد
            کنید
          </div>
        </div>
        <div
          v-if="errors"
          role="alert"
          v-bind:class="{ show: errors.length }"
          class="alert fade alert-danger"
        >
          <div class="alert-text" v-for="(error, i) in errors" :key="i">
            {{ error }}
          </div>
        </div>
        <b-form-group
          id="example-input-group-1"
          label=""
          label-for="example-input-1"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-1"
            name="example-input-1"
            v-model="$v.form.phonenumber.$model"
            :state="validateState('phonenumber')"
            aria-describedby="input-1-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="input-1-live-feedback">
            شماره موبایل خود را وارد کنید
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group
          id="example-input-group-2"
          label=""
          label-for="example-input-2"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            type="password"
            id="example-input-2"
            name="example-input-2"
            v-model="$v.form.password.$model"
            :state="validateState('password')"
            aria-describedby="input-2-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="input-2-live-feedback">
            رمز عبور خود را صحیح وارد کنید
          </b-form-invalid-feedback>
        </b-form-group>
        <!--begin::Action-->
        <div
          class="form-group d-flex flex-wrap justify-content-between align-items-center"
        >
          <p class="WrongCredMsg" v-if="ErrorMsgflag">
            نام کاربری و رمز عبور صحیح نمی باشد
          </p>
        </div>
        <div
          class="form-group d-flex flex-wrap justify-content-between align-items-center"
        >
          <button
            ref="kt_login_signin_submit"
            class="btn btn-primary font-weight-bold px-9 py-4 my-3 font-size-3"
          >
            ورود
          </button>
          <a
            href="#"
            class="text-dark-60 text-hover-primary my-3 mr-2"
            id="kt_login_forgot"
          >
            رمز عبور را فراموش کرده اید؟
          </a>
        </div>
        <!--end::Action-->
        <!--end::Form-->
      </b-form>
    </div>
    <!--end::Signin-->
  </div>
</template>

<style lang="scss" scoped>
.spinner.spinner-right {
  padding-right: 3.5rem !important;
}
</style>

<script>
// import { mapState } from "vuex";
import { mapGetters } from "vuex";
// import gql from "graphql-tag";
// import { LOGIN, LOGOUT } from "@/core/services/store/auth2.module";
// import { LOGIN } from "@/core/services/store/auth";
import { validationMixin } from "vuelidate";
import {
  email,
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
  data() {
    return {
      verified: true,
      ErrorMsgflag: false,
      ErrorMsgText: "",
      ErrorMsg: [
        "خطایی رخ داده است",
        "مشخصات وارد شده صحیح نمی باشد",
        "اکانت شما تایید نشده است"
      ],
      // Remove this dummy login info
      form: {
        email: "",
        phonenumber: "",
        password: ""
      }
    };
  },
  validations: {
    form: {
      email: {
        required,
        email
      },
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
    checkError() {
      let errors = this.$store.getters.errors;
      console.log(errors);
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
        email: null,
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

      // const email = this.$v.form.email.$model;
      const phoneNumber = this.$v.form.phonenumber.$model;
      const password = this.$v.form.password.$model;

      // add apollo
      this.$apollo
        .mutate({
          mutation: LOGIN_USER,
          variables: {
            phoneNumber: phoneNumber,
            // email: email,
            password: password
          }
        })
        .then(data => {
          let LoginData = data.data.tokenAuth;
          if (LoginData.success == true) {
            this.ErrorMsgflag = false;
            console.log(LoginData.token);
            console.log(LoginData.refreshToken);
            let encryptedRefreshToken = this.encryption(
              LoginData.refreshToken,
              "key"
            );
            let decryptedRefreshToken = this.decryption(
              encryptedRefreshToken,
              "key"
            );
            console.log(encryptedRefreshToken);
            console.log(decryptedRefreshToken);
            JwtService.destroyToken();
            JwtService.saveToken(encryptedRefreshToken);
            console.log(JwtService.getToken());
            let user = LoginData.user;
            // user.token = this.encryption(
            //   LoginData.token,
            //   LoginData.refreshToken
            // );
            user.token = LoginData.token;
            console.log(user);
            this.$store.dispatch("LOGIN", user);
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
          console.log(error);
          // console.log(LOGIN_USER);
          // console.log(email + " " + password);
          // this.$store.dispatch(SET_ERROR, error.data.errors);
        });

      // clear existing errors
      // this.$store.dispatch(LOGOUT);

      // set spinner to submit button
      const submitButton = this.$refs["kt_login_signin_submit"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send login request
        // this.$store
        //   .dispatch(LOGIN, { email, password })
        // go to which page after successfully login
        // .then(() => this.$router.push({ name: "dashboard" }));
        if (this.$store.getters.isAuthenticated)
          this.$router.push({ name: "Dashboard" });
        if (this.verified == false) this.$router.push({ name: "verify" });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    }
  },
  computed: {
    // ...mapState({
    //   errors: state => state.auth.errors
    // })
    ...mapGetters(["errors"])
  }
};
</script>
<style scoped>
.WrongCredMsg {
  color: red;
}
</style>
