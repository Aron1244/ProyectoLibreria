
function toggleTheme() {
  const content = document.getElementById('contenido');
  const footer = document.getElementById('footer');
  const navbar = document.getElementById('navbar');
  if (content.classList.contains('dark-mode')) {
    content.classList.remove('dark-mode');
    content.classList.add('light-mode');

    footer.classList.remove('dark-mode-footer');
    footer.classList.add('light-mode-footer');

    navbar.classList.remove('dark-mode-footer');
    navbar.classList.add('light-mode-footer');
    navbar.classList.remove('navbar-dark');
  } else {
    content.classList.remove('light-mode');
    content.classList.add('dark-mode');

    footer.classList.remove('light-mode-footer');
    footer.classList.add('dark-mode-footer');

    navbar.classList.remove('light-mode-footer');
    navbar.classList.add('dark-mode-footer');
    navbar.classList.add('navbar-dark');
  }
}

function toggleThemes() {
  const navbar = document.getElementById('navbar');
  
  if (navbar.classList.contains('dark-mode-footer')) {
    navbar.classList.remove('dark-mode-footer');
    navbar.classList.add('light-mode-footer');
  } else {
    navbar.classList.remove('light-mode-footer');
    navbar.classList.add('dark-mode-footer');
  }
}

function toggleNavbar() {
  const navbar = document.getElementById('navbarSupportedContent');
  navbar.classList.toggle('show');
}
