const getCardHTML = (img, title, votes) => {
    return `<div class="card">
    <img src="${URL_IMAGES}${img}" />
    <h3>${title}</h3>
    <p>Valoracion:${showStars(parseInt(votes))}(${parseInt(votes)})</p>
    <a href="${URL_SEARCH}${encodeURIComponent(title)}" target="_blank">Ver Más</a>
</div>`;
}

const showMovies = (array) => {
    debugger;
    const container = document.getElementById("showMovies");
    container.innerHTML = "";
    for (let movie of array) {
        container.innerHTML += getCardHTML(movie.poster_path, movie.title, movie.vote_average)
    }
}

const submitSearchEvent = async (e) => {
    debugger;
    e.preventDefault();
    const response = await getMovies(document.getElementById("txtSearch").value);
    if (response.status === "ok") {
        showMovies(response.data.results);
    } else {
        alert("OCURRIÓ UN ERROR");
    }
}


window.addEventListener("load", () => {
    debugger;
    const formSearch = document.getElementById("formSearch");
    formSearch.addEventListener("submit", submitSearchEvent);
});

function showStars(stars){
    let res = "";
    console.log(stars);
    console.log("semuestran");
    for (i=0; i < stars; i++){
 res += `<span>★</span>`}
return res;
}
