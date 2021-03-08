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
        <!-- <div class="row"> -->
        <!-- <label class="col-xl-3"></label> -->
        <!-- <div class="col-lg-1 col-xl-6">
            <h5 class="font-weight-bold mb-6">Customer Info</h5>
          </div> -->
        <!-- </div> -->
        <div class="form-group row">
          <span class="col-xl-1 col-lg-1 profile-labels">نام</span>
          <div class="col-lg-3 col-xl-4">
            <input
              ref="name"
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
              ref="surname"
              class="form-control form-control-lg form-control-solid"
              type="text"
              v-bind:value="currentUser.lastName"
            />
          </div>
        </div>
        <div class="form-group row">
          <span class="col-xl-1 col-lg-1 col-form-label profile-labels"
            >نام شرکت</span
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="company_name"
              class="form-control form-control-lg form-control-solid"
              type="text"
              v-bind:value="currentUser.company_name"
            />
            <span class="form-text text-muted"
              >در صورتی که برای شخصیت حقوقی قصد ثبت نام دارید، با ما مستقیما
              تماس بگیرید</span
            >
          </div>
        </div>
        <div class="row">
          <label class="col-xl-3"></label>
          <div class="col-lg-12 col-xl-12">
            <h5 class="font-weight-bold mb-6 text-right">اطلاعات تماس</h5>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >تلفن همراه</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="la la-phone"></i>
                </span>
              </div>
              <input
                ref="phone"
                type="text"
                class="form-control form-control-lg form-control-solid"
                placeholder="Phone"
                v-bind:value="currentUser.phoneNumber"
              />
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
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
                ref="email"
                type="text"
                class="form-control form-control-lg form-control-solid"
                placeholder="Email"
                v-bind:value="currentUser.email"
              />
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >سایت</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <input
                ref="company_site"
                type="text"
                class="form-control form-control-lg form-control-solid"
                placeholder="Username"
                v-bind:value="currentUser.company_site"
              />
            </div>
          </div>
        </div>
      </b-card-body>

      <!--end::Body-->
    </form>
    <!--end::Form-->
  </b-card>
</template>

<script>
import { mapGetters } from "vuex";
import { VERIFY_ACCESS_TOKEN, REFRESH_ACCESS_TOKEN } from "@/graphql/mutations";
import JwtService from "@/core/services/jwt.service";

// import { UPDATE_PERSONAL_INFO } from "@/core/services/store/profile.module";

export default {
  name: "PersonalInformation",
  data() {
    return {
      // default_photo: "media/users/blank.png",
      // current_photo: null
    };
  },
  mounted() {
    // this.current_photo = this.currentUser.photo;
  },
  methods: {
    verifyAccessToken(AccessToken) {
      this.$apollo
        .mutate({
          mutation: VERIFY_ACCESS_TOKEN,
          variables: {
            token: AccessToken
          }
        })
        .then(data => {
          console.log(data);
          let LoginData = data.data.verifyToken;
          console.log(LoginData.success);
          if (LoginData.success) {
            // this.$router.push({ name: "Dashboard" });
            this.$store.dispatch("RenewAccessToken", LoginData.token);
          } else if (LoginData == false) {
            let Rtoken = this.CryptoJS.AES.decrypt(
              JwtService.getToken(),
              "key"
            ).toString(this.CryptoJS.enc.Utf8);
            this.refreshAccessToken(Rtoken);
          }
        })
        .catch(error => {
          console.log(error);
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
          console.log(data);
          let LoginData = data.data.refreshToken;
          console.log(LoginData);
          if (!data.data.errors) {
            console.log(LoginData.success);
            if (LoginData.success) {
              // store new acc token to vuex

              this.$store.dispatch("RenewAccessToken", LoginData.token);
              // this.getQueryUser(LoginData.payload.username);
              // this.$router.push({ name: "Dashboard" });
            } else {
              console.log(LoginData.errors.nonFieldErrors[0].message);
              this.$store.dispatch("LOGOUT");
              // this.$router.push({ name: "login" });
              // this.$router.push({ name: "verify" });
            }
          } else {
            console.log(LoginData.errors.nonFieldErrors[0].message);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    UpdateAccount() {
      // this.$apollo
      // .mutate({})
    },
    save() {
      // var name = this.$refs.firstName.value;
      // var surname = this.$refs.lastName.value;
      // var company_name = this.$refs.company_name.value;
      // var phone = this.$refs.phoneNumber.value;
      // var email = this.$refs.email.value;
      // var company_site = this.$refs.company_site.value;
      // var photo = this.photo;

      // set spinner to submit button
      const submitButton = this.$refs["kt_save_changes"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send update request

        // this.$store.dispatch(UPDATE_PERSONAL_INFO, {
        //   name,
        //   surname,
        //   company_name,
        //   phone,
        //   email,
        //   company_site,
        //   photo
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
      // this.current_photo = this.currentUser.photo;
    },
    onFileChange(e) {
      const file = e.target.files[0];

      if (typeof FileReader === "function") {
        const reader = new FileReader();

        reader.onload = event => {
          this.current_photo = event.target.result;
        };

        reader.readAsDataURL(file);
      } else {
        alert("Sorry, FileReader API not supported");
      }
    }
  },
  computed: {
    ...mapGetters(["currentUser"]),
    photo() {
      return this.current_photo == null
        ? this.default_photo
        : this.current_photo;
    }
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
