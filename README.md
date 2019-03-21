Disclaimer: I am not responsible for any real / potential damage by the use of this project

I am not a professional penetration tester.

However, I do find network/socket programming very attractive and based on what I learned from

Network class in college, I have made this little sneaky programs.

Just because I like to understand about penetration testing, it does not mean I would like to use well known tools or frameworks. Instead, I wanted to try making my own script and see what I can do.

Server program opens up an accessible port.

Once the server program is running, client program can be executed to connect to the hosted port by the server.

Unlike normal shells or also known as "bind shell", in which server simply allow an user to connect and client program with a payload to attack the server node, the server program acts as a payload and allows the server to execute shell commands to a client.

In most network environment, it is a common practice that in-bound policy is set to be strict to prevent malicous actions to be done and typically, out-bound policy is set to be loose so that users within the network can freely traverse the endpoints outside of the firewall.

Due to this environment, exploitation by bind shell is not really easily acheiveable.

However, since the out-bound policy is relatively loose, implementing reverse shell is very effective to control a remote node.



Bind Shell:

Server (Victim) ---------|Firewall|<<---------Client (Attacker)

It is easy to fail to make connection if an out-bound policy of firewall is well set.

Reverse Shell:

Server (Attacker) -------NO-FIREWALL <<------------Client (Victim)

Attacker set no out-bound policy so that victims can freely connect to the trap server.

Again, even though this is a very simple program, it won't be detected by an anti-virus software as a threat.

So, DO NOT USE TO HARM OTHER ENDPOINTS.



