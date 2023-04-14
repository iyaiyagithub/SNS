// 모달 띄우기
const modal = document.getElementById("modal_profile_view");
const buttonProfileView = document.getElementById("profile_view_modal");

buttonProfileView.addEventListener("click", e => {
    modal.style.display = "flex";
    document.body.style.overflowY = "hidden";

    console.log(window.pageYOffset + " 위치");
});

// 모달 닫기
const buttonModalClose = document.getElementById("close_modal");
buttonModalClose.addEventListener("click", e => {
    modal.style.display = "none";
    document.body.style.overflowY = "visible";
});