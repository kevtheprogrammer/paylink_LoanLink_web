var options = {
  series: [74],
  chart: { height: 300, type: "radialBar", offsetY: 0 },
  plotOptions: {
    radialBar: {
      startAngle: -90,
      endAngle: 90,
      hollow: { margin: 0, size: "70%" },
      dataLabels: {
        showOn: "always",
        name: {
          show: true,
          fontSize: "13px",
          fontWeight: "700",
          offsetY: -5,
          color: ["#000000", "#E5ECFF"],
        },
        value: {
          color: ["#000000", "#E5ECFF"],
          fontSize: "30px",
          fontWeight: "700",
          offsetY: -40,
          show: true,
        },
      },
      track: { background: ["#E5ECFF", "#E5ECFF"], strokeWidth: "100%" },
    },
  },
  colors: ["#9767FD", "#E5ECFF"],
  stroke: { lineCap: "round" },
  labels: ["Progress"],
};
var chart = new ApexCharts(document.querySelector("#chart-currently"), options);
chart.render();
options = {
  chart: { height: 339, type: "line", stacked: !1, toolbar: { show: !1 } },
  stroke: { width: [0, 2, 4], curve: "smooth" },
  plotOptions: { bar: { columnWidth: "30%" } },
  colors: ["#9767FD", "#dfe2e6", "#f1b44c"],
  series: [
    {
      name: "Loan Application",
      type: "column",
      data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
    },
    {
      name: "Active Loan",
      type: "area",
      data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
    },
    {
      name: "Tablets",
      type: "line",
      data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
    },
  ],
  fill: {
    opacity: [0.85, 0.25, 1],
    gradient: {
      inverseColors: !1,
      shade: "light",
      type: "vertical",
      opacityFrom: 0.85,
      opacityTo: 0.55,
      stops: [0, 100, 100, 100],
    },
  },
  labels: [
    "01/01/2003",
    "02/01/2003",
    "03/01/2003",
    "04/01/2003",
    "05/01/2003",
    "06/01/2003",
    "07/01/2003",
    "08/01/2003",
    "09/01/2003",
    "10/01/2003",
    "11/01/2003",
  ],
  markers: { size: 0 },
  xaxis: { type: "datetime" },
  yaxis: { title: { text: "Points" } },
  tooltip: {
    shared: !0,
    intersect: !1,
    y: {
      formatter: function (e) {
        return void 0 !== e ? e.toFixed(0) + " points" : e;
      },
    },
  },
  grid: { borderColor: "#f1f1f1" },
};
(chart = new ApexCharts(
  document.querySelector("#management_bar"),
  options
)).render();
var options = {
  series: [{ name: "Net Profit", data: [30, 25, 45, 30, 55, 55] }],
  chart: {
    type: "area",
    height: 270,
    offsetY: 0,
    toolbar: { show: false },
    zoom: { enabled: false },
    sparkline: { enabled: true },
  },
  plotOptions: {},
  legend: { show: false },
  dataLabels: { enabled: false },
  fill: { type: "solid", opacity: 0.2 },
  stroke: {
    curve: "smooth",
    show: true,
    width: 3,
    colors: ["#9767FD", "#E5ECFF"],
  },
  xaxis: {
    categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    axisBorder: { show: false },
    axisTicks: { show: false },
    labels: { show: false, style: { fontSize: "12px" } },
    crosshairs: {
      show: false,
      position: "front",
      stroke: { color: ["#9767FD", "#E5ECFF"], width: 1, dashArray: 3 },
    },
    tooltip: {
      enabled: true,
      formatter: undefined,
      offsetY: 0,
      style: { fontSize: "12px" },
    },
  },
  yaxis: {
    min: 0,
    max: 60,
    labels: { show: false, style: { fontSize: "12px" } },
  },
  states: {
    normal: { filter: { type: "none", value: 0 } },
    hover: { filter: { type: "none", value: 0 } },
    active: {
      allowMultipleDataPointsSelection: false,
      filter: { type: "none", value: 0 },
    },
  },
  tooltip: {
    style: { fontSize: "12px" },
    y: {
      formatter: function (val) {
        return "$" + val + " thousands";
      },
    },
  },
  colors: ["#9767FD", "#E5ECFF"],
  markers: {
    colors: ["#9767FD", "#E5ECFF"],
    strokeColor: ["#9767FD", "#E5ECFF"],
    strokeWidth: 3,
  },
};
var chart = new ApexCharts(document.querySelector("#chart4"), options);
chart.render();

