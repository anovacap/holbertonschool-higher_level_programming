const $ = window.$;
$('#toggle_header').addClass('red');
$('#toggle_header').click(function () {
  $('#toggle_header').toggleClass('green');
});
