



let margin = {top: 10, right: 40, bottom: 30, left: 30},
width  = 500 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

let chart = d3.select('#chart');
let svg = chart
    .append('svg')
    .attr('width',width)
    .attr('height',height);
