const $ = window.$;
const url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (name) {
  $('#character').html(name.name);
});
