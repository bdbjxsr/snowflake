$(document).ready(function(){
  $('#maintab').tab();
  $('.menutop').popup({
    position   : 'bottom left',
    boundary:'body',
    delay: {
      show: 200,
      hide: 200
    }
  });
});