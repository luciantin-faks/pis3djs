import { getIPSdata } from '/static/js/dataRequest.js'
 

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

let gIPS = svg.append('g');

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                IPS Graf                          \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

async function IPSgraphPopulate(){
    const IPS_list = await getIPSdata('IPS');
    // console.log(IPS_list)

    // gIPS.selectAll('')
    //     .data(IPS_list)
    //     .enter()
    //     .append()
    //         .attr('cx',function(d){ return Xscale(d.x)})
    //         .attr('cy',function(d){ return Xscale(d.y)})
    //         .attr('r',100)
    //         .attr('fill',function(d){ return RandomRGB()});
}

function Arcs(nums){

    var arc = d3.arc()
    .innerRadius(50)
    .outerRadius(70)
    .startAngle( Math.PI/2 ) //converting from degs to radians
    .endAngle((6 * Math.PI) / 4) //just radians
    
}

//return arr = [ for each x in n => {startAngle:x * 2PI /n,endAngle: (x+1) * 2PI /n} ]
function SplitArc(n){
    let arr = [];
    for(let x = 0; x<n;x++) arr.push({startAngle:x * 2 * Math.PI /n,endAngle: (x+1) * 2 * Math.PI /n});
    return arr;
}

function CreateArcPaths(arcs,radiusIn,radiusOut){
    let aPaths = [];
    for(let x = 0; x<arcs.length;x++) 
        aPaths.push(
            d3.arc()
                .innerRadius(radiusIn)
                .outerRadius(radiusOut)
                .startAngle( arcs[x]['startAngle'] ) 
                .endAngle(  arcs[x]['endAngle']  )
        );
    return aPaths;
}

console.log(CreateArcPaths(SplitArc(10),50,60));


const g  = svg.append('g')
    .attr('transform',`translate(${height/2-50},${width/2-30})`);
    

let arcs = CreateArcPaths(SplitArc(10),50,60);
for(let x = 0; x<arcs.length;x++){

g.append('path')
.attr('d',arcs[x])
.attr('fill','black')
.attr('x',300)
.attr('y',300)
.attr('width',width/2)
.attr('height',height/2);
}


    var arc = d3.arc()
    .innerRadius(50)
    .outerRadius(70)
    .startAngle( Math.PI/2 ) //converting from degs to radians
    .endAngle((6 * Math.PI) / 4) //just radians


svg.append('path')
    .attr('d',arc)
    .attr('fill','black');

IPSgraphPopulate();