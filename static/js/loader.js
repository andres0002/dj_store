const loader = document.getElementById('loader');

function showLoader() {
    loader.style.display = 'flex';
}

function hideLoader() {
    loader.style.display = 'none';
}

// Interceptar TODOS los formularios
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', () => {
            showLoader();
        });
    });
});

// Interceptar fetch API globalmente
const originalFetch = window.fetch;
window.fetch = async (...args) => {
    try {
        showLoader();
        const response = await originalFetch(...args);
        return response;
    } catch (err) {
        throw err;
    } finally {
        hideLoader();
    }
};

// Interceptar XMLHttpRequest (AJAX clásico)
(function() {
    const oldOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, async, user, pass) {
        this.addEventListener('loadstart', () => showLoader());
        this.addEventListener('loadend', () => hideLoader());
        oldOpen.call(this, method, url, async, user, pass);
    };
})();

// Mostrar loader al cambiar de página
window.addEventListener('beforeunload', function () {
    showLoader();
});