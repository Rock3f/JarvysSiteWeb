$(document).ready(function(){
  // Initialize Tooltip
  $('[data-toggle="tooltip"]').tooltip(); 
	
	var $window = $(window);

    if ($window.width() > 767) {
        new WOW().init();
    }
  
    new SineWaveGenerator({
      el: document.getElementById('waves'),
      
      speed: 4,
      
      waves: [
        {
          timeModifier: 1,
          lineWidth: 3,
          amplitude: 150,
          wavelength: 200,
          segmentLength: 20,
    //       strokeStyle: 'rgba(255, 255, 255, 0.5)'
        },
        {
          timeModifier: 1,
          lineWidth: 2,
          amplitude: 150,
          wavelength: 100,
    //       strokeStyle: 'rgba(255, 255, 255, 0.3)'
        },
        {
          timeModifier: 1,
          lineWidth: 1,
          amplitude: -150,
          wavelength: 50,
          segmentLength: 10,
    //       strokeStyle: 'rgba(255, 255, 255, 0.2)'
        },
        {
          timeModifier: 1,
          lineWidth: 0.5,
          amplitude: -100,
          wavelength: 100,
          segmentLength: 10,
    //       strokeStyle: 'rgba(255, 255, 255, 0.1)'
        }
      ],
      
      initialize: function (){
    
      },
      
      resizeEvent: function() {
        var gradient = this.ctx.createLinearGradient(0, 0, this.width, 0);
        gradient.addColorStop(0,"rgba(0, 0, 0, 0)");
        gradient.addColorStop(0.5,"rgba(255, 255, 255, 0.5)");
        gradient.addColorStop(1,"rgba(0, 0, 0, 0)");
        
        var index = -1;
        var length = this.waves.length;
        while(++index < length){
          this.waves[index].strokeStyle = gradient;
        }
        
        // Clean Up
        index = void 0;
        length = void 0;
        gradient = void 0;
      }
    });
	
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
       if(window.pageYOffset == 0)
       {
        $('#scrollUp').css("display", "none")
       }
		
        window.location.hash = hash;
      });
    } // End if
  });

  $('.card').click(function() {
    $('.modal-wrapper').toggleClass('open');
    $('#team').toggleClass('blur-it');
    $('#Jarvys').toggleClass('blur-it');
    $('#header').toggleClass('blur-it');
    $('#footer').toggleClass('hidden');
    $('#features').toggleClass('blur-it');
    $('.navbar').toggleClass('hidden');
    $('#scrollUp').toggleClass('hidden');
    $('body').toggleClass('overflowHide')
 });

  $('#cardNicolas').click(function() {
    $('#modalGoureau').removeClass('hidden');
  })

  $('#cardTanguy').click(function() {
    $('#modalBadier').removeClass('hidden');
  })

  $('#cardLise').click(function() {
    $('#modalMonfort').removeClass('hidden');
  })

  $('#cardHenry').click(function() {
    $('#modalMaisonneuve').removeClass('hidden');
  })

  $('#cardMathias').click(function() {
    $('#modalLoiret').removeClass('hidden');
  })

  $('#cardCorentin').click(function() {
    $('#modalLeMarchand').removeClass('hidden');
  })

  $('#cardAntonin').click(function() {
    $('#modalJoulie').removeClass('hidden');
  })

  $('#cardMathieu').click(function() {
    $('#modalFournier').removeClass('hidden');
  })

  $('#cardAnthea').click(function() {
    $('#modalVivion').removeClass('hidden');
  })

  $('#cardAntoine').click(function() {
    $('#modalGosset').removeClass('hidden');
  })

 $('.btn-close').click(function() {
  $('.modal-wrapper').removeClass('open');
  $('#team').removeClass('blur-it');
  $('#Jarvys').removeClass('blur-it');
  $('#header').removeClass('blur-it');
  $('#footer').removeClass('hidden');
  $('#features').removeClass('blur-it');
  $('.navbar').removeClass('hidden');
  $('#scrollUp').removeClass('hidden');
  $('body').removeClass('overflowHide')

  if(!$('#modalGoureau').hasClass("hidden")){
    $('#modalGoureau').toggleClass('hidden');
  }

  if(!$('#modalBadier').hasClass("hidden")){
    $('#modalBadier').toggleClass('hidden');
  }

  if(!$('#modalMonfort').hasClass("hidden")){
    $('#modalMonfort').toggleClass('hidden');
  }

  if(!$('#modalMaisonneuve').hasClass("hidden")){
    $('#modalMaisonneuve').toggleClass('hidden');
  }

  if(!$('#modalLoiret').hasClass("hidden")){
    $('#modalLoiret').toggleClass('hidden');
  }

  if(!$('#modalLeMarchand').hasClass("hidden")){
    $('#modalLeMarchand').toggleClass('hidden');
  }

  if(!$('#modalJoulie').hasClass("hidden")){
    $('#modalJoulie').toggleClass('hidden');
  }

  if(!$('#modalFournier').hasClass("hidden")){
    $('#modalFournier').toggleClass('hidden');
  }

  if(!$('#modalVivion').hasClass("hidden")){
    $('#modalVivion').toggleClass('hidden');
  }

  if(!$('#modalGosset').hasClass("hidden")){
    $('#modalGosset').toggleClass('hidden');
  }
 });
})

    /**
 * Generates multiple customizable animated sines waves
 * using a canvas element. Supports retina displays and
 * limited mobile support
 *
 * I've created a seperate library based on this pen. 
 * Check it out at https://github.com/isuttell/sine-waves
 */
