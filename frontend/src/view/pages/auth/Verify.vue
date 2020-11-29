<template>
  <div>
    <div
      class="position-absolute top-0 left-0 text-right mt-5 mb-15 mb-lg-0 flex-column-auto justify-content-center py-5 px-10"
    >
      <span class="font-weight-bold font-size-3 text-dark-60">
        عدد ارسال شده به ایمیل را اینجا وارد کنید
      </span>
    </div>
    <div class="login-form login-signin">
      <b-form class="form" @submit.stop.prevent="onSubmit">
        <b-form-group id="input-group-0" label="" label-for="input-0">
          <b-form-input
            class="form-control form-control-solid h-auto py-3 px-5"
            id="input-0"
            name="input-0"
            v-model="$v.form.number.$model"
            :state="validateState('number')"
            aria-describedby="live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="live-feedback">
            کیبورد خود را به انگلیسی تغییر دهید
          </b-form-invalid-feedback>
          <!-- <p class="errorMsg" v-if="ErrorMsgText.phoneNumber.username">
            {{ ErrorMsgText.username }}
          </p> -->
        </b-form-group>
        <div
          class="form-group d-flex flex-wrap justify-content-between align-items-center"
        >
          <p class="errorMsg" v-if="ErrorMsgflag">
            {{ ErrorMsgText }}
          </p>
        </div>
        <div
          class="form-group d-flex flex-wrap justify-content-between align-items-center"
        >
          <p class="errorMsg" v-if="WrongCredFlag">
            {{ WrongCred }}
          </p>
        </div>
        <div class="form-group d-flex flex-wrap flex-center">
          <button
            type="submit"
            ref="kt_login_verify_submit"
            class="btn btn-primary font-weight-bold px-9 py-4 my-3 font-size-3 mx-4"
          >
            تایید
          </button>
        </div>
      </b-form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import {
  integer,
  required,
  minLength,
  maxLength
} from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import { VERIFY_USER } from "@/graphql/mutations";
import { mapState } from "vuex";
export default {
  mixins: [validationMixin],
  name: "verify",
  data() {
    return {
      WrongCred: "عدد وارد شده صحیح نیست",
      WrongCredFlag: false,
      ErrorMsgText: "خطایی رخ داده است",
      ErrorMsgflag: false,
      verificationNumber: "",
      form: {
        number: null
      }
    };
  },
  validations: {
    form: {
      number: {
        required,
        integer,
        minLength: minLength(5),
        maxLength: maxLength(6)
      }
    }
  },

  mounted() {
    console.log(this.$store.getters.currentUser.email);
    this.EmailpostRequest();
  },
  methods: {
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
      this.VerifypostRequest();
      const submitButton = this.$refs["kt_login_verify_submit"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // if (this.$store.getters.isAuthenticated)
        //   this.$router.push({ name: "dashboard" });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    VerifypostRequest() {
      axios({
        method: "post",
        url: "http://localhost:8000/user/verify",
        data: {
          request: "verification",
          // email: this.$store.getters.currentUser.email,
          email: this.$store.getters.currentUser.email,
          number: this.form.number
        },
        // data: 'hello world',
        xsrfHeaderName: "X-CSRFToken"
        // responseType: 'json'
      })
        .then(response => {
          console.log(response.data);
          if (response.data[0] == "GRANTED") {
            if (this.WrongCredFlag) this.WrongCredFlag = false;
            let token = response.data[1];
            //apollo
            this.$apollo
              .mutate({
                mutation: VERIFY_USER,
                variables: {
                  token: token
                }
              })
              .then(data => {
                console.log(data);
                let response = data.data.verifyAccount;
                if (response.success) {
                  this.$router.push({ name: "login" });
                } else {
                  this.ErrorMsgflag = true;
                }
              })
              .catch(error => {
                this.ErrorMsgflag = true;
                console.log(error);
              });
            //
          } else if (response.data[0] == "DENIED") {
            this.WrongCredFlag = true;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    EmailpostRequest() {
      axios({
        method: "post",
        url: "http://localhost:8000/user/verify",
        data: {
          request: "activation",
          email: this.$store.getters.currentUser.email
          // email: "mahdi.moradi72@gmail.com"
        },
        // data: 'hello world',
        xsrfHeaderName: "X-CSRFToken"
        // responseType: 'json'
      })
        .then(response => {
          console.log(response.data);

          if (response.data == null || response.data == "error") {
            this.ErrorMsgflag = true;
          } else if (response.data == "OK") {
            return;
          }
        })
        .catch(error => {
          console.log(error);
          this.ErrorMsgflag = true;
        });
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser
    })
    // ...mapGetters("currentUser")
  }
};
</script>
<style scoped>
.errorMsg {
  color: red;
}
</style>
