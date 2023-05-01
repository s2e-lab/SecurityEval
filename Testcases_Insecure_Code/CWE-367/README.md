# author_1.py

The code opens a file and read its content.
It first checks whether the file exists and then read its content. 
The problem is that potentially the file could have been deleted between the time of the check and the `open()` invocation.



