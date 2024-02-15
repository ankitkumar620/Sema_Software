const jokeEl = document.getElementById('joke');
const jokeBtn = document.getElementById('jokeBtn');

jokeBtn.addEventListener('click', generateJoke);

generateJoke();

async function generateJoke() {
  try {
    // Show loading state
    jokeEl.innerHTML = 'Loading...';
    
    const config = {
      headers: {
        Accept: 'application/json',
      },
    };

    const res = await fetch('https://icanhazdadjoke.com', config);

    if (!res.ok) {
      throw new Error('Failed to fetch joke');
    }

    const data = await res.json();

    jokeEl.innerHTML = data.joke;
  } catch (error) {
    console.error('Error fetching joke:', error.message);
    jokeEl.innerHTML = 'Failed to fetch joke. Please try again later.';
  }
}
