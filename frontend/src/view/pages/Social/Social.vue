<template>
  <div class="row">
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-icon dense class="mb-2 pl-1" color="#0E76A8"
              >mdi-linkedin</v-icon
            >
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >LinkedIn</v-toolbar-title
            >
          </v-toolbar>
          <div id="curator-feed-new-feed-layout-linkedin" class="mt-2">
            <a
              href="https://curator.io"
              target="_blank"
              class="crt-logo crt-tag"
            ></a>
          </div>
        </v-card>
      </div>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <i
              class="v-icon notranslate pl-1 v-icon--dense mdi mdi-instagram theme--light instagram-icon"
            ></i>
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >Instagram</v-toolbar-title
            >
          </v-toolbar>
          <!-- <v-card-title>Instagram</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider> -->
          <div id="curator-feed-default-feed-layout" class="mt-2">
            <a
              href="https://curator.io"
              target="_blank"
              class="crt-logo crt-tag"
            ></a>
          </div>
        </v-card>
      </div>
    </div>
    <div class="col-xxl-6 col-lg-6 col-md-12 col-sm-12">
      <div>
        <v-card>
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-icon dense class="pl-1" color="#593a92">mdi-twitch</v-icon>
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >Twitch</v-toolbar-title
            >
          </v-toolbar>
          <!-- <v-card-title>Twitch</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider> -->
          <!-- <iframe
            src="https://player.twitch.tv/finwiselive&parent=https://finwise.ir"
            height="400"
            width="100%"
            allowfullscreen="true"
          >
          </iframe> -->
          <!-- <v-card-title>Twitch</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider> -->
          <VueTwitchPlayer
            :channel="channel"
            width="100%"
            height="500px"
          ></VueTwitchPlayer>
        </v-card>
      </div>
    </div>
  </div>
</template>
<script src="https://embed.twitch.tv/embed/v1.js"></script>
<script>
import VueTwitchPlayer from "vue-twitch-player";
export default {
  components: {
    VueTwitchPlayer
  },
  name: "SocialMedia",
  data() {
    return {
      channel: "finwiselive"
    };
  },
  created() {
    document.title = "Finwise - شبکه های اجتماعی";
    ascpetedHeight = ((1366 * 16) / 9) * 0.5;
    // new Twitch.Embed("twitch-embed", {
    //   width: 854,
    //   height: 480,
    //   channel: "finwiselive",
    //   // Only needed if this page is going to be embedded on other websites
    //   parent: ["https://finwise.ir"]
    // });
  },
  mounted() {
    (function() {
      var i,
        e,
        d = document,
        s = "script";
      i = d.createElement("script");
      i.async = 1;
      i.src =
        "https://cdn.curator.io/published/4b49fed0-aa5f-47bf-9e4f-8b6ba06574fa.js";
      e = d.getElementsByTagName(s)[0];
      e.parentNode.insertBefore(i, e);
    })();
    (function() {
      var i,
        e,
        d = document,
        s = "script";
      i = d.createElement("script");
      i.async = 1;
      i.src =
        "https://cdn.curator.io/published/9167bc5f-ad8c-4984-9679-6fc2a72e1331.js";
      e = d.getElementsByTagName(s)[0];
      e.parentNode.insertBefore(i, e);
    })();
  },
  methods: {}
};
</script>
<style scoped>
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
</style>
