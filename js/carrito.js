function loadCart() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const cartItemsContainer = document.getElementById("cart-items");
  cartItemsContainer.innerHTML = "";

  let subtotal = 0;

  cart.forEach((item) => {
    const totalItemPrice = item.price * item.quantity;
    subtotal += totalItemPrice;

    const itemElement = document.createElement("div");
    itemElement.classList.add("row", "align-items-start");
    itemElement.innerHTML = `
        <div class="col-md-8 col-lg-3" style="text-align: left">
          <img src="${item.image}" style="width: 10vh" alt="" />
        </div>
        <div class="col-md-2" style="text-align: center">
          <div class="row" style="text-align: center">${item.title}</div>
          <div class="row" style="text-align: center">${item.author}</div>
          <div class="row" style="text-align: center">
            <button class="btn btn-danger" onclick="removeItem('${item.isbn}')">Eliminar</button>
          </div>
        </div>
        <div class="col-md-2 col-lg-2">
          <div class="row justify-content-center align-items-center">
            <button class="btn btn-secondary" style="width: 30px;" onclick="decrementQuantity('${item.isbn}')">-</button>
            <div>${item.quantity}</div>
            <button class="btn btn-secondary" style="width: 30px;" onclick="incrementQuantity('${item.isbn}')">+</button>
          </div>
        </div>
        <div class="col-md-2 col-lg-3">${item.price}</div>
        <div class="col">${totalItemPrice}</div>
      `;
    cartItemsContainer.appendChild(itemElement);
  });

  // Update subtotal
  document.getElementById("subtotal").textContent = subtotal;
  // Calculate shipping
  const shippingCost = calculateShipping(subtotal);
  document.getElementById("envio").textContent = shippingCost;
  // Update total
  const total = subtotal + shippingCost;
  document.getElementById("total").textContent = total;
}

function calculateShipping(subtotal) {
  return 0;
}

function removeItem(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart = cart.filter((item) => item.isbn !== itemId);
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();
}

function decrementQuantity(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const updatedCart = cart.map((item) => {
    if (item.isbn === itemId && item.quantity > 1) {
      item.quantity -= 1;
    }
    return item;
  });
  localStorage.setItem("cart", JSON.stringify(updatedCart));
  loadCart();
}

function incrementQuantity(itemId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const updatedCart = cart.map((item) => {
    if (item.isbn === itemId) {
      item.quantity += 1;
    }
    return item;
  });
  localStorage.setItem("cart", JSON.stringify(updatedCart));
  loadCart();
}

window.onload = function () {
  loadCart();
};

function pagar() {
  localStorage.removeItem("cart");
  location.reload();
}
