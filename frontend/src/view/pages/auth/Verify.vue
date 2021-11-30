<template>
  <div>
    <v-card class="cardColor">
      <v-container>
        <div class="text-center">
          <v-chip class="chip-top">
            <span style="color:white" class="pr-2 pl-2">تایید ایمیل</span>
          </v-chip>
        </div>
        <div class="text-center mt-2">
          <span>عدد ارسال شده به ایمیل را اینجا وارد کنید</span>
        </div>
        <v-divider></v-divider>
        <b-form class="form" @submit.stop.prevent="onSubmit">
          <b-form-group id="input-group-0" label="" label-for="input-0">
            <b-form-input
              class="input-form"
              id="input-0"
              name="input-0"
              v-model="$v.form.number.$model"
              :state="validateState('number')"
              aria-describedby="live-feedback"
              placeholder="کد"
            ></b-form-input>

            <b-form-invalid-feedback id="live-feedback">
              کد ۶ رقمی
            </b-form-invalid-feedback>
            <!-- <p class="errorMsg" v-if="ErrorMsgText.phoneNumber.username">
            {{ ErrorMsgText.username }}
          </p> -->
          </b-form-group>
          <div
            v-if="ErrorMsgflag"
            class="form-group d-flex flex-wrap justify-content-between align-items-center"
          >
            <p class="errorMsg">
              {{ ErrorMsgText }}
            </p>
          </div>
          <div
            v-if="WrongCredFlag"
            class="form-group d-flex flex-wrap justify-content-between align-items-center"
          >
            <p class="errorMsg">
              {{ WrongCred }}
            </p>
          </div>
          <div class="d-flex flex-wrap flex-center counterResetButton">
            <v-btn
              color="#4CAF50"
              class="submit-button mr-2"
              :loading="buttonLoading"
              @click="onSubmit"
              ><span class="submitButtonText">تایید</span></v-btn
            >
            <v-spacer></v-spacer>
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
        </b-form>
      </v-container>
    </v-card>
    <!-- <div
      class="position-absolute top-0 left-0 text-right mt-5 mb-15 mb-lg-0 flex-column-auto justify-content-center py-5 px-10"
    >
      <span class="font-weight-bold font-size-3 text-dark-60">
        عدد ارسال شده به ایمیل را اینجا وارد کنید
      </span>
    </div> -->
    <div class="login-form login-signin"></div>
  </div>
</template>
<script>
import {
  integer,
  required,
  minLength,
  maxLength
} from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import { VERIFY_USER, REFRESH_ACCESS_TOKEN } from "@/graphql/mutations";
import { GET_USER } from "@/graphql/queries";
import { mapState } from "vuex";
import JwtService from "@/core/services/jwt.service";
export default {
  mixins: [validationMixin],
  name: "verify",
  data() {
    return {
      buttonLoading: false,
      counter: 60,
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
    // TEMORARY COMMENT
    this.EmailpostRequest();
    this.ResetCounter();
    // setInterval(() => {
    //   while (this.counter > 0) this.counter = this.counter - 1;
    // }, 1000);
  },
  methods: {
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
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
      this.VerifypostRequest();
      // const submitButton = this.$refs["kt_login_verify_submit"];
      // submitButton.classList.add("spinner", "spinner-light", "spinner-right");
      this.buttonLoading = true;
      // dummy delay
      setTimeout(() => {
        // if (this.$store.getters.isAuthenticated)
        //   this.$router.push({ name: "dashboard" });
        this.buttonLoading = false;
        // submitButton.classList.remove(
        //   "spinner",
        //   "spinner-light",
        //   "spinner-right"
        // );
      }, 2000);
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    VerifypostRequest() {
      this.axios({
        method: "post",
        url: "/user/verify",
        data: {
          request: "verification",
          email: this.$store.getters.currentUser.email,
          number: this.form.number
        },
        xsrfHeaderName: "X-CSRFToken"
        // responseType: 'json'
      })
        .then(response => {
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
                let response = data.data.verifyAccount;
                if (response.success) {
                  if (JwtService.getToken()) {
                    let refreshToken = this.CryptoJS.AES.decrypt(
                      JwtService.getToken(),
                      "key"
                    ).toString(this.CryptoJS.enc.Utf8);
                    this.getAccessTokenAndUser(refreshToken);
                  } else this.$router.push({ name: "login" });
                } else {
                  this.ErrorMsgflag = true;
                }
              })
              .catch(error => {
                this.ErrorMsgflag = true;
                console.error(error);
              });
            //
          } else if (response.data[0] == "DENIED") {
            this.WrongCredFlag = true;
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    EmailpostRequest() {
      if (this.counter == 0) {
        this.counter = 60;
        this.ResetCounter();
      }
      this.axios({
        method: "post",
        url: "/user/verify",
        data: {
          request: "activation",
          email: this.$store.getters.currentUser.email
          //// email: "mahdi.moradi72@gmail.com"
        },
        xsrfHeaderName: "X-CSRFToken"
        // responseType: 'json'
      })
        .then(response => {
          if (response.data == null || response.data == "error") {
            this.ErrorMsgflag = true;
          } else if (response.data == "OK") {
            return;
          }
        })
        .catch(error => {
          console.error(error);
          this.ErrorMsgflag = true;
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
          this.$router.push({ name: "Dashboard" });
        });
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.auth.currentUser
    }),
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
  }
};
</script>
<style scoped>
.errorMsg {
  color: red;
}
.chip-top {
  background-color: rgba(0, 0, 0, 0.212) !important;
  color: white;
}
.cardColor {
  background-color: rgba(226, 194, 194, 0.61) !important;
  border-color: black !important;
  max-height: 100vh;
  min-width: 312px;
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
.submit-button {
  color: antiquewhite;
  /* font-size: 1em; */
  font-weight: 600;
}
.submitButtonText {
  color: antiquewhite;
  font-size: 1.1em;
  font-weight: 600;
}
.submitButtonText:hover {
  color: rgb(29, 7, 7);
}
.ResetButton {
  font-size: 1.3em;
  color: antiquewhite;
}
.counterResetButton {
  font-family: "Vazir-Light-FD" !important;
  font-size: 1.5em !important;
  color: white;
  /* display: flex; */
}
/* .counterResetButtonDiv {
  text-align: center;
  position: relative;
  display: block; 
  float: left; 
  overflow: hidden;
  margin-right: 2px;
} */
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

input:-internal-autofill-selected {
  color: white !important;
  background-color: rgba(82, 70, 70, 0.281) !important;
  /* background-image: none; */
}
input:-webkit-autofill {
  color: white !important;
  background-color: rgba(82, 70, 70, 0.281) !important;
  -webkit-background-clip: text;
  -webkit-box-shadow: 0 0 0 30px rgba(82, 70, 70, 0.281) inset !important;
}
</style>
