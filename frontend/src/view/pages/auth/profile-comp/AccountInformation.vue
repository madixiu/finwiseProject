<template>
  <!--begin::Card-->
  <b-card>
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <b-card-title>اطلاعات حساب کاربری</b-card-title>
        <b-card-sub-title>تغییرات اطلاعات کاربری </b-card-sub-title>
      </div>
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
      <div class="card-body">
        <!--begin::Heading-->
        <div class="row">
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mb-6 text-right">حساب کاربری:</h5>
          </div>
        </div>
        <!--begin::Form Group-->
        <div class="form-group row">
          <label class="col-xl-1 col-lg-1 col-form-label profile-labels"
            >نام کاربری</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="spinner spinner-sm spinner-success spinner-right">
              <input
                class="form-control form-control-lg form-control-solid"
                type="text"
                ref="username"
                :value="currentUserAccountInfo.username"
              />
            </div>
          </div>
        </div>
        <!--begin::Form Group-->
        <div class="form-group row">
          <label
            class="col-xl-1 col-lg-1 col-form-label profile-labels"
            style="text-align:right"
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
                type="text"
                class="form-control form-control-lg form-control-solid"
                ref="email"
                :value="currentUserAccountInfo.email"
                placeholder="Email"
              />
            </div>
          </div>
        </div>

        <!--begin::Form Group-->
        <div class="separator separator-dashed my-5"></div>
        <!--begin::Form Group-->
        <!-- <div class="row">
          <label class="col-xl-3"></label>
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mb-6">Security:</h5>
          </div>
        </div> -->
        <!--begin::Form Group-->
        <!-- <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label"
            >Login verification</label
          >
          <div class="col-lg-9 col-xl-6">
            <button
              type="button"
              class="btn btn-light-primary font-weight-bold btn-sm"
            >
              Setup login verification
            </button>
            <p class="form-text text-muted pt-2">
              After you log in, you will be asked for additional information to
              confirm your identity and protect your account from being
              compromised. <a href="#" class="font-weight-bold">Learn more</a>.
            </p>
          </div>
        </div> -->
      </div>
    </form>
    <!--end::Form-->
  </b-card>

  <!--end::Card-->
</template>

<script>
import { mapGetters } from "vuex";
import { UPDATE_ACCOUNT_INFO } from "@/core/services/store/profile.module";

export default {
  name: "AccountInformation",
  data() {
    return {};
  },
  methods: {
    save() {
      var username = this.$refs.username.value;
      var email = this.$refs.email.value;
      var language = this.$refs.language.value;
      var time_zone = this.$refs.time_zone.value;
      var communication = {
        email: this.$refs.email_com.checked,
        sms: this.$refs.sms_com.checked,
        phone: this.$refs.phone_com.checked
      };
      var verification = this.$refs.verification.checked;

      // set spinner to submit button
      const submitButton = this.$refs["kt_save_changes"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send update request
        this.$store.dispatch(UPDATE_ACCOUNT_INFO, {
          username,
          email,
          language,
          time_zone,
          communication,
          verification
        });

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    },
    cancel() {
      this.$refs.username.value = this.currentUserAccountInfo.username;
      this.$refs.email.value = this.currentUserAccountInfo.email;
      this.$refs.language.value = this.currentUserAccountInfo.language;
      this.$refs.time_zone.value = this.currentUserAccountInfo.time_zone;
      this.$refs.email_com.checked = this.currentUserAccountInfo.communication.email;
      this.$refs.sms_com.checked = this.currentUserAccountInfo.communication.sms;
      this.$refs.phone_com.checked = this.currentUserAccountInfo.communication.phone;
      this.$refs.verification.checked = this.currentUserAccountInfo.verification;
    }
  },
  computed: {
    ...mapGetters(["currentUserAccountInfo"])
  }
};
</script>

<style scoped>
.profile-labels {
  text-align: right;
  margin-top: auto;
  margin-bottom: auto;
}
</style>
