/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controlador;

import Modelo.User;
import ModeloDAO.ADPDAO;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Rocio Abrego
 */

@WebServlet(name = "login", urlPatterns = "/login")
public class cLogin extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet cLogin</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet cLogin at " + request.getContextPath() + "</h1>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //processRequest(request, response);
        
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        
        if(username != null && password != null){
            ADPDAO adp = new ADPDAO();
            User user_info = new User();
            user_info = adp.getUser(username, password);
            
            if(user_info.getUserName() != null){
                
                HttpSession session = request.getSession();
                session.setAttribute("UserName", user_info.getUserName());
                session.setAttribute("ClienteId", user_info.getClienteId());
                
                response.sendRedirect("/ADP/frmBusqueda.jsp");
            }
            else{
                response.sendRedirect("/ADP/index.jsp");
            }
        }
        else{
            response.sendRedirect("/ADP/index.jsp");
        }
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //processRequest(request, response);
        
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if(username != null && password != null){
            ADPDAO adp = new ADPDAO();
            User user_info = new User();
            user_info = adp.getUser(username, password);
            
            if(user_info.getUserName() != null){
                
                HttpSession session = request.getSession();
                session.setAttribute("UserName", user_info.getUserName());
                session.setAttribute("ClienteId", user_info.getClienteId());
                
                response.sendRedirect("/ADP/frmBusqueda.jsp");
            }
            else{
                
                response.sendRedirect("/ADP/index.jsp");
            }
        }
        else{
            response.sendRedirect("/ADP/index.jsp");
        }
        
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
