// ========================================
// Typing Animation for Loading Screen
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loadingScreen');
    const domainInput = document.getElementById('domainInput');
    
    // 🔥 ПРОВЕРКА: если анимация уже была показана в этой сессии — сразу скрываем
    if (sessionStorage.getItem('caplink_animation_shown') === 'true') {
        if (loadingScreen) {
            loadingScreen.classList.add('hidden');
        }
        return; // Прерываем выполнение, анимация не запускается
    }
    
    // Текст для анимации
    const textToType = 'БРЕНД ЖЕНСКОЙ ОДЕЖДЫ «КАПЛИНК»';
    let charIndex = 0;
    let typingSpeed = 60; // скорость печати (мс на символ)
    
    // Функция печати текста
    function typeText() {
        if (charIndex < textToType.length) {
            domainInput.textContent += textToType.charAt(charIndex);
            charIndex++;
            setTimeout(typeText, typingSpeed);
        } else {
            // 🔥 Ставим флаг, что анимация показана
            sessionStorage.setItem('caplink_animation_shown', 'true');
            
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
            }, 500);
        }
    }
    
    // Запускаем анимацию через 500ms после загрузки
    if (loadingScreen && domainInput) {
        setTimeout(typeText, 500);
    } else {
        // Если элементов нет, просто скрываем экран
        if (loadingScreen) {
            loadingScreen.classList.add('hidden');
        }
    }
});
// ========================================
// Navbar Scroll Effect
// ========================================
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
});

// ========================================
// Cart Count Update
// ========================================
function updateCartCount(count) {
    const cartCount = document.getElementById('cartCount');
    if (cartCount) {
        cartCount.textContent = count;
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
// Modal Functions
// ========================================
function openModal(productData) {
    const modal = document.getElementById('productModal');
    const modalBody = document.getElementById('modalBody');
    
    if (!modal || !modalBody) {
        alert('Товар: ' + productData.name + '\nЦена: ' + productData.price + ' ₽');
        return;
    }
    
    modalBody.innerHTML = `
    <img src="${productData.image}" alt="${productData.name}">
    <div class="modal-product-info">
        <h3>${productData.name}</h3>
        
        <span class="modal-heart-btn" id="modal-heart-${productData.id}" onclick="toggleWishlistModal(${productData.id})" style="cursor: pointer; font-size: 1.8rem; margin: 5px 0; display: inline-block;">
            🤍
        </span>
        
        <p class="modal-product-price">${productData.price} ₽</p>
        <select class="modal-size-select" id="modalSizeSelect">
            <option value="">Выберите размер</option>
            ${productData.sizes.map(size => `<option value="${size}">${size}</option>`).join('')}
        </select>
        <button onclick="addToCart(${productData.id}, document.getElementById('modalSizeSelect').value)" class="btn-add-to-cart">
            Добавить в корзину
        </button>
    </div>
`;
    
    modal.classList.add('active');
    
    const closeBtn = document.getElementById('modalClose');
    if (closeBtn) {
        closeBtn.onclick = closeModal;
    }
}

function closeModal() {
    const modal = document.getElementById('productModal');
    if (modal) {
        modal.classList.remove('active');
    }
}

// Close modal on outside click
document.addEventListener('click', (e) => {
    const modal = document.getElementById('productModal');
    if (e.target === modal) {
        closeModal();
    }
});

// ========================================
// Add to Cart
// ========================================
async function addToCart(productId, size) {
    try {
        const response = await fetch('/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                product_id: productId,
                size: size,
                quantity: 1
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            updateCartCount(data.cart_count);
            closeModal();
            alert('Товар добавлен в корзину!');
        }
    } catch (error) {
        console.error('Error:', error);
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
        
        if (response.ok && heartBtn) {
            // Меняем на красное сердечко
            heartBtn.textContent = '❤️';
        }
    } catch (error) {
        console.error('Ошибка при добавлении в избранное:', error);
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
        
        if (response.ok && heartBtn) {
            // Меняем на красное сердечко
            heartBtn.textContent = '❤️';
        }
    } catch (error) {
        console.error('Ошибка при добавлении в избранное:', error);
    }
}