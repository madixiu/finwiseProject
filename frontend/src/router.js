import Vue from "vue";
import Router from "vue-router";

const Layout = () => import("@/view/layout/Layout");
const StockMarketParent = () =>
  import("@/view/pages/StockMarket/StockMarketParent.vue");
// const Dashboard = () => import("@/view/pages/StockMarket/Dashboard.vue");
const DashboardNew = () => import("@/view/pages/StockMarket/DashboardNew.vue");
const Industries = () =>
  import("@/view/pages/StockMarket/Industries/Industries.vue");
const IndustriesDetail = () =>
  import("@/view/pages/StockMarket/Industries/IndustriesDetail.vue");
const Qarbal = () => import("@/view/pages/Saham/Qarbal.vue");
const Bonyad = () => import("@/view/pages/Saham/Bonyad.vue");
const GoldPrice = () => import("@/view/pages/Saham/Technical/GoldPrice.vue");
const Tools = () => import("@/view/pages/Saham/Technical/Tools.vue");
const Data = () => import("@/view/pages/Saham/Technical/TradingView.vue");
const Calendar = () => import("@/view/pages/Saham/Majame/Calendar.vue");
const Decisions = () => import("@/view/pages/Saham/Majame/Decisions.vue");
const Increase = () => import("@/view/pages/Saham/Majame/Increase.vue");
const Taqadom = () => import("@/view/pages/Saham/Taqadom.vue");
const Option = () => import("@/view/pages/Saham/Option.vue");
const Sandoq = () => import("@/view/pages/Fund/Sandoq.vue");
const Kala = () => import("@/view/pages/Kala/Kala.vue");
const Bourse = () => import("@/view/pages/Kala/Bourse.vue");
const Global = () => import("@/view/pages/Kala/Global.vue");
const MarketMap = () => import("@/view/pages/MarketMap/MarketMap.vue");
const MarketWatch = () => import("@/view/pages/MarketWatch.vue");
const Oraq = () => import("@/view/pages/Oraq/Oraq.vue");
const Shakhes = () => import("@/view/pages/Shakhes/Shakhes.vue");
const Ticker = () => import("@/view/pages/Ticker/Ticker.vue");
const Overview = () => import("@/view/pages/Ticker/Overview.vue");
const AdminNotice = () => import("@/view/pages/Ticker/Administration.vue");
const CodalNotifications = () =>
  import("@/view/pages/Ticker/CodalNotifications.vue");
const StatusChange = () => import("@/view/pages/Ticker/StatusChange.vue");
const HH = () => import("@/view/pages/Ticker/HH.vue");
const Board = () => import("@/view/pages/Ticker/Board.vue");
const ShareHolders = () => import("@/view/pages/Ticker/ShareHolders.vue");
const AdjustedPrices = () => import("@/view/pages/Ticker/AdjustedPrices.vue");
const Bonyadi = () => import("@/view/pages/Ticker/Bonyadi.vue");
const TickerTechnical = () => import("@/view/pages/Ticker/TickerTechnical.vue");
const BalanceSheet = () =>
  import("@/view/pages/Ticker/Sheets/BalanceSheet.vue");
const IncomeStatement = () =>
  import("@/view/pages/Ticker/Sheets/IncomeStatement.vue");
const CashFlow = () => import("@/view/pages/Ticker/Sheets/CashFlow.vue");

const Monthly = () => import("@/view/pages/Ticker/Monthly.vue");
const SahmRobot = () => import("@/view/pages/Ticker/SahmRobot.vue");
const Relations = () => import("@/view/pages/Ticker/Relations.vue");
const Industry = () => import("@/view/pages/Ticker/Industry.vue");
const AssemblyCalendar = () =>
  import("@/view/pages/Ticker/AssemblyWidget/AssemblyCalendar.vue");
const AssemblyAll = () =>
  import("@/view/pages/Ticker/AssemblyWidget/AssemblyAll.vue");
