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
    $('body').toggleClass('overflowHide')
 });

  $('#cardNicolas').click(function() {
    $('#contentModal').html(nicolasDes);
  })

  $('#cardTanguy').click(function() {
    $('#contentModal').html(tanguyDes);
  })

  $('#cardLise').click(function() {
    $('#contentModal').html(liseDes);
  })

  $('#cardHenry').click(function() {
    $('#contentModal').html(henryDes);
  })

  $('#cardMathias').click(function() {
    $('#contentModal').html(mathiasDes);
  })

  $('#cardCorentin').click(function() {
    $('#contentModal').html(corentinDes);
  })

  $('#cardAntonin').click(function() {
    $('#contentModal').html(antoninDes);
  })

  $('#cardMathieu').click(function() {
    $('#contentModal').html(matthieuDes);
  })

  $('#cardAnthea').click(function() {
    $('#contentModal').html(antheaDes);
  })

  $('#cardAntoine').click(function() {
    $('#contentModal').html(antoineDes);
  })

 $('.btn-close').click(function() {
  $('.modal-wrapper').removeClass('open');
  $('#team').removeClass('blur-it');
  $('#Jarvys').removeClass('blur-it');
  $('#header').removeClass('blur-it');
  $('#footer').removeClass('hidden');
  $('#features').removeClass('blur-it');
  $('.navbar').removeClass('hidden');
  $('body').removeClass('overflowHide')
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

var nicolasDes = '<div><img class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/licorne.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/nicolas_goureau.jpg\') }}"/></div><div class="contentModal"> <h3>Nicolas Goureau</h3><p><span class="bold">Son rôle :</span> Nicolas est à l\' initiative du projet. Chef de projet, il assure la cohésion et le partage des tâches entre les différentes équipes. </p><p> <span class="bold">Ses passions :</span> Les licornes et le quinoa</p><p><span class="bold">Poisson ascendant Cancer</span>, vous pouvez l\'amadouer avec des cookies moelleux.</p></div>';
var tanguyDes = '<div><img id="backgroundModalTanguy" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/guitare.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/tanguy_badier.jpg\') }}"/></div><div class="contentModal"> <h3>Tanguy Badier</h3><p><span class="bold">Son rôle :</span> Tanguy est l\'intégrateur web de l\'équipe. Il réalise l\'ensemble du site web destiné à la présentation de Jarvys. </p><p> <span class="bold">Ses passions :</span> Les cordes et sa magnifique Opel Corsa</p><p><span class="bold">Taureau ascendant Gémeau</span>, Il est corruptible à base de whisky.</p></div>';
var liseDes = '<div><img id="backgroundModalLise" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/oiseau.png\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/lise_monfort.jpg\') }}"/></div><div class="contentModal"> <h3>Lise Monfort</h3><p><span class="bold">Son rôle :</span> Lise est notre maitrise d\'ouvrage. Elle réalise la documentation fonctionnelle, et participe à l\'élaboration des différentes interfaces utilisateur. </p><p> <span class="bold">Ses passions :</span> L\'Opel Corsa de Tanguy et Kog\'Maw monarque</p><p><span class="bold">Cancer ascendant Vierge</span>, elle est facilement attendrie par des images d\'oiseaux.</p></div>';
var henryDes = '<div><img id="backgroundModalLise" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/salt.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/henry_maisonneuve.jpg\') }}"/></div><div class="contentModal"> <h3>Henry Maisonneuve</h3><p><span class="bold">Son rôle :</span> Henry est un concepteur développeur IONIC. Il s\'occupe de la réalisation de l\'application mobile. </p><p> <span class="bold">Ses passions :</span> Mathias et Monster Hunter World</p><p><span class="bold">Verseau ascendant Vierge</span>, plus facile à trigger qu\'une féministe.</p></div>';
var mathiasDes = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/dragodinde.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/mathias_loiret.jpg\') }}"/></div><div class="contentModal" id="contentModalMathias"> <h3>Mathias Loiret</h3><p><span class="bold">Son rôle :</span> Mathias est un concepteur développeur IONIC. Il s\'occupe de la réalisation de l\'application mobile. </p><p> <span class="bold">Ses passions :</span> Henry et la trotinette électrique</p><p><span class="bold">Taureau ascendant Cancer</span>, inconditionel du Quinoa.</p></div>';
var corentinDes = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/chocobo.jpg\') }}"/> <img class="profileModal" id="imageCorentinModal" src="{{ url_for(\'static\', filename=\'images/corentin_lemarchand.jpg\') }}"/></div><div class="contentModal" id="contentModalCorentin"> <h3>Corentin Lemarchand</h3><p><span class="bold">Son rôle :</span> Corentin est un graphiste et designer. Il s\'occupe de la réalisation des différents visuels, images, et icônes. </p><p> <span class="bold">Ses passions :</span> Le coloriage et Dofus</p><p><span class="bold">Poisson ascendant Cancer</span>, déteste les pédiluves.</p></div>';
var antoninDes  = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/crab.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/antonin_joulie.jpg\') }}"/></div><div class="contentModal"> <h3>Antonin Joulie</h3><p><span class="bold">Son rôle :</span> Antonin est un développeur concepteur Python. Il s\'occupe de la réalisation de l\'ensemble du back de l\'application. </p><p> <span class="bold">Ses passions :</span> les collines et le roller</p><p><span class="bold">Scorpion ascendant Balance</span>, il connaît le chemin</p></div>';
var matthieuDes  = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/singe.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/matthieu_fournier.jpg\') }}"/></div><div class="contentModal"> <h3>Matthieu Fournier</h3><p><span class="bold">Son rôle :</span> Matthieu est un développeur concepteur Python. Il s\'occupe de la réalisation de l\'ensemble du back de l\'application. </p><p> <span class="bold">Ses passions :</span> briser des coeurs et le jour du seigneur</p><p><span class="bold">Gémeaux ascendant Lion</span>, il se blesse dans sa confusion</p></div>';
var antheaDes = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/cute.jpg\') }}"/> <img class="profileModal" id="imageCorentinModal" src="{{ url_for(\'static\', filename=\'images/anthea_vivion.jpg\') }}"/></div><div class="contentModal" id="contentModalCorentin"> <h3>Anthea Vivion</h3><p><span class="bold">Son rôle :</span> Anthea est une graphiste et designer. Elle s\'occupe de la réalisation des différents visuels, images, et icônes. </p><p> <span class="bold">Ses passions :</span> les labradors et Yves Saint Laurent </p><p><span class="bold">??</span>, en fait, on sait pas trop.</p></div>';
var antoineDes  = '<div><img id="backgroundModalMathias" class="backgroundModal" src="{{ url_for(\'static\', filename=\'images/screen.jpg\') }}"/> <img class="profileModal" src="{{ url_for(\'static\', filename=\'images/antoine_gosset.jpg\') }}"/></div><div class="contentModal"> <h3>Antoine Gosset</h3><p><span class="bold">Son rôle :</span> Antoine est un développeur concepteur Python. Il s\'occupe de la réalisation de l\'ensemble du back de l\'application. </p><p> <span class="bold">Ses passions :</span> Le riz/dinde et pousser à la salle.</p><p><span class="bold">Poisson ascendant ?</span>, rageux de base</p></div>';