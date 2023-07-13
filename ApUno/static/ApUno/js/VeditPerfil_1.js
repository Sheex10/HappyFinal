$(document).ready(function(){
    $("#loginform").submit(function(e){
        e.preventDefault();
        var usuario = $("#usuario").val();
        var direccion = $("#direccion").val();
        var email = $("#email").val();
        var contrasena = $("#clave").val();
        var confirmacion = $("#confirmacion").val();
        var edad = $("#edad").val();


        let mensaje = "";
        let enviar = false;

        //Validar usuario
        if(usuario.trim().length < 4 || usuario.trim().length > 10){
            mensaje += "Usuario: El nombre de usuario debe tener al menos 4 a 10 caracteres";
            enviar = true;
        }
        if (!usuario.match(/([A-Z])/)){
            mensaje += "<br>Usuario: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!usuario.match(/([a-z])/)){
             mensaje += "<br>Usuario: Debe contener al menos una minuscula.";
              enviar = true;
          }
        //Validar direccion
        if(direccion.trim().length < 4 || direccion.trim().length > 20){
            mensaje += "<br>Direccion: La direccion debe tener al menos 4 a 10 caracteres";
            enviar = true;
        }
        if (!direccion.match(/([A-Z])/)){
            mensaje += "<br>Direccion: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!direccion.match(/([a-z])/)){
             mensaje += "<br>Direccion: Debe contener al menos una minuscula.";
              enviar = true;
          }
          //Validar email
        if((email).trim().indexOf('@',0) == -1 || (email).trim().indexOf('.',0) == -1){
            mensaje += "<br>Email: El email debe tener contener @";
            enviar = true;
        }

        if(email.trim() == ""){
            mensaje+= "<br>Email: Este campo no puede estar vacio";
            enviar=true;
        }
        //Validar password
        if(contrasena.trim().length < 8 || contrasena.trim().length > 12){
            mensaje = mensaje + "<br>Contraseña: Debe tener entre 8 y 12 caracteres.";
            enviar = true;
        }

        if(contrasena.trim()  == ""){
            mensaje += "<br>Contraseña: No puede estar vacia.";
            enviar = true;
        }

        if (!contrasena.match(/([A-Z])/)){
           mensaje += "<br>Contraseña: Debe contener al menos una mayuscula";
            enviar = true;
        }
        if (!contrasena.match(/([a-z])/)){
            mensaje += "<br>Contraseña: Debe contener al menos una minuscula.";
             enviar = true;
         }

         if (!contrasena.match(/([0-9])/)){
            mensaje += "<br>Contraseña: Debe contener al menos un digito numerico.";
            enviar = true;
         }

        if (!contrasena.match(/([@,#,.,,])/)){
            mensaje += "<br>Contraseña: Debe contener un simbolo o caracter especial (@,#,.,,)";
            enviar = true;
         }
         //validar confirmacion password
        if(confirmacion.trim().length < 8 || confirmacion.trim().length > 12){
            mensaje = mensaje + "<br>Confirmacion: Debe tener entre 8 y 12 caracteres.";
            enviar = true;
        }

        if(confirmacion.trim()  == ""){
            mensaje += "<br>Confirmacion: No puede estar vacia.";
            enviar = true;
        }

        if (!confirmacion.match(/([A-Z])/)){
           mensaje += "<br>Confirmacion: Debe contener al menos una mayuscula.";
            enviar = true;
        }
        if (!confirmacion.match(/([a-z])/)){
            mensaje += "<br>Confirmacion: Debe contener al menos una minuscula.";
             enviar = true;
         }

         if (!confirmacion.match(/([0-9])/)){
            mensaje += "<br>Confirmacion: Debe contener al menos un digito numerico.";
            enviar = true;
         }

        if (!confirmacion.match(/([@,#,.,,])/)){
            mensaje += "<br>Confirmacion: Debe contener un simbolo o caracter especial (@,#,.,,)";
            enviar = true;
         }
         //Validar edad
        if (!edad.match(/([0-9])/)){
            mensaje += "<br>Edad: Debe contener valores numericos.";
             enviar = true;
         }
        

        if(enviar){
            $("#warnings").html(mensaje);
        }
        else{
            $("#warnings").html("Sesion iniciada");
        }
        



    });
    
    function esMayuscula(letra){
        console.log(letra);
        console.log(letra.toUpperCase());
        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
    }
             
});