const params = new URLSearchParams(window.location.search);
const id = params.get("id");

fetch(`/api/movie?id=${id}`)
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("movieDetails");
    container.innerHTML = `
      <h1 class="text-2xl text-yellow-300 font-bold mb-4">${data.title}</h1>
      <img src="${data.poster}" class="w-full md:w-1/2 mb-4 rounded">
      <div class="space-y-2">
        <a href="${data.links['480p']}" target="_blank" class="block bg-blue-500 px-4 py-2 rounded text-center">Download 480p</a>
        <a href="${data.links['720p']}" target="_blank" class="block bg-green-500 px-4 py-2 rounded text-center">Download 720p</a>
        <a href="${data.links['1080p']}" target="_blank" class="block bg-red-500 px-4 py-2 rounded text-center">Download 1080p</a>
      </div>
    `;
  });
