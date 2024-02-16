const body = document.body;
const slides = document.querySelectorAll('.slide');
const leftBtn = document.getElementById('left');
const rightBtn = document.getElementById('right');

let activeSlide = 0;

rightBtn.addEventListener('click', () => {
  changeSlide(1);
});

leftBtn.addEventListener('click', () => {
  changeSlide(-1);
});

function changeSlide(direction) {
  activeSlide += direction;

  if (activeSlide > slides.length - 1) {
    activeSlide = 0;
  } else if (activeSlide < 0) {
    activeSlide = slides.length - 1;
  }

  updateSlideAppearance();
}

function updateSlideAppearance() {
  setBgToBody();
  setActiveSlide();
}

function setBgToBody() {
  body.style.backgroundImage = slides[activeSlide].style.backgroundImage;
}

function setActiveSlide() {
  slides.forEach((slide) => slide.classList.remove('active'));
  slides[activeSlide].classList.add('active');
}
