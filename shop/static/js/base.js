const nav_menu = document.querySelector('.nav__menu')

window.addEventListener('scroll', () => {
  nav_menu.classList.toggle('stick', this.window.scrollY > 0)
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
const showSearch = () => {

}