
  const $formulario_registro = document.getElementById('formulario_registro');

  (function(){
    $formulario_registro.addEventListener('submit', function (e) {
      // Validación de correo electrónico
      var email = $('#id_correo').val();
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        e.preventDefault();
      }
      // Validación de clave
      var clave = $('#id_password').val();
      var clave2 = $('#id_password2').val();
      if (clave != clave2){
        alert('Las claves deben ser iguales');
        e.preventDefault();
      }
    });
  })();

 