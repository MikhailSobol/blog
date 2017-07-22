$(document).ready(function () {
  $(window).scroll(function() {
    var scroll = $(this).scrollTop();
    
    move_text_with_scroll(scroll);
    make_active_with_scroll(scroll);

    add_is_showing('.about-wrapper', '.about-section', scroll);
    add_is_showing('.why-section', '.why-section', scroll);
  });

  scroll_to_section_on_click('.header-wrapper', '.home-scroll', 0);
  scroll_to_section_on_click('.about-wrapper', '.about-scroll', -100);
  scroll_to_section_on_click('.why-wrapper', '.why-scroll', -100);
  scroll_to_section_on_click('.posts-wrapper', '.posts-scroll', -100);
});