function SineWaveGenerator(options) {
  $.extend(this, options || {});
  
  if(!this.el) { throw "No Canvas Selected"; }
  this.ctx = this.el.getContext('2d');
  
  if(!this.waves.length) { throw "No waves specified"; }
  
  // Internal
  this._resizeWidth();
  window.addEventListener('resize', this._resizeWidth.bind(this));
  // User
  this.resizeEvent();
  window.addEventListener('resize', this.resizeEvent.bind(this));
  
  if(typeof this.initialize === 'function') {
    this.initialize.call(this);
  }
  // Start the magic
  this.loop();
}

// Defaults
SineWaveGenerator.prototype.speed = 10;
SineWaveGenerator.prototype.amplitude = 50;
SineWaveGenerator.prototype.wavelength = 50;
SineWaveGenerator.prototype.segmentLength = 10;

SineWaveGenerator.prototype.lineWidth = 2;
SineWaveGenerator.prototype.strokeStyle  = 'rgba(255, 255, 255, 0.2)';

SineWaveGenerator.prototype.resizeEvent = function() {};

// fill the screen
SineWaveGenerator.prototype._resizeWidth = function() {
  this.dpr = window.devicePixelRatio || 1;
  
  this.width = this.el.width = window.innerWidth ;
  this.height = this.el.height = window.innerHeight * this.dpr;
  this.el.style.width = window.innerWidth - 150  + 'px';
  this.el.style.height = window.innerHeight - 150 + 'px';
  
  this.waveWidth = this.width * 0.95;
  this.waveLeft = this.width * 0.025;
}

SineWaveGenerator.prototype.clear = function () {
  this.ctx.clearRect(0, 0, this.width, this.height);
}

SineWaveGenerator.prototype.time = 0;

SineWaveGenerator.prototype.update = function(time) {  
  this.time = this.time - 0.007;
  if(typeof time === 'undefined') {
    time = this.time;
  }

  var index = -1;
  var length = this.waves.length;

  while(++index < length) {
    var timeModifier = this.waves[index].timeModifier || 1;
    this.drawSine(time * timeModifier, this.waves[index]);
  }
  index = void 0;
  length = void 0;
}

// Constants
var PI2 = Math.PI * 2;
var HALFPI = Math.PI / 2;

SineWaveGenerator.prototype.ease = function(percent, amplitude) {
  return amplitude * (Math.sin(percent * PI2 - HALFPI) + 1) * 0.5;
}

SineWaveGenerator.prototype.drawSine = function(time, options) {
  options = options || {};
  amplitude = options.amplitude || this.amplitude;
  wavelength = options.wavelength || this.wavelength;
  lineWidth = options.lineWidth || this.lineWidth;
  strokeStyle = options.strokeStyle || this.strokeStyle;
  segmentLength = options.segmentLength || this.segmentLength;
  
  var x = time;
  var y = 0;  
  var amp = this.amplitude;
 
  // Center the waves
  var yAxis = this.height / 2; 
  
  // Styles
  this.ctx.lineWidth = lineWidth * this.dpr;
  this.ctx.strokeStyle = strokeStyle;
  this.ctx.lineCap = 'round';
  this.ctx.lineJoin = 'round';
  this.ctx.beginPath();
  
  // Starting Line
  this.ctx.moveTo(0, yAxis);
  this.ctx.lineTo(this.waveLeft, yAxis);
  
  for(var i = 0; i < this.waveWidth; i += segmentLength) {
    x = (time * this.speed) + (-yAxis + i) / wavelength; 
    y = Math.sin(x); 
    
    // Easing
    amp = this.ease(i / this.waveWidth, amplitude); 
    
    this.ctx.lineTo(i + this.waveLeft, amp * y + yAxis);
    
    amp = void 0;
  }
  
  // Ending Line
  this.ctx.lineTo(this.width, yAxis);
  
  // Stroke it
  this.ctx.stroke();
  
  // Clean up
  options = void 0;
  amplitude = void 0;
  wavelength = void 0;
  lineWidth = void 0;
  strokeStyle = void 0;
  segmentLength = void 0;
  x = void 0;
  y = void 0;
} 

SineWaveGenerator.prototype.loop = function() {
  this.clear();
  this.update();
  
  window.requestAnimationFrame(this.loop.bind(this));
}