package com.afundacion.inazumawiki.jugadores;
/*
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

public class GetPlayers {

    public static void main(String[] args) {
        // Ejemplo de uso
        // Buscar jugadores por nombre
        searchPlayers("Mark Evans");

        // Obtener jugador por ID
        int playerId = 1;
        getPlayerById(playerId);
    }

    // Método para obtener jugadores por nombre
    public static void searchPlayers(String searchName) {
        String url = "http://127.0.0.1:8000/players/search/?search=" + searchName;

        JsonArrayRequest request = new JsonArrayRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Procesar la respuesta JSON
                        // Aquí puedes extraer los datos de los jugadores del JSONArray response
                        // y mostrarlos en tu aplicación
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Manejar el error de la solicitud
                        error.printStackTrace();
                    }
                });

        // Configurar la cola de solicitudes de Volley
        Volley.newRequestQueue(null).add(request);
    }

    // Método para obtener jugador por ID
    public static void getPlayerById(int playerId) {
        String url = "http://tu_dominio.com/players/" + playerId + "/";

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Procesar la respuesta JSON
                        // Aquí puedes extraer los datos del jugador del JSONObject response
                        // y mostrarlos en tu aplicación
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Manejar el error de la solicitud
                        error.printStackTrace();
                    }
                });

        // Configurar la cola de solicitudes de Volley
        Volley.newRequestQueue(null).add(request);
    }
}*/
