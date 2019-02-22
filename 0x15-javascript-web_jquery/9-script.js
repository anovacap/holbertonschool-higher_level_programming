const $ = window.$;
const atr = $.attr('html');
const url = 'https://fourtonfish.com/hellosalut/?lang=' + atr;
$.get(url, function (dat) {
  $('#hello').html(dat.hello);
});
