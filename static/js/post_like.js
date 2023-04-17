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
// 장고 ajax 활용시 공식문서 
// https://docs.djangoproject.com/en/4.2/howto/csrf/



const likeClick = (buttonId) => {
    const postId = buttonId.split('-').pop();
    const likeButtonId = document.getElementById('like_button_' + postId);
    const dislikeButtonId = document.getElementById('dislike_button_' + postId);

    const csrftoken = getCookie('csrftoken');

    const url = '/post/' + 'post_like/' + postId

    // api 호출
    // https://developer.mozilla.org/ko/docs/Web/API/Fetch_API/Using_Fetch
    fetch(url, {
        method: "POST",
        mode: "same-origin",
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        // 결과를 받고 html(좋아요 하트) 모습을 변경
        if (data.result === "like") {
            // 좋아요 설정
            likeButtonId.style.display = 'flex';
            dislikeButtonId.style.display = 'none';


        } else {
            // 좋아요 취소 설정
            likeButtonId.style.display = 'none';
            dislikeButtonId.style.display = 'flex';

        }
    });
}

$(document).ready(function () {
    $(".like-i3").click(function () {
        var pk = $(this).attr('name')
        const url = '/post/' + 'post_like/' + pk
        $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
            type: "POST", // 데이터를 전송하는 방법을 지정
            url: url, // 통신할 url을 지정
            data: { 'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}' }, // 서버로 데이터 전송시 옵션
            dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단
            // 서버측에서 전송한 Response 데이터 형식 (json)
            // {'likes_count': post.like_count }
            success: function (response) { // 통신 성공시 - 동적으로 좋아요 개수 변경
                $("#count-" + pk).html("좋아요 " + response.like_count + "개");
            }
        })
    })
})