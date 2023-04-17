function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



// 모달 띄우기
const modal = document.getElementById("modal_comment_view");
// const buttonCommentView = document.getElementById("comment-view-modal");
// console.log(buttonCommentView);
// const postDetail = (buttonId) => {
//     const postId = buttonId.split('-').pop();
//     modal.style.top = window.pageYOffset + 'px';
//     modal.style.display = 'flex';
//     document.body.style.overflowY = 'hidden';
// }

const postDetail = (buttonId) => {
    console.log(buttonId);

    const postId = buttonId.split('-').pop();
    console.log(postId);
    const url = '/post/' + postId + '/post_modal/';
    console.log(url);
    modal.style.top = window.pageYOffset + 'px';
    modal.style.display = 'flex';
    document.body.style.overflowY = 'hidden';

    $.ajax({
        url: url,
        type: 'GET',
        datatype: 'json',
        data:{
            'post_id': postId,
        },
        success: function(data){
            console.log(data.image);
            $('#author_username').text(data.author.username);
            $('#create_at').text(data.create_at);
            
        }
    });
}




// // 모달 닫기
const buttonModalClose = document.getElementById("close_modal");
buttonModalClose.addEventListener("click", e => {
    modal.style.display = "none";
    document.body.style.overflowY = "visible";
});