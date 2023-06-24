// const product = [
//   {
//       id: 0,
//       image: 'image/coffee-2.jpg',
//       title: 'monkey',
//       price: 120,
//   },
//   {
//       id: 1,
//       image: 'image/coffee-3.jpg',
//       title: 'cat',
//       price: 230,
//   },
//   {
//       id: 2,
//       image: 'image/coffee-4.jpg',
//       title: 'baby',
//       price: 376,
//   },
//   {
//       id: 3,
//       image: 'image/coffee-5.jpg',
//       title: 'dog',
//       price: 120,
//   }
// ];

const categories = [...new Set(product.map((item) => item))];
let i = 0;
const rootElement = document.getElementById('root');
rootElement.innerHTML = categories.map((item) => {
  const { image, title, price } = item;
  return `
      <div class='box'>
          <div class='img-box'>
              <img class='image' src=${image}></img>
          </div>
          <div class='bottom'>
              <p>${title}</p>
              <h2>$ ${price}.00</h2>
              <button onclick='addtocart(${i++})'>Add to cart</button>
          </div>
      </div>
  `;
}).join('');

const cart = [];

function displaycart() {
  document.getElementById("count").innerHTML = cart.length;
  let j = 0;
  if (cart.length === 0) {
      document.getElementById('cartItem').innerHTML = 'Your cart is empty';
  } else {
      document.getElementById('cartItem').innerHTML = cart.map((items, index) => {
          const { image, title, price } = items;
          return `<div class="cart-item">
              <div class='row-img'>
                  <img class='rowing' src=${image}>
              </div>
              <p style='font-size:12px'>${title}</p>
              <h2 style='font-size:15px;'>$ ${price}.00</h2>
              <i class='fas fa-trash' onclick='delElement(${index})'></i>
          </div>`;
      }).join('');
  }
}

function addtocart(a) {
  const selectedItem = categories[a];
  cart.push(selectedItem);
  displaycart();
  calculateTotal();
}

function delElement(index) {
  cart.splice(index, 1);
  displaycart();
  calculateTotal();
}

function calculateTotal() {
  const totalPrice = cart.reduce((acc, item) => acc + item.price, 0);
  document.getElementById('total').textContent = `$ ${totalPrice.toFixed(2)}`;
}

displaycart();
