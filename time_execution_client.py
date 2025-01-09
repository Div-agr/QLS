from qls.qs_client import * 
import time


start = time.time()
client = QLS_Client()
client.qkd_connect("127.0.0.1",5401)
# client.aes_connect("127.0.0.1",5401)
# for i in range(1,1000):
#     client.send_given_data("127.0.0.1",5401)
  
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

