/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Interfaces;

import Modelo.User;
import java.util.List;

/**
 *
 * @author Rocio Abrego
 */
public interface InterfaceADP {
    public User getUser(String username, String upassword);
    public List listarMarca();
    public List listarModelo(String marcaid);
    public List listarEstados();
    public List damageList();
    public String GuardarBusqueda(String marca, String modelo, String anio, String color, String damageid, String state);
}
