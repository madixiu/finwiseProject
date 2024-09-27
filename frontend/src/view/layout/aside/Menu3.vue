<template>
  <ul class="menu-nav">
    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Overview')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon2-website"></i>
        <span class="menu-text">اطلاعات سهم</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            :to="`/ticker/Overview/Overall/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">خلاصه سهم</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Overview/Administration/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">پیام ناظر</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Overview/Notifications/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">اطلاعیه</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Overview/StatusChange/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">تغییر وضعیت</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Overview/HH/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">حقیقی - حقوقی</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>

    <router-link
      :to="`/ticker/AdjustedPrices/${$route.params.id}/`"
      v-slot="{ href, navigate, isActive, isExactActive }"
    >
      <li
        aria-haspopup="true"
        data-menu-toggle="hover"
        class="menu-item"
        :class="[
          isActive && 'menu-item-active',
          isExactActive && 'menu-item-active'
        ]"
      >
        <a :href="href" class="menu-link" @click="navigate">
          <i class="menu-icon flaticon-list-3"></i>
          <span class="menu-text">سابقه-قیمت تعدیلی</span>
        </a>
      </li>
    </router-link>

    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Technical')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-analytics"></i>
        <span class="menu-text">تکنیکال سهم</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            :to="`/ticker/TickerTechnical/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">نمودار پیشرفته</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/TechnicalDetailed/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">بررسی اندیکاتور ها</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`#`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">بررسی حمایت و مقاومت</span>
                <v-icon size="15px" color="#4682B4">mdi-lock-outline</v-icon>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>

    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Monthly')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-event-calendar-symbol"></i>
        <span class="menu-text">ماهیانه</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            :to="`/ticker/MonthlyAnalysis/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">تحلیل ماهیانه</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Monthly/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">گزارشات خام ماهیانه</span>
              </a>
            </li> </router-link
          >‍
        </ul>
      </div>
    </li>
    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Sheets')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-doc"></i>
        <span class="menu-text">صورت ها</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            :to="`/ticker/StatementAnalysis/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">تحلیل ترازنامه </span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Sheets/BalanceSheet/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">ترازنامه</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/IncomeStatementAnalysis/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">تحلیل صورت سود و زیان </span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Sheets/IncomeStatement/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">صورت سود و زیان</span>
              </a>
            </li>
          </router-link>

          <router-link
            :to="`/ticker/Sheets/CashFlow/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">صورت جریان نقدی</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>
    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/TickerAssembly')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon2-group"></i>
        <span class="menu-text">مجامع</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            :to="`/ticker/TickerAssembly/Report/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">گزارش جلسات</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/TickerAssembly/DPSAndIC/${$route.params.id}/`"
            v-slot="{ href, navigate, isActive, isExactActive }"
          >
            <li
              aria-haspopup="true"
              data-menu-toggle="hover"
              class="menu-item"
              :class="[
                isActive && 'menu-item-active',
                isExactActive && 'menu-item-active'
              ]"
            >
              <a :href="href" class="menu-link" @click="navigate">
                <i class="menu-bullet menu-bullet-dot"></i>
                <span class="menu-text">سود نقدی و افزایش سرمایه</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "KTMenu",
  methods: {
    hasActiveChildren(match) {
      return this.$route["path"].indexOf(match) !== -1;
    }
  }
};
</script>