const AssemblyDPS = () =>
  import("@/view/pages/Ticker/AssemblyWidget/AssemblyDPS.vue");
const Subset = () => import("@/view/pages/Ticker/Subset.vue");
const Robot = () => import("@/view/pages/Robot/Robot.vue");
const Login = () => import("@/view/pages/auth/Login");
const Register = () => import("@/view/pages/auth/Register");
const Verify = () => import("@/view/pages/auth/Verify");
const ERROR = () => import("@/view/pages/error/Error-1.vue");

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/StockMarket",
      component: Layout,
      // meta: {
      //   reload: true
      // },
      children: [
        {
          path: "/StockMarket",
          name: "StockMarket",
          redirect: "/StockMarket/Dashboard/",
          component: StockMarketParent,
          children: [
            {
              path: "Dashboard",
              name: "Dashboard",
              component: DashboardNew
            },
            // {
            //   path: "Market/MarketWatch",
            //   name: "marketwatch",
            //   component: () => import("@/view/pages/MarketWatch.vue")
            // },
            {
              path: "Industries",
              name: "Industries",
              component: Industries
            },
            {
              path: "Industries/:id",
              name: "IndustriesDetail",
              component: IndustriesDetail
            },
            {
              path: "Screener",
              name: "Screener",
              component: Qarbal
            },
            {
              path: "Fundamental",
              name: "Fundamental",
              component: Bonyad
            },
            {
              path: "Technical/Dashboard",
              name: "TechnicalDashboard",
              component: GoldPrice
            },
            {
              path: "Techincal/Tools",
              name: "TechnicalTools",
              component: Tools
            },
            {
              path: "Technical/Data",
              name: "TechnicalData",
              component: Data
            },
            {
              path: "Assembly/Calendar",
              name: "AssemblyCalendar",
              component: Calendar
            },
            {
              path: "Assembly/Decisions",
              name: "AssemblyDecisions",
              component: Decisions
            },
            {
              path: "Assembly/IncreaseCapitals",
              name: "AssemblyIC",
              component: Increase
            },
            {
              path: "Taghadom",
              name: "Taghadom",
              component: Taqadom
            },
            {
              path: "Option",
              name: "Option",
              component: Option
            }
          ]
        },
        {
          path: "/kala",
          name: "kala",
          redirect: "/kala/bourse",
          component: Kala,
          children: [
            {
              path: "bourse",
              name: "bourse",
              component: Bourse
            },
            {
              path: "global",
              name: "global",
              component: Global
            }
          ]
        },
        {
          path: "Funds",
          name: "Funds",
          component: Sandoq
        },
        // {
        //   path: "/builder",
        //   name: "builder",
        //   component: () => import("@/view/pages/Builder.vue")
        // },
        {
          path: "/marketmap",
          name: "marketmap",
          component: MarketMap
        },
        {
          path: "/MarketWatch",
          name: "marketwatch",
          component: MarketWatch
        },
        {
          path: "/oraq",
          name: "oraq",
          component: Oraq
        },
        {
          path: "/shakhes",
          name: "shakhes",
          component: Shakhes
        },

        //added route for ticker!
        {
          path: "/ticker",
          name: "ticker",
          redirect: "/ticker/Overview/",
          component: Ticker,
          children: [
            {
              path: "Overview/Overall/:id",
              name: "TickerOverall",
              props: true,
              component: Overview
            },
            {
              path: "Overview/Administration/:id",
              name: "Administration",
              component: AdminNotice
            },
            {
              path: "Overview/Notifications/:id",
              name: "Notifications",
              component: CodalNotifications
            },
            {
              path: "Overview/StatusChange/:id",
              name: "StatusChange",
              component: StatusChange
            },
            {
              path: "Overview/HH/:id",
              name: "HH",
              component: HH
            },
            {
              path: "Overview/Board/:id",
              name: "Board",
              component: Board
            },
            {
              path: "Overview/shareholders/:id",
              name: "shareholders",
              component: ShareHolders
            },
            {
              path: "AdjustedPrices/:id",
              name: "AdjustedPrices",
              component: AdjustedPrices
            },
            {
              path: "TickerFundamental/:id",
              name: "TickerFundamental",
              component: Bonyadi
            },
            {
              path: "TickerTechnical/:id",
              name: "TickerTechnical",
              component: TickerTechnical
            },
            {
              path: "Sheets/BalanceSheet/:id",
              // name: "Sheets",
              name: "BalanceSheet",
              component: BalanceSheet
            },
            {
              path: "Sheets/IncomeStatement/:id",
              // name: "Sheets",
              name: "IncomeStatement",
              component: IncomeStatement
            },
            {
              path: "Sheets/CashFlow/:id",
              // name: "Sheets",
              name: "CashFlow",
              component: CashFlow
            },
            {
              path: "Monthly/:id",
              name: "Monthly",
              component: Monthly
            },
            {
              path: "sahmRobot/:id",
              name: "sahmRobot",
              component: SahmRobot
            },
            {
              path: "TickerRatio/:id",
              name: "TickerRatio",
              component: Relations
            },
            {
              path: "TickerIndustry/:id",
              name: "TickerIndustry",
              component: Industry
            },
            // {
            //   path: "TickerAssembly/TickerAssemblyCalendar:id",
            //   name: "TickerAssembly",
            //   // redirect: "/ticker/TickerAssembly/TickerAssemblyCalendar",
            //   component: SahmMajame () => import("@/view/pages/Ticker/SahmMajame.vue")
            // },
            {
              path: "TickerAssembly/Calendar/:id",
              name: "TickerAssemblyCalendar",
              component: AssemblyCalendar
            },
            {
              path: "TickerAssembly/Report/:id",
              name: "TickerAssemblyReport",
              component: AssemblyAll
            },
            {
              path: "TickerAssembly/DPSAndIC/:id",
              name: "TickerAssemblyDPSAndIC",
              component: AssemblyDPS
            },
            // {
            //   path: "TickerAssembly/IC/:id",
            //   name: "TickerAssemblyIC",
            //   component: AssemblyIncreaseCapital
            // },
            {
              path: "subset/:id",
              name: "subset",
              component: Subset
            }
          ]
        },
        // added route for robot!
        {
          path: "/robot",
          name: "robot",
          component: Robot
        }
      ]
    },
    // {
    //   path: "/error",
    //   name: "error",
    //   component: () => import("@/view/pages/error/Error.vue"),
    //   children: [
    //     {
    //       path: "error-1",
    //       name: "error-1",
    //       component: () => import("@/view/pages/error/Error-1.vue")
    //     },
    //     {
    //       path: "error-2",
    //       name: "error-2",
    //       component: () => import("@/view/pages/error/Error-2.vue")
    //     },
    //     {
    //       path: "error-3",
    //       name: "error-3",
    //       component: () => import("@/view/pages/error/Error-3.vue")
    //     },
    //     {
    //       path: "error-4",
    //       name: "error-4",
    //       component: () => import("@/view/pages/error/Error-4.vue")
    //     },
    //     {
    //       path: "error-5",
    //       name: "error-5",
    //       component: () => import("@/view/pages/error/Error-5.vue")
    //     },
    //     {
    //       path: "error-6",
    //       name: "error-6",
    //       component: () => import("@/view/pages/error/Error-6.vue")
    //     }
    //   ]
    // },
    {
      path: "/",
      component: () => import("@/view/pages/auth/Auth"),
      children: [
        {
          name: "login",
          path: "/login",
          component: Login
        },
        {
          name: "register",
          path: "/register",
          component: Register
        },
        {
          name: "verify",
          path: "/verify",
          component: Verify
        }
      ]
    },
    {
      path: "*",
      redirect: "/404"
    },
    {
      // the 404 route, when none of the above matches
      path: "/404",
      name: "404",
      component: ERROR
    }
  ]
});
