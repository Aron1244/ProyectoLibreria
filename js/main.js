
function toggleTheme() {
  const content = document.getElementById('contenido');
  if (content.classList.contains('dark-mode')) {
    content.classList.remove('dark-mode');
    content.classList.add('light-mode');
  } else {
    content.classList.remove('light-mode');
    content.classList.add('dark-mode');
  }
}
