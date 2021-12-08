const API_KEY = "923bd91d34816fcfa35d1f8e753c77c0";
const API_URL = `https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}`;
const URL_SEARCH = "https://google.com/search?q="
const URL_IMAGES = "https://image.tmdb.org/t/p/w500";

const getJSONData = async (url) => {
    debugger;
    const result = {};
    try {
        const response = await fetch(url);
        if (response.ok) {
            result.data = await response.json();
            result.status = "ok";
        } else {
            throw Error(response.statusText);
        }
    }
    catch (error) {
        result.status = 'error';
        result.data = error;
    }
    return result;
}

const getMovies = async (search) => {
    return await getJSONData(`${API_URL}&query=${search}`);
}

