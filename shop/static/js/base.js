const nav_menu = document.querySelector('.nav__menu')

window.addEventListener('scroll', () => {
  nav_menu.classList.toggle('stick', this.window.scrollY > 0)
})
