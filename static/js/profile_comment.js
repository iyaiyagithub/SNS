$(document).ready(function () {
  var numToShow = 2; // 최근 댓글 몇개를 보여줄 것인지
  var post_count = document.querySelectorAll("#comments");
  
  for (i = 0; i < post_count.length; i++) {
      var comment = post_count[i].querySelectorAll('.conntent-box');
      var array = []
      comment.forEach(function(x) {
          array.unshift(x.id);
          document.getElementById(x.id).style.display = 'none';
        });
        if (array.length >= numToShow) {
            document.getElementById(array[0]).style.display = 'flex';
            document.getElementById(array[1]).style.display = 'flex';
        }
        if (array.length == 1) {
            document.getElementById(array[0]).style.display = 'flex';
        }
    };
});


var comment_view = document.getElementById("comment_all_view");

const commentViewAll = (buttonAllId) => {
    const commentButton = document.getElementById('post-' + buttonAllId);
    const a = commentButton.querySelectorAll('.conntent-box');

    a.forEach(function(i) {
        i.style.display = 'flex';
    });
}