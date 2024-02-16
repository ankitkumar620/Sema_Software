const nums = document.querySelectorAll('.nums span');
const counter = document.querySelector('.counter');
const finalMessage = document.querySelector('.final');
const replay = document.querySelector('#replay');

function resetDOM() {
  counter.classList.remove('hide');
  finalMessage.classList.remove('show');

  nums.forEach((num) => {
    num.classList.value = '';
  });

  nums[0].classList.add('in');
}

function handleAnimationEnd(e, idx) {
  const nextToLast = nums.length - 1;

  if (e.animationName === 'goIn' && idx !== nextToLast) {
    nums[idx].classList.remove('in');
    nums[idx].classList.add('out');
  } else if (e.animationName === 'goOut' && nums[idx + 1]) {
    nums[idx + 1].classList.add('in');
  } else {
    counter.classList.add('hide');
    finalMessage.classList.add('show');
  }
}

function runAnimation() {
  nums.forEach((num, idx) => {
    num.addEventListener('animationend', (e) => handleAnimationEnd(e, idx));
  });
}

replay.addEventListener('click', () => {
  resetDOM();
  runAnimation();
});