$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
