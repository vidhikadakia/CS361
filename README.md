1. Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.

2. Start by running the server code on your machine. This will create a socket object and bind it to a specific host and port.

3. Next, run the client code on your machine. This will create a socket object and connect to the server using the same host and port.

4. Once the connection is established, the client will prompt you to enter a string. Type in the string that you want to send to the server and press enter.

5. The client will then send the string to the server, which will receive the data using the recv() method.

6. The server will then convert the string to ASCII codes and send the response back to the client using the send() method.

7. The client will receive the response from the server and print it on the console.

Here's an example call for the microservice: Enter a string: Hello, world!

** Type in "Hello, world!" (without quotes) and press enter.
**
8. The client will then send the string to the server, and the server will respond with the ASCII codes of each character in the string.

9. The client will print the response on the console, which should look something like this: **ASCII codes: 72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33**

NOTE that the actual response may differ based on the input you provide.


_**Clear instructions for how to RECEIVE data from the microservice you implemented
**_

Start by running the server code on your machine. This will create a socket object and bind it to a specific host and port.

Next, run the client code on your machine. This will create a socket object and connect to the server using the same host and port.

Once the connection is established, the client will prompt you to enter a string. Type in the string that you want to send to the server and press enter.

The client will then send the string to the server, which will receive the data using the recv() method.

The server will then convert the string to ASCII codes and send the response back to the client using the send() method.

The client will receive the response from the server using the recv() method and store it in a variable.

You can then use the value of the variable to perform further processing or display the response to the user.



                Client                             Server
                  |                                  |
                  |                                  |
                  +                                  +
                  |                                  |
                  |        1. Connection request       |
                  |--------------------------------->|
                  |                                  |
                  +                                  +
                  |                                  |
                  |        2. Connection accepted      |
                  |<---------------------------------|
                  |                                  |
                  +                                  +
                  |                                  |
                  |      3. Prompt user for input      |
                  |<---------------------------------|
                  |                                  |
                  +                                  +
                  |                                  |
                  |        4. Send data to server      |
                  |--------------------------------->|
                  |                                  |
                  +                                  +
                  |                                  |
                  |       5. Receive data from client  |
                  |<---------------------------------|
                  |                                  |
                  +                                  +
                  |                                  |
                  |        6. Convert data to ASCII    |
                  |                                  |
                  |                                  |
                  |        7. Send response to client  |
                  |--------------------------------->|
                  |                                  |
                  +                                  +
                  |                                  |
                  |   8. Receive response from server  |
                  |<---------------------------------|
                  |                                  |
                  +                                  +
                  |                                  |
                  |        9. Display response         |
                  |                                  |
                  |                                  |
                  |                                  |
                  |                                  |
                  |                                  |
                  |                                  |
                  |<---------------------------------|
                  |                                  |
                  +                                  +
                  |                                  |
                  |         10. Close connection      |
                  |--------------------------------->|
                  |                                  |
                  +                                  +
                  |                                  |

**this UML sequence diagram illustrates both the process of requesting data from the client to the server (steps 1-4) and the process of receiving data from the server to the client (steps 5-9). Step 10 is the final step that occurs after both processes are complete, which is closing the connection between the client and server.**
