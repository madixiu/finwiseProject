<template>
  <!-- begin:: Header Topbar -->
  <div class="topbar">
    <!-- my search -->
    <SearchDefault class="ml-4"></SearchDefault>

    <Clock></Clock>
    <div class="topbar-item mr-2" v-if="!this.$store.getters.isAuthenticated">
      <v-btn small color="#ebebeb" dark @click="loginClick">
        <v-icon small class="pl-1 pr-0" color="#4177a5"
          >mdi-account-circle</v-icon
        >
        <span style="color:#4177a5">ورود</span>
      </v-btn>
    </div>

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

export default {
  name: "KTTopbar",

  components: {
    SearchDefault,
    Clock,
    Profile
  },
  methods: {
    loginClick() {
      this.$router.push({ name: "login" });
    }
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
    }
  }
};
</script>
