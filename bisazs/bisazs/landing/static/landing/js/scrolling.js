$(function () {

	//bottstrap scrollspy
	$('body').scrollspy({
		target: 'navbar'
	})

	//smooth scrolling
	$('.top-menu a').bind('click', function () {
		$('html, body').stop().animate({
			scrollTop: $($(this).attr('href')).offset().top - 100
		}, 1500, 'easeInOutExpo');
		event.preventDefault();
	});

	//initialize WOW
	new WOW().init();
	
});