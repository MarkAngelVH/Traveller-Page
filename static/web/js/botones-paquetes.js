function mostrarDescripcion(opcion) {
    // Ocultar todas las descripciones
    var descripciones = document.querySelectorAll('.descripcion-packages');
    descripciones.forEach(function(descripcion) {
        descripcion.classList.remove('show');
    });

    // Mostrar la descripción correspondiente a la opción seleccionada
    var descripcionSeleccionada = document.getElementById('descripcion-' + opcion);
    descripcionSeleccionada.classList.add('show');

    // Desactivar la clase 'active' en todos los botones
    var botones = document.querySelectorAll('.boton-packages');
    botones.forEach(function(boton) {
        boton.classList.remove('active');
    });

    // Activar la clase 'active' en el botón seleccionado
    event.target.classList.add('active');
}

window.onload = function() {
    mostrarDescripcion('hot-deals');
};
