$(document).ready(function() {
  init_calendar();
  change_month();
  close_success_msg();
  go_clock_in();
});

var go_clock_in = function() {
  post('/clock_in/', {'identify' : get_identify_safe()}, function(resp) {
    if (resp['errno'] != 0 && 'error' in resp) {
      alert(resp['error']);
      return false;
    }
    $('.income_box').text('激活 ' + resp['money'] + ' 个诚信币');
    $('.msg_box').text(resp['message']);
    $('.success_clock_in_msg').show();
  });
}

var close_success_msg = function() {
  $('.close_btn').on('tap', function() {
    $('.success_clock_in_msg').hide();
  });
}

var change_month = function() {
  $('.change_btn').on('tap', function() {
    var month_box = $(this).parent();
    var year = month_box.children('.year');
    var month = month_box.children('.month');
    var today = new Date(parseInt(year.text()), parseInt(month.text()) - 1, 1);
    var diff = parseInt($(this).attr('diff'));
    today.setMonth(today.getMonth() + diff);
    update_calendar(today, 10);
    year.text(today.getFullYear());
    month.text(today.getMonth() + 1);
  });
}

var init_calendar = function() {
  update_calendar(new Date(), 2);
}

var update_calendar = function(date, continuous) {
  var today = new Date(date);
  var now = new Date(date);
  var year = now.getFullYear();
  var month = now.getMonth() + 1;
  $('.month_box .year').text(year);
  $('.month_box .month').text(month);
  var cur_month = now.getMonth();
  now.setDate(1);
  var start = now.getDay();
  var tds = $('.calendar td');
  // 清空整个日历
  tds.children('.day_circle').text('');
  // 将日历中所有today和continuious都去除
  tds.children('.today').removeClass('today');
  tds.children('.continuous').removeClass('continuous');
  for (var i = 0; i < 31; i++) {
    now.setDate(i + 1);
    if (now.getMonth() != cur_month) {
      break;
    }
    $(tds[start + i]).parent().show();
    $(tds[start + i]).children('.day_circle').text(i + 1);
    if (now.getDate() == today.getDate()) {
      $(tds[start + i]).children('.day_circle').addClass('today');
    } else if (today.getDate() - now.getDate() <= continuous && today.getDate() - now.getDate() > 0) {
      $(tds[start + i]).children('.day_circle').addClass('continuous');
    }
  }
}