<template>
  <v-card rounded="lg">
    <v-toolbar elevation="1" dense style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em">
        سود نقدی
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-col class="d-flex justify-content-end" cols="3">
        <v-select
          class="vuetifySelectCustom flex-grow-1"
          :items="years"
          v-model="year"
          solo-inverted
          dense
        ></v-select>
      </v-col>
    </v-toolbar>
    <v-skeleton-loader
      v-if="loading"
      height="100px"
      type=" table-heading, table-thead, table-tbody"
    ></v-skeleton-loader>
    <b-table
      v-if="!loading"
      class="AssemblyDPSwidget-table"
      thClass="AssemblyDPSwidget-tableHeader"
      tbody-tr-class="AssemblyDPSwidget-table-row"
      small
      hover
      :items="filteredItems(year)"
      :fields="headers"
    >
    </b-table>
  </v-card>
</template>

<script>
export default {
  props: ["notices"],
  data() {
    return {
      year: "",
      loading: true,
      headers: [
        {
          label: "منتهی به",
          key: "ToDate",
          thClass: "AssemblyDPSwidget-tableHeader"
        },
        {
          label: "عنوان",
          key: "Title",
          thClass: "AssemblyDPSwidget-tableHeader"
        },
        {
          label: "مقدار ریالی",
          key: "Value",
          thClass: "AssemblyDPSwidget-tableHeader"
        }
      ]
    };
  },
  methods: {
    filteredItems(value) {
      return this.notices.filter(item => {
        return item.ToDate.normalize("NFC") == value.normalize("NFC");
      });
    }
  },
  computed: {
    years() {
      let lookup = {};
      let items = this.notices;
      let result = [];
      for (let item, i = 0; (item = items[i++]); ) {
        let name = item.ToDate;

        if (!(name in lookup)) {
          lookup[name] = 1;
          result.push(name);
        }
      }
      result.sort();
      result.reverse();
      return result;
      // let result2 = {};
      // // let items2 = result;
      // let counter = 0;
      // for (let item, i = 0; (item = result[i++]); ) {
      //   // let name = item;
      //   result2[counter] = item;
      //   counter += 1;
      // }
      // return result2;
    }
    // this.populateData();
  },
  watch: {
    notices() {
      // this.populateData();
      this.loading = false;
      // this.setYears();
      this.year = this.years[0];
    }
  }
};
</script>
<style scoped>
.AssemblyDPSwidget-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.AssemblyDPSwidget-table /deep/ .AssemblyDPSwidget-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
}
.AssemblyDPSwidget-table /deep/ .AssemblyDPSwidget-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}

.vuetifySelectCustom /deep/ .v-input__control {
  min-height: 25px !important;
  height: 25px !important;
}
.vuetifySelectCustom /deep/ .v-input__control {
  font-size: 0.7em !important;
}
.vuetifySelectCustom /deep/ .v-chip.v-size--small {
  border-radius: 3px;
  font-size: 10px;
  height: 17px;
}
.vuetifySelectCustom /deep/ .v-chip .v-chip__close.v-icon {
  font-size: 12px !important;
}
</style>
