function BrowseDisplay(call_number) {
  var data = 'number=' + call_number;
  alert("IN BROWSE DISPLAY");
  $.ajax({
    url:'/json/',
    data:data,
    success: function(response) {

    }
  });

}
