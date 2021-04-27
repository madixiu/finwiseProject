<template>
  <div>
    <v-card class="cardColor">
      <v-container>
        <div class="text-center">
          <v-chip class="chip-top">
            <span style="color:white" class="pr-2 pl-2">بازیابی رمز عبور</span>
          </v-chip>
        </div>
        <v-divider></v-divider>
        <!--begin::Form-->

        <b-form class="form" autocomplete="off" @submit.stop.prevent="onSubmit">
          <!-- <div v-if="!verified"> -->
          <!-- Email -->
          <b-form-group
            v-if="!verified"
            id="passReset-input-group-1"
            label=""
            label-for="passReset-input-1"
          >
            <b-form-input
              class="input-form"
              id="passReset-input-1"
              name="passReset-input-1"
              :disabled="numberField"
              placeholder="ایمیل"
              v-model="$v.form.email.$model"
              :state="validateState('email')"
              aria-describedby="email-live-feedback"
            ></b-form-input>

            <b-form-invalid-feedback id="email-live-feedback">
              ایمیل خود را وارد کنید
            </b-form-invalid-feedback>
          </b-form-group>

          <!-- verification number -->
          <b-form-group
            v-if="numberField && !verified"
            id="passReset-input-group-2"
            label=""
            label-for="passReset-input-2"
          >
            <b-form-input
              class="input-form"
              id="passReset-input-2"
              name="passReset-input-2"
              placeholder="کد تایید"
              v-model="$v.form.number.$model"
              :state="validateState('number')"
              aria-describedby="number-live-feedback"
            ></b-form-input>

            <b-form-invalid-feedback id="number-live-feedback">
              کد ۶ رقمی
            </b-form-invalid-feedback>
            <p class="errorMsg" v-if="WrongCredFlag">
              {{ ErrorMsgText.verificationNumber }}
            </p>
          </b-form-group>
          <!-- </div> -->

          <!-- <div v-if="verified"> -->
          <!-- New Password -->
          <b-form-group
            v-if="verified"
            id="passReset-input-group-2"
            label=""
            label-for="passReset-input-2"
          >
            <b-form-input
              class="input-form"
              id="passReset-input-3"
              name="passReset-input-3"
              placeholder="رمز عبور جدید"
              v-model="$v.form.newPassword.$model"
              :state="validateState('newPassword')"
              aria-describedby="newPass-live-feedback"
            ></b-form-input>

            <b-form-invalid-feedback id="newPass-live-feedback">
              رمز عبور خود جدید را وارد کنید (حداقل ۸ کاراکتر)
            </b-form-invalid-feedback>
            <p class="errorMsg" v-if="ErrorMsgText.password2.length">
              {{ ErrorMsgText.password2[0] }}
            </p>
          </b-form-group>
          <!-- New Password Repeat -->
          <b-form-group
            v-if="verified"
            id="passReset-input-group-2"
            label=""
            label-for="passReset-input-2"
          >
            <b-form-input
              class="input-form"
              id="passReset-input-4"
              name="passReset-input-4"
              placeholder="تکرار رمز عبور جدید"
              v-model="$v.form.newPassword2.$model"
              :state="validateState('newPassword2')"
              aria-describedby="newPassRepeat-live-feedback"
            ></b-form-input>

            <b-form-invalid-feedback id="newPassRepeat-live-feedback">
              تکرار رمز عبور خود جدید را وارد کنید (حداقل ۸ کاراکتر)
            </b-form-invalid-feedback>
          </b-form-group>
          <!-- </div> -->

          <div
            v-if="ErrorMsgflag"
            class="form-group d-flex flex-wrap justify-content-between align-items-center"
          >
            <p class="errorMsg">
              {{ ErrorMsgText }}
            </p>
          </div>
          <!-- <div
            v-if="WrongCredFlag"
            class="form-group d-flex flex-wrap justify-content-between align-items-center"
          >
            <p class="errorMsg">
              {{ WrongCred }}
            </p>
          </div> -->
          <div class="d-flex flex-wrap flex-center counterResetButton">
            <v-btn
              color="#4CAF50"
              class="submit-button mr-2"
              :loading="buttonLoading"
              @click="onSubmit"
              ><span class="submitButtonText">تایید</span></v-btn
            >
            <v-spacer></v-spacer>
            <div v-if="numberField && !verified">
              <v-btn
                v-if="counter != 0"
                x-small
                disabled
                color="#fff"
                min-width="77"
                max-width="77"
              >
                <!-- <div style="display:flex" class="counterResetButtonDiv"> -->
                <span class="counterResetButton">{{ counterText }}</span>
                <!-- </div> -->
              </v-btn>

              <v-btn
                v-else
                x-small
                color="#ff0000"
                min-width="77"
                @click="EmailpostRequest"
                ><span class="ResetButton">ارسال دوباره</span></v-btn
              >
            </div>
          </div>
        </b-form>
      </v-container>
    </v-card>
  </div>
