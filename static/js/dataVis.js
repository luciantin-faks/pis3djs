import { getIPSdata } from '/static/js/dataRequest.js'
import { GraphPopulate, SplitArc } from '/static/js/Graph.js'
import { } from "/static/js/TextToContainer.js"



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
    .attr('height',height);

//grupe
let ipsG = svg.append('g')
    .attr('transform',`translate(${height/2-50},${width/2-30})`);

svg.append('foreignObject')
    .attr('width', '100%')
    .attr('height', '100%')
    .attr('x', 0) 
   .append('xhtml:div').style('height','100%').style('width','100%')
  .append('xhtml:object')
  .attr('height','100%').attr('width','100%')
  .attr('type','image/svg+xml')
  .attr('data','https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Architectural_column_plinth_Gibberd_Garden_Essex_England_03.JPG/800px-Architectural_column_plinth_Gibberd_Garden_Essex_England_03.JPG')
  .append('img').attr('alt','notloaded');
  svg.append('foreignObject')
    .attr('width', '100%')
    .attr('height', '100%')
    .attr('x', 0) 
   .append('xhtml:p').style('height','100%').style('width','100%')
  .attr('height','100%').attr('width','100%')
  .html('TESHINSFSDF dalwn fjragnkj g ah bg hb sbfh <hjfb <jhfbjeh< bfhj<se fjhb <efbe<wb gwbuig buibgk sbgbsk jj fsdn fsdkj fkjdsfjk sdjkbfk<bs kjbkgb hjrbz grhjzb' )
//svg.append('rect')

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


