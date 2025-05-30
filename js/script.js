const mario = document.querySelector('.mario');
const pipe = document.querySelector('.pipe');

const jump = () => {
  mario.classList.add('jump');

  setTimeout(() => {
    mario.classList.remove('jump');
  }, 500);
}

const loop = setInterval(() => {

  console.log('loop')

  const pipePosition = pipe.offsetLeft;
  const marioPosition = +window.getComputedStyle(mario).bottom.replace
  ('px', '');
  
  console.log(marioPosition);

  if (pipePosition <= 120 && pipePosition > 0 && marioPosition < 60) {

    pipe.style.animation = 'nome';
    pipe.style.left = `${pipePosition}px`;

    mario.style.animation = 'nome';
    mario.style.bottom = `${marioPosition}px`;

    mario.src = './imagens/game-over.png';
    mario.style.width = '65px'
    mario.style.marginLeft = '50px'

    clearInterval(loop);
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

