package com.noobshubham.persondetails

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface PersonDAO {
    @Insert
    fun insertPerson(person: Person)

    @Query("SELECT * FROM person_table")
    fun getPerson() : LiveData<List<Person>>
}