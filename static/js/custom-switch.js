function createSweetAlert(type, title, text, reload) {
    Swal.fire({
        icon: type,
        title: title,
        text: text,
        confirmButtonClass: 'btn btn-success',
        confirmButtonText: 'باشه',
        onClose: function () {
            if (reload == true) {
                location.reload()
            }
        }
    },
    )
}

userStatusSwitch = document.querySelectorAll('.userStatusSwitch')
for (i = 0; i < userStatusSwitch.length; i++) {
    userStatusSwitch[i].addEventListener('change', function () {
        id = this.dataset.id
        db = this.dataset.db
        value = this.checked
        url = '/ajax/update-status/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'id': id, 'value': value, 'db': db })
        })
            .then(response => {
                return response.json()
            })
            .then(data => {
                if (data['status'] == '200') {
                    createSweetAlert('success', 'تغییر وضعیت کاربر', data['detail'], false)
                } else {
                    createSweetAlert('error', 'تغییر وضعیت کاربر', data['detail'], false)
                }
            })
    })
}