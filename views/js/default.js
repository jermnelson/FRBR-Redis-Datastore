function loadDetail(slide_id) {
  alert("Slides are " + slides);
  var slide = slides[slide_id];
  
  $('#main-content h1').attr('text',slide['title']);

}