</template>
<script>
import {
  email,
  integer,
  required,
  minLength,
  maxLength
} from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import { PASS_RESET } from "@/graphql/mutations";
// import { mapState } from "vuex";
// import axios from "axios";
export default {
  mixins: [validationMixin],
  name: "passwordReset",
  data() {
    return {
      verified: false,
      token: null,
      counter: 60,
      numberField: false,
      buttonLoading: false,
      ErrorMsgflag: false,
      WrongCred: "عدد وارد شده صحیح نیست",
      WrongCredFlag: false,
      // ErrorMsgText: "خطایی رخ داده است",
      ErrorMsgText: {
        common: "خطایی رخ داده است",
        verificationNumber: "عدد وارد شده صحیح نیست",
        email: "از صحیح بودن ایمیل خود اطمینان حاصل کنید",
        password2: []
      },
      verificationNumber: "",
      form: {
        email: "",
        number: "567456",
        newPassword: "dumy123456",
        newPassword2: "dumy123456"
      }
    };
  },
  validations: {
    form: {
      email: {
        required,
        email
      },
      number: {
        required,
        integer,
        minLength: minLength(5),
        maxLength: maxLength(6)
      },
      newPassword: {
        required,
        minLength: minLength(8)
      },
      newPassword2: {
        required,
        minLength: minLength(8)
      }
    }
  },
  computed: {
    counterText() {
      if (this.counter < 60) {
        if (this.counter > 9) return "00:" + this.counter;
        else return "00:0" + this.counter;
      } else {
        let min = Math.floor(this.counter / 60);
        let sec = this.counter % 60;
        if (sec > 9) return min + ":" + sec;
        else return min + ":0" + sec;
      }
    }
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    checkError(errorsIn) {
      let listOfErrors = [];
      // console.log(this.$store.getters.errors);
      let errors = errorsIn;
      if (errors.newPassword2) {
        for (let x of errors.newPassword2) {
          if (x.code == "password_mismatch")
            listOfErrors.push("عدم انطباق رمز عبور");
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
            if (x.message == "The password is too similar to the username.")
              listOfErrors.push("رمز وارد شده مشابه نام کاربری است");
          }
          if (x.code == "password_entirely_numeric")
            listOfErrors.push("رمز وارد شده فقط متشکل از اعداد است");

          this.ErrorMsgText.password2 = listOfErrors;
          // console.log(listOfErrors);
        }
      }
    },
    ResetCounter() {
      this.counter = this.counter - 1;
      let interval = setInterval(() => {
        if (this.counter == 0) {
          clearInterval(interval);
          return;
        }
        this.counter = this.counter - 1;
      }, 1000);
    },
    SendVerificationNumber() {
      this.buttonLoading = true;

      setTimeout(() => {
        this.numberField = true;
        this.ResetCounter();
        this.buttonLoading = false;
      }, 2000);
    },
    onSubmit() {
      // let verified = this.verified;
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
      if (!this.verified) {
        if (!this.numberField) {
          const email = this.$v.form.email.$model;
          this.EmailpostRequest(email);
        } else {
          const inputNumber = this.$v.form.number.$model;
          const email = this.$v.form.email.$model;
          this.VerifypostRequest(email, inputNumber);
        }
      } else if (this.verified) {
        const newPass = this.$v.form.newPassword.$model;
        const newPass2 = this.$v.form.newPassword2.$model;

        this.ChangePassword(newPass, newPass2);
      }
      this.buttonLoading = true;
      // dummy delay
      setTimeout(() => {
        this.buttonLoading = false;
      }, 2000);
    },
    EmailpostRequest(email) {
      this.axios({
        method: "post",
        url: "/user/passwordReset",
        data: {
          request: "activation",
          email: email
        },
        headers: { "Content-Type": "application/json" },
        xsrfHeaderName: "X-CSRFToken"
        // responseType: 'json'
      })
        .then(response => {
          if (response.data == null || response.data == "error") {
            this.ErrorMsgflag = true;
          } else if (response.data == "OK") {
            this.form.number = null;

            this.numberField = true;
            if (this.counter == 0) {
              this.counter = 60;
            }
            this.ResetCounter();

            return;
          }
        })
        .catch(error => {
          console.error(error);
          this.ErrorMsgflag = true;
        });
    },
    VerifypostRequest(email, inputNumber) {
      // console.log(email, inputNumber);
      this.axios({
        method: "post",
        url: "/user/passwordReset",
        data: {
          request: "verification",
          email: email,
          number: inputNumber
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          if (response.data[0] == "GRANTED") {
            if (this.WrongCredFlag) this.WrongCredFlag = false;
            this.token = response.data[1];
            this.verified = true;
            this.form.newPassword = null;
            this.form.newPassword2 = null;
          } else if (response.data[0] == "DENIED") {
            this.WrongCredFlag = true;
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    ChangePassword(pass1, pass2) {
      this.$apollo
        .mutate({
          mutation: PASS_RESET,
          variables: {
            newPassword1: pass1,
            newPassword2: pass2,
            token: this.token
          }
        })
        .then(data => {
          let response = data.data.passwordReset;
          if (response.success) {
            this.$router.push({ name: "login" });
            // console.log("PASS CHANGED");
          } else {
            // this.ErrorMsgflag = true;
            // this.$store.dispatch("SET_ERROR", data.data.register.errors);
            this.checkError(data.data.passwordReset.errors);
          }
        })
        .catch(error => {
          // this.ErrorMsgflag = true;
          console.error(error);
        });
    }
  }
};
</script>
<style scoped>
.chip-top {
  background-color: rgba(0, 0, 0, 0.212) !important;
  color: white;
}
.errorMsg {
  color: red;
}
.cardColor {
  background-color: rgba(226, 194, 194, 0.61) !important;
  border-color: black !important;
  max-height: 100vh;
  min-width: 312px;
}
.submitButtonText {
  color: antiquewhite;
  font-size: 1.1em;
  font-weight: 600;
}
.submitButtonText:hover {
  color: rgb(29, 7, 7);
}
.input-form {
  background-color: rgba(82, 70, 70, 0.281) !important;
  color: white;
}
.form-control {
  background-color: rgba(82, 70, 70, 0.281) !important;
  color: white;
  border-radius: 0.75rem;
}
.counterResetButton {
  font-family: "Vazir-Light-FD" !important;
  font-size: 1.5em !important;
  color: white;
  /* display: flex; */
}
.ResetButton {
  color: white;
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
