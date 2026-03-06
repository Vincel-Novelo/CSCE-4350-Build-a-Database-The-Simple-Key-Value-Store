CSCE 4350: Simple Key-Value Database
By Vincel Novelo (vcn0027)

Description:
  -This project implements a simple key-value database that reads commands from standard input and stores data in memory while also persisting it to disk. 
  -The program supports setting and retrieving values using simple text commands.
  -The database stores all entries in a file called data.db. 
  -When the program starts, it loads existing entries from this file so that data persists between program runs.

Files:
  -main.py – the main program that processes commands and manages the database

  -data.db – the file used to store persistent data (created automatically)

How to Run:
  -Run the program from the command line using:
    python main.py

Supported Commands:
  SET
    -Stores the value associated with the key. 
    -If the key already exists, the value is overwritten.

    INPUT:
    SET name Vincel
    
    OUTPUT:
    OK

  GET
    -Retrieves the value associated with the key.
    -If the key does not exist, the program returns:
    NULL
  
    INPUT:
    GET name
    
    OUTPUT:
    Vincel

  EXIT
    -Stops the program.

Persistence:
  -Every time a SET command is executed, the command is appended to the data.db file. 
  -When the program starts again, it reads this file and reconstructs the database in memory. 
  -Ensures that values persist after the program restarts.

Design:
  -The program uses two classes:
    1) Entry: represents a key-value pair
    2) Database: manages entries and handles loading/saving data
  -The database keeps entries in memory using a list and writes updates to disk for persistence.
