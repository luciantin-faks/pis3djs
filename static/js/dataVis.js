import { getIPSdata } from '/static/js/dataRequest.js'
import { GraphPopulate, SplitArc } from '/static/js/Graph.js'
import { responsify } from '/static/js/responsify.js'
//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                D3  settings & vars               \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

const CIRCLE_SIZE = [ 100,200,300];

// let margin = {top: 10, right: 40, bottom: 30, left: 30},
// width  = 500 - margin.left - margin.right,
// height = 500 - margin.top - margin.bottom;

// let width = window.screen.width,height =window.screen.height;
let width = window.innerWidth,
height = window.innerHeight;

let chart = d3.select('#chart');
let svg = d3.select('body')
    .append('svg')
    .attr('width',width)
    .attr('height',height)
    // .attr('viewBox','0 0 500 500')
    .attr('preserveAspectRatio','xMidYMid meet')
    .call(responsify); //da bude responzivan


    // viewBox="0 0 500 500"
    // preserveAspectRatio="xMidYMid meet"

//grupe
let ipsG = svg.append('g')
    .attr('transform',`translate(${width/2},${height/2})`);
let modsG = svg.append('g')
    .attr('transform',`translate(${width/2},${height/2})`);
//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                     MAIN                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

let IPS_list;
let MODULI_list;

main()
async function main(){

    let IPS_data = await getIPSdata("IPS");
    IPS_list = 
        GraphPopulate(
            IPS_data['IPS'],
            SplitArc(IPS_data['IPS'].length,200,210).map(el => el.centroid()),
            ipsG,
            TstOnClick
        )
    
    let MODULI_data = await getIPSdata("MODULI");
    MODULI_list = 
        GraphPopulate(
            MODULI_data['MODULI']['Prodaja i izlazna logistika'],
            SplitArc(MODULI_data['MODULI']['Prodaja i izlazna logistika'].length,100,110).map(el => el.centroid()),
            modsG,
            TstOnClick2
    )
}

function TstOnClick(data,i){
    console.log(IPS_list.selectAll('*'))
    // IPS_list.selectAll('*').filter(d=>d!=data).attr('fill','blue')
    //     .transition()
    //         .attr('x',0)
    IPS_list.filter(d=>d!=data)
        .transition()
            .attr("transform", `translate(${data['coord'][0]},${data['coord'][1]})scale(0)`)
            // .attr('x',)
            // .attr('y',)
            .duration(1000);
    
}

function TstOnClick2(data,i){
    console.log(MODULI_list.selectAll('*'))
    // IPS_list.selectAll('*').filter(d=>d!=data).attr('fill','blue')
    //     .transition()
    //         .attr('x',0)
    MODULI_list.filter(d=>d!=data)
        .transition()
            .attr("transform", `translate(${data['coord'][0]},${data['coord'][1]})scale(0)`)
            // .attr('x',)
            // .attr('y',)
            .duration(1000);
    
}




