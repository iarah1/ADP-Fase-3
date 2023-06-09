<%-- 
    Document   : Message
    Created on : May 14, 2023, 5:02:38 PM
    Author     : Rocio Abrego
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Confirmación</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <style>
            body {
                background-color: #4152B3;
            }
        
            .logo-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 220px;
            }

            .logo-container img {
                max-width: 12%;
                height: auto;
            }
            
            .custom-form {
                max-width: 24%;
                margin: 0 auto;
            }

            .custom-form input,
            .custom-form button {
                width: 100%;
            }
            
            .btn-custom {
                background-color: #7B96D4;
                color: #fff;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <!-- Parte superior -->
            <div class="row bg-white">
                <div class="col">
                    <div class="logo-container">
                        <img src="img/logo.png" alt="Logo">
                    </div>
                </div>
            </div>
        
            <!-- Parte inferior -->
            <div class="container-fluid d-flex flex-column justify-content-center align-items-center">
                <div class="col-4 mt-4">
                    <h4 class="text-white text-center mt-5">¡Gracias por utilizar Car Search! <br>Tan pronto se encuentren automóviles que cumplan con sus criterios de búsqueda, le notificaremos a su correo.</h4>
                    
                    <div class="form-group d-flex justify-content-center mt-5">
                        <button type="button" class="btn btn-custom btn-lg mt-3" font-weight-bold" style="background-color: #7B96D4;" onclick="history.back()">Regresar</button>
                    </div>
                </div>
            </div>
    </body>
</html>
