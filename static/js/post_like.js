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
    console.log(buttonId);
    const postId = buttonId.split('-').pop();
    const likeButtonId = document.getElementById('like_button_' + postId);
    const dislikeButtonId = document.getElementById('dislike_button_' + postId);

    const csrftoken = getCookie('csrftoken');

    const url = '/post/' + 'post_like/' + postId

    // api 호출
    // https://developer.mozilla.org/ko/docs/Web/API/Fetch_API/Using_Fetch
    fetch(url, {
        method : "POST",
        mode : "same-origin",
        headers : {
            'X-CSRFToken' : csrftoken
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