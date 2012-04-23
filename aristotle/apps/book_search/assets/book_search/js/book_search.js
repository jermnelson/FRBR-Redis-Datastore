function ChangeSearchBookText(btn_text) {
 $('#searchby').attr('html',btn_text);
 $('#searchby').val(btn_text);
 var search_char = btn_text.charAt(7);
 switch(search_char) {
  case 'A':
   $('#search-type').val("author_search");
   break;
  case 'J':
   ${'#search-type').val("title_search");
  case 'K':
   ${'#search-type').val("search");
  case 'S':
   ${'#search-type').val("subject_search");
  case 'T':
   ${'#search-type').val("title_search");
}
