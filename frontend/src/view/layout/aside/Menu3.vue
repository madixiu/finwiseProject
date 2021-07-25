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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">تغییر وضعیت</span>
              </a>
            </li>
          </router-link>
          <!-- <router-link
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">حقیقی - حقوقی</span>
              </a>
            </li>
          </router-link> -->
          <router-link
            :to="`/ticker/Overview/Board/${$route.params.id}/`"
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">هیئت مدیره</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/Overview/shareholders/${$route.params.id}/`"
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">سهامداران</span>
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
          <i class="menu-icon flaticon2-list"></i>
          <span class="menu-text">سابقه-قیمت تعدیلی</span>
        </a>
      </li>
    </router-link>

    <!-- <router-link
      :to="`/ticker/TickerFundamental/${$route.params.id}/`"
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
          <i class="menu-icon flaticon2-line-chart"></i>
          <span class="menu-text">بنیادی</span>
        </a>
      </li>
    </router-link> -->

    <!-- <router-link
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
          <i class="menu-icon flaticon-analytics"></i>
          <span class="menu-text">تکنیکال</span>
        </a>
      </li>
    </router-link> -->

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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">بررسی اندیکاتور ها</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="`/ticker/TickerTechnicalTrend/${$route.params.id}/`"
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">بررسی حمایت و مقاومت</span>
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
        <i class="menu-icon flaticon2-website"></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
        <i class="menu-icon flaticon2-website"></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">صورت جریان نقدی</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>

    <!-- <router-link
      :to="`/ticker/sahmrobot/${$route.params.id}/`"
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
          <i class="menu-icon flaticon2-user-1"></i>
          <span class="menu-text">ربات</span>
        </a>
      </li> 
    </router-link 
    >‍-->
    <!-- <router-link
      :to="`/ticker/TickerRatio/${$route.params.id}/`"
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
          <i class="menu-icon flaticon2-console"></i>
          <span class="menu-text">نسبت ها</span>
        </a>
      </li> </router-link
    >‍ -->
    <!-- <router-link
      :to="`/ticker/TickerIndustry/${$route.params.id}/`"
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
          <i class="menu-icon flaticon2-gear"></i>
          <span class="menu-text">در صنعت</span>
        </a>
      </li> 
    </router-link>‍ -->
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
          <!-- <router-link
            :to="`/ticker/TickerAssembly/Calendar/${$route.params.id}/`"
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">تقویم مجامع</span>
              </a>
            </li>
          </router-link> -->
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">سود نقدی و افزایش سرمایه</span>
              </a>
            </li>
          </router-link>
          <!-- <router-link
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
                <i class="menu-bullet menu-bullet-dot"><span></span></i>
                <span class="menu-text">افزایش سرمایه</span>
              </a>
            </li>
          </router-link> -->
        </ul>
      </div>
    </li>
    <!-- <router-link
      :to="`/ticker/subset/${$route.params.id}/`"
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
          <i class="menu-icon flaticon2-chart"></i>
          <span class="menu-text">سرمایه پذیر</span>
        </a>
      </li> 
    </router-link 
    >‍-->
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
