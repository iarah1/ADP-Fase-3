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
public class State {
    String statecode;
    String descripcion;

    public State() {
    }

    public String getId() {
        return statecode;
    }

    public void setId(String statecode) {
        this.statecode = statecode;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}
