const range = document.getElementById('range');
const label = document.getElementById('label');

range.addEventListener('input', updateLabel);

function updateLabel(e) {
  const value = +e.target.value;
  const max = +e.target.max;
  const min = +e.target.min;

  const rangeWidth = parseFloat(getComputedStyle(e.target).getPropertyValue('width'));
  const labelWidth = parseFloat(getComputedStyle(label).getPropertyValue('width'));

  const left = (value * (rangeWidth / max)) - (labelWidth / 2) + scale(value, min, max, 10, -10);

  label.style.left = `${left}px`;
  label.innerHTML = value;
}

function scale(num, inMin, inMax, outMin, outMax) {
  return (num - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
}
