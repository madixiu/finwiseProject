<template>
  <ul class="menu-nav">
    <router-link
      to="/StockMarket/Dashboard"
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
          <i class="menu-icon flaticon2-analytics-2"></i>
          <span class="menu-text">بازار</span>
        </a>
      </li>
    </router-link>
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
    <li class="menu-section">
      <h4 class="menu-text">سایر</h4>
      <i class="menu-icon flaticon-more-v2"></i>
    </li>
    <!-- **************************** TECHNICAL ONE BUTTON **************************** -->
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
          <i class="menu-icon flaticon-diagram"></i>
          <span class="menu-text">تکنیکال</span>
        </a>
      </li>
    </router-link>

    <li
      aria-haspopup="true"
      data-menu-toggle="hover"
      class="menu-item menu-item-submenu"
      v-bind:class="{
        'menu-item-active': hasActiveChildren('/Assembly')
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
            to="/StockMarket/Assembly/Decisions"
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
                <span class="menu-text">تصمیمات مجامع</span>
              </a>
            </li>
          </router-link>
          <router-link
            :to="
              this.$store.getters.isAuthenticated
                ? '/StockMarket/Assembly/IncreaseCapitals'
                : '/login'
            "
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

          <span class="menu-text"
            >آپشن
            <!-- <v-icon v-if="OptionLock" size="15px" color="#4682B4"
              >mdi-lock-outline</v-icon
            > -->
          </span>
        </a>
      </li>
    </router-link>
  </ul>
</template>

<script>
export default {
  name: "KTMenu",
  // created() {
  //   this.OptionStatus = this.$store.watch(
  //     getters => getters.getLockStatus,
  //     (newValue, oldValue) => {
  //     }
  //   );
  // },
  watch: {
    OptionLock(newCount) {
      this.OptionStatus = newCount;
    }
    // IncreaseCapitalsLock(newValue) {
    //   this.IncreaseCapitalsStatus = newValue;
    // }
  },
  data() {
    return {
      OptionStatus: true
      // IncreaseCapitalsStatus: false
    };
  },
  computed: {
    OptionLock() {
      return this.$store.getters.getLockStatus;
    }
    // IncreaseCapitalsLock() {
    //   // return this.$store.getters.
    //   return this.$store.getters.isAuthenticated;
    // }
  },
  methods: {
    hasActiveChildren(match) {
      return this.$route["path"].indexOf(match) !== -1;
    }
  }
};
</script>
