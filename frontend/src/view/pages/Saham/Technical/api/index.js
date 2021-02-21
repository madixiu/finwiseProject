/* eslint-disable no-unused-vars */
import historyProvider from "./historyProvider";
import stream from "./stream";
import { data } from "./pairs";

// const supportedResolutions = ["1", "3", "5", "15", "30", "60", "120", "240", "D", "W","M","3M","12M"]
const supportedResolutions = ["D", "W", "M", "3M", "12M"];

const config = {
  supported_resolutions: supportedResolutions,
  supports_marks: true
};

export default {
  onReady: cb => {
    // console.log('=====onReady running')
    setTimeout(() => cb(config), 0);
  },
  searchSymbols: (userInput, exchange, symbolType, onResultReadyCallback) => {
    if (userInput.length >= 1) {
      let searched = data.filter(function(v) {
        return v.symbol.includes(userInput);
      });
      // let searched =  data.filter(x => {
      //   return x.symbol.includes(userInput)
      //  })
      onResultReadyCallback(searched);
    } else {
      onResultReadyCallback(data);
    }
    for (var i = 0; i < data.length; ++i) {
      // if (!data[i].params) {
      //   data[i].params = [];
      // }
    }
    // onResultReadyCallback([data[0],data[1]]);
    // if (typeof data.s == 'undefined' || data.s != 'error') {
    //   onResultReadyCallback(data);
    // } else {
    //   onResultReadyCallback([]);
    // }
  },
  resolveSymbol: (
    symbolName,
    onSymbolResolvedCallback,
    onResolveErrorCallback
  ) => {
    // console.log(onSymbolResolvedCallback);
    // expects a symbolInfo object in response
    // console.log('======resolveSymbol running')
    // console.log('resolveSymbol:',{symbolName})
    // var split_data = symbolName.split(/[:/]/)
    // console.log({split_data})
    var symbol_stub = {
      name: symbolName,
      description: "",
      type: data[0].type,
      session: "24x7",
      timezone: "Asia/Tehran",
      ticker: symbolName,
      minmov: 1,
      pricescale: 1,
      has_intraday: true,
      intraday_multipliers: ["1", "60"],
      supported_resolution: supportedResolutions,
      volume_precision: 8,
      data_status: "streaming",
      // urlparam:data[0].urlparam
      urlparam: data.filter(x => {
        return x.symbol == symbolName;
      })[0].urlparam

      // haracters.filter(character => {
      //   return character.series.includes('Star Trek: The Next Generation');
      // });
    };

    // if (split_data[1].match(/USD|EUR|JPY|AUD|GBP|KRW|CNY/)) {
    //   symbol_stub.pricescale = 100
    // }
    setTimeout(function() {
      onSymbolResolvedCallback(symbol_stub);
      console.log("Resolving that symbol....", symbol_stub);
    }, 0);

    // onResolveErrorCallback('Not feeling it today')
  },
  getBars: function(
    symbolInfo,
    resolution,
    from,
    to,
    onHistoryCallback,
    onErrorCallback,
    firstDataRequest
  ) {
    // console.log('=====getBars running')
    // console.log('function args',arguments)
    // console.log(`Requesting bars between ${new Date(from * 1000).toISOString()} and ${new Date(to * 1000).toISOString()}`)
    historyProvider
      .getBars(symbolInfo, resolution, from, to, firstDataRequest)
      .then(bars => {
        if (bars.length) {
          console.log(to);
          onHistoryCallback(bars, { noData: false });
        } else {
          onHistoryCallback(bars, { noData: true });
        }
      })
      .catch(err => {
        // console.log({err})
        onErrorCallback(err);
      });
  },
  subscribeBars: (
    symbolInfo,
    resolution,
    onRealtimeCallback,
    subscribeUID,
    onResetCacheNeededCallback
  ) => {
    // console.log('=====subscribeBars runnning')
    stream.subscribeBars(
      symbolInfo,
      resolution,
      onRealtimeCallback,
      subscribeUID,
      onResetCacheNeededCallback
    );
  },
  unsubscribeBars: subscriberUID => {
    // console.log('=====unsubscribeBars running')

    stream.unsubscribeBars(subscriberUID);
  },
  calculateHistoryDepth: (resolution, resolutionBack, intervalBack) => {
    //optional
    // console.log('=====calculateHistoryDepth running')
    // while optional, this makes sure we request 24 hours of minute data at a time
    // CryptoCompare's minute data endpoint will throw an error if we request data beyond 7 days in the past, and return no data
    return resolution < 60
      ? { resolutionBack: "D", intervalBack: "1" }
      : undefined;
  },
  getMarks: function(symbolInfo, from, to, onDataCallback, resolution) {
    let result = historyProvider.getMarks(
      symbolInfo,
      from,
      to,
      onDataCallback,
      resolution
    );
    if (result.length) {
      onDataCallback(result);
      // onDataCallback(result)
    }
    // .then(result => {

    // }).catch(err => {
    //   console.log({err})
    //   // onErrorCallback(err)
    // })

    //optional
    // console.log('=====getMarks running')
  },
  getTimeScaleMarks: (
    symbolInfo,
    startDate,
    endDate,
    onDataCallback,
    resolution
  ) => {
    //optional
    // console.log('=====getTimeScaleMarks running')
  },
  getServerTime: cb => {
    // console.log('=====getServerTime running')
  }
};
