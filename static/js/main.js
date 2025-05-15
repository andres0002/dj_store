function errorNotification(message){
	Swal.fire({
		title: '¡Error!',
		text: message,
		icon: 'error'
	})
}

function successNotification(message){
	Swal.fire({
		title: '¡Success!',
		text: message,
		icon: 'success'
	})
}

function infoNotification(message) {
	Swal.fire({
		title: '¡Information!',
		text: message,
		icon: 'info'
	});
}

function warningNotification(message) {
	Swal.fire({
		title: '¡Warning!',
		text: message,
		icon: 'warning'
	});
}

function debugNotification(message){
	Swal.fire({
		title: '¡Debug!',
		text: message,
		icon: 'error'
	})
}

// sticky del navbar.
document.addEventListener("DOMContentLoaded", function () {
	const navbar = document.getElementById("mainNav");
	const stickyPoint = navbar.offsetTop;

	window.addEventListener("scroll", function () {
		if (window.scrollY >= stickyPoint) {
			navbar.classList.add("navbar-fixed-top");
		} else {
			navbar.classList.remove("navbar-fixed-top");
		}
	});
});

// Mostrar u ocultar el botón según la posición del scroll
window.addEventListener('scroll', function () {
	const btn = document.getElementById("scrollToTopBtn");
	if (window.scrollY > 300) {
		btn.style.display = "block";
	} else {
		btn.style.display = "none";
	}
});

// Subir suavemente al hacer clic
function scrollToTop() {
	window.scrollTo({
		top: 0,
		behavior: 'smooth'
	});
}

// dropdown.
document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggle = document.querySelector('.dropdown-toggle-custom');
    const dropdownParent = dropdownToggle.closest('.dropdown-custom');

    dropdownToggle.addEventListener('click', function (e) {
        e.preventDefault();
        dropdownParent.classList.toggle('show');
    });

    // Cerrar si se hace clic fuera del dropdown
    document.addEventListener('click', function (e) {
        if (!dropdownParent.contains(e.target)) {
            dropdownParent.classList.remove('show');
        }
    });
});