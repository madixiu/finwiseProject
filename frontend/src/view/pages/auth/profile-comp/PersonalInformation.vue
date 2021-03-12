<template>
  <!--begin::Card-->
  <b-card>
    <!--begin::Header-->

    <div class="card-header py-3">
      <b-card-title style="text-align:right">
        اطلاعات شخصی
      </b-card-title>
      <b-card-sub-title style="text-align:right">
        ویرایش اطلاعات شخصی
      </b-card-sub-title>
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
      <!--begin::Body-->
      <b-card-body>
        <div class="form-group row">
          <span class="col-xl-1 col-lg-1 profile-labels">نام</span>
          <div class="col-lg-3 col-xl-4">
            <input
              ref="firstName"
              class="form-control form-control-lg form-control-solid "
              type="text"
              v-bind:value="currentUser.firstName"
            />
          </div>
        </div>
        <div class="form-group row">
          <span class="col-xl-1 col-lg-1 col-form-label profile-labels"
            >نام خانوادگی</span
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="lastName"
              class="form-control form-control-lg form-control-solid"
              type="text"
              v-bind:value="currentUser.lastName"
            />
          </div>
        </div>
        <!-- <div class="form-group row">
          <span class="col-xl-1 col-lg-1 col-form-label profile-labels"
            >سن</span
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="age"
              class="form-control form-control-lg form-control-solid"
              type="text"
              v-bind:value="currentUser.age"
            />
       
          </div>
        </div> -->
        <div class="form-group row">
          <b-form inline>
            <label class="mr-3 ml-4 pl-3" for="inline-form-custom-select-pref"
              >سن</label
            >
            <b-form-select
              id="inline-form-custom-select-pref"
              class="mb-2 mr-4 mb-sm-0"
              :options="ages"
              v-model="currentUser.age"
            >
              <template #first>
                <b-form-select-option :value="null" disabled
                  >-- انتخاب کنید --</b-form-select-option
                >
              </template>
            </b-form-select>
          </b-form>
        </div>
        <div class="form-group row">
          <b-form inline>
            <label class="mr-sm-2" for="inline-form-custom-select-pref"
              >مقطع تحصیلی</label
            >
            <b-form-select
              id="inline-form-custom-select-pref"
              class="mb-2 mr-sm-2 mb-sm-0"
              v-model="currentUser.degree"
              :options="[
                'کارشناسی',
                'کارشناسی ارشد',
                'دکترا',
                'دیپلم',
                'زیر دیپلم'
              ]"
            >
              <template #first>
                <b-form-select-option :value="null" disabled
                  >-- انتخاب کنید --</b-form-select-option
                >
              </template>
            </b-form-select>
          </b-form>
        </div>
      </b-card-body>

      <!--end::Body-->
    </form>
    <!--end::Form-->
  </b-card>
</template>

<script>
import { mapGetters } from "vuex";
import {
  VERIFY_ACCESS_TOKEN,
  REFRESH_ACCESS_TOKEN,
  UPDATE_USER
} from "@/graphql/mutations";
import JwtService from "@/core/services/jwt.service";
export default {
  name: "PersonalInformation",
  data() {
    return {
      form: { age: "", degree: "" },
      ages: ["18", "19", "20", "21", "22"],
      Rtoken: "",
      Atocken: ""
    };
  },
  created() {
    for (let i = 23; i < 100; i++) {
      this.ages.push(i.toString());
    }
  },
  mounted() {},
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
            firstName: this.$refs.firstName.value,
            lastName: this.$refs.lastName.value,
            age: this.currentUser.age,
            degree: this.currentUser.degree,

            username: this.$store.getters.currentUser.username,
            email: this.$store.getters.currentUser.email,
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
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    save() {
      // var name = this.$refs.firstName.value;
      // var surname = this.$refs.lastName.value;
      // var age = this.$refs.age.value;
      // var ageNew = this.form.age;
      // // var email = this.$refs.email.value;
      // var degree = this.form.degree;
      // console.log(name, surname, age, ageNew, degree);
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

        // this.$store.dispatch(UPDATE_PERSONAL_INFO, {
        //   name,
        //   surname,
        //   company_name,
        //   phone,
        //   email,
        //   company_site,
        // });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    },
    cancel() {
      this.$refs.firstName.value = this.currentUser.firstName;
      this.$refs.lastName.value = this.currentUser.lastName;
      // this.$refs.company_name.value = this.currentUser.company_name;
      this.$refs.phoneNumber.value = this.currentUser.phoneNumber;
      this.$refs.email.value = this.currentUser.email;
      // this.$refs.company_site.value = this.currentUser.company_site;
    }
    // onFileChange(e) {
    //   const file = e.target.files[0];

    //   if (typeof FileReader === "function") {
    //     const reader = new FileReader();

    //     reader.onload = event => {
    //       this.current_photo = event.target.result;
    //     };

    //     reader.readAsDataURL(file);
    //   } else {
    //     alert("Sorry, FileReader API not supported");
    //   }
    // }
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
  margin-bottom: auto !important  ;
}
</style>
