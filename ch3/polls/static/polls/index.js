/**
 *? HTML요소를 index.html에 삽입하기 위한 함수
 * @param {string} endPoint 엔드포인트 지정
 * @param {string} insertPageId 읽어온 페이지를 넣을 id
 * @param {string} contentType 기본값은 text/html 그 이외라면 추가
 */
async function fetchModule(endPoint, insertPageId, contentType = "text/html") {
  // fetch 데이터 처리
  const response = await fetch(endPoint);
  const result = await response.text();

  const parser = new DOMParser();
  const doc = parser.parseFromString(result, contentType);

  const targetElement = document.getElementById(insertPageId);

  // 기존 targetElement가 있으면 제거 먼저 실행 후 새롭게 생성하는 로직
  if (targetElement) {
    while (targetElement.firstChild) {
      targetElement.removeChild(targetElement.firstChild);
    }

    while (doc.body.firstChild) {
      targetElement.appendChild(doc.body.firstChild);
    }
  }
}

// 불러올 html 파일 관리
document.addEventListener("DOMContentLoaded", () => {
  const umInfo = document.getElementById("um-info");
  umInfo.addEventListener("click", async () => {
    //* 정보
    await fetchModule("/pages/userInfo", "user-info");

    //* 유저정보 입력
    await fetchModule("/pages/create", "create-div");
  });

  document.body.addEventListener("click", async (e) => {
    const checkedValues = Array.from(document.querySelectorAll("input[type=checkbox]:checked")).map(
      (checkbox) => checkbox.value
    );

    if (e.target.id === "info-update" || e.target.id === "info-delete") {
      if (checkedValues.length === 0) {
        alert(
          e.target.id === "info-update"
            ? "변경할 항목을 선택해주세요."
            : "삭제할 항목을 선택해주세요."
        );
        return;
      }
    }

    if (e.target.id === "info-update") {
      e.preventDefault();

      console.log("info-update 버튼이 클릭되었습니다.");

      //* 유저정보 수정
      await fetchModule("/pages/update?noList=" + checkedValues.join(","), "update-div");

      handleUpdateButtonClick(checkedValues);

      // jQuery open modal
      $("#update-modal").modal("show");
      // 종료 시 백드롭 제거 안되는 코드 제거
      $("#update-modal").on("hidden.bs.modal", function (e) {
        $(".modal-backdrop").remove();
        $("#update-div").html("");
      });
    } else if (e.target.id === "info-delete") {
      e.preventDefault();

      console.log("info-delete 버튼이 클릭되었습니다.");

      console.log("checkbox: " + checkedValues);

      //* 유저정보 삭제
      await fetchModule("/pages/delete?noList=" + checkedValues.join(","), "delete-div");

      handleDeleteButtonClick(checkedValues);

      // jQuery open modal
      $("#delete-modal").modal("show");
      // 종료 시 백드롭 제거 안되는 코드 제거
      $("#delete-modal").on("hidden.bs.modal", function (e) {
        $(".modal-backdrop").remove();
        $("#delete-div").html("");
      });
    }
  });
});
