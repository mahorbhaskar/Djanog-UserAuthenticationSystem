 $("#usernameField").keyup(function(){
      var username = $(this).val();
      $.ajax({
      url: '/ajax/checkUserName/',
      data: {
              'username': username
            },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          $("#usernameField").after("<div class='validation' id='alert_msg' style='color:red;margin-bottom: 0px;'>username already taken choose another.</div>");
          document.getElementById("save").disabled = true;
          }
        else{
          document.getElementById("save").disabled = false;
          document.getElementById("alert_msg").remove();
        }
        }
      });
    });
  $("#emailField").keyup(function(){
      var email = $(this).val();
      $.ajax({
      url: '/ajax/checkEmailField/',
      data: {
              'email': email
            },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          $("#emailField").after("<div class='validation' id='alert_msg' style='color:red;margin-bottom: 0px;'>email already taken choose another.</div>");
          document.getElementById("save").disabled = true;
          }
        else{
          document.getElementById("save").disabled = false;
          document.getElementById("alert_msg").remove();
        }
        }
      });
    });
  $('#password, #confirm_password').on('keyup', function () {
                    if ($('#password').val() == $('#confirm_password').val()) {
                      $('#message').html('').css('color', 'green');
                      document.getElementById("save").disabled = false;
                    } 
                    else{
                      document.getElementById("save").disabled = true;
                      $('#message').html('Not Matching').css('color', 'red');
                    }
                  });