/* eslint-disable no-unused-vars */
// import pairs from './pairs'
var rp = require("request-promise").defaults({ json: true });
// const api_root = 'https://min-api.cryptocompare.com'
const history = {};

export default {
  history: history,

  getMarks: function(symbolInfo, from, to, onDataCallback, resolution) {
    // if (localStorage.bnApiStatus.toString() == "true") {
    // let symbol = symbolInfo.name;
    // console.log(symbolInfo.name);
    console.log(symbolInfo);

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
    console.log(symbolInfo);
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
      limit: 2000,
      urlParameter: "eq." + symbolInfo.urlparam,
      utc: to ? "lte." + to : "lte." + ""
      // order:'utc.desc'
    };

    console.log({ qs });
    return rp({
      //   url: `${api_root}${url}`,
      url: `http://37.152.180.99:3000/View_TV_Daily?`,
      qs
    }).then(data => {
      console.log(data);

      // console.log({data})
      if (data.Response && data.Response === "Error") {
        // console.log('CryptoCompare API error:',data.Message)
        return [];
      }
      if (data.length) {
        console.log(data);
        // console.log(qs);
        // console.log(`Actually returned: ${new Date(data.TimeFrom * 1000).toISOString()} - ${new Date(data.TimeTo * 1000).toISOString()}`)
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
          console.log(lastBar);
          history[symbolInfo.name] = { lastBar: lastBar };
        }
        return bars;
      } else {
        return [];
      }
    });
  }
};
