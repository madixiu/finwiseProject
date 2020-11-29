<template>
  <div>
    <!--begin::Content header-->
    <div
      class="position-absolute top-0 left-0 text-right mt-5 mb-15 mb-lg-0 flex-column-auto justify-content-center py-5 px-10"
    >
      <span class="font-weight-bold font-size-3 text-dark-60">
        قبلا ثبت نام کرده اید؟
      </span>
      <router-link
        class="font-weight-bold font-size-3 ml-2"
        :to="{ name: 'login' }"
      >
        ورود از اینجا
      </router-link>
    </div>
    <!--end::Content header-->

    <!--begin::Signup-->
    <div class="login-form login-signin">
      <div class="text-center mb-10 mb-lg-20">
        <h3 class="font-size-h1">ثبت نام</h3>
        <p class="text-muted font-weight-semi-bold">
          مشخصات خود را وارد کنید
        </p>
      </div>

      <!--begin::Form-->
      <!-- username -->
      <b-form class="form" @submit.stop.prevent="onSubmit">
        <b-form-group
          id="example-input-group-0"
          label=""
          label-for="example-input-0"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-0"
            name="example-input-0"
            v-model="$v.form.username.$model"
            :state="validateState('username')"
            aria-describedby="input-0-live-feedback"
            placeholder="نام کاربری"
          ></b-form-input>

          <b-form-invalid-feedback id="input-0-live-feedback">
            نام کاربری نیاز است
          </b-form-invalid-feedback>
          <p class="errorMsg" v-if="ErrorMsgText.phoneNumber.username">
            {{ ErrorMsgText.username }}
          </p>
        </b-form-group>

        <!-- email -->
        <b-form-group
          id="example-input-group-1"
          label=""
          label-for="example-input-1"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-1"
            name="example-input-1"
            v-model="$v.form.email.$model"
            :state="validateState('email')"
            aria-describedby="input-1-live-feedback"
            placeholder="آدرس ایمیل"
          ></b-form-input>

          <b-form-invalid-feedback id="input-1-live-feedback">
            ایمیل باید وارد شود
          </b-form-invalid-feedback>
          <p class="errorMsg" v-if="ErrorMsgText.email.length">
            {{ ErrorMsgText.email }}
          </p>
        </b-form-group>

        <!-- phoneNumber -->
        <b-form-group
          id="example-input-group-2"
          label=""
          label-for="example-input-2"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-2"
            name="example-input-2"
            v-model="$v.form.phonenumber.$model"
            :state="validateState('phonenumber')"
            aria-describedby="input-2-live-feedback"
            placeholder="شماره موبایل"
          ></b-form-input>
          <b-form-invalid-feedback id="input-2-live-feedback">
            شماره موبایل خود را وارد کنید
          </b-form-invalid-feedback>
          <p class="errorMsg" v-if="ErrorMsgText.phoneNumber.length">
            {{ ErrorMsgText.phoneNumber }}
          </p>
        </b-form-group>

        <!-- password -->
        <b-form-group
          id="example-input-group-3"
          label=""
          label-for="example-input-3"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            type="password"
            id="example-input-3"
            name="example-input-3"
            v-model="$v.form.password.$model"
            :state="validateState('password')"
            aria-describedby="input-3-live-feedback"
            autocomplete="on"
            placeholder="رمز عبور"
          ></b-form-input>
          <b-form-invalid-feedback id="input-3-live-feedback">
            رمز عبور خود را وارد کنید (حداقل ۸ کاراکتر)
          </b-form-invalid-feedback>
          <p class="errorMsg" v-if="ErrorMsgText.password2.length">
            {{ ErrorMsgText.password2[0] }}
          </p>
        </b-form-group>

        <!-- firstname -->
        <b-form-group
          id="example-input-group-4"
          label=""
          label-for="example-input-4"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-4"
            name="example-input-4"
            v-model="$v.form.firstname.$model"
            :state="validateState('firstname')"
            aria-describedby="input-4-live-feedback"
            placeholder="نام"
          ></b-form-input>

          <b-form-invalid-feedback id="input-4-live-feedback">
            نام خود را وارد کنید
          </b-form-invalid-feedback>
        </b-form-group>

        <!-- lastname -->
        <b-form-group
          id="example-input-group-5"
          label=""
          label-for="example-input-5"
        >
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-3"
            id="example-input-5"
            name="example-input-5"
            v-model="$v.form.lastname.$model"
            :state="validateState('lastname')"
            aria-describedby="input-5-live-feedback"
            placeholder="نام خانوادگی"
          ></b-form-input>

          <b-form-invalid-feedback id="input-5-live-feedback">
            نام خانوادگی خود را وارد کنید
          </b-form-invalid-feedback>
        </b-form-group>

        <!--begin::Action-->
        <div
          class="form-group d-flex flex-wrap justify-content-between align-items-center"
        >
          <p class="ErrorMsg" v-if="ErrorMsgflag">
            {{ ErrorMsgText }}
          </p>
        </div>
        <div class="form-group d-flex flex-wrap flex-center">
          <button
            type="submit"
            ref="kt_login_signup_submit"
            class="btn btn-primary font-weight-bold px-9 py-4 my-3 font-size-3 mx-4"
          >
            تکمیل ثبت نام
          </button>
          <button
            v-on:click="$router.push('login')"
            class="btn btn-light-primary font-weight-bold px-9 py-4 my-3 font-size-3 mx-4"
          >
            انصراف
          </button>
        </div>
        <!--end::Action-->
      </b-form>
      <!--end::Form-->
    </div>
    <!--end::Signup-->
  </div>
