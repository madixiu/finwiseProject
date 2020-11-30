<template>
  <ul class="menu-nav">
    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Market')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-coins"></i>
        <span class="menu-text">بازار</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            to="/StockMarket/Market/Dashboard"
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
                <span class="menu-text">صفحه اول</span>
              </a>
            </li>
          </router-link>
          <router-link
            to="/StockMarket/Market/MarketWatch"
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
                <span class="menu-text">دیدبان</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>
    <router-link
      to="/StockMarket/Industries"
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
          <span class="menu-text">صنایع</span>
        </a>
      </li>
    </router-link>
    <router-link
      to="/StockMarket/Screener"
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
          <i class="menu-icon flaticon-map"></i>
          <span class="menu-text">غربالگر</span>
        </a>
      </li>
    </router-link>
    <router-link
      to="/StockMarket/Fundamental"
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
          <i class="menu-icon flaticon-line-graph"></i>
          <span class="menu-text">بنیادی</span>
        </a>
      </li>
    </router-link>

    <li class="menu-section">
      <h4 class="menu-text">سایر</h4>
      <i class="menu-icon flaticon-more-v2"></i>
    </li>

    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Technical')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-diagram"></i>
        <span class="menu-text">تکنیکال</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            to="/StockMarket/Technical/Dashboard"
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
                <span class="menu-text">قیمت طلا</span>
              </a>
            </li>
          </router-link>
          <router-link
            to="/StockMarket/Technical/Tools"
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
                <span class="menu-text">ابزار</span>
              </a>
            </li>
          </router-link>
          <router-link
            to="/StockMarket/Technical/Data"
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
                <span class="menu-text">دیتا</span>
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
        'menu-item-active': hasActiveChildren('/Assembly')
      }"
    >
      <a href="#" class="menu-link menu-toggle">
        <i class="menu-icon flaticon-clock-2"></i>
        <span class="menu-text">مجامع</span>
        <i class="menu-arrow"></i>
      </a>
      <div class="menu-submenu menu-submenu-classic menu-submenu-right">
        <ul class="menu-subnav">
          <router-link
            to="/StockMarket/Assembly/Calendar"
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
                <span class="menu-text">تقویم</span>
              </a>
            </li>
          </router-link>
          <router-link
            to="/StockMarket/Assembly/IncreaseCapitals"
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
                <span class="menu-text">افزایش سرمایه ها</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
    </li>
    <router-link
      to="/StockMarket/Taghadom"
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
          <i class="menu-icon flaticon-notes"></i>
          <span class="menu-text">حق تقدم</span>
        </a>
      </li>
    </router-link>
    <router-link
      to="/StockMarket/Option"
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
          <i class="menu-icon flaticon-clipboard"></i>
          <span class="menu-text">آپشن</span>
        </a>
      </li>
    </router-link>
    <router-link
    to="/StockMarket/Funds"
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
          <i class="menu-icon flaticon2-box-1"></i>
          <span class="menu-text">صندوق</span>
        </a>
      </li>
    </router-link>
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
