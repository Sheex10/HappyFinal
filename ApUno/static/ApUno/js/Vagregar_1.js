$(document).ready(function(){
    $("#loginform").submit(function(e){
        e.preventDefault();
        var foto = $("#imagen").val();
        var nombre = $("#nombre").val();
        var precio = $("#precio").val();
        var descripcion = $("#descripcion").val();


        let mensaje = "";
        let enviar = false;

        //Validar nombre
        if(nombre.trim().length < 4 || nombre.trim().length > 20){
            mensaje += "Nombre producto: El nombre del producto debe tener al menos 20 caracteres";
            enviar = true;
        }
        if (!nombre.match(/([A-Z])/)){
            mensaje += "<br>Nombre producto: Debe contener al menos una mayuscula.";
             enviar = true;
         }
         if (!nombre.match(/([a-z])/)){
             mensaje += "<br>Nombre producto: Debe contener al menos una minuscula.";
              enviar = true;
          }

        /*var letra=nombre.charAt(0);
        if(!esMayuscula(letra)){
            mensaje+= "<br>Nombre: El primer caracter debe ser mayuscula";
            enviar=true;
        }*/

        //Validar precio
        if (!precio.match(/([0-9])/)){
            mensaje += "<br>Precio producto: Debe contener valores numericos.";
             enviar = true;
         }
        if (!precio.match(/([$])/)){
            mensaje += "<br>Precio producto: Debe contener al menos el simbolo $.";
             enviar = true;
         }
        //Validar descripcion
        if(descripcion.trim().length < 20 || descripcion.trim().length > 200){
            mensaje += "<br>Descripcion: La descripcion del producto debe tener al menos 20 caracteres";
            enviar = true;
        }
        if (!descripcion.match(/([A-Z])/)){
            mensaje += "<br>Descripcion: Debe comenzar con una mayuscula.";
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