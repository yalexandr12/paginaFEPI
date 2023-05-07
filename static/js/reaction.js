const collapsible = document.querySelector('.boton');
const contenido = document.querySelector('.contenidoWidget');
const botonReacciones = document.getElementById('toggle-reactions');
const reacciones = document.querySelectorAll(".reaction");


const reaccionDiv = document.getElementById('reaccion');
const reaction = reaccionDiv.getAttribute('data-reaction');
const noticiaId = reaccionDiv.getAttribute('data-noticia-id');

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

      // Realizar una solicitud fetch a Flask para guardar la reacción seleccionada
      fetch(`/noticia/${noticiaId}/guardar_reaccion`, {
          method: 'POST',
          body: JSON.stringify({
            reaction: selectedReaction,
            //noticia_id: noticia_id
           }),
          headers: {
              'Content-Type': 'application/json'
          }
      })
      .then(response => { 
          // Manejar la respuesta del servidor si es necesario
          console.log(response);
      })
      .catch(error => {
          // Manejar cualquier error en la solicitud fetch
          console.error(error);
      });
  });
});

