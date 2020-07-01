// https://stackoverflow.com/questions/48429014/d3-text-wrap-with-text-anchor-middle

export function TextElement(d,i,){

}


function wrap(text, width) {
    text.each(function() {
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
        if (tspan.node().getComputedTextLength() > width) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
        }
      }
    });
  }















  // EXAMPLE 


// let dat = [1,2,3,4,5]


// let textEl = svg.append('g');

// textEl.selectAll('text').data(dat)
//     .enter()
//     .append('text')
//         .attr("x", (d,i) => 50*i)
//         .attr("y", (d,i) => 100*i)
//         .attr("text-anchor", "middle")
//         .attr("font-family", "sans-serif")
//         .text("Nabava i izlazna logistika")
//         .each(function() {
//             let text = d3.select(this),
//               words = text.text().split(/\s+/).reverse(),
//               word,
//               line = [],
//               lineNumber = 0,
//               lineHeight = 1.1, // ems
//               x = text.attr("x"),
//               y = text.attr("y"),
//               dy = 1.1,
//               tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dy", dy + "em");
//             while (word = words.pop()) {
//               line.push(word);
//               tspan.text(line.join(" "));
//               if (tspan.node().getComputedTextLength() > 100) { //100 - width od jedne lajne
//                 line.pop();
//                 tspan.text(line.join(" "));
//                 line = [word];
//                 tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
//               }
//             }
//         });
