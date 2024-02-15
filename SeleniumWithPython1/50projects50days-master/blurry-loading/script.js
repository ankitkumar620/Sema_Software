const loadText = document.querySelector('.loading-text');
const bg = document.querySelector('.bg');

let load = 0;

// Use requestAnimationFrame for smoother animations
function blurring() {
  load++;

  if (load > 99) {
    return; // Don't proceed if already reached 100%
  }

  // Update the loading text
  loadText.innerText = `${load}%`;

  // Calculate opacity and blur using the scale function
  const opacityValue = scale(load, 0, 100, 1, 0);
  const blurValue = scale(load, 0, 100, 30, 0);

  // Apply styles
  loadText.style.opacity = opacityValue;
  bg.style.filter = `blur(${blurValue}px)`;

  // Continue the animation
  requestAnimationFrame(blurring);
}

// Start the animation
requestAnimationFrame(blurring);

// Function to map a range of numbers to another range
function scale(num, in_min, in_max, out_min, out_max) {
  return ((num - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min;
}
