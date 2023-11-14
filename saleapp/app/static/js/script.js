// var $ = document.querySelector.bind(document)
// var $$ = document.querySelectorAll.bind(document)

// window.onload = function init() {
//     const addToCartButtons = $$('.add-to-cart-button')
//     addToCartButtons.forEach(button => {
//         button.addEventListener('click', function add(e) {
//             addToCart(e.target.attributes['data-id'].value)
//         })
//     })
// }

// async function addToCart(id) {
//     try {
//         await fetch(`/carts/${id}`, {
//             method: 'POST',
//             headers: {
//                 'Accept': 'application/json',
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ quantity: 1 })
//         })
//     } catch (error) {
//         console.log(error.message)
//     }
// }
