const $ = window.$;
const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (films) {
  let movies = films.results;
  for (let i = 0; i < movies.length; i++) {
    $('#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
