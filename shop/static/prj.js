
function success(data){
    
    if(data.status==0){
        $('#login_form').hide();
        $('#logout_link').show();
    } else {
        alert(data.message);
    }
    
}

function ajax_login(){

data = {
    'login': $('#login').val(),
    'password':  $('#password').val(),
    'csrfmiddlewaretoken': $( "[name='csrfmiddlewaretoken']" ).val()
}

$.ajax({
    type: "POST",
    url: "/account/alogin",
    data: data,
    success: success
  });

}

$('#login_link').on('click',ajax_login);