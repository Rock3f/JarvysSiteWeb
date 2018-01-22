$(document).ready(function(){
  // Initialize Tooltip
  $('[data-toggle="tooltip"]').tooltip(); 
	
	var $window = $(window);

    if ($window.width() > 767) {
        new WOW().init();
    }
	
	$(window).scroll( function() { 
		$('#scrollUp').css("display", "block");
	});
  
  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a, #scrollUp").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {

      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
		$('#scrollUp').css("display", "none")
        window.location.hash = hash;
      });
    } // End if
  });
})