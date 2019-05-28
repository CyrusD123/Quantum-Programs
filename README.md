# Demonstrating Quantum Properties
For my genre, I have created four different programs to demonstrate superposition, entanglement, and the random errors of qubits.
You can check out the complete source code for each program in the repository above. The following will be a brief summary and analysis of each program.  

# The Base - Quantum.py
Quantum.py is the basis for all of the other programs in this genre. It is written using Qiskit, a programming library developed my IBM that simulates a quantum computer on your own computer or connects to a real-world IBM quantum computer over the Cloud.

## What it Does
Quantum.py first creates three qubits to simulate on your computer. We can call these Qubit 0, Qubit 1, and Qubit 2. The program puts Qubit 0 through a Hadamard Gate, which puts the qubit in superposition. Qubit 1 and Qubit 2 are both put in Controlled-Not Gates with Qubit 0 as the "control qubit." This is the same as entanglement, where the value of one qubit changes the value of another. In this case, the value of Qubit 0 will dictate the values of Qubit 1 and Qubit 2.
The values of the qubits are measured 1,024 different times, and the measurements are recorded on a bar graph and Bloch sphere.

## The Output
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Quantum%20Graph.png?raw=true "Bar Graph with Counts")  

At the top of the graph is the number of times each output was recorded. A value of 111 was recorded 494 times, while a value of 000 was recorded 530 times. The graph shows that 51.8% of the values recorded were 000, and 48.2% of the values were 111.
But why were only values of 000 and 111 recorded? After all, there are six other binary values that the qubits could have possibly ended up in, 001, 011, 010, 100, 110, or 101. This is where superposition and entanglement come in.  

Each qubit in the program begins with a default value of 0. When Qubit 0 is put through a Hadamard Gate, it goes into a state of superposition. But once we have to measure the value of Qubit 0, the qubit must collapse into a definite value of 0 or 1. Then, Qubits 1 and 2, in the Controlled-Not Gates, will change their values depending on what value Qubit 0 collapses to. If Qubit 0 collapses to 0, then Qubit 1 and 2 both keep the same value they had before. If Qubit 0 collapses to 1, then Qubit 1 and 2 switch to the opposite value of what they had before.
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Quantum%20Bloch.png?raw=true "Bloch Sphere Output")  

In the picture above, each qubit is represented through a Bloch sphere (my repetend). In this case, Qubit 0 has collapsed to 0, so Qubit 1 and Qubit 2 didn't change from their default value of 0. This has created the value 000. If Qubit 0 had collapsed to 1, Qubit 1 and Qubit 2 would have switched from their default values of 0 to 1, creating a value of 111.
Because there is a 50/50 chance that Qubit 0 will collapse to 0 or 1, the output of the 1,024 measurements is split about 50/50 as well.  

So it was no coincedince that the outputs turned out the way they did. This is all thanks to superposition and entanglement. In the next program, we'll take away entanglement to show just how important it is to quantum computing.  

# The Importance of Entanglement - QuantumRandom.py
Also created with Qiskit, QuantumRandom.py is the same as Quantum.py, but instead of putting Qubits 1 and 2 in Controlled-Not Gates, every qubit is put in superposition. There is no entanglement at all in the program.

## The Output
