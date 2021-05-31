<template>
  <div :id="containerId" class="TVChartContainer"></div>
</template>

<script>
import Datafeed from "./api/";
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
      default: "شستا"
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
  tvWidget: null,
  created() {
    document.title = "Finwise - نمودار پیشرفته";
  },
  mounted() {
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
      symbol: this.symbol,
      datafeed: Datafeed,
      custom_css_url: "../assets/chart.css",
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
        .attr("title", "Click to show a notification popup")
        .addClass("apply-common-tooltip")
        .on("click", () =>
          tvWidget.showNoticeDialog({
            title: "Notification",
            body: "TradingView Charting Library API works correctly",
            callback: () => {}
          })
        )[0].innerHTML = "Notice";

      tvWidget
        .createButton()
        .attr("title", "Dark Mode")
        .addClass("apply-common-tooltip")
        .on("click", () => tvWidget.changeTheme("Dark"))[0].innerHTML = "Dark";
      tvWidget
        .createButton()
        .attr("title", "Light Mode")
        .addClass("apply-common-tooltip")
        .on("click", () => tvWidget.changeTheme("Light"))[0].innerHTML =
        "Light";
    });
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
<style scoped>
.TVChartContainer {
  height: calc(90vh);
  direction: rtl;
}
</style>
