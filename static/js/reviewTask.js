function createSweetAlert(type, title, text, reload) {
    Swal.fire({
        icon: type,
        title: title,
        text: text,
        confirmButtonText: 'باشه',
        customClass: {
            confirmButton: 'btn btn-success me-3',
            cancelButton: 'btn btn-label-secondary'
        },
    },
    ).then(function (result) {
        if (result.value) {
            if (reload) {
                location.reload()
            }
        }
    })
}

reviewTaskEditBtns = document.querySelectorAll('.reviewTaskEditBtn')
for (i = 0; i < reviewTaskEditBtns.length; i++) {
    reviewTaskEditBtns[i].addEventListener('click', async function () {
        id = this.dataset.id
        description = document.querySelector('#description_' + id)
        done = document.querySelector('#done_' + id)

        description.disabled = false
        done.disabled = false
        if (this.dataset.function == 'edit') {
            this.dataset.function = 'submit'
        }
        else {
            url = `/review/task/edit/`
            response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({ 'description': description.value, 'done': done.value, 'taskId': id })
            })

            data = await response.json()
            if (data['status'] == '200') {
                createSweetAlert('success', 'ویرایش بازدید', data['text'], true)
            } else {
                createSweetAlert('error', 'ویرایش بازدید', data['text'], false)
            }

        }
    })
}