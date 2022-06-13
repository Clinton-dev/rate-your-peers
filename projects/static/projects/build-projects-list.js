buildList()

function buildList() {
    let wrapper = document.getElementById('list-wrapper')
    let url = 'http://127.0.0.1:8000/api/project-list/'

     fetch(url)
     .then((res) => res.json())
     .then(function(data){
        console.log(data)
        let list = data

        for (let i in list) {
            let project = `
            <div class="col-md-6 col-lg-4">
                <div class="card my-2">
                    <img style='height: 250px;object-fit:cover;' src="${list[i].image}" class="card-img-top" alt="photo image">
                    <div class="card-body">
                    <p class="card-text">Title: ${list[i].title}</p>
                    </div>
                    <a href="#" class="btn btn-outline-dark btn-sm">view</a>
                </div>
            </div>
            `
            wrapper.innerHTML += project
        }

     })
}
