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
              v-for="(value, key) in DataItems2"
              :key="key"
              v-bind:class="[key % 2 != 0 ? 'text-right' : '']"
            >
              <v-alert dense type="info"
                >{{ value.persianDate.slice(0, 4) }}/{{
                  value.persianDate.slice(4, 6)
                }}/{{ value.persianDate.slice(6, 8) }}<br />
                {{ value.Hour }} <br />
                {{ value.Status }}
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
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      // console.log("Watcher");
      this.populateData();
      // console.log(this.notices);
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
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
</style>
