<template>
  <div id="clock" class="topbar-item">
    <div class="outer">
      <div class="top">
        <v-icon size="15px" color="#4682B4" class="mr-1"
          >mdi-calendar-month</v-icon
        >
        <span class="date">{{ date }}</span>
        <v-icon size="15px" :color="StockStatusColor">mdi-circle-medium</v-icon>
      </div>
      <div class="below">
        <v-icon size="15px" color="#4682B4" class="mr-1"
          >mdi-clock-outline</v-icon
        >
        <span class="time">{{ time }}</span>
        <!-- <v-icon
              size="15px"
              color="#c50202"
              @click="info(row.item)"
              class="mr-1"
              >mdi-circle-medium</v-icon
            > -->
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      // week: ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
      StockOpen: false,
      StockStatusColor: "#d50000",
      time: "",
      date: ""
    };
  },
  mounted() {
    // var timerID = setInterval(this.updateTime, 1000);
    setInterval(this.updateTime, 1000);
  },
  methods: {
    StockStatusChecker() {
      if (this.StockOpen == true) this.StockStatusColor = "#64dd17";
      else this.StockStatusColor = "#d50000";
    },
    updateTime() {
      let newDate = new Date();
      this.time =
        this.zeroPadding(newDate.getHours(), 2) +
        ":" +
        this.zeroPadding(newDate.getMinutes(), 2) +
        ":" +
        this.zeroPadding(newDate.getSeconds(), 2);
      let date =
        this.zeroPadding(newDate.getFullYear(), 4) +
        "/" +
        this.zeroPadding(newDate.getMonth() + 1, 2) +
        "/" +
        this.zeroPadding(newDate.getDate(), 2);
      this.date = this.$moment(date, "YYYY/MM/DD")
        .locale("fa")
        .format("YYYY/MM/DD");
      if (
        newDate.getHours() >= 9 &&
        newDate.getHours() < 12 &&
        newDate.getDay() != 5 &&
        newDate.getDay() != 4
      ) {
        this.StockOpen = true;
      } else if (
        newDate.getHours() == 12 &&
        newDate.getMinutes() <= 30 &&
        newDate.getDay() != 5 &&
        newDate.getDay() != 4
      ) {
        this.StockOpen = true;
      } else this.StockOpen = false;
      this.StockStatusChecker();
    },
    // moment('1989/01/24', 'YYYY/MM/DD').locale('fa').format('YYYY/MM/DD'); // 1367/11/04
    zeroPadding(num, digit) {
      let zero = "";
      for (let i = 0; i < digit; i++) {
        zero += "0";
      }
      return (zero + num).slice(-digit);
    }
  }
};
</script>
<style scoped>
#clock {
  font-family: "Dirooz FD";
  /* color: #ffffff; */
  /* position: relative; */
  /* left: 5%;
  top: 30%; */
  /* transform: translate(-50%, -50%); */
  color: #daf6ff;
  text-shadow: 0 0 20px rgba(10, 175, 230, 1), 0 0 20px rgba(10, 175, 230, 0);
}
.time {
  font-family: "Dirooz FD";
  letter-spacing: 0.05em;
  font-size: 0.8rem;
  padding: 5px 0;
}
.date {
  font-family: "Dirooz FD";
  letter-spacing: 0.1em;
  font-size: 0.7rem;
}
.top {
  direction: ltr;
}
.below {
  direction: ltr;
  align-items: left;
}
/* .outer {
  display: grid;
  grid-template: 1fr / 1fr;0
  place-items: center;
  position: relative;
} */
/* .outer > * {
  grid-column: 1 / 1;
  grid-row: 1 / 1;
} */
/* .outer .top {
  position: absolute;
  z-index: 1;
}
.outer .below {
  position: absolute;
  z-index: 2;
} */
/* .text {
  letter-spacing: 0.1em;
  font-size: 12px;
  padding: 20px 0 0;
} */
</style>
