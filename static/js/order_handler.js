// var changeToSeenBtn = document.getElementById('changeToSeen');
// changeToSeenBtn.addEventListener('click', fetchData);
//
// function fetchData() {
//   fetch('/order/change_status/')
//     .then(function (response) {
//       if (response.status !== 200) {
//         console.log(
//           'Looks like there was a problem. Status Code: ' + response.status
//         );
//         return;
//       }
//       response.json().then(function (data) {
//         console.log(data);
//         document.getElementById('w3review').value = data;
//       });
//     })
//     .catch(function (err) {
//       console.log('Fetch Error :-S', err);
//     });
// }
async function changeStatus(orderId) {
    await fetch(`/order/change_status/${orderId}`).then((result) => {
        console.log(result)
    })
    let response = await fetch(`/order/change_status/${orderId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    console.log(response)
}
