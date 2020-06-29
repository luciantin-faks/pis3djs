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
    text.map((el,i) => { data.push({'data':el,'coord':path[i]})});
    // console.log(data)
    
    let selection = group.selectAll().data(data);

    selection.enter()
        .append('circle')
            .attr('r',20)
            .attr('cx', d => d['coord'][0])
            .attr('cy', d => d['coord'][1])
            .attr('fill','black')
            .attr('stroke','black');
    
    selection.enter()
        .append('text')
            .attr('x', d => d['coord'][0])
            .attr('y', d => d['coord'][1])
            .attr('dy', '0.33em')
            .text(d => d['data'])
            .attr('fill','red')
            .style("text-anchor", "middle");
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
