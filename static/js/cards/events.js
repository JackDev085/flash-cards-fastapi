cardBack.addEventListener("click", virarCarta);
cardFront.addEventListener("click", virarCarta);
document.addEventListener("DOMContentLoaded", () => {
  cardAleatorio();
});

nextCard.addEventListener("click", () => {
  cardAleatorio();
  cardFront.classList.remove("disabled");
  cardBack.classList.add("disabled");
});

listen.addEventListener("click", () => {
  audio.innerHTML = `<audio controls autoplay class="disabled"><source src=${URL_BASE}/static/audios/audio${cardId.textContent}.mp3 type="audio/mpeg"></audio>`;
});
