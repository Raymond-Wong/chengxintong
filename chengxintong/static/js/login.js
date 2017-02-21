$(document).ready(function() {
  $('.login_btn').on('tap', function() {
    var params = {};
    params['mobile'] = $('input[name="phone"]').val();
    params['password'] = $('input[name="password"]').val();
    post('/login/', params, function(resp) {
      if ('msg' in resp) {
        alert(resp['msg']);
      }
      if (resp['errno'] == 0) {
        window.location.href = "/home/";
      }
    });
  });
});