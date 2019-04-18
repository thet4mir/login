function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
    replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    console.log(prefix);
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    console.log(formCount);
    if (formCount < 1000) {
        // Clone a form (without event handlers) from the first form
        var row = $("."+ prefix +":last").clone(false).get(0);
        console.log(row);
        // Insert it after the last form
        $(row).removeAttr('id').hide().insertAfter("."+ prefix +":last").slideDown(300);

        // Remove the bits we don't want in the new row/form
        // e.g. error messages
        $(".errorlist", row).remove();
        $(row).children().removeClass("error");

        // Relabel or rename all the relevant bits
        $(row).find('.'+ prefix +'-fields').each(function () {
            updateElementIndex(this, prefix, formCount);
            $(this).val('');
            $(this).removeAttr('value');
            $(this).prop('checked', false);
        });

        // Add an event handler for the delete item/form link
        $(row).find(".delete").click(function () {
            return deleteForm(this, prefix);
        });
        // Update the total form count
        $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

    } // End if

    return false;
}


function deleteForm(btn, prefix) {
      console.log(prefix);
      var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
      console.log(formCount);
      if (formCount > 1) {
          // Delete the item/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.'+ prefix).remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.'+ prefix).remove();
          }

          var forms = $('.'+ prefix); // Get all the forms
          // Update the total number of forms (1 less than before)
          $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
          var i = 0;
          // Go through the forms and set their indices, names and IDs
          for (formCount = forms.length; i < formCount; i++) {
              $(forms.get(i)).find('.'+ prefix +'-fields').each(function () {
                  updateElementIndex(this, prefix, i);
              });
          }
      } // End if

      return false;
  }

  $("body").on('click', '.remove-form-row',function () {
    deleteForm($(this), String($(this).attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });

// Show image
  $("#id_image").change(function () {
    readURL(this);
  });

  function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#blah').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}
// Show image
history.pushState(null, null, location.href);
    window.onpopstate = function () {
        history.go(1);
    };
