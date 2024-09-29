package com.example.soody;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class HomeActivity extends AppCompatActivity {

    private View _bg__android_large___1_ek2;
    private ImageView purple_illustrated_home__dashboard__upgrade_premium__and_join_classroom_screens_minimalist_mobile_prototype__360___724_px__1__1;
    private View rectangle_2;
    private View rectangle_6;
    private View rectangle_4;
    private View rectangle_5;
    private TextView modunu_y_kselt;
    private TextView modunu_y_kselt_ek1;
    private TextView modunda_kal_;
    private TextView modunda_kal__ek1;
    private TextView foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin_;
    private TextView emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin;
    private TextView emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin_ek1;
    private TextView foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin__ek1;
    private ImageView moodupgradewemoji;
    private ImageView staymoodwemoji;
    private ImageView staymoodwphoto;
    private ImageView moodupgradewphoto;
    private ImageView untitled_design_22__1;

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);


        _bg__android_large___1_ek2 = (View) findViewById(R.id._bg__android_small___1_ek2);
        purple_illustrated_home__dashboard__upgrade_premium__and_join_classroom_screens_minimalist_mobile_prototype__360___724_px__1__1 = (ImageView) findViewById(R.id.purple_illustrated_home__dashboard__upgrade_premium__and_join_classroom_screens_minimalist_mobile_prototype__360___724_px__1__1);
        rectangle_2 = (View) findViewById(R.id.rectangle_2);
        rectangle_6 = (View) findViewById(R.id.rectangle_6);
        rectangle_4 = (View) findViewById(R.id.rectangle_4);
        rectangle_5 = (View) findViewById(R.id.rectangle_5);
        modunu_y_kselt = (TextView) findViewById(R.id.modunu_y_kselt);
        modunu_y_kselt_ek1 = (TextView) findViewById(R.id.modunu_y_kselt_ek1);
        modunda_kal_ = (TextView) findViewById(R.id.modunda_kal_);
        modunda_kal__ek1 = (TextView) findViewById(R.id.modunda_kal__ek1);
        foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin_ = (TextView) findViewById(R.id.foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin_);
        emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin = (TextView) findViewById(R.id.emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin);
        emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin_ek1 = (TextView) findViewById(R.id.emojilerden_modunu_se__yapay_zeka_moduna_g_re__nersin_ek1);
        foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin__ek1 = (TextView) findViewById(R.id.foto_raf_n___ek_yapay_zeka_moduna_g_re__nersin__ek1);
        moodupgradewemoji = (ImageView) findViewById(R.id.moodupgradewemoji);
        staymoodwemoji = (ImageView) findViewById(R.id.staymoodwemoji);
        staymoodwphoto = (ImageView) findViewById(R.id.staymoodwphoto);
        moodupgradewphoto = (ImageView) findViewById(R.id.moodupgradewphoto);
        untitled_design_22__1 = (ImageView) findViewById(R.id.untitled_design_22__1);


        staymoodwphoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //goto snap mood

                    Intent intent = new Intent(HomeActivity.this, MainActivity.class);

                    HomeActivity.this.startActivity(intent);

            }
        });
        moodupgradewphoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //goto snap mood

                Intent intent = new Intent(HomeActivity.this, MainActivity.class);

                HomeActivity.this.startActivity(intent);

            }
        });
        moodupgradewemoji.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //goto snap mood

                Intent intent = new Intent(HomeActivity.this, EmojiPage.class);

                HomeActivity.this.startActivity(intent);

            }
        });
        staymoodwemoji.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //goto snap mood

                Intent intent = new Intent(HomeActivity.this, EmojiPage.class);

                HomeActivity.this.startActivity(intent);

            }
        });
    }
}
