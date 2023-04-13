{/* 사용자 ID를 URL 파라미터에서 추출합니다. */}
const params = new URLSearchParams(window.location.search);
const userId = params.get('id');
{/* 서버로부터 사용자 프로필 정보를 가져와서 화면에 표시합니다. */}
fetch(`/api/users/${userId}`)
.then(response => response.json())
.then(data => {
    document.getElementById('username').textContent = data.username;
    document.getElementById('email').textContent = data.email;
})
.catch(error => console.error(error));