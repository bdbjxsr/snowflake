$(document).ready(function(){
  $('#maintab').tab();
  $('.ui.dropdown').dropdown({
    on: 'hover',
    action:'select'
  });
$('.browse').popup({
    inline: true,
    hoverable  : true,
    position   : 'bottom left',
    delay: {
      show: 300,
      hide: 100
    }
  });

});