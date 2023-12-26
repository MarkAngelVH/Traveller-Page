function toggleMenu() {
    const navegacion = document.querySelector('.navegacion');
    navegacion.style.display = (navegacion.style.display === 'none' || navegacion.style.display === '') ? 'flex' : 'none';
}