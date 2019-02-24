$(document).ready(function() {
    /* CATEGORY MODAL CLICK*/
    var loadForm = function (e) {
      e.preventDefault();
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-box").modal("show");
          },
          success: function (data) {
            $("#modal-box .modal-content").html(data.html_personal);
          }
        });
    };
  
    /* CATEGORY MODAL FORM */
   var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            toastr.success("Información guardada satisfactoriamente");
            $("#modal-box").modal("hide");  // <-- Close the modal
          }
          else {
            $("#modal-box .modal-content").html(data.html_personal);
          }
        }
      });
      return false;
    };
    /* logos events */
    $(".js-create-personal").click(loadForm);
    $("#modal-box").on("submit", ".js-personal-form", saveForm);
});

