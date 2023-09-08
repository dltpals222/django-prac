function submitUserInfo() {
  // 폼 데이터를 가져옵니다.
  const formElement = document.getElementById("addInfoForm");
  const formData = new FormData(formElement);

  // 폼 데이터를 객체로 변환
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  // AJAX 요청을 사용하여 서버와 통신합니다.
  $.ajax({
    type: "POST",
    url: "/api/userInfo",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (data) {
      // 정상 응답 처리 (ex: 팝업창 표시)
      alert("정보가 성공적으로 추가되었습니다.");
    },
    error: function (jqXHR, textStatus, errorThrown) {
      // 오류 처리 (팝업창 표시)
      // alert(jqXHR.responseText); //에러의 내용을 보여줌
      alert("5가지 값 전부 입력해주시기 바랍니다.");
    },
  });
}