<%@page import="java.util.Iterator"%>
<%@page import="Modelo.AModelo"%>
<%@page import="java.util.List"%>
<%@page import="ModeloDAO.ADPDAO"%>

<%
if(request.getParameter("marcaid")!=null) 
{
    String marcaid= request.getParameter("marcaid"); 
    

    ADPDAO dao=new ADPDAO();
    List<AModelo>list=dao.listarModelo(marcaid);
    Iterator<AModelo>iter=list.iterator();
    AModelo mod=null;
    %>
    <option selected="selected">--Seleccione un modelo --</option>
    <%
    while(iter.hasNext()){ mod=iter.next(); %>
        
        <option value="<%= mod.getId()%>"> <%= mod.getDescripcion()%> </option>
    <%}%>
 <%}%>
