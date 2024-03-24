$(document).ready(function() {
    $('#formulario_registro').submit(function(e) {
        // Evitar que el formulario se envíe automáticamente
        e.preventDefault();

        // Validación de correo electrónico
        var email = $('#correo').val();
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, ingresa un correo electrónico válido.');
            return;
        }
        // Validación de clave
        var clave = $('#clave').val();
        var clave2 = $('#clave2').val();
        if (clave != clave2){
            alert('Las claves deben ser iguales');
             return;
        }

        // Si todas las validaciones son exitosas, puedes enviar el formulario
        this.submit();
    });
});
        /*$(document).ready(function() {
          jQuery.validator.addMethod("lettersonly", function(value, element) {
            return this.optional(element) || /^[a-z]+$/i.test(value);
          }, "Solo letras por favor");
          
          $("#formulario_registro").validate({
             rules: {
              //nombre_completo: { required: true},
              //nombre_usuario: { required: true},
              correo: { required: true, email: true },
              clave: { required: true,  minlength: 6, maxlength: 18 },
              clave2: {required: true, equalTo: '#clave' },
              //fecha_nacimiento: { required: true }
            },
           messages: {
              //nombre_completo: "Por favor ingresa tu nombre completo",
              //nombre_usuario: "Por favor ingresa un nombre de usuario",
              correo : "Por favor ingresa un correo",
              clave: { 
                required: "Por favor ingresa una contraseña",
                minlength: "La contraseña debe tener al menos 6 caracteres",
                maxlength: "La contraseña no puede tener más de 18 caracteres"
              },
              clave2: {
                required: "Por favor repite tu contraseña",
                equalTo: "Las contraseñas no coinciden"
              },
              fecha_nacimiento: "Por favor ingresa tu fecha de nacimiento"
            }
          });
        });*/