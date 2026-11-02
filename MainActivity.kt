package com.dmc5.launcher

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.widget.*

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val layout = LinearLayout(this)
        layout.orientation = LinearLayout.VERTICAL
        layout.setPadding(30, 40, 30, 30)
        layout.setBackgroundColor(Color.rgb(18, 18, 24))

        val title = TextView(this)
        title.text = "DMC5 LAUNCHER"
        title.textSize = 28f
        title.setTextColor(Color.RED)
        layout.addView(title)

        val button = Button(this)
        button.text = "CHECK GAME FILES"
        button.setOnClickListener {
            Toast.makeText(this, "Emulator not connected", Toast.LENGTH_LONG).show()
        }
        layout.addView(button)

        setContentView(layout)
    }
}
