<template>
  <div>
    <div class="py-1 px-2" v-if="currentUser">
      <div class="headerProfile">
        <span>{{ currentUser.username }}</span>
      </div>
    </div>
    <!-- <v-btn depressed block class="mb-1 mt-1 customBTN">
      <v-icon dense class="mr-1">mdi-account</v-icon>
      <span>پروفایل</span>
    </v-btn>
    <v-btn depressed block class="mb-1 mt-1">
      <v-icon dense class="mr-1">mdi-logout</v-icon>
      <span>خروج</span>
    </v-btn> -->

    <!-- <hr />
    <div class="bigRow" @mouseenter="login = true" @mouseleave="login = false">
      <div class="py-1 px-2">
        <div class="rowProfile">
          <v-icon dense class="mr-1" :color="loginColor">mdi-login</v-icon>
          <span>ورود</span>
        </div>
      </div>
    </div> -->

    <hr />
    <div
      class="bigRow"
      @mouseenter="profile = true"
      @mouseleave="profile = false"
      @click="profileClick"
    >
      <div class="py-1 px-2">
        <div class="rowProfile">
          <v-icon dense class="mr-1" :color="profileColor">mdi-account</v-icon>
          <span>پروفایل</span>
        </div>
      </div>
    </div>
    <hr />
    <div
      class="bigRow"
      @mouseenter="logout = true"
      @mouseleave="logout = false"
      @click="logoutClick"
    >
      <div class="py-1 px-1">
        <div class="rowProfile">
          <v-icon dense class="mr-1" :color="logoutColor">mdi-logout</v-icon>
          <!-- <i class="mdi-logout"></i> -->
          <!-- <span class="iconify" data-icon="mdi-logout" data-inline="false" ></span> -->
          <span>خروج</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
    profile: false,
    login: false,
    logout: false
  }),
  computed: {
    ...mapGetters(["currentUser"]),
    profileColor() {
      if (this.profile) {
        return "#000";
      } else return "";
    },
    // loginColor() {
    //   if (this.login) {
    //     return "#000";
    //   } else return "";
    // },
    logoutColor() {
      if (this.logout) {
        return "#000";
      } else return "";
    }
  },
  methods: {
    profileClick() {
      // Close the menu and (by passing true) return focus to the toggle button
      // this.$parent.$refs.profileDropdown.hide(true);
      if (this.$router.name != "profile")
        this.$router.push({ name: "profile" });
    },
    logoutClick() {
      this.$store
        .dispatch("LOGOUT")
        .then(() => this.$router.push({ name: "login" }));
    }
  }
};
</script>

<style scoped>
hr {
  margin-top: 0rem;
  margin-bottom: 0rem;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}
span.v-btn__content {
  justify-content: flex-start !important;
}
.bigRow {
  background-color: #ececec;
}
.bigRow:hover {
  background-color: #fff;
}
/* .bigRow:hover .rowProfile span i {
  color: red;
  font-weight: 500;
} */
.bigRow span {
  color: rgb(32, 32, 32);
}
.bigRow:hover span {
  color: black;
  font-weight: 600;
}
.rowProfile {
  display: flex;
  align-items: center;
  align-content: center;
  cursor: pointer;
  min-height: 30px;
}
.headerProfile {
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
  min-height: 30px;
  border-radius: 10px;
  background-color: #1e1e2d;
}
.headerProfile span {
  color: white;
}
/* .rowProfile:hover {
  background-color: gray;
} */

.flex-container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: normal;
  align-items: stretch;
  align-content: normal;
}

.flex-items {
  display: block;
  flex-grow: 0;
  flex-shrink: 1;
  flex-basis: auto;
  align-self: auto;
  order: 0;
}
/* .dropdown-content-enter-active,
.dropdown-content-leave-active {
  transition: all 0.2s;
}
.dropdown-content-enter,
.dropdown-content-leave-to {
  opacity: 0;
  transform: translateY(-5px);
} */
</style>
