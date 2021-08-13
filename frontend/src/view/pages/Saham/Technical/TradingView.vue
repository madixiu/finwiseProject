<template>
  <div :id="containerId" class="TVChartContainer"></div>
</template>

<script>
import Datafeed from "./api/";
import { EventBus } from "@/main.js";
import { widget } from "@/assets/charting_library/charting_library.min";
// function getLanguageFromURL() {
//   const regex = new RegExp('[\\?&]lang=([^&#]*)');
//   const results = regex.exec(window.location.search);
//   return results === null ? null : decodeURIComponent(results[1].replace(/\+/g, ' '));
// }
export default {
  name: "TVChartContainer",
  props: {
    symbol: {
      type: String,
      default: "فولاد"
    },
    datafeedUrl: {
      // default: 'https://demo_feed.tradingview.com',
      type: String
    },
    interval: {
      type: String,
      default: "D"
    },
    containerId: {
      type: String,
      default: "tv-chart"
    },
    libraryPath: {
      type: String,
      default: "/charting_library/"
    },
    chartsStorageUrl: {
      type: String,
      default: "https://saveload.tradingview.com"
    },
    chartsStorageApiVersion: {
      type: String,
      default: "1.1"
    },
    clientId: {
      type: String,
      default: "tradingview.com"
    },
    userId: {
      type: String,
      default: "public_user_id"
    },
    fullscreen: {
      type: Boolean,
      default: false
    },
    autosize: {
      type: Boolean,
      default: true
    },
    studiesOverrides: {
      type: Object
    },
    theme: {
      type: String,
      default: "Light"
    }
  },
  data() {
    return {
      key: 0,
      selectedSymbol: "",
      adjustType: "noAdjust",
      selectForm: [
        "<select> <option selected  value='noAdjust'>بدون تعدیل</option>    <option value='AdjustDPS'>تعدیل با سود نقدی</option> <option value='AdjustIC'>تعدیل با افزایش سرمایه</option> <option value='AdjustICDPS'>تعدیل با افزایش سرمایه و سود نقدی</option> </select>",
        "<select> <option  value='noAdjust'>بدون تعدیل</option>    <option selected value='AdjustDPS'>تعدیل با سود نقدی</option> <option value='AdjustIC'>تعدیل با افزایش سرمایه</option> <option value='AdjustICDPS'>تعدیل با افزایش سرمایه و سود نقدی</option> </select>",
        "<select> <option  value='noAdjust'>بدون تعدیل</option>    <option value='AdjustDPS'>تعدیل با سود نقدی</option> <option selected value='AdjustIC'>تعدیل با افزایش سرمایه</option> <option value='AdjustICDPS'>تعدیل با افزایش سرمایه و سود نقدی</option> </select>",
        "<select> <option  value='noAdjust'>بدون تعدیل</option>    <option value='AdjustDPS'>تعدیل با سود نقدی</option> <option value='AdjustIC'>تعدیل با افزایش سرمایه</option> <option selected value='AdjustICDPS'>تعدیل با افزایش سرمایه و سود نقدی</option> </select>"
      ]
    };
  },
  tvWidget: null,
  created() {
    document.title = "Finwise - نمودار پیشرفته";
    this.selectedSymbol = this.symbol;
  },

  mounted() {
    this.renderChart();
    EventBus.$on("TradingViewSymbol", data => {
      this.selectedSymbol = data;
    });
  },
  watch: {
    symbol() {
      this.selectedSymbol = this.symbol;
    },
    key() {
      // console.log(oldValue,newValue);
      // if (newValue == 1 && oldValue == 0){
      this.renderChart();

      // }
    }
  },
  computed: {
    dropDown() {
      if (this.adjustType == "noAdjust") return this.selectForm[0];
      else if (this.adjustType == "AdjustDPS") return this.selectForm[1];
      else if (this.adjustType == "AdjustIC") return this.selectForm[2];
      else return this.selectForm[3];
    }
  },
  methods: {
    EmitFunction(e) {
      EventBus.$emit(
        "TradingViewAdjust",
        e.target[e.target.selectedIndex].value
      );
      this.key++;
      this.adjustType = e.target[e.target.selectedIndex].value;
    },
    renderChart() {
      const INTERVAL = {
        MINUTE: "1",
        MINUTES_5: "5",
        MINUTES_15: "15",
        MINUTES_30: "30",
        HOUR: "60",
        HOURS_3: "180",
        HOURS_6: "360",
        HOURS_12: "720",
        DAY: "D",
        WEEK: "W"
      };

      const TIME_FRAMES = [
        { text: "3y", resolution: INTERVAL.WEEK, description: "3 Years" },
        { text: "1y", resolution: INTERVAL.DAY, description: "1 Year" },
        // { text: '3m', resolution: INTERVAL.HOURS_12, description: '3 Months' },
        // { text: '1m', resolution: INTERVAL.HOURS_6, description: '1 Month' },
        { text: "7d", resolution: INTERVAL.HOUR, description: "7 Days" },
        { text: "3d", resolution: INTERVAL.MINUTES_30, description: "3 Days" },
        { text: "1d", resolution: INTERVAL.MINUTES_15, description: "1 Day" }
        // { text: '6h', resolution: INTERVAL.MINUTES_5, description: '6 Hours' },
        // { text: '1h', resolution: INTERVAL.MINUTE, description: '1 Hour' },
      ];
      const widgetOptions = {
        supports_marks: true,
        supports_time: true,
        timezone: "Asia/Tehran",
        debug: false,
        symbol: this.selectedSymbol,
        datafeed: Datafeed,
        custom_css_url: "./chart.css",
        interval: this.interval,
        container_id: this.containerId,
        library_path: this.libraryPath,
        locale: "fa",
        disabled_features: ["use_localstorage_for_settings"],
        enabled_features: ["study_templates"],
        disabledDrawings: true,
        charts_storage_url: this.chartsStorageUrl,
        charts_storage_api_version: this.chartsStorageApiVersion,
        client_id: this.clientId,
        user_id: this.userId,
        fullscreen: this.fullscreen,
        time_frames: TIME_FRAMES,
        autosize: this.autosize,
        theme: this.theme,
        studies_overrides: this.studiesOverrides,
        overrides: {
          "mainSeriesProperties.showCountdown": false
        }
      };
      const tvWidget = new widget(widgetOptions);
      this.tvWidget = tvWidget;
      tvWidget.onChartReady(() => {
        tvWidget
          .createButton()
          .attr("title", "Select or Search Pairings")
          .addClass("apply-common-tooltip")
          .on("click", () =>
            tvWidget.chart().executeActionById("symbolSearch")
          )[0].innerHTML = "Pairings";
        tvWidget.chart();

        // .setMarkers([
        // 	{ time: 1610693220, position: 'belowBar', color: 'orange', shape: 'arrowUp' },
        // ]);
        tvWidget
          .createButton()
          .addClass("apply-common-tooltip")
          .on(
            "change",
            e => this.EmitFunction(e)
            // EventBus.$emit(
            //   "TradingViewAdjust",
            //   e.target[e.target.selectedIndex].value,
            // )
            // this.key++
            // console.log(e.target[e.target.selectedIndex].value)
          )[0].innerHTML = this.dropDown;
        // "<select> <option  value='noAdjust'>بدون تعدیل</option>    <option value='AdjustDPS'>تعدیل با سود نقدی</option> <option value='AdjustIC'>تعدیل با افزایش سرمایه</option> <option value='AdjustICDPS'>تعدیل با افزایش سرمایه و سود نقدی</option> </select>";

        // tvWidget
        //   .createButton()
        //   .attr("title", "Dark Mode")
        //   .addClass("apply-common-tooltip")
        //   .on("click", () => tvWidget.changeTheme("Dark"))[0].innerHTML = "Dark";
        // tvWidget
        //   .createButton()
        //   .attr("title", "Light Mode")
        //   .addClass("apply-common-tooltip")
        //   .on("click", () => tvWidget.changeTheme("Light"))[0].innerHTML =
        //   "Light"
      });
    }
  },
  destroyed() {
    if (this.tvWidget !== null) {
      this.tvWidget.remove();
      this.tvWidget = null;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.chart-page {
  font-family: "Vazir-Medium-FD" !important;
}
.TVChartContainer {
  height: calc(90vh);
  direction: rtl;
}
</style>
