const mario = document.querySelector('.mario');

const jump = () => {
  mario.classList.add('jump');

  setTimeout(() => {

    mario.classList.remove('jump');

  }, 500)

}

document.addEventListener('keydown', jump);
document.addEventListener('touchstart', jump);

const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
  console.log('Usuário está no celular');
  // Aqui você pode ativar controles por toque, esconder botões, mudar UI...
} else {
  console.log('Usuário está no PC');
}
