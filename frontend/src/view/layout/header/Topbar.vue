<template>
  <!-- begin:: Header Topbar -->
  <div class="topbar">
    <!-- my search -->
    <SearchDefault class="ml-4"></SearchDefault>

    <!--begin: Search -->
    <!-- <b-dropdown
      size="sm"
      id="kt_quick_search_toggle"
      variant="link"
      toggle-class="topbar-item text-decoration-none"
      no-caret
      right
      no-flip
    >
      <template v-slot:button-content>
        <div class="btn btn-icon btn-clean btn-lg btn-dropdown mr-1">
          <span class="svg-icon svg-icon-xl svg-icon-primary">
            <inline-svg :src="SearchIcon" />
          </span>
        </div>
      </template>
      <b-dropdown-text tag="div" class="min-w-md-350px">
        <KTSearchDefault></KTSearchDefault>
      </b-dropdown-text>
    </b-dropdown> -->
    <!--end: Search -->

    <!--begin: Notifications -->
    <!-- <b-dropdown
      size="sm"
      variant="link"
      toggle-class="topbar-item text-decoration-none"
      no-caret
      right
      no-flip
    >
      <template v-blockslot:button-content>
        <div
          class="btn btn-icon btn-clean btn-dropdown btn-lg mr-1 pulse pulse-primary"
        >
          <span class="svg-icon svg-icon-xl svg-icon-primary">
            <inline-svg :src="NotificationIcon" />
          </span>
          <span class="pulse-ring"></span>
        </div>
      </template>
      <b-dropdown-text tag="div" class="min-w-md-350px">
        <form>
          <KTDropdownNotification></KTDropdownNotification>
        </form>
      </b-dropdown-text>
    </b-dropdown> -->
    <!--end: Notifications -->
    <!-- Clock -->
    <Clock></Clock>
    <div class="topbar-item mr-2" v-if="!this.$store.getters.isAuthenticated">
      <v-btn small color="#3d3e4e" dark @click="loginClick">
        <v-icon dense class="" color="#4177a5">mdi-account-circle</v-icon>
        ورود
      </v-btn>
    </div>
    <!-- <Profile />\ -->
    <!-- Clock end -->
    <!--begin: Quick Actions -->
    <!-- <div class="btn btn-icon btn-clean btn-dropdown btn-lg mr-1">
      <v-icon size="25px" color="#4682B4" class="mr-1"
        >mdi-account-circle</v-icon
      >
      <Profile />
    </div> -->
    <!-- v-if="this.$store.getters.isAuthenticated" -->

    <b-dropdown
      v-if="this.$store.getters.isAuthenticated"
      ref="profileDropdown"
      size="lg"
      variant="link"
      toggle-class="topbar-item text-decoration-none"
      no-caret
      left
      no-flip
      menu-class="profileDropdownClass"
    >
      <template v-slot:button-content>
        <div class="btn btn-icon btn-clean btn-dropdown mr-1">
          <v-icon size="25px" color="#4682B4" class="mr-1"
            >mdi-account-circle</v-icon
          >
          <!-- <span class="svg-icon svg-icon-xl svg-icon-primary">
            <inline-svg :src="QuickActionIcon" />
            
          </span> -->
        </div>
      </template>
      <b-dropdown-text tag="div">
        <!-- <KTDropdownQuickAction></KTDropdownQuickAction> -->
        <Profile />
      </b-dropdown-text>
    </b-dropdown>
    <!--end: Quick Actions -->

    <!--begin: My Cart -->
    <!-- <b-dropdown
      size="sm"
      variant="link"
      toggle-class="topbar-item text-decoration-none"
      no-caret
      right
      no-flip
    >
      <template v-slot:button-content>
        <div class="btn btn-icon btn-clean btn-dropdown btn-lg mr-1">
          <span class="svg-icon svg-icon-xl svg-icon-primary">
            <inline-svg :src="MyCartIcon" />
          </span>
        </div>
      </template>
      <b-dropdown-text tag="div" class="min-w-md-350px">
        <KTDropdownMyCart></KTDropdownMyCart>
      </b-dropdown-text>
    </b-dropdown> -->
    <!--end: My Cart -->

    <!--begin: Quick panel toggle -->
    <!-- <KTQuickPanel></KTQuickPanel> -->
    <!--end: Quick panel toggle -->

    <!--begin: Language bar -->
    <!-- <div class="topbar-item">
      <b-dropdown
        size="sm"
        variant="link"
        toggle-class="btn btn-icon btn-clean btn-dropdown btn-lg mr-1 text-decoration-none"
        no-caret
        right
        no-flip
      >
        <template v-slot:button-content>
          <img
            class="h-20px w-20px rounded-sm"
            :src="languageFlag || getLanguageFlag"
            alt=""
          />
        </template>
        <b-dropdown-text tag="div" class="min-w-md-175px">
          <KTDropdownLanguage
            v-on:language-changed="onLanguageChanged"
          ></KTDropdownLanguage>
        </b-dropdown-text>
      </b-dropdown>
    </div> -->
    <!--end: Language bar -->

    <!--begin: User Bar -->
    <!-- <KTQuickUser></KTQuickUser> -->
    <!-- <KTQuickUser2 /> -->

    <!--end: User Bar -->
  </div>
  <!-- end:: Header Topbar -->
