<%-- 
    Document   : index
    Created on : May 13, 2023, 12:34:43 PM
    Author     : Rocio Abrego
--%>

<%@page import="Modelo.Damage"%>
<%@page import="Modelo.State"%>
<%@page import="java.util.Iterator"%>
<%@page import="Modelo.AMarca"%>
<%@page import="java.util.List"%>
<%@page import="ModeloDAO.ADPDAO"%>
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
        <title>Búsqueda de vehículos</title>
        
        <script type="text/javascript">
        
        function MarcaOnChange(){
            var marcaid = $("#marca").val();
            
            $.ajax({
                type: "POST",
                url: "modelos.jsp",
                data: "marcaid="+marcaid,
                cache: false,
                success: function(response)
                {
                    $('#modelo').empty();
                    $("#modelo").html(response);
                }
            });
        }
        
        
        </script>
        
        <style>
            .logo-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 120px;
            }

            .logo-container img {
                max-width: 8%;
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
        <%
        //allow access only if session exists
        String UserName = null;
        if(session.getAttribute("UserName") == null || session.getAttribute("UserName") == "" ){
                response.sendRedirect("/ADP/index.jsp");
        }

        %>
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
            <div class="row" style="background-color: #4152B3;">
                <div class="col text-white">
                    <h5 class="mt-4 text-center">Seleccione los atributos que busca en su próximo vehículo:</h5>

                    <form action="Controller" method="post" class="mt-4 custom-form">
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Marca</label>
                            <select class="form-control form-control-md" id="marca" name="marca" onchange="MarcaOnChange()">
                            <option value="0" selected="selected">-- Seleccione una marca --</option>
                            <%
                                ADPDAO dao=new ADPDAO();
                                List<AMarca>list=dao.listarMarca();
                                Iterator<AMarca>iter=list.iterator();
                                AMarca marca=null;
                                while(iter.hasNext()){
                                marca=iter.next();
                            %>
                            <option value="<%= marca.getId()%>"><%= marca.getDescripcion()%></option>
                            <%}%>
                            </select>
                        </div>
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Modelo</label>
                            <select class="form-control form-control-md" id="modelo" name="modelo">
                            <option value="0" selected="selected">-- Seleccione un modelo --</option>
                            </select>
                        </div>
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Año</label>
                            <select class="form-control form-control-md" id="anio" name="anio">
                                <option value="0" selected="selected">-- Seleccione un año --</option>
                                <option value="2022">2022</option>
                                <option value="2021">2021</option>
                                <option value="2020">2020</option>
                                <option value="2019">2019</option>
                                <option value="2018">2018</option>
                            </select>
                        </div>
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Color</label>
                            <select class="form-control form-control-md" id="color" name="color">
                                <option value="0" selected="selected">-- Seleccione un color --</option>
                                <option value="NEGRO">Negro</option>
                                <option value="BLANCO">Blanco</option>
                                <option value="AZUL">Azul</option>
                                <option value="ROJO">Rojo</option>
                            </select>
                        </div>
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Tipo de daño</label>
                            <select class="form-control form-control-md" id="damage" name="damage">
                                <option value="0" selected="selected">-- Seleccione un tipo de daño --</option>
                                <%
                                    List<Damage> damageList = dao.damageList();
                                    Iterator<Damage> iDamage = damageList.iterator();
                                    Damage damage=null;
                                    while(iDamage.hasNext()){
                                    damage=iDamage.next();
                                %>
                                <option value="<%= damage.getId()%>"><%= damage.getDescripcion()%></option>
                                <%}%>
                            </select>
                        </div>
                        <div class="form-group m-2">
                            <label for="exampleInputEmail1">Ubicación</label>
                            <select class="form-control form-control-md" id="state" name="state">
                                <option value="0" selected="selected">-- Seleccione un estado --</option>
                                <%
                                    List<State> list_state =dao.listarEstados();
                                    Iterator<State> iState =list_state.iterator();
                                    State state=null;
                                    while(iState.hasNext()){
                                    state=iState.next();
                                %>
                                <option value="<%= state.getId()%>"><%= state.getDescripcion()%></option>
                                <%}%>
                            </select>
                        </div>
                        <div class="form-group m-2 d-flex justify-content-center">
                            <button type="submit" class="btn btn-custom btn-block" style="margin-top: 25px; margin-bottom: 25px;">Enviar</button>
                        </div>
            
                    </form>
                </div>
            </div>
        </div>
    </body>
    
</html>
