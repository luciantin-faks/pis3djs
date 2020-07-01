import { getIPSdata } from '/static/js/dataRequest.js'
import { GraphPopulate, SplitArc } from '/static/js/Graph.js'
import { } from "/static/js/TextToContainer.js"
import { TextElement } from "/static/js/SVGforeign.js"
import { responsivefy } from "/static/js/responsify.js"

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                D3  settings & vars               \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

const CIRCLE_SIZE = [ 100,200,300];

let margin = {top: 10, right: 40, bottom: 30, left: 30},
width  = 500 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

let chart = d3.select('#chart');
let svg = chart
    .append('svg')
    .attr('width',width)
    .attr('height',height)
    .attr('viewBox','0 0 500 500')
    .attr('preserveAspectRatio','xMidYMid meet')
    // .call(responsivefy); //da bude responzivan
    // viewBox="0 0 500 500"
    // preserveAspectRatio="xMidYMid meet"

//grupe
let ipsG = svg.append('g')
    // .attr('transform',`translate(${height/2-50},${width/2-30})`);

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                     MAIN                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\
main()

function main(){

    let IPS_list = getIPSdata("IPS")
        .then(d => { 
            return GraphPopulate(
                        d['IPS'],
                        SplitArc(d['IPS'].length,100,100).map(el => el.centroid()),
                        ipsG,
                        TstOnClick)})

    // const IPS_MODULI_list = getIPSdata("MODULI")
    //     .then(d => { return FormatIPSdata(d)})
    //     .catch(er => console.log('ERROR : CANT GET DATA'))
}

function TstOnClick(d,i){
    console.log(d,i)
}









// let dat = [1,2,3,4,5]


// let textEl = svg.append('g');

// textEl.selectAll('text').data(dat)
//     .enter()
//     .append('text')
//         .attr("x", (d,i) => 50*i)
//         .attr("y", (d,i) => 100*i)
//         .attr("text-anchor", "middle")
//         .attr("font-family", "sans-serif")
//         .text("Nabava i izlazna logistika")
//         .each(function() {
//             let text = d3.select(this),
//               words = text.text().split(/\s+/).reverse(),
//               word,
//               line = [],
//               lineNumber = 0,
//               lineHeight = 1.1, // ems
//               x = text.attr("x"),
//               y = text.attr("y"),
//               dy = 1.1,
//               tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dy", dy + "em");
//             while (word = words.pop()) {
//               line.push(word);
//               tspan.text(line.join(" "));
//               if (tspan.node().getComputedTextLength() > 100) {
//                 line.pop();
//                 tspan.text(line.join(" "));
//                 line = [word];
//                 tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
//               }
//             }
//         });



// textEl.append("text")
//   .attr("x", 100)
//   .attr("y", 200)
//   .attr("text-anchor", "middle")
//   .attr("font-family", "sans-serif")
//   .text("Nabava i izlazna logistika")
//   .call(wrap, 100);

// txtHeight = parseInt(textEl.select('text').node().getBoundingClientRect().txtHeight);

// textEl.select("text").attr('transform', 'translate(0, ' + (-txtHeight / 2) + ')');

function wrap(text, width) {
    console.log(text)
//   text.each(function() {
//     let text = d3.select(this),
//       words = text.text().split(/\s+/).reverse(),
//       word,
//       line = [],
//       lineNumber = 0,
//       lineHeight = 1.1, // ems
//       x = text.attr("x"),
//       y = text.attr("y"),
//       dy = 1.1,
//       tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dy", dy + "em");
//     while (word = words.pop()) {
//       line.push(word);
//       tspan.text(line.join(" "));
//       if (tspan.node().getComputedTextLength() > width) {
//         line.pop();
//         tspan.text(line.join(" "));
//         line = [word];
//         tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
//       }
//     }
//   });
}