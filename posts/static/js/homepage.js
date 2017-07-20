$(document).ready(function () {
  $(window).scroll(function() {
    var add_is_showing = function($elem_class, $add_to_class, $scroll_val) {
      if ($scroll_val > $($elem_class).offset().top - 600) {
        $($add_to_class).each(function(i) {
          setTimeout(function() {
            $($add_to_class).eq(i).addClass("is-showing");
          }, 75 * (i + 1));
        })
      }
    }

    var scroll = $(this).scrollTop();
    
    if (scroll < 300) {
      $(".header-text-wrapper").css({
        "transform": "translate(0px, " + scroll / 8 + "%)"
      });
    }

    if (scroll > 1500 && scroll < 1800) {
      console.log('lak;jsdf');
      $(".posts-text-wrapper").css({
        "transform": "translate(0px, " + (scroll - 1500) / 8 + "%)"
      });
    }

    add_is_showing(".about-wrapper", ".about-section", scroll);
    add_is_showing(".why-section", ".why-section", scroll);
  });
});
