const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (dat) {
  $('#hello').html(dat.hello);
});
