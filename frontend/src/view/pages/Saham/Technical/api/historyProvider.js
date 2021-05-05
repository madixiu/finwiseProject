/* eslint-disable no-unused-vars */
// import pairs from './pairs'
var rp = require("request-promise").defaults({ json: true });
const axios = require("axios");
// const api_root = 'https://min-api.cryptocompare.com'
const history = {};

export default {
  history: history,

  getMarks: function(symbolInfo, from, to, onDataCallback, resolution) {
    // if (localStorage.bnApiStatus.toString() == "true") {
    // let symbol = symbolInfo.name;

    var result = [];
    var el = {
      id: "Dividend-13800430",
      color: "green",
      time: 1610892000,
      text: "abc",
      label: "label",
      labelFontColor: "#fff",
      minSize: 8
    };
    result.push(el);
    onDataCallback(result);
    return result;
  },
  getBars: function(symbolInfo, resolution, from, to, first, limit) {
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
      todate: to ? "" + to : ""
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
      //   url: `${api_root}${url}`,
      // url: `http://185.231.115.223:3000/View_TV_Daily?`,
      // url: `http://185.231.115.223:3000/rpc/ViewTVDaily?`,
      url: `http://localhost:8000/api/TVData/${qs.limits}/${qs.url}/${qs.todate}`
      // qs
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
