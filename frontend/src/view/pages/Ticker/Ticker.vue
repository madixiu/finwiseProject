<template>
    <div>
      <!-- <div class="row">
          <div class="col-sm-12"></div>
            <v-card outlined class="col-sm-12">
              <div class="row h-100 my-auto">
                 <v-card outlined class="col-sm-3 ">
                   
                   <apexchart width="300" type="bar" :options="options" :series="series"></apexchart>
                 </v-card>
                 <v-card outlined class="col-sm-3">
                   <apexchart width="300" type="bar" :options="options" :series="series"></apexchart>
                 </v-card>
                 <v-card outlined class="col-sm-3">
                   <apexchart width="300" type="bar" :options="options" :series="series"></apexchart>
                 </v-card>
              </div>
            
             
            </v-card>
        </div> -->


        <div class="row">
          <div class="col-sm-3">
            <v-card outlined class="col-sm-3">
                   
                  <div class="card card-custom card-stretch gutter-b">
                    <div class="card-header border-0">
                        <h1 class="card-title font-weight-bolder text-dark fs-x-large fc-primary fw-bolder">{{tickerName}}
                          <h2 class="card-title font-weight-bolder fs-medium text-dark">{{price}}</h2>
                          <span class="fs-regular">
                          
                            <span class="color-red">
                              
                              <span class="mdi mdi-chevron-down tick-color-minus"></span>
                              <span class="tick-color-minus">{{tick}}</span>
                            </span>

                          </span>
                        </h1>
             
                            <!-- <div class="card-toolbar">
                              <Dropdown4 :btnClass="'btn-light-primary'"></Dropdown4>
                            </div> -->
                        </div>

                        <b-container class="bv-example-row stock-summary-table fc-regular">
                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>Volume: </p>
                                <p>123</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>Avg Vol (1m): </p>
                                <p>162,120,963</p>
                              </b-row>
                            </b-col>
                          </b-row>

                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>Market Cap: </p>
                                <p>533.63 Bil</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>Enterprise Value $: </p>
                                <p>553.33 Bil</p>
                              </b-row>
                            </b-col>
                           
                          </b-row>

                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>P/E (TTM): </p>
                                <p>37.96</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>P/B: </p>
                                <p>7.40</p>
                              </b-row>
                            </b-col>
                          </b-row>

                        </b-container>
                     
           
                   </div>
                      
                      
                  </v-card>
            </div>
          <div >
             <v-card outlined class="col-sm-3">
                <apexchart width="300" type="bar" :options="options" :series="series"></apexchart>
             </v-card>
          </div>
          <div >
            <v-card class="col-sm-4">
                   <img src="@/assets/PrototypeImages/linechart.png" />
                  </v-card>
          </div>
    
        </div>
          
            <b-container class="bv-example-row">
              
              <b-row>
                <b-col>
                  <v-card outlined>
                   
                  <div class="card card-custom card-stretch gutter-b">
                    <div class="card-header border-0">
                        <h1 class="card-title font-weight-bolder text-dark fs-x-large fc-primary fw-bolder">{{tickerName}}
                          <h2 class="card-title font-weight-bolder fs-medium text-dark">{{price}}</h2>
                          <span class="fs-regular">
                          
                            <span class="color-red">
                              
                              <span class="mdi mdi-chevron-down tick-color-minus"></span>
                              <span class="tick-color-minus">{{tick}}</span>
                            </span>

                          </span>
                        </h1>
             
                            <!-- <div class="card-toolbar">
                              <Dropdown4 :btnClass="'btn-light-primary'"></Dropdown4>
                            </div> -->
                        </div>

                        <b-container class="bv-example-row stock-summary-table fc-regular">
                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>Volume: </p>
                                <p>123</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>Avg Vol (1m): </p>
                                <p>162,120,963</p>
                              </b-row>
                            </b-col>
                          </b-row>

                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>Market Cap: </p>
                                <p>533.63 Bil</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>Enterprise Value $: </p>
                                <p>553.33 Bil</p>
                              </b-row>
                            </b-col>
                           
                          </b-row>

                          <b-row>
                            <b-col sm="6">
                              <b-row>
                                <p>P/E (TTM): </p>
                                <p>37.96</p>
                              </b-row>
                            </b-col>
                            <b-col sm="6">
                              <b-row>
                                <p>P/B: </p>
                                <p>7.40</p>
                              </b-row>
                            </b-col>
                          </b-row>

                        </b-container>
                     
           
                   </div>
                      
                      
                  </v-card>
                </b-col>
                <b-col>
                  <!-- BAR CHART GOES HERE -->
                 
                  <v-card class="app">
                  
                      <apexchart width="300" type="bar" :options="options" :series="series"></apexchart>

                    
                      
                      
                      <!-- <GChart
                        
                        type="BarChart"
                        :data="chartData"
                        :options="chartOptions"
                        
                        @ready="onChartReady"
                        /> -->
                    
                    
                  </v-card>
                </b-col>
                <b-col><v-card>
                   <img src="@/assets/PrototypeImages/linechart.png" />
                  </v-card></b-col>
              </b-row>
              
            </b-container>
          
         
        <div class="col-xxl-4 order-1 order-xxl-2">
        <ListWidget3></ListWidget3>
        </div>
     

    </div>