</template>

<style lang="scss">
.topbar {
  .dropdown-toggle {
    padding: 0;
    &:hover {
      text-decoration: none;
    }

    &.dropdown-toggle-no-caret {
      &:after {
        content: none;
      }
    }
  }
  // .profileDropdownClass.show {
  //   border-radius: 5px;
  //   // transition-property: height;
  //   transition-property: height;
  //   transition-duration: 2s;
  //   transition-timing-function: linear;
  //   background-color: aqua;
  //   // height: 100px;
  //       // box-sizing: 0 5px 25px rgba(0,0,0,0.1);
  // }
  .profileDropdownClass {
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    -ms-transition: all 0.3s;
    -o-transition: all 0.3s;
    transition: all 0.3s;

    max-height: 0;
    display: block;
    overflow: hidden;
    opacity: 0;
  }

  .profileDropdownClass.show {
    /* For Bootstrap 4, use .dropdown.show instead of .dropdown.open */
    max-height: 300px;
    opacity: 1;
  }
  .dropdown-menu {
    margin: 0;
    padding: 0;
    outline: none;
    .b-dropdown-text {
      padding: 0;
    }
  }
}
</style>

<script>
import SearchDefault from "@/view/layout/extras/Search.vue";
import Clock from "@/view/content/Clock.vue";
import Profile from "@/view/layout/extras/dropdown/ProfileDropdown";
// import KTDropdownNotification from "@/view/layout/extras/dropdown/DropdownNotification.vue";
// import KTSearchDefault from "@/view/layout/extras/dropdown/SearchDefault.vue";

// import KTDropdownQuickAction from "@/view/layout/extras/dropdown/DropdownQuickAction.vue";
// import KTDropdownMyCart from "@/view/layout/extras/dropdown/DropdownMyCart.vue";
// import KTDropdownLanguage from "@/view/layout/extras/dropdown/DropdownLanguage.vue";
// import KTQuickUser from "@/view/layout/extras/offcanvas/QuickUser.vue";
// import KTQuickUser2 from "@/view/layout/extras/offcanvas/QuickUser2.vue";

// import KTQuickPanel from "@/view/layout/extras/offcanvas/QuickPanel.vue";
import i18nService from "@/core/services/i18n.service.js";

export default {
  name: "KTTopbar",
  data() {
    return {
      languageFlag: "",
      languages: i18nService.languages
    };
  },
  components: {
    SearchDefault,
    Clock,
    Profile
    // KTSearchDefault,
    // KTDropdownNotification,
    // KTDropdownQuickAction

    // KTDropdownMyCart,
    // KTDropdownLanguage,
    // KTQuickUser,
    // KTQuickUser2
    // KTQuickPanel
  },
  methods: {
    onLanguageChanged() {
      this.languageFlag = this.languages.find(val => {
        return val.lang === i18nService.getActiveLanguage();
      }).flag;
    },
    loginClick() {
      this.$router.push({ name: "login" });
    }
    // onClick() {
    //   // Close the menu and (by passing true) return focus to the toggle button
    //   this.$refs.dropdown.hide(true);
    // }
  },
  computed: {
    SearchIcon() {
      return process.env.BASE_URL + "media/svg/icons/General/Search.svg";
    },
    NotificationIcon() {
      return process.env.BASE_URL + "media/svg/icons/Code/Compiling.svg";
    },
    QuickActionIcon() {
      return (
        process.env.BASE_URL + "media/svg/icons/Communication/Shield-user.svg"
      );
    },
    MyCartIcon() {
      return process.env.BASE_URL + "media/svg/icons/Shopping/Cart3.svg";
    },
    getLanguageFlag() {
      return this.onLanguageChanged();
    }
  }
};
</script>
