var WIDTH = 640;
var HEIGHT = 480;
var SPACER = 15;


function drawWEMIDemo() {
  $("#visualization").attr("html","");
  var paper = Raphael("visualization",WIDTH,HEIGHT);
  var item_plane = paper.rect(75,140,270,190);
  item_plane.attr("stroke","#600");
  item_plane.attr("fill","#F3C73f");
  var manifestation_plane = paper.rect(95,120,270,190);
  manifestation_plane.attr("stroke","#0064CD");
  manifestation_plane.attr("fill","green");
  var expression_plane = paper.rect(115,100,270,190);
  expression_plane.attr("stroke","#0064CD");
  expression_plane.attr("fill","brown");
  var work_plane = paper.rect(135,80,270,190);
  work_plane.attr("stroke","#0064CD");
  work_plane.attr("fill","#049CDB");
  var work_label = paper.text(240,160,"frbr_rda:Work");
  
  var mods_brane = paper.path("M155 60L60 120");
  


}
