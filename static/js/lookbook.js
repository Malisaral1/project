// ========================================
// Lookbook Hotspots (Кликабельные точки)
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    const hotspotsData = window.lookbookHotspots || [];
    const imageWrapper = document.querySelector('.lookbook-image-wrapper');
    
    // Если мы не на странице lookbook — просто выходим без ошибок
    if (!imageWrapper) {
        return;
    }
    
    if (hotspotsData.length === 0) {
        console.log('No hotspots data');
        return;
    }
    
    // Создаём точки на основе координат из базы
    hotspotsData.forEach((hotspot, index) => {
        const hotspotElement = document.createElement('div');
        hotspotElement.className = 'hotspot';
        hotspotElement.style.left = hotspot.position_x + '%';
        hotspotElement.style.top = hotspot.position_y + '%';
        hotspotElement.dataset.productId = hotspot.product_id;
        hotspotElement.dataset.productName = hotspot.product_name;
        hotspotElement.dataset.productPrice = hotspot.product_price;
        hotspotElement.dataset.productImage = hotspot.product_image;
        
        // Клик по точке
        hotspotElement.addEventListener('click', (e) => {
            e.stopPropagation();
            console.log('Hotspot clicked:', hotspot.product_name);
            
            if (typeof openModal === 'function') {
                openModal({
                    id: hotspot.product_id,
                    name: hotspot.product_name,
                    price: hotspot.product_price,
                    image: hotspot.product_image,
                    sizes: hotspot.product_sizes || ['XS', 'S', 'M', 'L', 'XL']
                });
            } else {
                alert('Товар: ' + hotspot.product_name + '\nЦена: ' + hotspot.product_price + ' ₽');
            }
        });
        
        imageWrapper.appendChild(hotspotElement);
        console.log('Hotspot created:', index);
    });
});

// ========================================
// Add Entire Lookbook to Cart
// ========================================
async function addLookbookToCart(lookbookSlug) {
    try {
        // ✅ Правильный URL: /cart/lookbook/.../add-to-cart/
        const response = await fetch('/cart/lookbook/' + lookbookSlug + '/add-to-cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            updateCartCount(data.cart_count);
            console.log('Образ добавлен:', data.items_added, 'товаров');
        } else {
            console.error('Ошибка при добавлении образа:', data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// ========================================
// Get CSRF Token
// ========================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ========================================
// Update Cart Count
// ========================================
function updateCartCount(count) {
    const cartCount = document.getElementById('cartCount');
    if (cartCount) {
        cartCount.textContent = count;
    }
}
// ========================================
// Toggle Wishlist from Modal (Сердечко в модальном окне)
// ========================================
async function toggleWishlistModal(productId) {
    const heartBtn = document.getElementById(`modal-heart-${productId}`);
    const csrftoken = getCookie('csrftoken');
    
    try {
        const response = await fetch(`/wishlist/add/${productId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            // Меняем цвет сердечка на красный
            if (heartBtn) heartBtn.textContent = '❤️';
        }
    } catch (error) {
        console.error('Ошибка при добавлении в избранное:', error);
    }
}