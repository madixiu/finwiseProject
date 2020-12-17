<template>
  <div>
    <v-card>
      <div class="row">
        <div class="col-xxl-2 col-lg-2 mr-2 mt-2">
          <b-form-select
            v-model="filters.tableMarketSelected"
            :options="filters.tableMarketFilters"
          >
            <template #first>
              <b-form-select-option :value="null" disabled
                >-- انتخاب کنید --</b-form-select-option
              >
            </template>
          </b-form-select>
        </div>
      </div>
      <div class="row">
        <!-- type selctor -->
        <div class="col-xxl-5 col-lg-5 mr-2 dropdown-rtl">
          <b-form-group label="نوع" label-for="tags-with-dropdown">
            <b-form-tags
              id="tags-with-dropdown"
              tag-class="form-tag-class"
              v-model="value"
              no-outer-focus
              class="mb-2"
            >
              <template v-slot="{ tags, disabled, addTag, removeTag }">
                <ul
                  v-if="tags.length > 0"
                  class="list-inline d-inline-block mb-2"
                >
                  <li v-for="tag in tags" :key="tag" class="list-inline-item">
                    <b-form-tag
                      @remove="removeTag(tag)"
                      :title="tag"
                      :disabled="disabled"
                      variant="info"
                      >{{ tag }}</b-form-tag
                    >
                  </li>
                </ul>

                <b-dropdown
                  size="sm"
                  variant="outline-secondary"
                  block
                  menu-class="w-100 dropdown-rtl"
                >
                  <template #button-content>
                    <b-icon icon="tag-fill"></b-icon>نوع
                  </template>
                  <b-dropdown-form @submit.stop.prevent="() => {}">
                    <b-form-group
                      label="Search tags"
                      label-for="tag-search-input"
                      label-cols-md="auto"
                      class="mb-0"
                      label-size="sm"
                      :description="searchDesc"
                      :disabled="disabled"
                    >
                      <b-form-input
                        v-model="search"
                        id="tag-search-input"
                        input-class="form-input-class"
                        type="search"
                        size="sm"
                        autocomplete="off"
                      ></b-form-input>
                    </b-form-group>
                  </b-dropdown-form>
                  <b-dropdown-divider></b-dropdown-divider>
                  <b-dropdown-item-button
                    v-for="option in availableOptions"
                    :key="option"
                    @click="onOptionClick({ option, addTag })"
                  >
                    {{ option }}
                  </b-dropdown-item-button>
                  <b-dropdown-text v-if="availableOptions.length === 0">
                    There are no tags available to select
                  </b-dropdown-text>
                </b-dropdown>
              </template>
            </b-form-tags>
          </b-form-group>
        </div>
        <!-- industry selector -->
        <div class="col-xxl-5 col-lg-5 mr-2 dropdown-rtl">
          <b-form-group label="صنعت" label-for="tags-with-dropdown">
            <b-form-tags
              id="tags-with-dropdown"
              tag-class="form-tag-class"
              v-model="value"
              no-outer-focus
              class="mb-2"
            >
              <template v-slot="{ tags, disabled, addTag, removeTag }">
                <ul
                  v-if="tags.length > 0"
                  class="list-inline d-inline-block mb-2"
                >
                  <li v-for="tag in tags" :key="tag" class="list-inline-item">
                    <b-form-tag
                      @remove="removeTag(tag)"
                      :title="tag"
                      :disabled="disabled"
                      variant="info"
                      >{{ tag }}</b-form-tag
                    >
                  </li>
                </ul>

                <b-dropdown
                  size="sm"
                  variant="outline-secondary"
                  block
                  menu-class="w-100 dropdown-rtl"
                >
                  <template #button-content>
                    <b-icon icon="tag-fill"></b-icon>صنعت
                  </template>
                  <b-dropdown-form @submit.stop.prevent="() => {}">
                    <b-form-group
                      label="Search tags"
                      label-for="tag-search-input"
                      label-cols-md="auto"
                      class="mb-0"
                      label-size="sm"
                      :description="searchDesc"
                      :disabled="disabled"
                    >
                      <b-form-input
                        v-model="search"
                        id="tag-search-input"
                        input-class="form-input-class"
                        type="search"
                        size="sm"
                        autocomplete="off"
                      ></b-form-input>
                    </b-form-group>
                  </b-dropdown-form>
                  <b-dropdown-divider></b-dropdown-divider>
                  <b-dropdown-item-button
                    v-for="option in availableOptions"
                    :key="option"
                    @click="onOptionClick({ option, addTag })"
                  >
                    {{ option }}
                  </b-dropdown-item-button>
                  <b-dropdown-text v-if="availableOptions.length === 0">
                    There are no tags available to select
                  </b-dropdown-text>
                </b-dropdown>
              </template>
            </b-form-tags>
          </b-form-group>
        </div>
      </div>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "marketwatch",
  components: {},
  data() {
    return {
      filters: {
        tableMarketSelected: null,
        tableMarketFilters: ["همه", "بورس", "فرابورس"],
        tableMarketTypeSelected: null,
        tableMarketTypeFilters: []
      },

      options: [
        "Apple",
        "Orange",
        "Banana",
        "Lime",
        "Peach",
        "Chocolate",
        "Strawberry"
      ],
      search: "",
      value: []
    };
  },
  computed: {
    //search for selectors
    criteria() {
      // Compute the search criteria
      return this.search.trim().toLowerCase();
    },
    availableOptions() {
      const criteria = this.criteria;
      // Filter out already selected options
      const options = this.options.filter(
        opt => this.value.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.toLowerCase().indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    },
    searchDesc() {
      if (this.criteria && this.availableOptions.length === 0) {
        return "There are no tags matching your search criteria";
      }
      return "";
    }
  },
  methods: {
    onOptionClick({ option, addTag }) {
      addTag(option);
      this.search = "";
    }
  }
};
</script>
<style>
.form-input-class {
  direction: rtl;
}
.form-tag-class {
  direction: rtl !important;
}
.dropdown-rtl {
  text-align: right !important;
  direction: rtl;
  /* width: w-100; */
}
</style>
