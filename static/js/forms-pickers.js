/**
 * Form Picker
 */

'use strict';

(function () {
    // Flat Picker
    // --------------------------------------------------------------------
    const flatpickrDate = document.querySelector('#flatpickr-date'),
        flatpickrTime1 = document.querySelector('#flatpickr-time1'),
        flatpickrTime2 = document.querySelector('#flatpickr-time2')
    console.log(flatpickrDate)
    // Date
    if (flatpickrDate) {
        flatpickrDate.required = true
        flatpickrDate.flatpickr({
            monthSelectorType: 'static',
            locale: 'fa',
            altInput: true,
            altFormat: 'Y/m/d',
            disableMobile: true,
        });
    }

    // Time
    if (flatpickrTime1) {
        flatpickrTime1.required = true
        flatpickrTime1.flatpickr({
            enableTime: true,
            noCalendar: true,
            locale: 'fa',
            altInput: true,
            altFormat: 'H:i',
            disableMobile: true
        });
    }

    // Time
    if (flatpickrTime2) {
        flatpickrTime2.required = true
        flatpickrTime2.flatpickr({
            enableTime: true,
            noCalendar: true,
            locale: 'fa',
            altInput: true,
            altFormat: 'H:i',
            disableMobile: true
        });
    }

})();
