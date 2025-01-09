
<div align="center">

<samp>

<h2> Modified TLS protocol using BB84 protocol and Bit Masking </h1>

<h4> Sanjai Kumar Mani, Rithvik Ravilla, and Rajeswari Sridhar* </h3>

</samp>   

---
| **[[```Paper```]()]** |     
Proceedings of the 6th International Conference on Advances in Distributed Computing and Machine Learning

</div>     

---

## Installation

To install the dependencies, run the following:
```sh
pip install -r requirements.txt
```


## Execute

To run the code, execute the script

```sh
bash run.sh
```

This code runs the server as a seperate background process with the client running in the same shell. To see the server running, independently execute the python scripts in seperate terminals.

*Note:* For key sizes, the constraints as per the libraries used require key sizes to be either 16, 24 or 32 bytes. Update accordingly in QLS_SERVER and QLS_CLIENT.

## Test

To test the code, execute the script

```sh
bash benchmark.sh
```

