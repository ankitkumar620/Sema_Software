const buttons = document.querySelectorAll('.ripple');

buttons.forEach(button => {
    button.addEventListener('click', createRipple);
});

function createRipple(e) {
    const x = e.pageX;
    const y = e.pageY;

    const buttonRect = e.target.getBoundingClientRect();

    const xInside = x - buttonRect.left;
    const yInside = y - buttonRect.top;

    const ripple = document.createElement('span');
    ripple.classList.add('circle');
    ripple.style.top = `${yInside}px`;
    ripple.style.left = `${xInside}px`;

    this.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 500);
}
