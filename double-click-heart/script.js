class LoveMe {
  constructor(loveMe, times) {
    this.loveMe = loveMe;
    this.times = times;
    this.clickTime = 0;
    this.timesClicked = 0;

    this.setup();
  }

  setup() {
    this.loveMe.addEventListener('click', (e) => this.handleDoubleClick(e));
  }

  handleDoubleClick(e) {
    if (this.clickTime === 0) {
      this.clickTime = new Date().getTime();
    } else {
      if (new Date().getTime() - this.clickTime < 800) {
        this.createHeart(e);
        this.clickTime = 0;
      } else {
        this.clickTime = new Date().getTime();
      }
    }
  }

  createHeart(e) {
    const heart = document.createElement('i');
    heart.classList.add('fas', 'fa-heart');

    const x = e.clientX;
    const y = e.clientY;

    const leftOffset = e.target.offsetLeft;
    const topOffset = e.target.offsetTop;

    const xInside = x - leftOffset;
    const yInside = y - topOffset;

    heart.style.top = `${yInside}px`;
    heart.style.left = `${xInside}px`;

    this.loveMe.appendChild(heart);

    this.times.innerHTML = ++this.timesClicked;

    setTimeout(() => heart.remove(), 1000);
  }
}

// Initialize LoveMe object
const loveMeElement = document.querySelector('.loveMe');
const timesElement = document.querySelector('#times');
const loveMeInstance = new LoveMe(loveMeElement, timesElement);
