<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder">
        تغییر وضعیت
      </h3>
    </div>
    <div class="row">
      <div class="col-xxl-12">
        <template>
          <v-timeline>
            <v-timeline-item
              dense
              color="#212529"
              small
              v-for="(value, key) in DataItems2"
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
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "StatusChanges",
  props: ["notices"],
  data() {
    return {
      search: "",
      DataItems2: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems2 = this.notices;
    },
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
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      this.populateData();
    }
  }
};
</script>
<style scoped>
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
.v-timeline {
  direction: ltr !important;

  text-align: left;
}
.v-timeline:before {
  margin-left: 50%;
}
.customAlert {
  font-family: "Dirooz FD" !important;
  font-size:0.9em
}
</style>
