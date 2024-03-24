var updateBtns = document.querySelectorAll('.update-cart')
const totalPrice = document.querySelector('.total__price')
for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function () {
    var override, quantity
    var productId = this.dataset.product
    if (this.classList.contains('override')) {
      quantity = this.parentElement.querySelector('input').value.trim()
      if (!quantity) {
        this.parentElement.querySelector('input').style.borderColor = "red"
        return
      }
    } else {
      quantity = this.dataset.quantity
    }

    if (this.dataset.override === 'true') {
      override = true
    } else {
      override = false
    }
    if (user === 'AnonymousUser') {
      console.log('Not logged in')
    } else {
      cartAdd(productId, quantity, override)
    }
  })
}
const cartNumber = document.querySelectorAll('.cart__number')
const cartAdd = (productId, quantity, override) => {
  var url = '/cart/update-cart/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      productId: productId,
      quantity: quantity,
      override: override
    })
  })
    .then(res => {
      return res.json()
    })

    .then(data => {
      cartNumber.forEach(element => {
        element.classList.remove("hidden")
        element.innerHTML = data.cart_number
      });
      console.log(data)
      totalPrice.innerHTML = data.total_price
    })
}

const cartRemoveBtns = document.querySelectorAll('.remove_item')
for (var i = 0; i < cartRemoveBtns.length; i++) {
  cartRemoveBtns[i].addEventListener('click', function () {
    var productId = this.dataset.product
    var item = this.parentElement
    if (user === 'AnonymousUser') {
      console.log('Not logged in')
    } else {
      cartRemove(productId, item)
    }

  })
}
const cartRemove = async (productId, item) => {
  var url = '/cart/cart-remove/'
 await  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      productId: productId
    })
  })
    .then(res => {
      return res.json()
    })

    .then(data => {
      cartNumber.forEach(element => {
        element.innerHTML = data.cart_number
      });
      totalPrice.innerHTML = data.total_price
      item.style.display = 'none'
      console.log(data)
      if (data.total_price == 0 ) {
        location.reload()
      }
    })
}


