document.addEventListener('DOMContentLoaded', () => {
    const productTiles = document.querySelectorAll('.product-tile');
    const categorySelect = document.getElementById('category-select');
    const categoryRadios = document.querySelectorAll('.category-checklist input[type="radio"]');
    const popup = document.getElementById('product-popup');
    const closeBtn = popup.querySelector('.close-btn');
    const mainImage = popup.querySelector('#main-image');
    const imageOptions = popup.querySelectorAll('.image-options img');
    const popupName = popup.querySelector('#popup-name');
    const popupPrice = popup.querySelector('#popup-price');
    const popupDescription = popup.querySelector('#popup-description');
    const popupCartBtn = popup.querySelector('#popup-cart-btn');

    // Function to filter products by category
    function filterProducts(category) {
        productTiles.forEach(tile => {
            const tileCategory = tile.getAttribute('data-category');
            if (category === 'all' || tileCategory === category) {
                tile.style.display = 'block';
            } else {
                tile.style.display = 'none';
            }
        });
    }

    // Event listener for mobile category dropdown
    categorySelect.addEventListener('change', (e) => {
        filterProducts(e.target.value);
    });

    // Event listener for desktop category checklist
    categoryRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            filterProducts(e.target.value);
        });
    });

    // Event listener for "More Info" buttons
    document.querySelectorAll('.more-info-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            const itemId = e.target.getAttribute('data-item-id');
            // Fetch item details (use AJAX in real implementation)
            const item = items.find(item => item.id == itemId);  // Placeholder
            mainImage.src = item.item_img1;
            imageOptions[0].src = item.item_img1;
            imageOptions[1].src = item.item_img2;
            imageOptions[2].src = item.item_img3;
            popupName.textContent = item.name;
            popupPrice.textContent = item.price ? `$${item.price}` : 'Price unavailable';
            popupDescription.textContent = item.description;
            popupCartBtn.textContent = 'Add to Cart';
            popup.classList.remove('hidden');
            popup.style.opacity = '1';
            popup.style.visibility = 'visible';
        });
    });

    // Event listener for closing the popup
    closeBtn.addEventListener('click', () => {
        popup.classList.add('hidden');
        popup.style.opacity = '0';
        popup.style.visibility = 'hidden';
    });

    // Event listener for image options
    imageOptions.forEach((img, index) => {
        img.addEventListener('click', () => {
            mainImage.src = img.src;
            imageOptions.forEach(option => option.classList.remove('selected'));
            img.classList.add('selected');
        });
    });
});
