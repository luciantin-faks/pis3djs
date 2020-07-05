import { TextToContainer } from "/static/js/TextToContainer.js"

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                IPS Graf                          \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\
/*
    new Graph(group,w,h)
        .setContainerStyle(style)
        .populate(TextArray);

*/

export class Graph{

    constructor(group,screenWidth,screenHeight){
        // this.textData = text; // text list
        this.group = group; // main group
        // this.dataIDfieldName = dataIDfieldName; // TODO
        this.subGraph = null;
        this.screenWidth = screenWidth;
        this.screenHeight = screenHeight;
        this.offX = 0;
        this.offY = 0;
        this.hasSubGraf = false;
    }

    SetContainerStyle(style){ this.style = style; return this;  }// container && path

    Populate(text){   //vraca selekciju svih podgrupa koje imaju element     
        // console.log(text);
        //init
        this.Clear();
        this.textData = text;
        this.FormatData();
        //


        let selection = this.group.selectAll().data(this.data);

        selection.enter()
            .append('g')
            .on('click', BindGraphClickEvent(this))
            .attr('transform',d => { return `translate( ${ d['coord'][0] },${ d['coord'][1] })`});;

        let groups =  this.group.selectAll('g');

        if(this.style.Ctype == 'circle'){
            this.groups.append('circle')
                .attr('r',20)
                .attr('fill',this.style.Cfill)
                .attr('stroke',this.style.Cstroke)
                .attr('cx', 0)
                .attr('cy', 0);
        }
        else if( this.style.Ctype == 'rect'){
            groups.append('rect')
                .attr('fill',this.style.Cfill)
                .attr('stroke',this.style.Cstroke)
                .attr('width',this.style.Cwidth)
                .attr('height',this.style.Cheight)
                .attr('x', -this.style.Cwidth/2)
                .attr('y', -this.style.Cheight/2);
        }
    
        groups.append('text')
            .attr("x", 0)
            .attr("y",  0)
            .attr("text-anchor", "middle")
            .attr("font-family", "sans-serif")
            .style("font-size", this.style.fontSize)
            .text(d=>d['data'])
            .each(TextToContainer(this.style.Cwidth-5,1));   
    
        this.TranslateGraphH();
        return this;    
    }

    Clear(){ this.group.selectAll('g').remove(); return this; }

    // setData(data){ this.data = data; return this;}

    SetupSubGraph(sub){this.hasSubGraf=true; this.subGraph = sub;  return this; }

    async PopulateSubGraph(withDataID){
        console.log(withDataID);
        let data = await this.DataSourceFun(withDataID);
        this.subGraph.Populate(data);
    }

    ClearSubGraph(){ this.subGraph.Clear(); return this;}

    // DataSourceFunction for given textId (just text) return array of text for subgraph 
    SetDataSource(dsFun){ this.DataSourceFun = dsFun; return this;}
    
    FormatData(){
        let path;
        if( this.style.Ptype == 'arc') path = SplitArc(this.textData.length,this.style.Prad,this.style.Prad+1);
        else if( this.style.Ptype == 'linX') path = SplitLineX(this.textData.length,this.style.Plen);
        else if( this.style.Ptype == 'linY') path = SplitLineY(this.textData.length,this.style.Plen);
    
        // console.log(this.style.Ptype)
        this.data = GraphDataFormat(   
            this.textData,
            path
            );
        return this;
    }

    //TODO
    TranslateGraphH(){  this.CenterGroup(this.offX,-this.GetGroupBBox()['height']/2  + this.offY) }
    
    CenterGroup(offX=0,offY=0){
        this.TranslateGroup(
            this.screenWidth/2   + offX,
            this.screenHeight/2  + offY
    )}

    GetGroupBBox(){ return this.group.node().getBBox(); }

    TranslateGroup(w,h){ this.group.attr('transform',`translate(${w},${h})`);  }
    
    SetXoff(offX){ this.offX = offX; return this;}
    SetYoff(offY){ this.offY = offY; return this;}
}



//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                Elem Path                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

export function GraphDataFormat(text,path){ 
    let data = []; 
    text.map((el,i) => { data.push({'data':el,'coord':[path[i][0],path[i][1]] })});
    return data;
}

//i< num of sections, rInnner, rOuter
//o> arr of arcs
export function SplitArc(n,radius){
    let arr = [];
    for(let x = 0; x<n;x++) {
        arr.push(
            d3.arc()
                .innerRadius(radius)
                .outerRadius(radius+1)
                .startAngle( x * 2 * Math.PI /n ) 
                .endAngle( (x+1) * 2 * Math.PI /n )
        );
    }
    return arr.map(el => el.centroid());
}



export function SplitLineX(n,len){
    let arr = Array.from(Array(n).keys());
    const step = len/n;
    arr = arr.map((el,i)=>{ return [ i*step , 0]; });
    // console.log(arr)
    return arr;
}

//koristi se i visina,
export function SplitLineY(n,len){
    let arr = Array.from(Array(n).keys());
    const step = len/n;
    arr = arr.map((el,i)=>{ return [ 0 , i*step]; });
    return arr;
}

//++++++++++++++++++++++++++++++++++++++++++++++++++\\
//                    Click                         \\
//++++++++++++++++++++++++++++++++++++++++++++++++++\\

function BindGraphClickEvent(graph){
    return function GraphClick(data,i){
        const parentG = d3.select(this.parentNode);  
        let isClicked = IsClicked(parentG); //dali je vec kliknut
        let LastNodeClickedID = parentG.attr('NodeClickedID');

        if(isClicked && LastNodeClickedID == data['data']) { //ako je opet klkunt isti
            parentG.selectAll('g')
                .transition()
                    // .attr("transform",d=> `translate(${d['coord'][0]},${d['coord'][1]})scale(1)`)
                    .style("opacity", 1)
                    .duration(500);  

            if(graph.hasSubGraf)graph.ClearSubGraph();

            parentG.attr('isClicked',null);
            console.log('vec klikunt isti')
        }
        else if(isClicked && LastNodeClickedID != data['data'] ){ //ako ClickID nije jednak a kliknulo se
                parentG.selectAll('g')
                    .transition()
                        // .attr("transform",d=> `translate(${d['coord'][0]},${d['coord'][1]})scale(1)`)
                        .style("opacity", 1)
                        // .duration(500);
                parentG.selectAll('g').filter(d=>d!=data)
                    .transition()
                        // .attr("transform",`translate(${data['coord'][0]},${data['coord'][1]})scale(0)`)
                        .style("opacity", 0.3)
                        .duration(500);  

            if(graph.hasSubGraf)graph.PopulateSubGraph(data['data']);

            parentG.attr('isClicked','');
            console.log('vec klikunt novi')
        }
        else if(!isClicked){
            parentG.selectAll('g')
                .transition().filter(d=>d!=data)
                    // .attr("transform",d=> `translate(${d['coord'][0]},${d['coord'][1]})scale(1)`)
                    .style("opacity", 0.3)
                    .duration(500);  

            if(graph.hasSubGraf)graph.PopulateSubGraph(data['data']);

            parentG.attr('isClicked','');
            console.log('klikunt')
        }
        parentG.attr('NodeClickedID',data['data']);
    }    
}

function IsClicked(node){
    const isClicked = node.attr('isClicked')
    if(isClicked == null) return false;
    else return true;
}
