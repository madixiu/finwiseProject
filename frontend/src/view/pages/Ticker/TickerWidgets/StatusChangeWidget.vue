<template>
  <v-card rounded="lg">
    <!-- <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder">
        تغییر وضعیت
      </h3>
    </div> -->
    <div class="row">
      <div class="col-xxl-12">
        <template>
          <v-timeline>
            <v-timeline-item
              dense
              color="#4682B4"
              small
              v-for="(value, key) in notices"
              :key="key"
              v-bind:class="[key % 2 != 0 ? 'text-right' : '']"
            >
              <v-alert dense type="info" :color="getColor(value.Status)">
                <span class="customAlert"
                  >{{ value.persianDate.slice(0, 4) }}/{{
                    value.persianDate.slice(4, 6)
                  }}/{{ value.persianDate.slice(6, 8) }}<span> - </span>
                  {{ value.Hour }} <br />
                  {{ value.Status }}
                </span>
              </v-alert>
            </v-timeline-item>
          </v-timeline>
        </template>
      </div>
    </div>
    <!--end::Header-->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
export default {
  name: "StatusChanges",
  props: ["notices"],
  methods: {
    getColor(x) {
      if (x == "مجاز") {
        return "#1B5E20";
      }
      if (x == "مجاز-محفوظ") {
        return "#4CAF50";
      }
      if (x == "ممنوع") {
        return "#b71c1c";
      }
      if (x == "مجاز-مسدود") {
        return "#4CAF50";
      }
      if (x == "ممنوع-محفوظ") {
        return "#c62828";
      }
      if (x == "ممنوع-متوقف") {
        return "#c62828";
      }
      if (x == "مجاز-متوقف") {
        return "#4CAF50";
      }
    }
  }
};
</script>
<style scoped>
.v-timeline {
  direction: ltr !important;

  text-align: left;
}
.v-timeline:before {
  margin-left: 50%;
}
.customAlert {
  font-family: "Vazir-Light-FD" !important;
  font-size: 0.9em;
}
</style>