</template>

<script>
// impoorting proto type images
// import linechart from "@/assets/PrototypeImages/linechart.png"
// import { LOGIN, LOGOUT } from "@/core/services/store/auth.module";

// import { GChart } from 'vue-google-charts'
import ListWidget3 from "@/view/content/widgets/list/Widget3.vue";
export default {
  name: "ticker",
  components: {
    ListWidget3,
    // GChart
  },
  data() {
    return {
      
      // data of horizontal bar chart
          series: [{
        name: 'series-1',
        data: [-100, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
      },
      // {
      //   name: 'series-0',
      //   data: 1000
      // }],
      ],
      options: {
        chart: {
          type: 'bar',
          height: 400,
          id: 'vuechart-example'
        },
        legend: {
            show: false
        },

        annotations: {
              xaxis: [
                {
                  x: 1500,
                  borderColor: '#eb4034',
                  label: {
                    text: '1500',
                    orientation: 'horizontal',
                    borderColor: '#eb4034',
                    style: {
                      color: '#fff',
                      background: '#eb4034',
                    },
                  },
                },
              ],
            },
        plotOptions: {
              bar: {
                barHeight: '100%',
                distributed: true,
                horizontal: true,
                dataLabels: {
                
                  position: 'left',
                  color: 'black'
                },
              }
            },
        colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e',
              '#f48024', '#69d2e7'
            ],
            dataLabels: {
              enabled: false,
              textAnchor: 'start',
              style: {
                colors: ['#fff']
              },
              formatter: function (val, opt) {
                return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
              },
              offsetX: 0,
              dropShadow: {
                enabled: true
              }
            },
            stroke: {
              width: 1,
              colors: ['#fff']
            },
        xaxis: {
          
          categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan',
                'United States', 'China', 'India']
        },
        yaxis: {
              labels: {
                show: true,
                align: 'center',
              }
       },
       title: {
                text: 'Custom DataLabels',
                align: 'center',
                floating: true
          },
          subtitle: {
                text: 'Category Names as DataLabels inside bars',
                align: 'center',
                
            },
            tooltip: {
              theme: 'dark',
              x: {
                show: true
              },
              y: {
                title: {
                  
                  formatter: function () {
                    return ''
                  }
                }
              }
            }
          
      },
      // end of bar chart data
      ////

  
      tickerName : "شتران",
      tick: "-0.81(-0.16%)",
      price: "۳۸۰۰",


      ///////
     
    };
  },


  computed: {
    
  },

  methods: {
   
  } // end of methods
    
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

 .fs-regular {
   font-size: 12px;
   line-height: 20px;
 }
 .fc-regular {
    color: #606266;
 }
 .fc-primary {
    color: #303133;
 }
 .fw-bolder {
    font-weight: 600;
 }
 .fs-x-large {
    font-size: 16px;
    line-height: 28px;
 }
 h1, h2, h3 {
    margin-top: 0;
    margin-bottom: 0;
    font-weight: 500;
    padding-right: 4px;
 }
  .ticket-data {
    padding-right: 4px;
    margin-right: 30px;
  }
  .fs-medium {
    font-size: 11px;
  }

 .tick-color-minus {
   color: crimson;
 }
 .tick-color-plus {
   color: green;
 }
 .stock-summary-table{
    font-size: 10px;
    line-height: 20px;
    margin: 0 4px;
}
.table.no-border tr td, .table.no-border tr th {
  border-width: 60px;
}

caption {
  font-size: 16pt;
}
.jumbotron {
  padding: 5px inherit;
}
</style>

