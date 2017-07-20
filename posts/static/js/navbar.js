$(document).ready(function () {
  $(window).scroll(function() {
    var scroll = $(this).scrollTop();

    if (scroll > 140) {
      $(".navbar-inverse")
      .removeClass("navbar-inverse-background-transparent");
    }

    if (scroll < 300) {
      $(".navbar-inverse")
      .addClass("navbar-inverse-background-transparent");
    }
  });
});
