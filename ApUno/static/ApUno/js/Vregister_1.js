$(document).ready(function(){
    $("#loginform").submit(function(e){
        e.preventDefault();
        var nombre = $("#nomUser").val();
        var apellido = $("#apeUser").val();       
        var email = $("#mailUser").val();
        var contrasena = $("#Contraseña").val();
        var confirmacion = $("#conContraseña").val();

        let mensaje = "";
        let enviar = false;

        //Validar nombre
        if(nombre.trim().length < 3 || nombre.trim().length > 99){
            mensaje += "Nombre: El nombre de usuario debe tener al menos 4 a 10 caracteres";
            enviar = true;
        }
        if (!nombre.match(/([A-Z])/)){
            mensaje += "<br>Nombre: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!nombre.match(/([a-z])/)){
             mensaje += "<br>Nombre: Debe contener al menos una minuscula.";
              enviar = true;
          }
          /*
        var letra=nombre.charAt(0);
        if(!esMayuscula(letra)){
            mensaje+= "<br>Nombre: El primer caracter debe ser mayuscula";
            enviar=true;
        }*/
        //Validar apellido
        if(apellido.trim().length < 3 || apellido.trim().length > 99){
            mensaje += "<br>Apellido: El apellido debe tener al menos 4 a 10 caracteres";
            enviar = true;
        }
        if (!apellido.match(/([A-Z])/)){
            mensaje += "<br>Apellido: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!apellido.match(/([a-z])/)){
             mensaje += "<br>Apellido: Debe contener al menos una minuscula.";
              enviar = true;
          }
          /*
        var letra=apellido.charAt(0);
        if(!esMayuscula(letra)){
            mensaje+= "<br>Apellido: El primer caracter debe ser mayuscula";
            enviar=true;
        }*/
        //Validar Usuario
        if(usuario.trim().length < 3 || usuario.trim().length > 99){
            mensaje += "<br>Usuario: El usuario debe tener al menos 4 a 10 caracteres";
            enviar = true;
        }
        if (!usuario.match(/([A-Z])/)){
            mensaje += "<br>Contraseña: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!usuario.match(/([a-z])/)){
             mensaje += "<br>Contraseña: Debe contener al menos una minuscula.";
              enviar = true;
          }
          /*
        var letra=usuario.charAt(0);
        if(!esMayuscula(letra)){
            mensaje+= "<br>Usuario: El primer caracter debe ser mayuscula";
            enviar=true;
        }*/
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