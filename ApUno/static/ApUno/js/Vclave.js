$(document).ready(function(){
    $("#loginform").submit(function(e){
        e.preventDefault();
        var email = $("#email").val();


        let mensaje = "";
        let enviar = false;

        //Validar email
        if((email).trim().indexOf('@',0) == -1 || (email).trim().indexOf('.',0) == -1){
            mensaje += "<br>Email: El email debe tener contener @";
            enviar = true;
        }

        if(email.trim() == ""){
            mensaje+= "<br>Email: Este campo no puede estar vacio";
            enviar=true;
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