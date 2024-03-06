let audio = document.getElementById('audio');
let text = document.getElementById('text');




audio.addEventListener("click", function () {
  let utterance = new SpeechSynthesisUtterance(text.innerText);
  speechSynthesis.speak(utterance);
});








