#Use qiskit binder online

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ

#Load IBM Token
IBMQ.save_account('df786894ab16a5972d591bcc751acd71ae0a12c22131b0c89dfb7e65b3f503846ecc985e21e95dab005faf5abe837ad393bab096effa181a691a616e0e371168')
IBMQ.load_accounts()

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
backend = IBMQ.get_backend('ibmqx4')

#Specify shots and number of credits spent on execution
shots = 1024
max_credits = 3

#Hadamard Gate
circ.h(q[0])
#Entanglement with Controlled Not Gate
circ.cx(q[0], q[1])
circ.cx(q[0], q[2])

#Combining the circuits
qc = circ+meas

#Draw circuit
print(qc.draw())

#Execute circuit and save to 'job_sim' object
job_sim = execute(qc, backend_sim, shots=1024)
job_exp = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
#Monitors progress of execution
job_monitor(job_exp)

result_sim = job_sim.result()
result_exp = job_exp.result()

#Get outputs of circuit
counts = result_sim.get_counts(qc)
print(counts)
counts_exp = result_exp.get_counts(qc)
print(counts_exp)

plot_histogram([counts_exp,counts])