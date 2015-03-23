$(function () {

  $('#id_username').on('change', function(){
    //get the username from the input box
    var username = $(#id_username).val();
    var password = $(#id_password).val();

    //make the ajax call using a dictionary
    $.ajax({
      url:'/homepage/ajaxtest.check_username',

      data: {
        u: username,
        p: password,
      },//data

      type:"POST",

      //this is to receive the answer from the server (1 or 0 from .py)
      success: function(resp){
        if (resp == '1'){
          $(id_username_message).text('This username is available!');
        }else{
          $(id_username_message).text('This username is unavailable!');
        }
      }
    })://ajax
  });//change
}); //ready