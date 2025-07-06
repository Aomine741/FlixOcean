let movies = [], currentPage = 1, perPage = 12;

fetch('/api/movies')
  .then(res => res.json())
  .then(data => {
    movies = data;
    renderMovies();
  });

function renderMovies() {
  const start = (currentPage - 1) * perPage;
  const end = start + perPage;
  const current = movies.slice(start, end);
  const grid = document.getElementById('movieGrid');
  grid.innerHTML = '';
  current.forEach(movie => {
    const html = `
      <div class="bg-gray-900 p-2 rounded shadow-md">
        <img src="${movie.poster}" class="w-full h-48 object-cover rounded">
        <h2 class="text-yellow-300 mt-2 font-bold text-center">${movie.title}</h2>
        <a href="movie.html?id=${movie.id}" class="block text-center text-blue-400 mt-1">View</a>
      </div>`;
    grid.innerHTML += html;
  });
  document.getElementById("pageNumber").textContent = `Page ${currentPage}`;
}

function nextPage() {
  if ((currentPage * perPage) < movies.length) {
    currentPage++;
    renderMovies();
  }
}

function prevPage() {
  if (currentPage > 1) {
    currentPage--;
    renderMovies();
  }
}
