// Element references
const header = document.getElementById('header');
const title = document.getElementById('title');
const excerpt = document.getElementById('excerpt');
const profile_img = document.getElementById('profile_img');
const name = document.getElementById('name');
const date = document.getElementById('date');

const animated_bgs = document.querySelectorAll('.animated-bg');
const animated_bg_texts = document.querySelectorAll('.animated-bg-text');

// Delayed function call to simulate data fetching
setTimeout(getData, 2500);

// Function to fetch and display data
function getData() {
  // Mock data
  const imageData =
    'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2102&q=80';
  const profileImageData = 'https://randomuser.me/api/portraits/men/45.jpg';

  // Display data with fade-in effect
  fadeInElement(header, `<img src="${imageData}" alt="" />`);
  fadeInElement(title, 'Lorem ipsum dolor sit amet');
  fadeInElement(
    excerpt,
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore perferendis'
  );
  fadeInElement(profile_img, `<img src="${profileImageData}" alt="" />`);
  fadeInElement(name, 'John Doe');
  fadeInElement(date, 'Oct 08, 2020');

  // Remove animation classes after data is displayed
  animated_bgs.forEach((bg) => bg.classList.remove('animated-bg'));
  animated_bg_texts.forEach((bg) => bg.classList.remove('animated-bg-text'));
}

// Function to apply fade-in effect to an element
function fadeInElement(element, content) {
  element.style.opacity = 0;
  element.innerHTML = content;
  let opacity = 0;

  const fadeIn = setInterval(() => {
    if (opacity < 1) {
      opacity += 0.1;
      element.style.opacity = opacity;
    } else {
      clearInterval(fadeIn);
    }
  }, 100);
}
