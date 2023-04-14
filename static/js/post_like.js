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

    const likeButton = document.getElementById(buttonId);
    const likeIconFind = likeButton.querySelector(".bi-heart2");
    const likeIcon = likeIconFind.children;

    const csrftoken = getCookie('csrftoken');

    const postId = buttonId.split('-').pop();
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
            likeIcon[0].style.display = 'flex';
            likeIcon[1].style.display = 'none';

        } else {
            // 좋아요 취소 설정
            likeIcon[0].style.display = 'none';
            likeIcon[1].style.display = 'flex';
        }
    });

}