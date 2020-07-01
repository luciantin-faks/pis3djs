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
            .attr('fill','green')
            .attr('stroke','green');
    
    
// let textEl = svg.append('g');

    group.selectAll('g')        
            .append('text')
                .attr("x",  d => d['coord'][0])
                .attr("y",  d => d['coord'][1])
                .attr("text-anchor", "middle")
                .attr("font-family", "sans-serif")
                .style("font-size", "10px")
                .text(d=>d['data'])
                .each(function() {
                    let text = d3.select(this),
                    words = text.text().split(/\s+/).reverse(),
                    word,
                    line = [],
                    lineNumber = 0,
                    lineHeight = 1.1, // ems
                    x = text.attr("x"),
                    y = text.attr("y"),
                    dy = 1.1,
                    tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dy", dy + "em");
                    while (word = words.pop()) {
                        line.push(word);
                        tspan.text(line.join(" "));
                        if (tspan.node().getComputedTextLength() > 100) { //100 - width od jedne lajne
                            line.pop();
                            tspan.text(line.join(" "));
                            line = [word];
                            tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
                        }
                    }
                    console.log(d3.select(this)['_groups'][0][0].getBoundingClientRect())
                    let offset = d3.select(this)['_groups'][0][0].getBoundingClientRect();
                    d3.select(this).attr('transform',`translate(${0},${-offset['height']/2})`);
                });

    // group.selectAll('g')
    //     .each(appendCircle)

    // group.selectAll('g')
    //     .each(TextElement)

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
