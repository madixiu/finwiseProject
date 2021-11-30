<template>
  <!-- <div class="d-flex flex-column flex-root"> -->
  <!-- <div
      class="login login-1 login-signin-on d-flex flex-column flex-lg-row flex-row-fluid bg-white"
      id="kt_login"
    > -->
  <!--begin::Aside-->
  <div id="loginFormID" class="login-form-page d-flex">
    <v-container fluid style="height: 100vh">
      <v-row style="height:100%">
        <v-col
          lg="3"
          xs="12"
          sm="3"
          md="4"
          xl="4"
          col="4"
          class="d-flex gradient justify-content-center align-items-center"
        >
          <!--begin: Aside Container -->
          <div
            class="d-flex flex-row-fluid flex-column justify-content-center align-items-center"
          >
            <!--begin: Aside header -->
            <router-link to="/" v-slot="{ href, navigate }">
              <a :href="href" class="flex-column-auto" @click="navigate">
                <img
                  src="media/logos/logo-letter-1.png"
                  style="max-height:80px"
                />
              </a>
            </router-link>

            <!--end: Aside header -->
            <!--begin: Aside content -->
            <div
              class="flex-column-fluid d-flex flex-column justify-content-center mt-3"
            >
              <span class="welcome-text">
                به فین وایز خوش آمدید
              </span>
            </div>
            <!--end: Aside content -->
            <!--begin: Aside footer for desktop -->
            <div
              class="flex-column-fluid d-flex flex-column justify-content-center mt-2"
            >
              <div class="finwiseCo">
                © 2021 FinWise
              </div>
            </div>
            <div class="mt-5">
               <i @click="instagramLink"
              class="v-icon notranslate pl-1 v-icon--dense mdi mdi-instagram theme--light instagram-icon"
            ></i>
            </div>
            <!--end: Aside footer for desktop -->
          </div>
          <!--end: Aside Container -->
        </v-col>
        <v-col
          lg="9"
          xs="12"
          sm="9"
          md="8"
          xl="8"
          col="8"
          class="d-flex gradient justify-content-center align-items-center"
        >
          <!--begin::Content-->
          <div
            class="flex-row-fluid d-flex flex-column position-relative overflow-hidden"
          >
            <div class="d-flex flex-column-fluid flex-center">
              <router-view></router-view>
            </div>
          </div>
          <!--end::Content-->
        </v-col>
      </v-row>
    </v-container>
  </div>
  <!--begin::Aside-->

  <!-- </div> -->
  <!-- </div> -->
</template>

<!-- Load login custom page styles -->
<style lang="scss">
@import "@/assets/sass/pages/login/login-4.scss";
// .login-form-page {
//   background-size: cover;
//   background-position: center center;
//   height: calc(100vh);
// }
.welcome-text {
  font-size: 1em;
  color: white;
}
.finwiseCo {
  // opacity-70 font-weight-bold text-white
  opacity: 0.7;
  direction: ltr;
  font-size: 0.9em;
  color: white;
}
.login-form-page {
  background: linear-gradient(-90deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  // animation: gradient 95s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
.instagram-icon {
  background: radial-gradient(
    circle at 30% 107%,
    #fdf497 0%,
    #fdf497 5%,
    #fd5949 45%,
    #d6249f 60%,
    #285aeb 90%
  );
  -webkit-background-clip: text;
  /* Also define standard property for compatibility */
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.instagram-icon:hover {
  cursor: pointer;
} 
</style>

<script>
import { mapState } from "vuex";

export default {
  name: "auth",
  methods:{
    instagramLink(){
      window.open("https://www.instagram.com/finwise.ir", "_blank");

    }
  },
  computed: {
    ...mapState({
      errors: state => state.auth.errors
    }),
    backgroundImage() {
      return process.env.BASE_URL + "media/bg/bg-2.jpg";
    },
    ratio() {
      if (window.screen.height > window.screen.width) return true;
      else return false;
    }
  }
};
</script>
