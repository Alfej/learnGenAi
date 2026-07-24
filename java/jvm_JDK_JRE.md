JDK -> JRE -> JVM

Interpreter : Converts code line by line into machine code that the computer can understand and execute.
Compiler : Translates the entire code into machine code before execution, creating an executable file.

java (Compiled + interpreted) 
Code-> Compiler-> bytecode -> JVM (Interpreter) -> Machine code (At the very start of the language dev).

why interpreter
    -> Goal is to start the execution ASAP
    -> Hardware and Discs were slow and limited RAM that's why we choose interpreter


Code-> Compiler-> bytecode -> JVM (Interpreter + JIT (just in time)compiler) -> Machine code (now).

jvm 
    -> Converts Bytecode to machinecode
    -> Run in secure environment using Sandbox
    -> Garbage collection

JRE
    -> JVM + Class libraries

JDK
    -> JRE + Compiler + Debugger + JavaDocs



JSE -> Java Standard Edition
JEE -> Java Enterprise Edition = JaKarta EE
JME -> Java Micro Edition = Lightweight 
