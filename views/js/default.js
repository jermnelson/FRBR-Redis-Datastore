function loadDetail(slide_id) {
  alert("Slides are " + slides);
  var slide = slides[slide_id];
  
  $('#main-content h1').attr('text',slide['title']);

}

function frbrDisplay() {
  var paper = Raphael("frbr-redis-ds-illustration");

  paper.clear();
  var work = paper.rect(10,10,40,40);
  work.attr("stroke","#600");
  //var expr = paper.rect(15,15,45,45);
  //var manifestation = paper.rect(20,20,50,50);
  //var item = paper.rect(25,25,55,55);
  
}
