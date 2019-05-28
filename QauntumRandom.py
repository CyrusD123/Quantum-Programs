#Use qiskit binder online

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import plot_bloch_multivector

#Create quantum and classical register
q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
#Create quantum circtuits, which hold registers
circ = QuantumCircuit(q)
meas = QuantumCircuit(q, c)
meas.barrier(q)
#Map quantum register to classical register
meas.measure(q,c)
#Backend that does computations
backend_sim = BasicAer.get_backend('qasm_simulator')
backend_vis = BasicAer.get_backend('statevector_simulator')

#Hadamard Gate
circ.h(q[0])
circ.h(q[1])
circ.h(q[2])

#Combining the circuits
qc = circ+meas

#Draw circuit
print(qc.draw())

#Execute circuit and save to 'job_sim' object
job_sim = execute(qc, backend_sim, shots=1024)
job_vis = execute(qc, backend_vis)

result_sim = job_sim.result()
result_vis = job_vis.result()

#Get outputs of circuit
counts = result_sim.get_counts(qc)
print(counts)
state = result_vis.get_statevector()

plot_histogram(counts)

#Do this later
plot_bloch_multivector(state)