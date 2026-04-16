// ========================================
// Typing Animation for Loading Screen
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loadingScreen');
    const domainInput = document.getElementById('domainInput');
    
    // Текст для анимации
    const textToType = 'БРЕНД ЖЕНСКОЙ ОДЕЖДЫ «CAPLINK»';
    let charIndex = 0;
    let typingSpeed = 60; // 150ms на букву (медленнее)
    
    // Функция печати текста
    function typeText() {
        if (charIndex < textToType.length) {
            domainInput.textContent += textToType.charAt(charIndex);
            charIndex++;
            setTimeout(typeText, typingSpeed);
        } else {
            // После завершения печати ждем 4 секунды и скрываем
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
            }, 500); // 4 секунды ожидания
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