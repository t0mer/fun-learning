$(document).ready(function () {
    scan_for_tags();

    $('#bind').click(function () {
        clearInterval(tag_scanner);
        var formData = {
            tagid: $("#tagid").val(),
            heb: $("#heb").val(),
            eng: $("#eng").val(),
            math: $("#math").val()
        };
    
        $.ajax({
            url: '/api/tag/bind',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            processData: false,
            success: function (data, textStatus, jQxhr) {
                $("#tagid").val(data.tag_id)
                $("#heb").prop('selectedIndex',0);
                $("#eng").prop('selectedIndex',0);
                $("#math").prop('selectedIndex',0);
                scan_for_tags();
                ShowMessage("Got it")
            },
            error: function (jqXhr, textStatus, errorThrown) {
                
                ShowError(jqXhr.responseJSON.message)
                scan_for_tags();
            }
        });
    });





    $.ajax({
        url: '/api/hebrewletters', // Replace with your actual API endpoint
        method: 'GET',
        dataType: 'json',
        success: function(data) {
          var select = $('#heb');

          // Loop through the data and populate the select options
          $.each(data, function(index, item) {
            select.append($('<option>', {
              value: item.LetterId,
              text: item.Letter
            }));
          });
        },
        error: function(xhr, status, error) {
          console.error('Error fetching data from the API:', error);
        }
      });

      $.ajax({
        url: '/api/englishletters', // Replace with your actual API endpoint
        method: 'GET',
        dataType: 'json',
        success: function(data) {
          var select = $('#eng');

          // Loop through the data and populate the select options
          $.each(data, function(index, item) {
            select.append($('<option>', {
              value: item.LetterId,
              text: item.Letter
            }));
          });
        },
        error: function(xhr, status, error) {
          console.error('Error fetching data from the API:', error);
        }
      });

      $.ajax({
        url: '/api/numbers', // Replace with your actual API endpoint
        method: 'GET',
        dataType: 'json',
        success: function(data) {
          var select = $('#math');

          // Loop through the data and populate the select options
          $.each(data, function(index, item) {
            select.append($('<option>', {
              value: item.NumberId,
              text: item.Number
            }));
          });
        },
        error: function(xhr, status, error) {
          console.error('Error fetching data from the API:', error);
        }
      });





});

function scan_for_tags() {
    tag_scanner = setInterval(get_new_tag_id, 1000);
}

//Bind new tag


//Scan for new tag
function get_new_tag_id() {
    $.ajax(
        {
            url: '/api/tag/scan',
            dataType: "json",
            success: function (data) {

                console.log(data)
                if (data.success == 'true') {
                    $("#tagid").val(data.tag_id)
                }
            },
            error: function (e) {
            }
        });
}

//Show error message
function ShowError(message) {
    Swal.fire({
        title: 'Error!',
        text: message,
        icon: 'error',
        confirmButtonText: 'Ok'
    })
}


//Show success message
function ShowMessage(message) {
    Swal.fire({
        title: 'Success!',
        text: message,
        icon: 'success',
        confirmButtonText: 'Ok'
    })
}