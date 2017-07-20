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

    if (scroll > 1100 && scroll < 1800) {
      $(".posts-text-wrapper").css({
        "transform": "translate(0px, " + (scroll - 1500) / 8 + "%)"
      });
    }

    add_is_showing(".about-wrapper", ".about-section", scroll);
    add_is_showing(".why-section", ".why-section", scroll);

    // $("#click").click(function (){
      // $('html, body').animate({
        // scrollTop: $("#div1").offset().top
      // }, 2000);
    // });


  });

  $(".home-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".header-wrapper").offset().top
    }, 2000);

    $('.active').removeClass('active');
    $('.home-scroll').addClass('active');
  });    

  $(".about-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".about-wrapper").offset().top - 100
    }, 2000);

    $('.active').removeClass('active');
    $('.about-scroll').addClass('active');
  });    

  $(".why-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".why-wrapper").offset().top - 100
    }, 1500);

    $('.active').removeClass('active');
    $('.why-scroll').addClass('active');
  });    

  $(".posts-scroll").click(function() {
    $('html, body').animate({
      scrollTop: $(".posts-wrapper").offset().top - 100
    }, 1500);

    $('.active').removeClass('active');
    $('.posts-scroll').addClass('active');
  });    
});
