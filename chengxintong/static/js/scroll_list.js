SCROLLERS = {};
$(document).ready(function() {
  init_scrollers();
})

var init_scrollers = function() {
  $('.list_box').each(function() {
    SCROLLERS[this] = init_scroller($(this));
  });
}

var init_scroller = function(list_box, start_pos) {
  var hint = list_box.children('.hint');
  var list = list_box.children('.list');
  if (start_pos) {
    var new_scroller = new IScroll(list_box[0], {probeType:3, momentum:false, startY:start_pos});
  } else {
    var new_scroller = new IScroll(list_box[0], {probeType:3, momentum:false});
  }
  new_scroller.on('scroll', function() {
    var end_pos = (list.height() - list_box.height() + 4 * 14) * 1;
    if (this.directionY == 1 && Math.abs(parseInt(this.y)) >= end_pos) {
      this.y = -end_pos;
      this.destroy();
      update(list_box, -end_pos);
    }
  });
  return new_scroller;
}

var update = function(list_box, start_pos) {
  var scroller = init_scroller(list_box, start_pos);
  var list = list_box.children('.list');
  var hint = list_box.children('.hint');
  if (hint.text() == '正在加载数据...') return false;
  hint.text('正在加载数据...');
  setTimeout(function() {
    list.css('height', list.height() + 14 * 5 + 'px');
    scroller.refresh();
    hint.text('上拉加载更多数据');
  }, 3000);
}
