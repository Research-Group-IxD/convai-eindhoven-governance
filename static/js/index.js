window.HELP_IMPROVE_VIDEOJS = false;


$(document).ready(function() {
    // Check for click events on the navbar burger icon
  // Function to check if an element is in the viewport
    function isElementInViewport(el) {
        var $el = $(el);
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        var elTop = $el.offset().top;
        var elBottom = elTop + $el.outerHeight();
        var buffer = 50; 
        
        return elBottom > viewportTop + buffer && elTop < viewportBottom - buffer;
    }

    // Function to run the fade-in logic
    function checkFade() {
        $('.fade-in-target').each(function() {
            // Check if the element is in the viewport for the fade-in effect
            if (isElementInViewport(this)) {
                $(this).addClass('is-visible');
            }
        });
    }

    // Run on load and on scroll
    checkFade();
    $(window).on('scroll', checkFade); 
	
    var options = {
			slidesToScroll: 1,
			slidesToShow: 1,
			loop: true,
			infinite: true,
			autoplay: true,
			autoplaySpeed: 5000,
    }

		// Initialize all div with carousel class
    var carousels = bulmaCarousel.attach('.carousel', options);
	
    bulmaSlider.attach();

})