var options = {
          series: [{
          name: 'Net Profit',
          data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
          name: 'Revenue',
          data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }, {
          name: 'Free Cash Flow',
          data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
        }],
          chart: {
          type: 'bar',
          height: 350
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        xaxis: {
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        },
        yaxis: {
          title: {
            text: '$ (thousands)'
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands"
            }
          }
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();

      //loan details
      var options = {
        series: [{
        name: 'Net Profit',
        data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
      }, {
        name: 'Revenue',
        data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
      }, {
        name: 'Free Cash Flow',
        data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
      }],
        chart: {
        type: 'bar',
        height: 350
      },
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: '55%',
          endingShape: 'rounded'
        },
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        show: true,
        width: 2,
        colors: ['transparent']
      },
      xaxis: {
        categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
      },
      yaxis: {
        title: {
          text: '$ (thousands)'
        }
      },
      fill: {
        opacity: 1
      },
      tooltip: {
        y: {
          formatter: function (val) {
            return "$ " + val + " thousands"
          }
        }
      }
      };

      var chart = new ApexCharts(document.querySelector("#loan_details_bar"), options);
      chart.render();

      var options = {
        series: [44, 55, 67, 83],
        chart: {
        height: 350,
        type: 'radialBar',
      },
      plotOptions: {
        radialBar: {
          dataLabels: {
            name: {
              fontSize: '22px',
            },
            value: {
              fontSize: '16px',
            },
            total: {
              show: true,
              label: 'Total',
              formatter: function (w) {
                // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                return 249
              }
            }
          }
        }
      },
      labels: ['Approved', 'Pending', 'Closed', 'Rejected'],
      };

      var chart = new ApexCharts(document.querySelector("#rader"), options);
      chart.render();

//Age loan analysis
var options = {
  series: [{
  name: 'Current Less 30 days',
  data: [44, 55, 41, 67, 22, 43]
}, {
  name: '31 - 60 days',
  data: [13, 23, 20, 8, 13, 27]
}, {
  name: '61 - 90 days',
  data: [11, 17, 15, 15, 21, 14]
}, {
  name: '91 -180 days',
  data: [21, 7, 25, 13, 22, 8]
}],
  chart: {
  type: 'bar',
  height: 350,
  stacked: true,
  toolbar: {
    show: true
  },
  zoom: {
    enabled: true
  }
},
responsive: [{
  breakpoint: 480,
  options: {
    legend: {
      position: 'bottom',
      offsetX: -10,
      offsetY: 0
    }
  }
}],
plotOptions: {
  bar: {
    horizontal: false,
    borderRadius: 10,
    borderRadiusApplication: 'end', // 'around', 'end'
    borderRadiusWhenStacked: 'last', // 'all', 'last'
    dataLabels: {
      total: {
        enabled: true,
        style: {
          fontSize: '13px',
          fontWeight: 900
        }
      }
    }
  },
},
xaxis: {
  type: 'datetime',
  categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
    '01/05/2011 GMT', '01/06/2011 GMT'
  ],
},
legend: {
  position: 'right',
  offsetY: 40
},
fill: {
  opacity: 1
}
};

var chart = new ApexCharts(document.querySelector("#loan-age"), options);
chart.render();


//None performing Loans

