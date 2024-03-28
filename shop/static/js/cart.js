var updateBtns = document.querySelectorAll('.update-cart')
const totalPrice = document.querySelector('.total__price')
for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function (event) {
    var override, quantity
    var productId = this.dataset.product
    element = event.target
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
      cartAdd(productId, quantity, override, element)
    }
  })
}

const updateCartInput = document.querySelectorAll(".update_cart_input")

for(var i = 0; i < updateCartInput.length; i++ ) {
  var value, productId, override
  updateCartInput[i].addEventListener("input", (event) => {
    value = event.target.value
    override = event.target.dataset.override
    productId = event.target.dataset.product
    element = event.target
    if (value == 0) {
      event.target.style.borderColor = "red"
    } else  {
      event.target.style.borderColor = "rgb(56, 56, 56)"
      if (override === "true") {
        override = true
      }
      cartAdd(productId, value, override, element)
    }

  })
}

const cartNumber = document.querySelectorAll('.cart__number')
const cartAdd = (productId, quantity, override, element) => {
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
      element.parentElement.querySelector(".total-price").innerHTML = data.item_price
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