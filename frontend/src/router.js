import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/saham",
      component: () => import("@/view/layout/Layout"),
      children: [
        {
          path: "/saham",
          name: "saham",
          redirect: "/saham/market/dashboard",
          component: () => import("@/view/pages/Saham.vue"),
          children: [
            {
              path: "market/dashboard",
              name: "dashboard",
              component: () => import("@/view/pages/Dashboard.vue")
            },
            {
              path: "market/marketwatch",
              name: "marketwatch",
              component: () => import("@/view/pages/MarketWatch.vue")
            },
            {
              path: "industries",
              name: "industries",
              component: () => import("@/view/pages/Saham/Industries.vue")
            },
            {
              path: "qarbal",
              name: "qarbal",
              component: () => import("@/view/pages/Saham/Qarbal.vue")
            },
            {
              path: "bonyad",
              name: "bonyad",
              component: () => import("@/view/pages/Saham/Bonyad.vue")
            },
            {
              path: "technical/goldprice",
              name: "goldprice",
              component: () =>
                import("@/view/pages/Saham/Technical/GoldPrice.vue")
            },
            {
              path: "technical/tools",
              name: "tools",
              component: () => import("@/view/pages/Saham/Technical/Tools.vue")
            },
            {
              path: "technical/data",
              name: "data",
              component: () => import("@/view/pages/Saham/Technical/Data.vue")
            },
            {
              path: "majame/calendar",
              name: "calendar",
              component: () => import("@/view/pages/Saham/Majame/Calendar.vue")
            },
            {
              path: "majame/afzayesh",
              name: "afzayesh",
              component: () => import("@/view/pages/Saham/Majame/Afzayesh.vue")
            },
            {
              path: "taqadom",
              name: "taqadom",
              component: () => import("@/view/pages/Saham/Taqadom.vue")
            },
            {
              path: "option",
              name: "option",
              component: () => import("@/view/pages/Saham/Option.vue")
            },
            {
              path: "sandoq",
              name: "sandoq",
              component: () => import("@/view/pages/Saham/Sandoq.vue")
            }
          ]
        },
        {
          path: "/kala",
          name: "kala",
          redirect: "/kala/bourse",
          component: () => import("@/view/pages/Kala/Kala.vue"),
          children: [
            {
              path: "bourse",
              name: "bourse",
              component: () => import("@/view/pages/Kala/Bourse.vue")
            },
            {
              path: "global",
              name: "global",
              component: () => import("@/view/pages/Kala/Global.vue")
            }
          ]
        },
        {
          path: "/builder",
          name: "builder",
          component: () => import("@/view/pages/Builder.vue")
        },
        {
          path: "/marketmap",
          name: "marketmap",
          component: () => import("@/view/pages/MarketMap/MarketMap.vue")
        },
        {
          path: "/oraq",
          name: "oraq",
          component: () => import("@/view/pages/Oraq/Oraq.vue")
        },
        {
          path: "/shakhes",
          name: "shakhes",
          component: () => import("@/view/pages/Shakhes/Shakhes.vue")
        },
        //added route for ticker!
        {
          path: "/ticker",
          name: "ticker",
          redirect: "/ticker/kholaseSahm/nazer",
          component: () => import("@/view/pages/Ticker/Ticker.vue"),
          children: [
            {
              path: "kholaseSahm/nazer",
              name: "nazer",
              component: () => import("@/view/pages/Ticker/Nazer.vue")
            },
            {
              path: "kholaseSahm/information",
              name: "information",
              component: () => import("@/view/pages/Ticker/Information.vue")
            },
            {
              path: "kholaseSahm/vaziat",
              name: "vaziat",
              component: () => import("@/view/pages/Ticker/Vaziat.vue")
            },
            {
              path: "kholaseSahm/haghighi&hoghughi",
              name: "haghighi&hoghughi",
              component: () =>
                import("@/view/pages/Ticker/Haghighi&Hoghughi.vue")
            },
            {
              path: "kholaseSahm/managers",
              name: "managers",
              component: () => import("@/view/pages/Ticker/Managers.vue")
            },
            {
              path: "kholaseSahm/shareholders",
              name: "shareholders",
              component: () => import("@/view/pages/Ticker/ShareHolders.vue")
            },
            {
              path: "tadili",
              name: "tadili",
              component: () => import("@/view/pages/Ticker/Tadili.vue")
            },
            {
              path: "bonyadi",
              name: "bonyadi",
              component: () => import("@/view/pages/Ticker/Bonyadi.vue")
            },
            {
              path: "sahmTechnical",
              name: "sahmTechnical",
              component: () => import("@/view/pages/Ticker/SahmTechnical.vue")
            },
            {
              path: "surats",
              name: "surats",
              component: () => import("@/view/pages/Ticker/Surats.vue")
            },
            {
              path: "monthly",
              name: "monthly",
              component: () => import("@/view/pages/Ticker/Monthly.vue")
            },
            {
              path: "sahmRobot",
              name: "sahmRobot",
              component: () => import("@/view/pages/Ticker/SahmRobot.vue")
            },
            {
              path: "relations",
              name: "relations",
              component: () => import("@/view/pages/Ticker/Relations.vue")
            },
            {
              path: "industry",
              name: "industry",
              component: () => import("@/view/pages/Ticker/Industry.vue")
            },
            {
              path: "sahmMajame",
              name: "sahmMajame",
              component: () => import("@/view/pages/Ticker/SahmMajame.vue")
            },
            {
              path: "sarmaye",
              name: "sarmaye",
              component: () => import("@/view/pages/Ticker/Sarmaye.vue")
            }
          ]
        },
        // added route for robot!
        {
          path: "/robot",
          name: "robot",
          component: () => import("@/view/pages/Robot/Robot.vue")
        },
        {
          path: "/vue-bootstrap",
          name: "vue-bootstrap",
          component: () =>
            import("@/view/pages/vue-bootstrap/VueBootstrap.vue"),
          children: [
            {
              path: "alert",
              name: "vue-bootstrap-alert",
              component: () => import("@/view/pages/vue-bootstrap/Alert.vue")
            },
            {
              path: "badge",
              name: "vue-bootstrap-badge",
              component: () => import("@/view/pages/vue-bootstrap/Badge.vue")
            },
            {
              path: "button",
              name: "vue-bootstrap-button",
              component: () => import("@/view/pages/vue-bootstrap/Button.vue")
            },
            {
              path: "button-group",
              name: "vue-bootstrap-button-group",
              component: () =>
                import("@/view/pages/vue-bootstrap/ButtonGroup.vue")
            },
            {
              path: "button-toolbar",
              name: "vue-bootstrap-button-toolbar",
              component: () =>
                import("@/view/pages/vue-bootstrap/ButtonToolbar.vue")
            },
            {
              path: "card",
              name: "vue-bootstrap-card",
              component: () => import("@/view/pages/vue-bootstrap/Card.vue")
            },
            {
              path: "carousel",
              name: "vue-bootstrap-carousel",
              component: () => import("@/view/pages/vue-bootstrap/Carousel.vue")
            },
            {
              path: "collapse",
              name: "vue-bootstrap-collapse",
              component: () => import("@/view/pages/vue-bootstrap/Collapse.vue")
            },
            {
              path: "dropdown",
              name: "vue-bootstrap-dropdown",
              component: () => import("@/view/pages/vue-bootstrap/Dropdown.vue")
            },
            {
              path: "embed",
              name: "vue-bootstrap-embed",
              component: () => import("@/view/pages/vue-bootstrap/Embed.vue")
            },
            {
              path: "form",
              name: "vue-bootstrap-form",
              component: () => import("@/view/pages/vue-bootstrap/Form.vue")
            },
            {
              path: "form-checkbox",
              name: "vue-bootstrap-form-checkbox",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormCheckbox.vue")
            },
            {
              path: "form-file",
              name: "vue-bootstrap-form-file",
              component: () => import("@/view/pages/vue-bootstrap/FormFile.vue")
            },
            {
              path: "form-group",
              name: "vue-bootstrap-form-group",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormGroup.vue")
            },
            {
              path: "form-input",
              name: "vue-bootstrap-form-input",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormInput.vue")
            },
            {
              path: "form-radio",
              name: "vue-bootstrap-form-radio",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormRadio.vue")
            },
            {
              path: "form-select",
              name: "vue-bootstrap-form-select",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormSelect.vue")
            },
            {
              path: "form-textarea",
              name: "vue-bootstrap-form-textarea",
              component: () =>
                import("@/view/pages/vue-bootstrap/FormTextarea.vue")
            },
            {
              path: "image",
              name: "vue-bootstrap-image",
              component: () => import("@/view/pages/vue-bootstrap/Image.vue")
            },
            {
              path: "input-group",
              name: "vue-bootstrap-input-group",
              component: () =>
                import("@/view/pages/vue-bootstrap/InputGroup.vue")
            },
            {
              path: "jumbotron",
              name: "vue-bootstrap-jumbotron",
              component: () =>
                import("@/view/pages/vue-bootstrap/Jumbotron.vue")
            },
            {
              path: "layout-grid-system",
              name: "vue-bootstrap-layout-grid-system",
              component: () =>
                import("@/view/pages/vue-bootstrap/LayoutGridSystem.vue")
            },
            {
              path: "link",
              name: "vue-bootstrap-link",
              component: () => import("@/view/pages/vue-bootstrap/Link.vue")
            },
            {
              path: "list-group",
              name: "vue-bootstrap-list-group",
              component: () =>
                import("@/view/pages/vue-bootstrap/ListGroup.vue")
            },
            {
              path: "media",
              name: "vue-bootstrap-media",
              component: () => import("@/view/pages/vue-bootstrap/Media.vue")
            },
            {
              path: "modal",
              name: "vue-bootstrap-modal",
              component: () => import("@/view/pages/vue-bootstrap/Modal.vue")
            },
            {
              path: "nav",
              name: "vue-bootstrap-nav",
              component: () => import("@/view/pages/vue-bootstrap/Nav.vue")
            },
            {
              path: "navbar",
              name: "vue-bootstrap-navbar",
              component: () => import("@/view/pages/vue-bootstrap/Navbar.vue")
            },
            {
              path: "pagination",
              name: "vue-bootstrap-pagination",
              component: () =>
                import("@/view/pages/vue-bootstrap/Pagination.vue")
            },
            {
              path: "pagination-nav",
              name: "vue-bootstrap-pagination-nav",
              component: () =>
                import("@/view/pages/vue-bootstrap/PaginationNav.vue")
            },
            {
              path: "popover",
              name: "vue-bootstrap-popover",
              component: () => import("@/view/pages/vue-bootstrap/Popover.vue")
            },
            {
              path: "progress",
              name: "vue-bootstrap-progress",
              component: () => import("@/view/pages/vue-bootstrap/Progress.vue")
            },
            {
              path: "spinner",
              name: "vue-bootstrap-spinner",
              component: () => import("@/view/pages/vue-bootstrap/Spinner.vue")
            },
            {
              path: "table",
              name: "vue-bootstrap-table",
              component: () => import("@/view/pages/vue-bootstrap/Table.vue")
            },
            {
              path: "tabs",
              name: "vue-bootstrap-tabs",
              component: () => import("@/view/pages/vue-bootstrap/Tabs.vue")
            },
            {
              path: "toasts",
              name: "vue-bootstrap-toasts",
              component: () => import("@/view/pages/vue-bootstrap/Toasts.vue")
            },
            {
              path: "tooltip",
              name: "vue-bootstrap-tooltip",
              component: () => import("@/view/pages/vue-bootstrap/Tooltip.vue")
            }
          ]
        },
        {
          path: "/vuetify",
          name: "vuetify",
          component: () => import("@/view/pages/vuetify/Vuetify.vue"),
          children: [
            {
              path: "alerts",
              name: "vuetify-alerts",
              component: () => import("@/view/pages/vuetify/Alerts.vue")
            },
            {
              path: "avatars",
              name: "vuetify-avatars",
              component: () => import("@/view/pages/vuetify/Avatars.vue")
            },
            {
              path: "badges",
              name: "vuetify-badges",
              component: () => import("@/view/pages/vuetify/Badges.vue")
            },
            {
              path: "buttons",
              name: "vuetify-buttons",
              component: () => import("@/view/pages/vuetify/Buttons.vue")
            },
            {
              path: "calendars",
              name: "vuetify-calendars",
              component: () => import("@/view/pages/vuetify/Calendars.vue")
            },
            {
              path: "cards",
              name: "vuetify-cards",
              component: () => import("@/view/pages/vuetify/Cards.vue")
            },
            {
              path: "chips",
              name: "vuetify-chips",
              component: () => import("@/view/pages/vuetify/Chips.vue")
            },
            {
              path: "dialog",
              name: "vuetify-dialog",
              component: () => import("@/view/pages/vuetify/Dialog.vue")
            },
            {
              path: "autocompletes",
              name: "vuetify-autocompletes",
              component: () =>
                import("@/view/pages/vuetify/forms/Autocompletes.vue")
            },
            {
              path: "file-inputs",
              name: "vuetify-file-inputs",
              component: () =>
                import("@/view/pages/vuetify/forms/FileInputs.vue")
            },
            {
              path: "forms",
              name: "vuetify-forms",
              component: () => import("@/view/pages/vuetify/forms/Forms.vue")
            },
            {
              path: "selection-controls",
              name: "vuetify-selection-controls",
              component: () =>
                import("@/view/pages/vuetify/forms/SelectionControls.vue")
            },
            {
              path: "selects",
              name: "vuetify-selects",
              component: () => import("@/view/pages/vuetify/forms/Selects.vue")
            },
            {
              path: "textareas",
              name: "vuetify-textareas",
              component: () =>
                import("@/view/pages/vuetify/forms/Textareas.vue")
            },
            {
              path: "text-fields",
              name: "vuetify-text-fields",
              component: () =>
                import("@/view/pages/vuetify/forms/TextFields.vue")
            },
            {
              path: "simple-tables",
              name: "vuetify-simple-tables",
              component: () =>
                import("@/view/pages/vuetify/tables/SimpleTables.vue")
            },
            {
              path: "data-tables",
              name: "vuetify-data-tables",
              component: () =>
                import("@/view/pages/vuetify/tables/DataTables.vue")
            },
            {
              path: "tabs",
              name: "vuetify-tabs",
              component: () => import("@/view/pages/vuetify/Tabs.vue")
            },
            {
              path: "timelines",
              name: "vuetify-timelines",
              component: () => import("@/view/pages/vuetify/Timelines.vue")
            },
            {
              path: "tooltips",
              name: "vuetify-tooltips",
              component: () => import("@/view/pages/vuetify/Tooltips.vue")
            },
            {
              path: "treeview",
              name: "vuetify-treeview",
              component: () => import("@/view/pages/vuetify/Treeview.vue")
            }
          ]
        },
        {
          path: "/wizard",
          name: "wizard",
          component: () => import("@/view/pages/wizard/Wizard.vue"),
          children: [
            {
              path: "wizard-1",
              name: "wizard-1",
              component: () => import("@/view/pages/wizard/Wizard-1.vue")
            },
            {
              path: "wizard-2",
              name: "wizard-2",
              component: () => import("@/view/pages/wizard/Wizard-2.vue")
            },
            {
              path: "wizard-3",
              name: "wizard-3",
              component: () => import("@/view/pages/wizard/Wizard-3.vue")
            },
            {
              path: "wizard-4",
              name: "wizard-4",
              component: () => import("@/view/pages/wizard/Wizard-4.vue")
            }
          ]
        },
        {
          path: "/plugins",
          name: "plugins",
          component: () => import("@/view/pages/plugins/Plugins.vue"),
          children: [
            {
              path: "cropper",
              name: "cropper",
              component: () => import("@/view/pages/plugins/Cropper.vue")
            }
          ]
        }
      ]
    },
    {
      path: "/error",
      name: "error",
      component: () => import("@/view/pages/error/Error.vue"),
      children: [
        {
          path: "error-1",
          name: "error-1",
          component: () => import("@/view/pages/error/Error-1.vue")
        },
        {
          path: "error-2",
          name: "error-2",
          component: () => import("@/view/pages/error/Error-2.vue")
        },
        {
          path: "error-3",
          name: "error-3",
          component: () => import("@/view/pages/error/Error-3.vue")
        },
        {
          path: "error-4",
          name: "error-4",
          component: () => import("@/view/pages/error/Error-4.vue")
        },
        {
          path: "error-5",
          name: "error-5",
          component: () => import("@/view/pages/error/Error-5.vue")
        },
        {
          path: "error-6",
          name: "error-6",
          component: () => import("@/view/pages/error/Error-6.vue")
        }
      ]
    },
    {
      path: "/",
      component: () => import("@/view/pages/auth/Auth"),
      children: [
        {
          name: "login",
          path: "/login",
          component: () => import("@/view/pages/auth/Login")
        },
        {
          name: "register",
          path: "/register",
          component: () => import("@/view/pages/auth/Register")
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
      component: () => import("@/view/pages/error/Error-1.vue")
    }
  ]
});
