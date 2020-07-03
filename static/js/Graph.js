import { TextToContainer } from "/static/js/TextToContainer.js"

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
export function GraphPopulate(text, path, group, onClickFun){
   
    let data = [];
    text.map((el,i) => { data.push({'data':el,'coord':[path[i][0]+100,path[i][1]+100] })});
    // console.log(data)
    
    let selection = group.selectAll().data(data);

    selection.enter()
        .append('g')
        .on('click',onClickFun)
        .attr('transform',d => { return `translate( ${ d['coord'][0] },${ d['coord'][1] })`});;

    let groups =  group.selectAll('g');

    groups.append('circle')
        .attr('r',20)
        // .attr('cx', d => d['coord'][0])
        // .attr('cy', d => d['coord'][1])
        .attr('fill','green')
        .attr('cx', 0)
        .attr('cy', 0)
        .attr('stroke','green');
   
    groups.append('text')
        // .attr("x",  d => d['coord'][0])
        // .attr("y",  d => d['coord'][1])
        .attr("x", 0)
        .attr("y",  0)
        .attr("text-anchor", "middle")
        .attr("font-family", "sans-serif")
        .style("font-size", "10px")
        .text(d=>d['data'])
        .each(TextToContainer(100,1));
    
   
    
    return groups;    
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
