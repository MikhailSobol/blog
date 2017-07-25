$(document).ready(function() {
	$(window).scroll(function() {
		var scroll = $(this).scrollTop();
		move_text_with_scroll(scroll);
	})
	scroll_to_section_on_click('.header-wrapper', '.home-scroll', 0);
})