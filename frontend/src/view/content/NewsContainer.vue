<template>
  <div>
    <div v-if="News.length != 0" class="d-flex flex-lg-column NewsFooter">
      <News v-if="News.length" :News="News"></News>
    </div>
  </div>
</template>

<script>
import News from "@/view/content/News.vue";
export default {
  name: "NewsContainer",
  components: {
    News
  },
  data() {
    return {
      News: []
    };
  },
  mounted() {
    this.getNews();
  },
  methods: {
    async getNews() {
      await this.axios
        .get("/api/LatestNews")
        .then(getNewsResp => {
          if (getNewsResp.data != "noData") this.News = getNewsResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
<style scoped>
.NewsFooter {
  position: fixed;
  height: 20px;
  bottom: 0px;
  right: 0;
  left: 0;
  transition: top 0.3s ease;
  z-index: 95;
  box-shadow: 0 10px 30px 0 #1e1e2d;
  border-top: 1px solid #ebedf3;
  margin: 0;
}
</style>
