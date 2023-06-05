package com.afundacion.inazumawiki;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


public class FragmentBuscarObjetosNombre extends Fragment {
    private static final String TEXT_ID = "text_id";


    public FragmentBuscarObjetosNombre() {

    }

    public static FragmentBuscarObjetosNombre newInstance(int titleId) {
        FragmentBuscarObjetosNombre frag = new FragmentBuscarObjetosNombre();

        Bundle args = new Bundle();
        args.putInt(TEXT_ID, titleId);
        frag.setArguments(args);

        return frag;
    }


    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable
    Bundle savedInstanceState) {
        View layout = inflater.inflate(R.layout.fragment_buscar_objetos_nombre, container, false);
        return layout;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        if (getArguments() != null) {
            String text = getString(getArguments().getInt(TEXT_ID));
            TextView textView = view.findViewById(R.id.textPruebaObjetoNombre);
            textView.setText(text);
        } else {
            throw new IllegalArgumentException("Argument " + TEXT_ID + " is mandatory");
        }
    }

}