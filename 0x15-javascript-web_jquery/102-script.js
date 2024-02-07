$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const urlApi = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}';

    $.get(urlApi, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
