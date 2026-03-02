# PARA-METER-V2.1-ESP
PARA-METER for ESP32

Code adapted to be used with ESP32

* No need for PROGMEM
* Uses HardwareSerial (Serial2 with pins RX 16 and TX 17)
* Uses open pins 35 and 34 to read random data
* Adopted for ADC1 

The unconnected yellow wire that goes from D34 to the center of the breadboard is uses as an "antenna" to gather random data.


<img width="464" height="351" alt="image" src="https://github.com/user-attachments/assets/093f2382-33a7-4a1c-9fc6-e7abc5752bdb" />


Known issue of the main program

The software will choose and replay the category names as the category names are placed as the first entry to each category string. 
They are not filtered from being chosen by the random word algorithm and the speech generation. 
Filtering the index 0 from each category would stop this behaviour. 
As it is not mandatory to put category names in front of the string you may do so or use the space for a different word.
Be aware the the first word from category 0 will lead to the filename 0000xxx.mp3 which will not be played.
