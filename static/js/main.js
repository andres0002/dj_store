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