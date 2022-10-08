package com.noobshubham.persondetails

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "person_table")
data class Person(
    @PrimaryKey(autoGenerate = true)
    val idval : Long,
    val fname : String,
    val lname : String,
    val ageval : Int,
    val genderval : String,
    val emailval : String
)
