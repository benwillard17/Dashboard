$(function () {
  $('#loginform').ajaxForm(function(data) {
    $('#view_shopping_cart').find('.modal-body').html(data);
  });//ajaxForm
}); //ready