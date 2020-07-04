import { getIPSdata } from '/static/js/dataRequest.js'
import { Graph, SplitArc, GraphDataFormat, SplitLineX, SplitLineY } from '/static/js/Graph.js'
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


//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                     MAIN                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

main()
async function main(){

    //podaci za prvi red
    let IPS_data = (await getIPSdata("IPS"))['IPS'];
    let MODULI_data = (await getIPSdata("MODULI"))['MODULI']['Prodaja i izlazna logistika'];
    //grupe
    let ipsG = svg.append('g')
    let modsG = svg.append('g')
    //grafovi
    let IPSgraf;
    let MODULIgraf;

    console.log(IPS_data)
  
    MODULIgraf = (new Graph(modsG,width,height))
        .SetContainerStyle(GraphStyleRectLinY)
        .SetXoff(-200)
        .Populate(MODULI_data);

    IPSgraf = (new Graph(ipsG,width,height))
        .SetContainerStyle(GraphStyleRectLinY)
        .SetXoff(-400)
        .SetDataSource(ModuliDataSource)
        .SetupSubGraph(MODULIgraf)
        .Populate(IPS_data); 

    
    // setTimeout(()=>{IPS_list.clear()},1000)
}

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                     Style                        \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

const GraphStyleRectLinY ={ // C-container , P-path
    Ctype : 'rect',
    Cfill : 'white',
    Cstroke : 'black',
    Cwidth : 105,
    Cheight : 45,

    Ptype : 'linY',
    Plen : 500,
};

const GraphStyleCircArc ={
    Ctype : 'circle',
    Cfill : 'none',
    Cstroke : 'green',
    Cr : 50,

    Ptype : 'Arc',
    Prad : 200,
};


async function ModuliDataSource(IPSid){
    let MODULI_data = await getIPSdata("MODULI");
    console.log(MODULI_data)
    return MODULI_data['MODULI'][IPSid];
}