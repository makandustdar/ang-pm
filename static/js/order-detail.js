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


confirmOrderBtn = document.querySelector('#confirmOrderBtn')

if (confirmOrderBtn) {
    confirmOrderBtn.addEventListener('click', function () {
        orderId = this.dataset.orderid
        console.log('orderId', orderId)
        Swal.fire({
            title: 'تایید وضعیت سفارش',
            text: " سفارش  تایید شود؟",
            icon: 'info',
            showCancelButton: true,
            confirmButtonText: 'تایید',
            confirmButtonClass: 'btn btn-success',
            cancelButtonClass: 'btn btn-danger ml-1',
            cancelButtonText: 'انصراف',
            buttonsStyling: false,
        }).then(async function (result) {
            if (result.value) {
                url = '/ajax/confirm-order/'
                response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({ 'orderId': orderId })
                })

                data = await response.json()
                if (data['status'] == 200) {
                    createSweetAlert('success', 'تایید سفارش', `سفارش شما به شماره ${orderId} تایید شد`, true)
                } else {
                    createSweetAlert('error', 'تایید سفارش', data['text'], false)
                }
            }
        })
    })
}