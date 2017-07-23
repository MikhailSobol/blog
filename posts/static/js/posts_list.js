$(document).ready(function() {
  $(window).scroll(function() {
    var scroll = $(this).scrollTop();
    add_is_showing('.posts-wrapper > .container > .row', '.post',
     scroll);
  });

  scroll_to_section_on_click('.header-wrapper', '.home-scroll', 0);

  $.each( jQuery('.carousel .item'), function( i, val ) {
    $(this).css('background-image','url('+$(this).find('img').attr('src')+')').css('background-size','cover').find('img').css('visibility','hidden');
  })

});
