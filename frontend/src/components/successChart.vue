<template>
<div class="card chart">
    <header class="card-header">
        <p class="card-header-title">Probability of Success ({{iterations.toLocaleString()}} Possibilities)</p>
    </header>
    <div class="card-content">
        <div class="content">
        <highcharts :options="successChartOptions" class="vh70"></highcharts>
        </div>
    </div>
    </div>
</template>
<script>
// higcharts
import { Chart } from "highcharts-vue";
export default {
  name: "successChart",
  components: {
    highcharts: Chart,
  },
  props: {
      data: {
          required: true,
          type: Array
      },
      iterations: {
          required: true,
          type: Number
      }
  },
  computed: {
      successChartOptions() {
      return {
        chartType: "line",
        chart: {
          height: 300
        },
        credits: {
          enabled: false
        },
        title: {
          text: ""
        },
        legend: {
          enabled: false
        },
        yAxis: {
          title: {
            text: "Probability of success (percent)"
          },
          max: 100,
          min: 0
        },
        xAxis: {
          title: {
            text: "Difference betweeen test difficulty and character skill"
          },
          type: "category",
          categories: this.tests
        },
        plotOptions: {
          line: {
            dataLabels: {
              enabled: true,
              formatter: function() {
                return this.x + ": " + this.y.toFixed(2) + "%";
              }
            }
          }
        },
        series: [{ data: this.data, color: "#00d1b2" }]
      };
    },
  }
}
</script>