/* eslint-disable no-unused-vars */
// import pairs from './pairs'
var rp = require("request-promise").defaults({ json: true });
// const api_root = 'https://min-api.cryptocompare.com'
const history = {};
var typeOf = 0;
import { EventBus } from "@/main.js";
EventBus.$on("TradingViewAdjust", data => {
  // this.header = data;
  if (data == "noAdjust") typeOf = 0;
  else if (data == "AdjustDPS") typeOf = 1;
  else if (data == "AdjustIC") typeOf = 2;
  else if (data == "AdjustICDPS") typeOf = 3;
  console.log(data);
});

export default {
  history: history,
  typeOf: typeOf,
  getMarks: function(symbolInfo, from, to, onDataCallback, resolution) {
    // if (localStorage.bnApiStatus.toString() == "true") {
    // let symbol = symbolInfo.name;
    // var result = [];
    // var el = {
    //   id: "Dividend-13800430",
    //   color: "green",
    //   time: 1610892000,
    //   text: "abc",
    //   label: "label",
    //   labelFontColor: "#fff",
    //   minSize: 8
    // };
    // result.push(el);
    // onDataCallback(result);
    // return result;
  },
  getBars: function(symbolInfo, resolution, from, to, first, limit) {
    console.log(symbolInfo);
    EventBus.$emit("TradingViewSymbol",symbolInfo.name)
    // var split_symbol = symbolInfo.name.split(/[:/]/)
    // const url = resolution === 'D' ? '/data/histoday' : resolution >= 60 ? '/data/histohour' : '/data/histominute'
    var url = "";
    const qs = {
      // e: pairs[split_symbol[0] + "/" + split_symbol[1]],
      // 		fsym: split_symbol[0],
      // 		tsym: split_symbol[1],
      // 		toTs:  to ? to : '',
      // 		limit: limit ? limit : 2000,
      // 		// aggregate: 1//resolution
      limits: 2000,
      url: symbolInfo.urlparam,
      todate: to ? "" + to : "",
      typeof: typeOf
      // order:'utc.desc'
    };

    // axios
    //   .get("http://185.231.115.223:3000/rpc/ViewTVDaily", { params: qs })
    //   .then(data => {
    //     if (data.Response && data.Response === "Error") {
    //       return [];
    //     }
    //     if (data.length) {
    //       var bars = data.map(el => {
    //         return {
    //           time: el.utc * 1000, //TradingView requires bar time in ms
    //           low: el.low,
    //           high: el.high,
    //           open: el.first,
    //           close: el.close,
    //           volume: el.tradevol
    //         };
    //       });
    //       if (first) {
    //         var lastBar = bars[bars.length - 1];
    //         history[symbolInfo.name] = { lastBar: lastBar };
    //       }
    //       return bars;
    //     } else {
    //       return [];
    //     }
    //   });
    return rp({
      url: `http://localhost:8000/api/TVData/${qs.limits}/${qs.url}/${qs.todate}/${qs.typeof}`
    }).then(data => {
      if (data.Response && data.Response === "Error") {
        return [];
      }
      if (data.length) {
        var bars = data.map(el => {
          return {
            time: el.utc * 1000, //TradingView requires bar time in ms
            low: el.low,
            high: el.high,
            open: el.first,
            close: el.close,
            volume: el.tradevol
          };
        });
        if (first) {
          var lastBar = bars[bars.length - 1];
          history[symbolInfo.name] = { lastBar: lastBar };
        }
        return bars;
      } else {
        return [];
      }
    });
  }
};
