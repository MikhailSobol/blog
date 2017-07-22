function make_active($class_to_become_active) {
  $('.active').removeClass('active');
  $($class_to_become_active).addClass('active');
}

function add_is_showing ($elem_class, $add_to_class, $scroll_val) {
  if ($scroll_val > $($elem_class).offset().top - 600) {
    $($add_to_class).each(function(i) {
      setTimeout(function() {
        $($add_to_class).eq(i).addClass('is-showing');
      }, 150 * (i + 1));
    })
  }
}

function move_text_with_scroll($scroll) {
  if ($scroll < 300) {
    $('.header-text-wrapper').css({
      'transform': 'translate(0px, ' + $scroll / 8 + '%)'
    });
  }
}

function make_class_active_with_scroll($scroll, $class, $to_be_active) {
  if ($scroll >= $($class).offset().top - 250) {
    console.log('asdf');
    make_active($to_be_active);
  }
}

function make_active_with_scroll($scroll) {
  make_class_active_with_scroll($scroll, '.header-wrapper', '.home-scroll');
  make_class_active_with_scroll($scroll, '.about-wrapper', '.about-scroll');
  make_class_active_with_scroll($scroll, '.why-wrapper', '.why-scroll');
  make_class_active_with_scroll($scroll, '.posts-wrapper', '.posts-scroll');
}

function scroll_to_section_on_click($section, $button, $coef) {
  $($button).click(function() {
    $('html, body').animate({
      scrollTop: $($section).offset().top + $coef
    }, 2000);
  });    

}

