/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

/**
 *
 * @author Rocio Abrego
 */
public class User {
    String username;
    String cliente_id;

    public User() {
    }

    public String getUserName() {
        return username;
    }

    public void setUserName(String username) {
        this.username = username;
    }

    public String getClienteId() {
        return cliente_id;
    }

    public void setClienteId(String cliente_id) {
        this.cliente_id = cliente_id;
    }
}
