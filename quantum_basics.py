# Quantum Computing with Qiskit
# Author: Aman Trivedi
# Quantum computing blew my mind when I first read about it in ECE class.
# Started learning Qiskit to understand it practically!

# NOTE: Install Qiskit first: pip install qiskit qiskit-aer
# If Qiskit not installed, this script shows the concepts with simulation

try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
    from qiskit.visualization import plot_histogram
    QISKIT_AVAILABLE = True
    print("✅ Qiskit available!")
except ImportError:
    QISKIT_AVAILABLE = False
    print("⚠️  Qiskit not installed. Showing simulation results.")
    print("    Install with: pip install qiskit qiskit-aer")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("\n⚛️  Quantum Computing with Qiskit")
print("=" * 45)

# ─────────────────────────────────────────────
# Concept 1: Qubit vs Classical Bit
# ─────────────────────────────────────────────
print("\n📚 Concept 1: Classical Bit vs Qubit")
print("  Classical bit : can be 0 OR 1")
print("  Qubit         : can be |0⟩, |1⟩, or BOTH simultaneously (superposition!)")
print("  This is what makes quantum computers powerful.")

# ─────────────────────────────────────────────
# Circuit 1: Superposition (Bell State)
# ─────────────────────────────────────────────
print("\n🔬 Circuit 1: Superposition using Hadamard Gate")

if QISKIT_AVAILABLE:
    qc1 = QuantumCircuit(1, 1)
    qc1.h(0)          # Hadamard — puts qubit in superposition
    qc1.measure(0, 0)

    sim = AerSimulator()
    compiled = transpile(qc1, sim)
    result = sim.run(compiled, shots=1000).result()
    counts = result.get_counts()
    print(f"  Results (1000 shots): {counts}")
    print(f"  ~50% |0⟩ and ~50% |1⟩ — this is superposition!")
else:
    counts = {'0': 497, '1': 503}
    print(f"  Simulated results (1000 shots): {counts}")
    print(f"  ~50% |0⟩ and ~50% |1⟩ — this is superposition!")

# ─────────────────────────────────────────────
# Circuit 2: Bell State (Quantum Entanglement)
# ─────────────────────────────────────────────
print("\n🔬 Circuit 2: Bell State — Quantum Entanglement")
print("  When two qubits are entangled, measuring one instantly")
print("  determines the state of the other, no matter the distance!")

if QISKIT_AVAILABLE:
    qc2 = QuantumCircuit(2, 2)
    qc2.h(0)           # superposition on qubit 0
    qc2.cx(0, 1)       # CNOT — entangles qubits 0 and 1
    qc2.measure([0,1], [0,1])

    result2 = sim.run(transpile(qc2, sim), shots=1000).result()
    counts2 = result2.get_counts()
    print(f"  Bell State results: {counts2}")
    print(f"  Only |00⟩ and |11⟩ — always correlated!")
else:
    counts2 = {'00': 502, '11': 498}
    print(f"  Simulated Bell State results: {counts2}")
    print(f"  Only |00⟩ and |11⟩ — always correlated!")

# ─────────────────────────────────────────────
# Circuit 3: Deutsch Algorithm (Quantum Speedup!)
# ─────────────────────────────────────────────
print("\n🔬 Circuit 3: Deutsch Algorithm")
print("  Classical: needs 2 queries to determine if f is constant/balanced")
print("  Quantum:   needs only 1 query! This is quantum speedup.")

if QISKIT_AVAILABLE:
    # Balanced oracle
    qc3 = QuantumCircuit(2, 1)
    qc3.x(1)
    qc3.h([0, 1])
    qc3.cx(0, 1)      # balanced oracle
    qc3.h(0)
    qc3.measure(0, 0)

    result3 = sim.run(transpile(qc3, sim), shots=1000).result()
    counts3 = result3.get_counts()
    outcome = "Balanced ✅" if '1' in counts3 else "Constant"
    print(f"  Result: {counts3} → Function is {outcome}")
else:
    print(f"  Result: {{'1': 1000}} → Function is Balanced ✅")

# ─────────────────────────────────────────────
# Visualization
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('⚛️  Quantum Computing with Qiskit', fontsize=14, fontweight='bold', color='#6929C4')

# Superposition histogram
states1 = list(counts.keys())
vals1   = list(counts.values())
axes[0].bar(states1, vals1, color=['#6929C4','#1B3A6B'], alpha=0.85, edgecolor='white', width=0.4)
axes[0].set_title('Circuit 1: Superposition\n(Hadamard Gate)', fontweight='bold')
axes[0].set_xlabel('Measurement Result'); axes[0].set_ylabel('Counts (out of 1000)')

# Bell state histogram
states2 = list(counts2.keys())
vals2   = list(counts2.values())
axes[1].bar(states2, vals2, color=['#6929C4','#1B3A6B'], alpha=0.85, edgecolor='white', width=0.4)
axes[1].set_title('Circuit 2: Bell State\n(Quantum Entanglement)', fontweight='bold')
axes[1].set_xlabel('Measurement Result'); axes[1].set_ylabel('Counts (out of 1000)')

# Bloch sphere visualization (manual)
theta = np.linspace(0, 2*np.pi, 200)
axes[2].plot(np.cos(theta), np.sin(theta), 'gray', lw=1, alpha=0.4)
axes[2].axhline(0, color='gray', lw=0.8, alpha=0.4)
axes[2].axvline(0, color='gray', lw=0.8, alpha=0.4)
axes[2].annotate('', xy=(0, 0.9), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='#6929C4', lw=2.5))
axes[2].text(0.08, 0.9, '|0⟩', color='#6929C4', fontsize=12, fontweight='bold')
axes[2].text(0.08, -0.95, '|1⟩', color='#1B3A6B', fontsize=12, fontweight='bold')
axes[2].text(-0.95, 0.08, '|+⟩', color='green', fontsize=11)
axes[2].set_xlim(-1.2, 1.2); axes[2].set_ylim(-1.2, 1.2)
axes[2].set_aspect('equal'); axes[2].set_title('Bloch Sphere\n(Qubit State Visualization)', fontweight='bold')
axes[2].set_facecolor('#f8f8ff')

plt.tight_layout()
plt.savefig('quantum_circuits.png', dpi=150)
plt.show()

print("\n📌 Key Quantum Concepts Covered:")
print("  ✅ Superposition  — qubit in multiple states simultaneously")
print("  ✅ Entanglement   — correlated qubits (Bell State)")
print("  ✅ Quantum Gates  — H gate, CNOT gate, X gate")
print("  ✅ Quantum Speedup — Deutsch Algorithm")
print("\n✅ Quantum Computing demo complete!")
