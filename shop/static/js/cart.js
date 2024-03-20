var updateBtns = document.querySelectorAll('.update-cart')

for (var i = 0; i < updateBtns.length; i++) {
  console.log(updateBtns[i])
  updateBtns[i].addEventListener('click', function () {
    var productId = this.dataset.product
    var action = this.dataset.action

    if (user === 'AnonymousUser') {
      console.log('Not logged in')
    } else {
      updateUserOrder(productId, action)
    }
  })
}

const updateUserOrder = (productId, action) => {
  var url = '/update-cart/'

  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      productId: productId,
      action: action
    })
  })
    .then(res => {
      return res.json()
    })

    .then(data => {
      console.log(data)
    })
}
