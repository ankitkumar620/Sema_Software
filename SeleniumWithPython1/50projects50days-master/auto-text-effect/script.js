const textEl = document.getElementById('text');
const speedEl = document.getElementById('speed');
const text = 'We Love Programming!';
let idx = 0;
let speed = calculateSpeed();

writeText();

function writeText() {
  textEl.innerText = text.slice(0, idx);

  idx++;

  if (idx > text.length) {
    idx = 0;
  }

  setTimeout(writeText, speed);
}

function calculateSpeed() {
  return 300 / speedEl.value;
}

speedEl.addEventListener('input', () => {
  speed = calculateSpeed();
});

// Optionally, you can add event listeners for better control
// e.g., stop the animation when the user focuses on the text area
textEl.addEventListener('focus', () => {
  clearTimeout(timeoutId);
});

// Resume the animation when the user removes focus
textEl.addEventListener('blur', () => {
  writeText();
});
