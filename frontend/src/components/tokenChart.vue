<template>
<div class="card chart">
    <header class="card-header">
        <p class="card-header-title">Probability of Resolving Token ({{iterations.toLocaleString()}} Possibilities)</p>
    </header>
    <div class="card-content">
        <div class="content">
        <highcharts :options="tokenChartOptions" class="vh70"></highcharts>
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
      },
      tokens: {
          required: true,
          type: Array
      }
  },
  computed: {
      tokenChartOptions() {
        return {
            chart: {
                height: 300
            },
            chartType: "column",
            legend: {
                enabled: false
            },
            credits: {
                enabled: false
            },
            title: {
                text: ""
            },
            xAxis: {
                categories: this.tokens.map(token => token.label),
            title: {
                text: "Tokens"
            },
            type: "category"
            },
            yAxis: {
                title: {
                    text: "Probability of Resolving (percent)"
                },
                max: 25,
                min: 0,
                type: "column"
            },
            series: [
                {
                    data: this.data,
                    color: "#00d1b2",
                    type: "column"
                }
            ],
            plotOptions: {
                column: {
                    dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return String(parseFloat(this.y).toFixed(2)) + "%";
                    }
                }
            }
        }
    };
        },
  }
}
</script>