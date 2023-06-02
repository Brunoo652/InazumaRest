package com.afundacion.inazumawiki;


import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.widget.Toolbar;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(findViewById(R.id.toolbar));

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

    public static Fragment newInstance(int titleId) {
        Fragment fragment = null;
        switch (titleId) {
            case R.string.buscadorJugadorNombre:
                fragment = new FragmentBuscarJugadoresNombre();
                break;
            case R.string.buscadorJugadorXClub:
                fragment = new FragmentBuscarJugadoresXClub();
                break;
            case R.string.buscadorObjetosNombre:
                fragment = new FragmentBuscarObjetosNombre();
                break;
            case R.string.buscadorObjetoXTipo:
                fragment = new FragmentBuscarObjetosXTipo();
                break;
            case R.string.AcercaDe:
                fragment = new FragmentAcercaDe();
                break;
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
            default:
                throw new IllegalArgumentException("menu option not implemented!!");
        }
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int titleId = getTitle(item);
        new Fragment(titleId);
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }
}