<template>
  <div>
    <apexchart
      height="220"
      width="340"
      type="bar"
      :options="options"
      :series="series"
    ></apexchart>
  </div>
</template>
<script>
export default {
  name: "HorizontalBarChart",
  data() {
    return {
      // data of horizontal bar chart
      series: [
        {
          name: "series-1",
          data: [-100, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
        }
        // {
        //   name: 'series-0',
        //   data: 1000
        // }],
      ],
      options: {
        chart: {
          type: "bar",
          height: 400,
          id: "vuechart-example"
        },
        legend: {
          show: false
        },

        annotations: {
          xaxis: [
            {
              x: 1500,
              borderColor: "#eb4034",
              label: {
                text: "1500",
                orientation: "horizontal",
                borderColor: "#eb4034",
                style: {
                  color: "#fff",
                  background: "#eb4034"
                }
              }
            }
          ]
        },
        plotOptions: {
          bar: {
            barHeight: "100%",
            distributed: true,
            horizontal: true,
            dataLabels: {
              position: "left",
              color: "black"
            }
          }
        },
        colors: [
          "#33b2df",
          "#546E7A",
          "#d4526e",
          "#13d8aa",
          "#A5978B",
          "#2b908f",
          "#f9a3a4",
          "#90ee7e",
          "#f48024",
          "#69d2e7"
        ],
        dataLabels: {
          enabled: false,
          textAnchor: "start",
          style: {
            colors: ["#fff"]
          },
          formatter: function(val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
          },
          offsetX: 0,
          dropShadow: {
            enabled: true
          }
        },
        stroke: {
          width: 1,
          colors: ["#fff"]
        },
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "India"
          ]
        },
        yaxis: {
          labels: {
            show: true,
            align: "center"
          }
        },
        title: {
          text: "Custom DataLabels",
          align: "center",
          floating: true
        },
        subtitle: {
          text: "Category Names as DataLabels inside bars",
          align: "center"
        },
        tooltip: {
          theme: "dark",
          x: {
            show: true
          },
          y: {
            title: {
              formatter: function() {
                return "";
              }
            }
          }
        }
      }
    };
  }
};
</script>