</template>

<style lang="scss" scoped>
.spinner.spinner-right {
  padding-right: 3.5rem !important;
}
</style>

<script>
import { mapState } from "vuex";
// import { REGISTER } from "@/core/services/store/auth.module";
// import { SET_ERROR, SET_AUTH } from "@/core/services/store/auth.module";
import { REGISTER_USER } from "@/graphql/mutations";

import { validationMixin } from "vuelidate";
import {
  email,
  required,
  minLength,
  maxLength,
  integer
} from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  name: "register",
  data() {
    return {
      ErrorMsgText: { phoneNumber: "", email: "", username: "", password2: [] },
      ErrorMsgflag: false,
      form: {
        username: "test",
        email: "admin@demo.com",
        password: "demo",
        firstname: "yest",
        lastname: "yest",
        phonenumber: "09166616666"
      }
    };
  },
  validations: {
    form: {
      username: {
        required,
        minLength: minLength(3)
      },
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(8)
      },
      firstname: {
        required,
        minLength: minLength(3)
      },
      lastname: {
        required,
        minLength: minLength(3)
      },
      phonenumber: {
        integer,
        required,
        minLength: minLength(11),
        maxLength: maxLength(11)
      }
    }
  },
  methods: {
    checkError() {
      let listOfErrors = [];
      console.log(this.$store.getters.errors);
      let errors = this.$store.getters.errors;
      if (errors.password2) {
        for (let x of errors.password2) {
          if (x.code == "password_too_short")
            listOfErrors.push("رمز وارد شده کوتاه است");
          if (x.code == "password_too_common")
            listOfErrors.push("رمز وارد شده ضعیف است");
          if (x.code == "password_too_similar") {
            if (x.message == "The password is too similar to the first name.")
              listOfErrors.push("رمز وارد شده مشابه نام است");
            if (x.message == "The password is too similar to the last name.")
              listOfErrors.push("رمز وارد شده مشابه نام خانوادگی است");
            if (
              x.message == "The password is too similar to the email address."
            )
              listOfErrors.push("رمز وارد شده مشابه ایمیل است");
          }
          if (x.code == "password_entirely_numeric")
            listOfErrors.push("رمز وارد شده فقط متشکل از اعداد است");

          this.ErrorMsgText.password2 = listOfErrors;
          console.log(listOfErrors);
        }
      }
      if (errors.username) {
        this.ErrorMsgText.username = "نام کاربری قبلا ثبت شده است";
      }
      if (errors.email) {
        this.ErrorMsgText.email = "ایمیل قبلا ثبت شده است";
      }
      if (errors.phoneNumber) {
        this.ErrorMsgText.phoneNumber = "شماره تلفن قبلا ثبت شده است";
      }
      console.log(listOfErrors);
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        username: null,
        email: null,
        password: null,
        firstname: null,
        lastname: null,
        phoneNumber: null
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }

      // // clear existing errors
      // this.$store.dispatch("LOGOUT");

      const username = this.$v.form.username.$model;
      const email = this.$v.form.email.$model;
      const password = this.$v.form.password.$model;
      const firstname = this.$v.form.firstname.$model;
      const lastname = this.$v.form.lastname.$model;
      const phonenumber = this.$v.form.phonenumber.$model;

      this.$apollo
        .mutate({
          mutation: REGISTER_USER,
          variables: {
            email: email,
            password1: password,
            password2: password,
            username: username,
            phoneNumber: phonenumber,
            firstName: firstname,
            lastName: lastname
          }
        })
        .then(data => {
          console.log(data);
          if (data.data.register.success == true) {
            // clear existing errors
            this.$store.dispatch("LOGOUT");
            // HAVE TO write code for saving encrypted refresh token to storage
            // LATER
            this.$store.dispatch("REGISTER", data.data.register.user);
          } else if (data.data.register.success == false) {
            // console.log(data.data.register.errors.password2);
            this.$store.dispatch("SET_ERROR", data.data.register.errors);
            this.checkError();
          }
          // this.$store.dispatch("SET_AUTH", data);
        })

        .catch(error => {
          console.log(error);
          // console.log(phonenumber + " " + username);
          // this.$store.dispatch("SET_ERROR", error.data.errors);
        });
      // set spinner to submit button
      const submitButton = this.$refs["kt_login_signup_submit"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send register request
        // this.$store
        //   .dispatch(REGISTER, {
        //     email: email,
        //     password: password,
        //     username: username,
        //     firstname: firstname,
        //     lastname: lastname,
        //     phoneNumber: phonenumber
        //   })
        //   .then(() => this.$router.push({ name: "dashboard" }));
        // if (this.$store.getters.isAuthenticated)
        this.$router.push({ name: "verify" });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    }
  },
  computed: {
    ...mapState({
      errors: state => state.auth.errors
    })
  }
};
</script>
<style scoped>
.errorMsg {
  color: red;
}
</style>
