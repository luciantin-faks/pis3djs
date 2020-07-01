import { TextElement } from "/static/js/SVGforeign.js"

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                IPS Graf                          \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

//GRAPH POPULATE
//
// group < d3 group 
// data  < arr [ 'text','text',....] 
// onClickFun < fun on click
//
//no return;
export async function GraphPopulate(text, path, group, onClickFun){
    // const IPS_list = await getIPSdata('IPS');
    // console.log(path,text)
    let data = [];
    text.map((el,i) => { data.push({'data':el,'coord':[path[i][0]+100,path[i][1]+100] })});
    console.log(data)
    
    let selection = group.selectAll().data(data);

    selection.enter()
        .append('g')
        .attr('transform',d => { return `translate( ${ d['coord'][0] },${ d['coord'][1] })`});;

    group.selectAll('g')
        .append('circle')
            .attr('r',20)
            // .attr('cx', 0)
            // .attr('cy', 0)
            .attr('cx', d => d['coord'][0])
            .attr('cy', d => d['coord'][1])
            .attr('fill','black')
            .attr('stroke','black');
    

    group.selectAll('g')
        .each(appendCircle)

    group.selectAll('g')
        .each(TextElement)

    // selection.enter()
    //     .append('g')
    //     // .attr('r',20)
    //     .attr('transform',`translate(${d => d['coord'][0]},${d => d['coord'][1]})`)
    //     .attr('width', 20)
    //     .attr('height', 20);
        
    // group.selectAll('g')
    //     .each(TextElement)

    
    // selection.enter()
    //     .append('text')
    //         .attr('x', d => d['coord'][0])
    //         .attr('y', d => d['coord'][1])
    //         .attr('width', 20)
    //         .attr('height', 20)
    //         .attr('font-size', '10px')
    //         .text(d => d['data'])
    //         .attr('fill','red')
    //         .style("text-anchor", "middle");

    
}

function appendCircle(){
    d3.select(this)
                .append('circle')
                .attr('r',10)
                .attr('cx', d => d['coord'][0])
                .attr('cy', d => d['coord'][1])
                .attr('fill','red')
                .attr('stroke','black');
}

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                Elem Path                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//i< num of sections, rInnner, rOuter
//o> arr of arcs
export function SplitArc(n,radiusIn,radiusOut){
    let arr = [];
    for(let x = 0; x<n;x++) {
        arr.push(
            d3.arc()
                .innerRadius(radiusIn)
                .outerRadius(radiusOut)
                .startAngle( x * 2 * Math.PI /n ) 
                .endAngle( (x+1) * 2 * Math.PI /n )
        );
    }
    return arr;
}