var options = {
  series: [{
    name: "Loan Arrears",
    data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
}],
  chart: {
  height: 350,
  type: 'line',
  zoom: {
    enabled: false
  }
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
title: {
  text: 'Annual Projection',
  align: 'left'
},
grid: {
  row: {
    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
    opacity: 0.5
  },
},
xaxis: {
  categories: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2022', '2023'],
}
};

var chart = new ApexCharts(document.querySelector("#non-performing"), options);
chart.render();

//Arrears pie chart
var options = {
  series: [44, 55, 13, 43],
  chart: {
  width: 380,
  type: 'pie',
},
title: {
  text: 'Arrears Quaterly',
  align: 'left'
},
labels: ['1st Quater', '2nd Quater', '1rd Quater', '1fth Quater'],
responsive: [{
  breakpoint: 480,
  options: {
    chart: {
      width: 200
    },
    legend: {
      position: 'bottom'
    }
  }
}]
};

var chart = new ApexCharts(document.querySelector("#arrears"), options);
chart.render();


//Interest Book
var options = {
  series: [
  {
    name: "Accounts",
    data: [128,229, 433, 536,632, 732, 833]
  },
  {
    name: "Interest",
    data: [212, 411, 614, 818, 917, 1113, 1113]
  }
],
  chart: {
  height: 350,
  type: 'line',
  dropShadow: {
    enabled: true,
    color: '#000',
    top: 18,
    left: 7,
    blur: 10,
    opacity: 0.2
  },
  zoom: {
    enabled: false
  },
  toolbar: {
    show: false
  }
},
colors: ['#77B6EA', '#545454'],
dataLabels: {
  enabled: true,
},
stroke: {
  curve: 'smooth'
},
title: {
  text: 'Average High & Low Temperature',
  align: 'left'
},
grid: {
  borderColor: '#e7e7e7',
  row: {
    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
    opacity: 0.5
  },
},
markers: {
  size: 1
},
xaxis: {
  categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
  title: {
    text: 'Month'
  }
},
yaxis: {
  title: {
    text: 'Interest'
  },
  min: 100,
  max: 3000
},
legend: {
  position: 'top',
  horizontalAlign: 'right',
  floating: true,
  offsetY: -25,
  offsetX: -5
}
};

var chart = new ApexCharts(document.querySelector("#interest-book-chart"), options);
chart.render();


//Loan listing with repayments and end date
var options = {
  series: [
  {
    data: [
      {
        x: 'Jan',
        y: [2800, 4500]
      },
      {
        x: 'Feb',
        y: [3200, 4100]
      },
      {
        x: 'Mar',
        y: [2950, 7800]
      },
      {
        x: 'Apr',
        y: [3000, 4600]
      },
      {
        x: 'May',
        y: [3500, 4100]
      },
      {
        x: 'Jun',
        y: [4500, 6500]
      },
      {
        x: 'Jul',
        y: [4100, 5600]
      }
    ]
  }
],
  chart: {
  height: 350,
  type: 'rangeBar',
  zoom: {
    enabled: false
  }
},
plotOptions: {
  bar: {
    isDumbbell: true,
    columnWidth: 3,
    dumbbellColors: [['#00E396', '#00E396']]
  }
},
legend: {
  show: true,
  showForSingleSeries: true,
  position: 'top',
  horizontalAlign: 'left',
  customLegendItems: ['Start Date Loan', 'End Date Loan']
},
fill: {
  type: 'gradient',
  gradient: {
    type: 'vertical',
    gradientToColors: ['#FF0000'],
    inverseColors: true,
    stops: [0, 100]
  }
},
grid: {
  xaxis: {
    lines: {
      show: true
    }
  },
  yaxis: {
    lines: {
      show: false
    }
  }
},
xaxis: {
  tickPlacement: 'on'
}
};

var chart = new ApexCharts(document.querySelector("#loan-repayment-listings"), options);
chart.render();

//Loan Diseburment Listing

var options = {
  series: [{
  data: [400, 430, 448, 470, 540, 580, 690]
}],
  chart: {
  type: 'bar',
  height: 350
},
annotations: {
  xaxis: [{
    x: 500,
    borderColor: '#00E396',
    label: {
      borderColor: '#00E396',
      style: {
        color: '#fff',
        background: '#00E396',
      },
      text: 'Disbursement',
    }
  }],
  yaxis: [{
    y: 'July',
    y2: 'September',
    label: {
      text: 'Disbursement'
    }
  }]
},
plotOptions: {
  bar: {
    horizontal: true,
  }
},
dataLabels: {
  enabled: true
},
xaxis: {
  categories: ['June', 'July', 'August', 'September', 'October', 'November', 'December'],
},
grid: {
  xaxis: {
    lines: {
      show: true
    }
  }
},
yaxis: {
  reversed: true,
  axisTicks: {
    show: true
  }
}
};

var chart = new ApexCharts(document.querySelector("#disbursement-listings"), options);
chart.render();

