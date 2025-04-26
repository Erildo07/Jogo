const mario = document.querySelector('.mario');
const pipe = document.querySelector('.pipe');

const jump = () => {
  mario.classList.add('jump');

  setTimeout(() => {
    mario.classList.remove('jump');
  }, 500);
}

const loop = setInterval(() => {

  const pipePosition = pipe.offsetLeft;
  
  if (pipePosition <= 120) {

    pipe.style.animation = 'nome';
    pipe.style.left = `${pipePosition}px`;

  }

}, 10);

document.addEventListener('keydown', jump);
document.addEventListener('touchstart', jump);

const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
  console.log('Usuário está no celular');
  // Aqui você pode ativar controles por toque, esconder botões, mudar UI...
} else {
  console.log('Usuário está no PC');
}
