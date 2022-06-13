buildList()

function buildList() {
    let wrapper = document.getElementById('list-wrapper')
    let url = 'http://127.0.0.1:8000/api/project-detail/2/'

     fetch(url)
     .then((res) => res.json())
     .then(function(data){
        console.log(data)

        let project = `
            <div class="col">
                <div class="card my-2">
                    <img style='max-width: 100%;max-height:100%;' src="${data.image}" class="card-img-top" alt="photo image">
                    <div class="card-body">
                    <p class="card-text">Title: ${data.title}</p>
                    <p class="card-text">Description: ${data.description}</p>
                    <p class="card-text"><a href='${data.link}' target='_blank'> link</a></p>
                    </div>
                    <div class="mb-3">
                        <a href="#" class="btn btn-info">rate</a>
                        <a href="#" class="btn btn-secondary">update</a>
                        <a href="#" class="btn btn-danger">
                            <i class="bi bi-trash3"></i>
                            delete
                        </a>

                    </div>
                </div>
            </div>
            `
            wrapper.innerHTML += project
     })
}
