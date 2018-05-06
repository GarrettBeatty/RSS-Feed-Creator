// App initialization code goes here
$(() => {
  $('#login-form-link').click(function loginclick(e) {
    $('#loginForm').delay(100).fadeIn(100);
    $('#registerForm').fadeOut(100);
    $('#register-form-link').removeClass('active');
    $(this).addClass('active');
    e.preventDefault();
  });
  $('#register-form-link').click(function registerclick(e) {
    $('#registerForm').delay(100).fadeIn(100);
    $('#loginForm').fadeOut(100);
    $('#login-form-link').removeClass('active');
    $(this).addClass('active');
    e.preventDefault();
  });
});
