/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ModeloDAO;

import Config.Conexion;
import Interfaces.InterfaceADP;
import Modelo.AMarca;
import Modelo.AModelo;
import Modelo.Damage;
import Modelo.State;
import Modelo.User;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Rocio Abrego
 */
public class ADPDAO implements InterfaceADP {
    
    Conexion cn = new Conexion();
    Connection con;
    PreparedStatement ps;
    ResultSet rs;
    
    @Override
    public List listarMarca() {
        ArrayList<AMarca> list = new ArrayList<>();
        String sql="SELECT marcaid, descripcion FROM adp.amarca where estado = 1;";
        try {
            con=Conexion.getConnection();
            ps=con.prepareStatement(sql);
            rs=ps.executeQuery();
            while(rs.next()){
                AMarca mod = new AMarca();
                mod.setId(rs.getInt("marcaid"));
                mod.setDescripcion(rs.getString("descripcion"));
                list.add(mod);
            }
        } catch (Exception e) {
        }
        return list;
    }

    @Override
    public List listarModelo(String marcaid) {
        ArrayList<AModelo> list = new ArrayList<>();
        String sql="SELECT mo.modeloid, mo.descripcion FROM adp.amarca m join adp.amodelo mo on m.marcaid = mo.marcaid where m.estado = 1 and mo.estado = 1 and m.marcaid = " + marcaid ;
        try {
            con=cn.getConnection();
            ps=con.prepareStatement(sql);
            rs=ps.executeQuery();
            while(rs.next()){
                AModelo mod = new AModelo();
                mod.setId(rs.getInt("modeloid"));
                mod.setDescripcion(rs.getString("descripcion"));
                list.add(mod);
            }
        } catch (Exception e) {
        }
        return list;
    }

    @Override
    public List listarEstados() {
        ArrayList<State> list = new ArrayList<>();
        String sql="SELECT stateid, descripcion FROM adp.country_state where estado = 1;";
        try {
            con=Conexion.getConnection();
            ps=con.prepareStatement(sql);
            rs=ps.executeQuery();
            while(rs.next()){
                State mod = new State();
                mod.setId(rs.getString("stateid"));
                mod.setDescripcion(rs.getString("descripcion"));
                list.add(mod);
            }
        } catch (Exception e) {
        }
        return list;
    }

    @Override
    public List damageList() {
        ArrayList<Damage> list = new ArrayList<>();
        String sql="SELECT damageid, descripcion FROM adp.damage where estado = 1;";
        try {
            con=Conexion.getConnection();
            ps=con.prepareStatement(sql);
            rs=ps.executeQuery();
            while(rs.next()){
                Damage mod = new Damage();
                mod.setId(rs.getInt("damageid"));
                mod.setDescripcion(rs.getString("descripcion"));
                list.add(mod);
            }
        } catch (Exception e) {
        }
        return list;
    }

    @Override
    public String GuardarBusqueda(String marca, String modelo, String anio, String color, String damageid, String state) {
        String result = "";
        String sql="INSERT INTO `adp`.`adp_busqueda`(`marca`,`modelo`,`anio`,`color`,`damageid`,`state`,`ciudad`,`busqueda_estado`,`user_id`,`cliente_id`) VALUES ";
        sql+="("+ marca +", "+ modelo +", "+ anio +", '"+ color +"', "+ damageid +", '"+ state+"', 0, 1, 1, 1);";
        
        try {
            con=Conexion.getConnection();
            ps=con.prepareStatement(sql);
            ps.executeUpdate();
        } catch (Exception e) {
             System.err.print("Error al realizar la conexión: "+e);
             e.printStackTrace();
        }
        
        result = "SAVED";
        return result;
    }

    @Override
    public User getUser(String username, String upassword) {
        String sql="SELECT u.username, u.cliente_id FROM adp.adp_user u where u.username = '"+ username +"' and upassword = '"+ upassword +"' limit 1;;";
        User _user = new User();
        try {
            con=Conexion.getConnection();
            ps=con.prepareStatement(sql);
            rs=ps.executeQuery();
            while(rs.next()){
                
                _user.setUserName(rs.getString("username"));
                _user.setClienteId(rs.getString("cliente_id"));
            }
        } catch (Exception e) {
            System.err.print("Error al realizar la conexión: "+e);
             e.printStackTrace();
        }
        return _user; //To change body of generated methods, choose Tools | Templates.
    }
    
}
