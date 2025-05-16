document.addEventListener('DOMContentLoaded', function () {
    // Menú hamburguesa para móvil
    const menuToggle = document.getElementById('mobile-menu');
    const nav = document.getElementById('main-nav');

    menuToggle.addEventListener('click', function () {
        nav.classList.toggle('active');
    });

    // Dropdowns en móvil
    document.querySelectorAll('.dropdown-toggle').forEach(function (toggle) {
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            const dropdown = this.nextElementSibling;
            dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
        });
    });
});