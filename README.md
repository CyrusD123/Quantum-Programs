# Demonstrating Quantum Properties
For my genre, I have created four different programs to demonstrate superposition, entanglement, and the random errors of qubits.
You can check out the complete source code for each program in the repository above. The following will be a brief summary and analysis of each program.


# The Base - Quantum.py
Quantum.py is the basis for all of the other programs in this genre. It is written using Qiskit, a program that simulates a quantum computer on your own computer or connects to an IBM quantum computer over the Cloud.

## What it Does
Quantum.py first creates three qubits to simulate on your computer. We can call these Qubit 0, Qubit 1, and Qubit 2. The program puts Qubit 0 through a Hadamard Gate, which puts the qubit in superposition. Qubit 1 and Qubit 2 are both but in Controlled-Not Gates with Qubit 0 as the "control qubit." This is the same as entanglement, where the value of qubit changes the value of another. In this case, the value of Qubit 0 will dictate the values of Qubit 1 and Qubit 2.
The values of the qubits are measured 1,024 different times, and the measurements are recorded on a bar graph and Bloch sphere.

## The Output