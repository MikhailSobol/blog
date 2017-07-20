function make_active($class_to_become_active) {
  $('.active').removeClass('active');
  $($class_to_become_active).addClass('active');
}

function add_is_showing ($elem_class, $add_to_class, $scroll_val) {
  if ($scroll_val > $($elem_class).offset().top - 600) {
    $($add_to_class).each(function(i) {
      setTimeout(function() {
        $($add_to_class).eq(i).addClass("is-showing");
      }, 75 * (i + 1));
    })
  }
}

function move_text_with_scroll($scroll) {
  if ($scroll < 300) {
    $(".header-text-wrapper").css({
      "transform": "translate(0px, " + $scroll / 8 + "%)"
    });
  }
    
  if ($scroll > 1100 && $scroll < 1800) {
    $(".posts-text-wrapper").css({
      "transform": "translate(0px, " + ($scroll - 1500) / 8 + "%)"
    });
  }
}

$(document).ready(function () {
  $(window).scroll(function() {
    var scroll = $(this).scrollTop();
    
    move_text_with_scroll(scroll);

    add_is_showing(".about-wrapper", ".about-section", scroll);
    add_is_showing(".why-section", ".why-section", scroll);
  });

  $(".home-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".header-wrapper").offset().top
    }, 2000);

    make_active('.home-scroll');
  });    

  $(".about-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".about-wrapper").offset().top - 100
    }, 2000);

    make_active('.about-scroll');
  });    

  $(".why-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".why-wrapper").offset().top - 100
    }, 1500);

    make_active('.why-scroll');
  });    

  $(".posts-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".posts-wrapper").offset().top - 100
    }, 1500);

    make_active('.posts-scroll');
  });    
});
