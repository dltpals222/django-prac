$(document).on('submit', '#create-add', function(e) {
    e.preventDefault();

    var isValid = true;
    
    // 각각의 formset의 div를 찾음
    for (let i = 0; i < 10; i++) {
        var formset = $(this).find(`#crtn-input-${i}`);
        var inputs = formset.find('input');
        var emptyInputs = inputs.filter(function() {
            return !$(this).val();
        });

        // 만약 한 세트에서 하나라도 비어있는 input이 있다면,
        if (emptyInputs.length > 0 && emptyInputs.length < 5) {
            isValid = false;
            break;  // 전체 반복문 종료
        }
    }

    if (isValid) {
        const serializedData = $(this).serialize();
        $.ajax({
            url: '/polls/create/',
            type: 'POST',
            data: serializedData,
            success: function(data) {
                $("#create-modal").modal("hide");
            },
            error: function(xhr, errmsg, err) {
                alert("에러 발생 : " + errmsg);
                $('#create-add').html(xhr.responseText);
            }
        });
    } else {
      alert('각 세트의 모든 필드를 입력하여 주시기 바랍니다.');
    }
});
