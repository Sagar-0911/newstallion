hamburger = document.querySelector(".hamburger");
hamburger.onclick = function () {
    navBar = document.querySelector(".nav-bar");
    navBar.classList.toggle("active");
}

// class Myheader extends HTMLElement {
//     connectedCallback() {
//         this.innerHTML = `
//             < header >
//             <link href="style/css/style.css" rel="stylesheet">
//             <div class="logo">Stallion Stainless</div>
//         <div class="hamburger">
//             <div class="line"></div>
//             <div class="line"></div>
//             <div class="line"></div>
//         </div>
//         <nav class="nav-bar active">
//             <ul>
//                 <li>
//                     <a href="" class="active">HOME</a>
//                 </li>
//                 <li>
//                     <a href="">Product</a>
//                 </li>
//                 <li>
//                     <a href="">Service</a>
//                 </li>
//                 <li>
//                     <a href="">about us</a>
//                 </li>
//                 <li>
//                     <a href="">contact us</a>
//                 </li>
//             </ul>
//         </nav>
//     </header >
//             `
//     }
// }

// customElements.define('myHeader', Myheader)


// js for product description 
const sizes = document.querySelectorAll('.size');
const colors = document.querySelectorAll('.color');
const shoes = document.querySelectorAll('.shoe');
const gradients = document.querySelectorAll('.gradient');
const shoeBg = document.querySelector('.shoeBackground');

let prevColor = "blue";
let animationEnd = true;

function changeSize() {
    sizes.forEach(size => size.classList.remove('active_p'));
    this.classList.add('active_p');
}

function changeColor() {
    if (!animationEnd) return;
    let primary = this.getAttribute('primary');
    let color = this.getAttribute('color');
    let shoe = document.querySelector(`.shoe[color="${color}"]`);
    let gradient = document.querySelector(`.gradient[color="${color}"]`);
    let prevGradient = document.querySelector(`.gradient[color="${prevColor}"]`);

    if (color == prevColor) return;

    colors.forEach(c => c.classList.remove('active_p'));
    this.classList.add('active_p');

    document.documentElement.style.setProperty('--primary', primary);

    shoes.forEach(s => s.classList.remove('show'));
    shoe.classList.add('show');

    gradients.forEach(g => g.classList.remove('first', 'second'));
    gradient.classList.add('first');
    prevGradient.classList.add('second');

    prevColor = color;
    animationEnd = false;

    gradient.addEventListener('animationend', () => {
        animationEnd = true;
    })
}

sizes.forEach(size => size.addEventListener('click', changeSize));
colors.forEach(c => c.addEventListener('click', changeColor));

let x = window.matchMedia("(max-width: 1000px)");

function changeHeight() {
    if (x.matches) {
        let shoeHeight = shoes[0].offsetHeight;
        shoeBg.style.height = `${shoeHeight * 0.9}px`;
    }
    else {
        shoeBg.style.height = `475px`;
    }
}

changeHeight();

window.addEventListener('resize', changeHeight);


function changeImage() {
    let displayImg = document.getElementById("blue");
    const seat1 = document.getElementById("seat1")
    const seat2 = document.getElementById("seat2")
    const seat3 = document.getElementById("seat3")
    const seat4 = document.getElementById("seat4")
    const seat5 = document.getElementById("seat5")

    if (seat1.classList.contains("active_p")) {
        displayImg.src = "./style/img/blue1.jpg"
    }
    else if (seat2.classList.contains("active_p")) {
        displayImg.src = "./style/img/blue2.webp"
    }
    else if (seat3.classList.contains("active_p")) {
        displayImg.src = "./style/img/blue3.jpeg"
    }
    else if (seat4.classList.contains("active_p")) {
        displayImg.src = "./style/img/blue4.jpeg"
    }
    else {
        displayImg.src = "./style/img/blue5.jpeg"
    }

}



