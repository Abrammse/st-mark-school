const slides = document.querySelectorAll('.card-banner-slider figure');
let currentSlide = 0;

// Set first slide as active
slides[0].classList.add('active');

// Set interval to auto-advance slides
setInterval(() => {
  let nextSlide = currentSlide + 1;
  if (nextSlide >= slides.length) {
    nextSlide = 0;
  }
  goToSlide(nextSlide);
}, 5000);

function goToSlide(slideIndex) {
  slides[currentSlide].classList.remove('active');
  slides[slideIndex].classList.add('active');
  currentSlide = slideIndex;
}