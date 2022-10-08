package com.noobshubham.persondetails

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.noobshubham.persondetails.databinding.ActivityMainBinding
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    private lateinit var database: PersonDatabase
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        database = PersonDatabase.getDatabase(this)
        binding.btnAddPersonInfo.setOnClickListener { addPersonInfo() }
    }

    private fun addPersonInfo() {
        val firstName = binding.etFirstName.editText?.text?.toString()
        val lastName = binding.etLastName.editText?.text?.toString()
        val age = binding.etAge.editText?.text?.toString()
        val gender = binding.etGender.editText?.text?.toString()
        val email = binding.etEmail.editText?.text?.toString()

        if (firstName!!.isNotEmpty() && lastName!!.isNotEmpty() && age!!.isNotEmpty() && gender!!.isNotEmpty() && email!!.isNotEmpty()) {
            val person = Person(0, firstName, lastName, age.toInt(), gender, email)

            GlobalScope.launch(Dispatchers.IO) { database.personDao().insertPerson(person) }

            binding.etFirstName.editText?.text?.clear()
            binding.etLastName.editText?.text?.clear()
            binding.etAge.editText?.text?.clear()
            binding.etGender.editText?.text?.clear()
            binding.etEmail.editText?.text?.clear()

            Toast.makeText(this, "Successfully Added Person to DB", Toast.LENGTH_SHORT).show()
        } else
            Toast.makeText(this, "Please fill all the fields", Toast.LENGTH_SHORT).show()
    }
}