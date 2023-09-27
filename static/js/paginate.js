const pages = document.getElementsByClassName('paging')

// console.log('pages', pages)

for (i = 0; i < pages.length; i++) {
    // console.log('i', i)
    pages[i].addEventListener('click', function () {
        let page_num = this.dataset.num
        console.log('page_num', page_num)
        let parameters = location.search
        if (parameters) {
            let page = parameters.split("=")
            let number = page[page.length - 1]
            console.log('number', number)
            let url = new URL(location.href)
            url.searchParams.set('page', page_num)
            console.log('href', url.toString())
            location.href = url.toString()
        } else {
            location.href = `?page=${page_num}`
        }
    })
}