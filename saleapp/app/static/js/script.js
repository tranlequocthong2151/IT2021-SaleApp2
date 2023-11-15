document.addEventListener('DOMContentLoaded', function () {
    var paginationLinks = document.querySelectorAll('.pagination a')

    paginationLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault()

            var urlParams = new URLSearchParams(window.location.search)
            var page = link.getAttribute('data-page')
            urlParams.set('page', page)
            window.location.href = window.location.pathname + '?' + urlParams
        })
    })

    var addToCartButtons = document.querySelectorAll('.add-to-cart-button')

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault()

            var productId = button.getAttribute('product-id')
            fetch(`/cart/${productId}`, {
                method: 'POST',
            })
                .then(response => response.json())
                .then(_ => {
                    location.reload()
                })
                .catch(error => console.error('Error:', error))
        })
    })

    var deleteButtons = document.querySelectorAll('.cart-delete-product-button')

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var productId = button.getAttribute('product-id')

            fetch(`/cart/${productId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok')
                    }
                    return response.json()
                })
                .then(data => {
                    location.reload()
                })
                .catch(error => console.error('Error:', error))
        })
    })
})
