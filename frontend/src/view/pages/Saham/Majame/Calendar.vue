<template>
  <div>
    <persian-calendar
      v-if="events.length"
      :events-list="events"
      @on-day-click="test2"
      :display-period.sync="period"
    >
      <template slot="event" slot-scope="i" @on-event-click="test">
        <div
          :key="i.value.id"
          :class="i.value.classes"
          :style="`top:${i.top};`"
          class="vpc_event"
          style="border:1px #eee; "
        >
          <!--  Anything You Wish -->
          <v-tooltip right>
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                dark
                v-bind="attrs"
                v-on="on"
                label
                :color="i.value.color"
                @click="test(i)"
              >
                {{ i.value.title }}
              </v-chip>
            </template>
            <span>{{ i.value.type }}</span>
          </v-tooltip>
          <!-- <span
            class="vpc_event-title"
            :style="
              `top:${i.top};background-color:${i.value.color};color:white`
            "
            >{{ i.value.title }}</span> -->
        </div>
      </template>
    </persian-calendar>
    <!-- <h2>Current Display Period {{ period }}</h2> -->
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-6.vue";
import PersianCalendar from "vue-persian-calendar";
export default {
  name: "calendar",
  components: {
    PersianCalendar
    // Error,
    // ErrorMine
  },
  data() {
    return {
      period: "month",
      tempData: [],
      events: []
      // events: [
      //   {
      //     id: 1,
      //     startDateTime: this.$moment(
      //       "1399/05/07 23:31:33",
      //       "jYYYY/jMM/jDD HH:mm:ss"
      //     ),
      //     endDateTime: this.$moment(
      //       "1399/05/07 23:31:33",
      //       "jYYYY/jMM/jDD HH:mm:ss"
      //     ),
      //     title: "رویداد شماره ۱",
      //     color: "#8879b8",
      //     classes: []
      //   },
      //   {
      //     id: 2,
      //     startDateTime: this.$moment(
      //       "1399/05/13 10:30:33",
      //       "jYYYY/jMM/jDD HH:mm"
      //     ),
      //     endDateTime: this.$moment("1399/05/13 15:00", "jYYYY/jMM/jDD HH:mm"),
      //     title: "رویداد شماره ۲",
      //     color: "#aa7749",
      //     classes: []
      //   },
      //   {
      //     id: 7,
      //     startDateTime: this.$moment(
      //       "1399/05/13 10:30",
      //       "jYYYY/jMM/jDD HH:mm"
      //     ),
      //     endDateTime: this.$moment("1399/05/13 11:30", "jYYYY/jMM/jDD HH:mm"),
      //     title: "گفتگوی اسکایپی با مدیر شرکت آرمان",
      //     color: "#a71749",
      //     classes: []
      //   },
      //   {
      //     id: 4,
      //     startDateTime: this.$moment(
      //       "1399/05/09 10:30",
      //       "jYYYY/jMM/jDD HH:mm"
      //     ),
      //     endDateTime: this.$moment("1399/05/13 14:00", "jYYYY/jMM/jDD HH:mm"),
      //     title: "رویداد شماره ۳",
      //     color: "#34147e",
      //     classes: []
      //   },
      //   {
      //     id: 5,
      //     startDateTime: this.$moment(
      //       "1399/05/06 10:30",
      //       "jYYYY/jMM/jDD HH:mm"
      //     ),
      //     endDateTime: this.$moment("1399/05/08 18:35", "jYYYY/jMM/jDD HH:mm"),
      //     title: "رویداد شماره ۴",
      //     color: "#34147e",
      //     classes: []
      //   },
      //   {
      //     id: 456456463,
      //     startDateTime: this.$moment("1399/05/10", "jYYYY/jMM/jDD"),
      //     endDateTime: this.$moment("1399/05/25", "jYYYY/jMM/jDD"),
      //     title: "گفتگوی اسکایپی با مدیر شرکت آرمان",
      //     color: "#cb09cb",
      //     classes: []
      //   }
      // ]
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    loadData() {
      this.DataReq();
      // this.formater();
    },
    formater() {
      let temp = [];
      if (this.tempData.length) {
        for (let item of this.tempData) {
          temp.push({
            id: item.report_id,
            startDateTime: this.$moment(
              item.PublishTime,
              "jYYYY/jMM/jDD HH:mm:ss"
            ),
            endDateTime: this.$moment(
              item.PublishTime,
              "jYYYY/jMM/jDD HH:mm:ss"
            ),
            title: item.Ticker,
            type: item.Type,
            color: "#aa7749",
            classes: []
          });
        }
        this.events = temp;
      } else console.log("empty data");
    },
    async DataReq() {
      await this.axios
        .get("api/MainCalendar")
        .then(response => {
          this.tempData = response.data;
          this.formater();
        })
        .catch(error => {
          console.log(error);
        });
    },
    test(i) {
      console.log(i);
    },
    test2() {
      console.log("today");
    }
  }
};
</script>
