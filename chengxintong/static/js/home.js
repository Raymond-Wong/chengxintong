$(document).ready(function() {
  init_banner();
  init_msg();
});

var init_banner = function() {
  var slider = $('#carousel');
  var item_container = slider.children('.carousel-inner');
  var indicator_list = slider.children('.carousel-indicators');
  post('/get_banner_list/', {'identify' : get_identify_safe()}, function(resp) {
    if (resp['errno'] == 0) {
      for (var idx = 0; idx < resp['banner'].length; idx++) {
        var item = resp['banner'][idx];
        item_container.append('<a target="_top" href="' + ('url' in item ? item['url'] : '#') + '" class="item' + (idx == 0 ? ' active' : '') + '"><img src="' + item['image'] + '" alt="' + item['name'] + '" /></a>')
        indicator_list.append('<li data-target="#' + slider.attr('id') + '" data-slide-to="' + idx + '" ' + (idx == 0 ? 'class="active"' : '')+ '></li>');
      }
      slider.carousel({interval:false});
      init_slide_action(slider);
    } else {
      alert(resp['error'])
    }
  });
}

var init_slide_action = function(slider) {
  $(slider.find('.item')).on('swipeleft', function() {
    slider.carousel('next');
  });
  $(slider.find('.item')).on('swiperight', function() {
    slider.carousel('prev');
  });
}

var init_msg = function() {
  post('/get_msg_count/', {'identify' : get_identify_safe()}, function(resp) {
    if (resp['errno'] != 0 && 'error' in resp) {
      alert(resp['error']);
      return false;
    }
    if (resp['count'] > 0) {
      $('.have_msg_point').show();
    }
  });
}