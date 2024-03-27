const nav_menu = document.querySelector('.nav__menu')
const base__content = document.querySelector('.base__content')

window.addEventListener('scroll', () => {
  if (window.scrollY > 0) {
    nav_menu.classList.add('stick');
   base__content.style.paddingTop = nav_menu.offsetHeight + 'px'; // Add padding to body
  } else {
      nav_menu.classList.remove('stick');
      base__content.style.paddingTop = 0; // Reset padding
  }
  // nav_menu.classList.toggle('stick', () => {
  //   this.window.scrollY > 0
  //   base__content.style.paddingTop = nav_menu.offsetHeight + 'px';
  // })

})

const searchBtn = document.querySelector('.search_menu')
const searchDialog = document.querySelector('dialog')
console.log(searchDialog)
searchBtn.addEventListener('click', () => {
  searchDialog.showModal()

})

// close search modal when outside its boundary is clicked
searchDialog.addEventListener('click', e => {
  const searchFormDim = searchDialog.getBoundingClientRect()
  if (
    e.clientX < searchFormDim.left ||
    e.clientX > searchFormDim.right ||
    e.clientY < searchFormDim.top ||
    e.clientY > searchFormDim.bottom
  ) {
    searchDialog.close()
  } else {
  }
})