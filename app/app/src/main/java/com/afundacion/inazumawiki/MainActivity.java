package com.afundacion.inazumawiki;

import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.appcompat.widget.Toolbar;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;


import com.google.android.material.navigation.NavigationView;


public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);

        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
    }

    //cierre del menú con la pulsación del botón Atrás o back de Android.
    @Override
    public void onBackPressed() {
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    public Fragment newInstance(int titleId) {
        Fragment fragment = null;
        switch (titleId) {
            case R.string.buscadorJugadorNombre:
                fragment = FragmentBuscarJugadoresNombre.newInstance(titleId);
                break;
            case R.string.buscadorJugadorXClub:
                fragment = FragmentBuscarJugadoresXClub.newInstance(titleId);
                break;
            case R.string.buscadorObjetosNombre:
                fragment = FragmentBuscarObjetosNombre.newInstance(titleId);
                break;
            case R.string.buscadorObjetoXTipo:
                fragment = FragmentBuscarObjetosXTipo.newInstance(titleId);
                break;
            case R.string.AcercaDe:
                fragment = FragmentAcercaDe.newInstance(titleId);
                break;
            case R.string.Opciones:
                fragment = FragmentOpciones.newInstance(titleId);
                break;
        }

        if (fragment != null) {
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();
        }

        return fragment;
    }



    private int getTitle(@NonNull MenuItem menuItem) {
        switch (menuItem.getItemId()) {
            case R.id.buscadorJugadorNombre:
                return R.string.buscadorJugadorNombre;
            case R.id.buscadorJugadorXClub:
                return R.string.buscadorJugadorXClub;
            case R.id.buscadorobjetosNombre:
                return R.string.buscadorObjetosNombre;
            case R.id.buscadorObjetoXTipo:
                return R.string.buscadorObjetoXTipo;
            case R.id.AcercaDe:
                return R.string.AcercaDe;
            case R.id.opciones:
                return  R.string.Opciones;

            default:
                throw new IllegalArgumentException("menu option not implemented!!");
        }
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int titleId = getTitle(item);
        Fragment fragment = newInstance(titleId);
        if (fragment != null) {
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();

            // Cambiar el título del DrawerLayout
            setTitle(item.getTitle());
        }
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }

}