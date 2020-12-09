<template>
  <div>
    <div class="card card-custom card-stretch gutter-b">
      <!--begin::Header-->
      <div class="card-header border-0 pt-2">
        <h3 class="card-title font-weight-bolder FinancialStrength">
          پر بازدید
        </h3>
        <!-- <v-subheader class="ltr_aligned" v-if="loading == false">
        آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }}
      </v-subheader> -->
      </div>
      <div class="card-body d-flex flex-column">
        <v-data-table
          v-if="loading == false"
          :headers="mvheaders"
          :items="filteredItems"
          :hide-default-footer="true"
          :hide-default-header="true"
          class="elevation-1 FinancialStrength"
          :header-props="{ sortIcon: null }"
        >
          <template v-slot:[`item.ticker`]="{ item }">
            <v-chip
              small
              label
              :to="{ name: 'TickerOverall', params: { id: item.ID } }"
              >{{ item.ticker }}</v-chip
            >
          </template>
        </v-data-table>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  }
};
</script>
