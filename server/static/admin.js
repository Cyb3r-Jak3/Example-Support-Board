$(document).delegate('form', 'submit', function(event) {
    event.preventDefault();
    const $form = $(this);
    $.ajax({
        url: "/api/admin/" + $form.attr("type"),
        method: "post",
        data: $form.serializeArray(),
    })

});