<template>
  <div class="d-flex flex-row">
    <!-- <div
      class="flex-row-auto offcanvas-mobile w-300px w-xl-350px"
      id="kt_profile_aside"
    >
      <b-card>
        <div
          class="navi navi-bold navi-hover navi-active navi-link-rounded"
          role="tablist"
        >
          <div class="navi-item mb-2">
            <a
              class="navi-link py-4"
              @click="setActiveTab"
              href="#"
              data-tab="0"
              data-toggle="tab"
              role="tab"
              aria-selected="false"
            >
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg src="media/svg/icons/General/User.svg" />
                </span>
              </span>
              <span class="navi-text font-size-lg">Personal Information</span>
            </a>
          </div>
          <div class="navi-item mb-2">
            <a
              class="navi-link py-4"
              @click="setActiveTab"
              href="#"
              data-tab="1"
              data-toggle="tab"
              role="tab"
              aria-selected="false"
            >
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg src="media/svg/icons/Code/Compiling.svg" />
                </span>
              </span>
              <span class="navi-text font-size-lg">Account Information</span>
            </a>
          </div>
          <div class="navi-item mb-2">
            <a
              class="navi-link py-4"
              @click="setActiveTab"
              href="#"
              data-tab="2"
              data-toggle="tab"
              role="tab"
              aria-selected="false"
            >
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg
                    src="media/svg/icons/Communication/Shield-user.svg"
                  />
                </span>
              </span>
              <span class="navi-text font-size-lg">Change Passwort</span>
              <span class="navi-label">
                <span
                  class="label label-light-danger label-rounded font-weight-bold"
                  >5</span
                >
              </span>
            </a>
          </div>
          <div class="navi-item mb-2">
            <a
              class="navi-link py-4"
              @click="setActiveTab"
              href="#"
              data-tab="3"
              data-toggle="tab"
              role="tab"
              aria-selected="false"
            >
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg
                    src="media/svg/icons/Communication/Mail-opened.svg"
                  />
                </span>
              </span>
              <span class="navi-text font-size-lg">Email settings</span>
            </a>
          </div>
        </div>
      </b-card>
    </div> -->

    <!--begin::Content-->
    <div class="flex-row-fluid ml-lg-1">
      <b-card no-body>
        <b-tabs pills card vertical v-model="tabIndex">
          <b-tab active>
            <template #title>
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg src="media/svg/icons/General/User.svg" />
                </span>
              </span>
              <span>اطلاعات شخصی</span>
            </template>
            <KTPersonalInformation></KTPersonalInformation>
          </b-tab>

          <b-tab>
            <template #title>
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg src="media/svg/icons/Code/Compiling.svg" />
                </span>
              </span>
              <span>اطلاعات حساب</span>
            </template>
            <KTAccountInformation></KTAccountInformation>
          </b-tab>

          <b-tab>
            <template #title>
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg
                    src="media/svg/icons/Communication/Shield-user.svg"
                  />
                </span>
              </span>
              <span>رمز عبور</span>
            </template>
            <KTChangePassword></KTChangePassword>
          </b-tab>

          <b-tab>
            <template #title>
              <span class="navi-icon mr-2">
                <span class="svg-icon">
                  <inline-svg
                    src="media/svg/icons/Communication/Mail-opened.svg"
                  />
                </span>
              </span>
              <span>تنظیمات ایمیل</span>
            </template>
            <KTEmailSettings></KTEmailSettings>
          </b-tab>
        </b-tabs>
      </b-card>
    </div>
    <!--end::Content-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { mapGetters } from "vuex";
// import KTDropdown2 from "@/view/pages/auth/profile-comp/Dropdown2";
// import KTProfileOverview from "@/view/pages/auth/profile-comp/ProfileOverview";
import KTPersonalInformation from "@/view/pages/auth/profile-comp/PersonalInformation";
import KTAccountInformation from "@/view/pages/auth/profile-comp/AccountInformation";
import KTChangePassword from "@/view/pages/auth/profile-comp/ChangePassword";
import KTEmailSettings from "@/view/pages/auth/profile-comp/EmailSettings";

export default {
  name: "custom-page",
  components: {
    // KTDropdown2,
    // KTProfileOverview,
    KTPersonalInformation,
    KTAccountInformation,
    KTChangePassword,
    KTEmailSettings
  },
  data() {
    return {
      tabIndex: 0
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Profile" }]);
  },
  methods: {
    /**
     * Set current active on click
     * @param event
     */
    setActiveTab(event) {
      let target = event.target;
      if (!event.target.classList.contains("navi-link")) {
        target = event.target.closest(".navi-link");
      }

      const tab = target.closest('[role="tablist"]');
      const links = tab.querySelectorAll(".navi-link");
      // remove active tab links
      for (let i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
      }

      // set clicked tab index to bootstrap tab
      this.tabIndex = parseInt(target.getAttribute("data-tab"));

      // set current active tab
      target.classList.add("active");
    }
  },
  computed: {
    ...mapGetters(["currentUserPersonalInfo"]),

    getFullName() {
      return (
        this.currentUserPersonalInfo.name +
        " " +
        this.currentUserPersonalInfo.surname
      );
    }
  }
};
</script>
