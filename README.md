# Demonstrating Quantum Properties
For my genre, I have created four different programs to demonstrate superposition, entanglement, and the random errors of qubits.
You can check out the complete source code for each program in the repository above. The following will be a brief summary and analysis of each program.  

# The Base - Quantum.py
Quantum.py is the basis for all of the other programs in this genre. It is written using Qiskit, a programming library that developed my IBM that simulates a quantum computer on your own computer or connects to an IBM quantum computer over the Cloud.

## What it Does
Quantum.py first creates three qubits to simulate on your computer. We can call these Qubit 0, Qubit 1, and Qubit 2. The program puts Qubit 0 through a Hadamard Gate, which puts the qubit in superposition. Qubit 1 and Qubit 2 are both put in Controlled-Not Gates with Qubit 0 as the "control qubit." This is the same as entanglement, where the value of one qubit changes the value of another. In this case, the value of Qubit 0 will dictate the values of Qubit 1 and Qubit 2.
The values of the qubits are measured 1,024 different times, and the measurements are recorded on a bar graph and Bloch sphere.

## The Output
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Quantum%20Graph.png?raw=true "Bar Graph with Counts for Quantum.py")  

At the top of the graph is the number of times each output was recorded. A value of 111 was recorded 494 times, while a value of 000 was recorded 530 times. The graph shows that 51.8% of the values recorded were 000, and 48.2% of the values were 111.
But why were only values of 000 and 111 recorded? After all, there are six other binary values that the qubits could have possibly ended up in, 001, 011, 010, 100, 110, or 101. This is where superposition and entanglement come in.  

Each qubit in the program begins with a default value of 0. When Qubit 0 is put through a Hadamard Gate, it goes into a state of superposition. But once we have to measure the value of Qubit 0, the qubit must collapse into a definite value of 0 or 1. Then, Qubits 1 and 2, in the Controlled-Not Gates, will change their values depending on what value Qubit 0 collapses to. If Qubit 0 collapses to 0, then Qubit 1 and 2 both keep the same value they had before. If Qubit 0 collapses to 1, then Qubit 1 and 2 switch to the opposite value of what they had before.
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Quantum%20Bloch.png?raw=true "Bloch Sphere Output for Quantum.py")  

In the picture above, each qubit is represented through a Bloch sphere (my repetend). In this case, Qubit 0 has collapsed to 0, so Qubit 1 and Qubit 2 didn't change from their default value of 0. This has created the value 000. If Qubit 0 had collapsed to 1, Qubit 1 and Qubit 2 would have switched from their default values of 0 to 1, creating a value of 111.
Because there is a 50/50 chance that Qubit 0 will collapse to 0 or 1, the output of the 1,024 measurements is split about 50/50 as well.  

So it was no coincedince that the outputs turned out the way they did. This is all thanks to superposition and entanglement. In the next program, we'll take away entanglement to show just how important it is to quantum computing.  

# The Importance of Entanglement - QuantumRandom.py
Also created with Qiskit, QuantumRandom.py is the same as Quantum.py, but instead of putting Qubits 1 and 2 in Controlled-Not Gates, every qubit is put in superposition (A Hadamard Gate). There is no entanglement at all in the program.

## The Output
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Random%20Graph.png?raw=true "Bar Graph with Counts for QuantumRandom.py")  

We can see that all eight possible values of the qubits have been measured multiple times. We have just created a random number generator.
Quantum.py used entanglement to ensure that the qubits could only end up as 000 or 111. However, once we use only superposition, this is not the case. In QuantumRandom.py, the qubits must collapse to a definite state when they are measured. In our program, there is a 50/50 chance that a single qubit will collapse to a 0 or a 1, so what value the qubit ends up in is completely random. This goes for every qubit in the program, as they are all in superposition.  

Take a look at the Bloch spheres below:  

![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Random%20Bloch.png?raw=true "Bloch Sphere Output for QuantumRandom.py")
In this case, Qubit 0 collapsed to a value of 0 after superposition, Qubit 1 collapsed to 1, and Qubit 2 collapsed to 0. It was completely random what each qubit collapsed to. Scientists harness the power of entanglement to provide predictable data and avoid scenarios like the one  above.

## Relation to a Traditional Computer - ClassicalRandomNumber.js
We can also see that without entanglement, the a quantum computer is no better than a traditional computer using classical bits. I created ClassicalRandomNumber.js, a random number generator that uses a traditional computer's classical bits rather than qubits.  

You can see the output below:  

![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Classical%20Random.png?raw=true "Percentages Output for ClassicalRandomNumber.js")  

These percentages are very similar to those on the graph of QuantumRandom.py. When it comes to tasks like these, a traditional computer can do it faster and easier than a quantum computer that doesn't fully utilize the capabilites of qubits. Both superposition and entanglement together sets apart quantum computing from the rest.  

# Noise and Errors - QuantumError.py
QuantumError.py, written again using Qiskit, is the same as Quantum.py but runs the program twice, once on a simulated quantum computer (just like Quantum.py did) and again using one of IBM's owm 5-qubit quantum computers, the IBM Q 5. We will be able to see how "noise," the random flipping of qubits due to their interactions with the outside environment, hampers a quantum computation.

## The Output
![alt text](https://github.com/CyrusD123/Quantum-Programs/blob/master/Pics/Error%20Graph.png?raw=true "Bar Graph for QuantumError.py")  

The simulated quantum computer acts exactly the same way in Quantum.py, with only values of 000 and 111 measured, but the real-world IBM quantum computer has some erroneous values that aren't 000 or 111. But why is this? If each computer is running the same program, shouldn't the outputs be near-identical?  

What prevents the IBM Q 5 from measuring only values of 000 or 111 is "noise." Noise is when outside environmental factors can cause qubits to randomly change values, potentially derailing calculations. For example, relatively warm temperatures may cause a qubit to change from a value of 0 to 1 when it wasn't supposed to. In QuantumError.py, noise caused some qubits to flip when they were measured, causing the values between 000 and 111 that weren't supposed to happen. There aren't many of these "incorrect" values, but there are just enough that they are noticeable. In an important calculation, noise could completely corrupt the data or output of a quantum computer.  

Noise remains one of the largest obstacles to improving quantum computing in the future. It is important that scientists overcome it so that quantum computing can be reliably used in more complex ways.