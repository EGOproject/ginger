document.addEventListener('DOMContentLoaded', function () {
    const mainImage = document.getElementById('main-image');
    const imageOptions = document.querySelectorAll('.thumb');
    const closeButton = document.getElementById('close-detail');
    const previewContainer = document.querySelector('.preview-container');
    const cartBtn = document.getElementById('cart-btn');
    
    // Event listener for image options (thumbnails)
    imageOptions.forEach((img) => {
        img.addEventListener('click', () => {
            // Set the main image source to the clicked thumbnail's source
            mainImage.src = img.src;

            // Remove 'selected' class from all thumbnails
            imageOptions.forEach(option => option.classList.remove('selected'));

            // Add 'selected' class to the clicked thumbnail
            img.classList.add('selected');
        });
    });

    // Close button event to hide the popup
    closeButton.addEventListener('click', function () {
        previewContainer.style.display = 'none';
    });

    // Example Add to Cart functionality
    cartBtn.addEventListener('click', function () {
        cartBtn.innerHTML = '<i class="ri-shopping-cart-2-line"></i>View in Cart';
        cartBtn.style.backgroundColor = 'hsla(207, 95%, 17%, 1)';
    });
});
