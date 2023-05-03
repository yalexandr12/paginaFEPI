const collapsible = document.querySelector('.boton');
const contenido = document.querySelector('.contenidoWidget');
const botonReacciones = document.getElementById('toggle-reactions');
const reacciones = document.querySelectorAll(".reaction");

collapsible.addEventListener('click', () => {
    contenido.classList.toggle('contenido-abierto');
});

reacciones.forEach(r => {
    r.addEventListener("click", function() {
    reacciones.forEach(r => {
        r.classList.remove("selected");
    });
    this.classList.add("selected");
    botonReacciones.innerHTML = this.innerHTML;
    botonReacciones.style.backgroundColor = getComputedStyle(this).getPropertyValue('background-color');
    contenido.classList.toggle('contenido-abierto');
    });
});

reacciones.forEach(button => {
    button.addEventListener('click', () => {
      const selectedReaction = button.getAttribute('data-reaction');
      console.log(selectedReaction);
    });
});