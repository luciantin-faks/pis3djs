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


