function reset_map() {
  $('#frbr-entity').val('NONE');
  $('#frbr-entity-property-name').attr('value','');
  $('#frbr-entity-property-uri').attr('value','');
}

function save_map() {
  var data = 'entity=' + $('#frbr-entity option:selected').val();
  data += '&prop=' + $('#frbr-entity-property-name').val();
  data += '&propuri=' + $('#frbr-entity-property-uri').val();
  data += '&schema=' + $('#metadata-schema').val();
  data += '&schemauri=' + $('#metadata-schema-uri').val();
  data += '&ordered=' + $('#orderedCollection checkbox:checked').val();
  
  //alert(data);		
}
