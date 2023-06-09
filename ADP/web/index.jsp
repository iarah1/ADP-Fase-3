<%-- 
    Document   : index.jsp
    Created on : May 14, 2023, 12:55:04 PM
    Author     : Rocio Abrego
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.4/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
        <title>Inicio de sesión</title>
        <style>
            .login-container {
                display: flex;
                height: 100vh;
            }

            .blue-side {
                background-color: #4152B3;
                color: #fff;
                text-align: left;
                padding: 30px;
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .white-side {
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #fff;
            }

            .image-container {
                max-width: 45%;
            }
        
            .btn-custom {
                background-color: #7B96D4;
                color: #fff;
                margin-top: 20px;
                font-weight: bold;
            }

            .form-container {
                width: 60%;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <div class="blue-side">
                <h1>¡Busca tu próximo auto!</h1>
                <form action="login" method="post" class="form-container">
                    <div class="form-group m-2">
                        <label for="exampleInputEmail1">Usuario:</label>
                        <input type="text" class="form-control" id="username" name="username" aria-describedby="emailHelp">
                    </div>
                    <div class="form-group m-2">
                        <label for="exampleInputPassword1">Contraseña:</label>
                        <input type="password" class="form-control" id="password" name="password">
                    </div>            
                    <div class="form-group m-2 d-flex justify-content-center">
                        <button type="submit" class="btn btn-custom btn-block">Ingresar</button>
                    </div>
            </div>
            <div class="white-side">
                <div class="image-container">
                    <img src="img/logo.png" alt="Imagen de fondo" class="img-fluid">
                </div>
            </div>
        </form>
    </body>
</html>
