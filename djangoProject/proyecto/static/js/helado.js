/**
 * Autor: EDIS
 * Cuando el modal con ID "exampleModal" se muestra, se ejecuta la función anónima.
 * Esta función cambia el título del modal a "Nuevo Voto" y obtiene el valor de un input en el cuerpo del modal.
 */
$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); 
    var recipient = button.data('whatever'); 
    var modal = $(this);
    modal.find('.modal-title').text("Nuevo Voto");
    modal.find('.modal-body input').val();
});

/**
 * Cuando el modal con ID "resultadoVotacion" se muestra, se ejecuta la función anónima.
 * Esta función obtiene el botón relacionado al evento y no realiza ninguna acción adicional.
 */
$('#resultadoVotacion').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); 
});

/**
 * Esta función "mostrarYOcultar" se utiliza para mostrar u ocultar elementos en la página.
 * Cambia la propiedad de visualización (display) de los elementos "botones_votacion" y "iniciar_votacion".
 */
function mostrarYOcultar() {
    var botones_votos = document.getElementById("botones_votacion");
    botones_votos.style.display = "block";
    var boton_iniciar = document.getElementById("iniciar_votacion");
    boton_iniciar.style.display = "none";
}