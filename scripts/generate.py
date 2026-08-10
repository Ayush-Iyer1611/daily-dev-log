from datetime import datetime, timezone
from pathlib import Path
import hashlib
import random

LOG_FILE = Path("daily-log.md")

TOPICS = [
    {
        "category": "Quantum Computing",
        "title": "Qubits and Superposition",
        "body": "A qubit can exist in a linear combination of the computational basis states |0⟩ and |1⟩. Its state can be written as α|0⟩ + β|1⟩, where the probability amplitudes satisfy |α|² + |β|² = 1.",
        "why": "Superposition is one of the fundamental resources that allows quantum algorithms to manipulate probability amplitudes rather than classical bit values.",
        "tags": ["quantum-computing", "qubits", "quantum-mechanics"],
    },
    {
        "category": "Quantum Computing",
        "title": "Quantum Entanglement",
        "body": "Entanglement occurs when the joint state of multiple quantum systems cannot be described as independent states of the individual systems.",
        "why": "Entanglement is central to protocols such as quantum teleportation, superdense coding, and many quantum algorithms.",
        "tags": ["quantum-computing", "entanglement", "quantum-information"],
    },
    {
        "category": "Quantum Computing",
        "title": "Quantum Measurement",
        "body": "Measurement maps a quantum state to a classical outcome according to probabilities determined by the state's amplitudes.",
        "why": "Understanding measurement is essential because quantum algorithms ultimately need to extract classical information from a quantum system.",
        "tags": ["quantum-computing", "measurement", "quantum-mechanics"],
    },
    {
        "category": "Quantum Computing",
        "title": "Quantum Error Mitigation",
        "body": "Quantum error mitigation attempts to reduce the effect of noise in computation results without necessarily performing full fault-tolerant error correction.",
        "why": "QEM is particularly relevant to noisy intermediate-scale quantum devices where hardware noise remains significant.",
        "tags": ["quantum-computing", "QEM", "NISQ"],
    },
    {
        "category": "Quantum Computing",
        "title": "Zero-Noise Extrapolation",
        "body": "Zero-noise extrapolation estimates a noiseless expectation value by evaluating a circuit at multiple effective noise levels and extrapolating toward zero noise.",
        "why": "ZNE is one of the major techniques used to extract more useful information from noisy quantum hardware.",
        "tags": ["quantum-computing", "QEM", "ZNE"],
    },
    {
        "category": "Algorithms",
        "title": "Binary Search",
        "body": "Binary search repeatedly divides a sorted search interval in half, eliminating approximately half of the remaining candidates after each comparison.",
        "why": "Its logarithmic time complexity makes it dramatically more scalable than linear search for large sorted datasets.",
        "tags": ["algorithms", "search", "complexity"],
    },
    {
        "category": "Algorithms",
        "title": "Big-O Complexity",
        "body": "Big-O notation describes an asymptotic upper bound on how the resource requirements of an algorithm grow as its input size increases.",
        "why": "Complexity analysis provides a common language for comparing algorithmic scalability.",
        "tags": ["algorithms", "complexity", "computer-science"],
    },
    {
        "category": "Computer Architecture",
        "title": "CPU Cache Locality",
        "body": "Programs tend to access memory locations that are close to recently accessed locations or reuse recently accessed data. This is known as spatial and temporal locality.",
        "why": "Modern processors exploit locality through multiple levels of cache to reduce the effective cost of memory access.",
        "tags": ["architecture", "CPU", "cache"],
    },
    {
        "category": "Operating Systems",
        "title": "Virtual Memory",
        "body": "Virtual memory provides processes with an abstraction of a large, private address space while the operating system and hardware map virtual addresses onto physical memory.",
        "why": "It provides isolation, simplifies memory management, and allows systems to use storage as an extension of physical memory.",
        "tags": ["operating-systems", "memory", "OS"],
    },
    {
        "category": "Operating Systems",
        "title": "Process vs Thread",
        "body": "A process is an independent execution environment with its own address space, while threads within a process share that process's memory resources.",
        "why": "Understanding this distinction is fundamental to concurrency, scheduling, and application architecture.",
        "tags": ["operating-systems", "threads", "processes"],
    },
    {
        "category": "Networking",
        "title": "TCP vs UDP",
        "body": "TCP provides connection-oriented, reliable and ordered byte-stream delivery, while UDP provides a lightweight datagram-oriented transport without TCP's reliability guarantees.",
        "why": "The choice between them depends heavily on whether reliability or low overhead and latency are the dominant requirements.",
        "tags": ["networking", "TCP", "UDP"],
    },
    {
        "category": "Git",
        "title": "Git Commits",
        "body": "A Git commit records a snapshot of tracked project state along with metadata such as its author, timestamp, message, and parent commit.",
        "why": "Understanding commits as snapshots rather than simple diffs makes Git's branching and history model much easier to reason about.",
        "tags": ["git", "version-control", "software-engineering"],
    },
    {
        "category": "Git",
        "title": "Git Branches",
        "body": "A Git branch is essentially a movable reference to a commit. Creating a branch is therefore inexpensive compared with duplicating an entire repository.",
        "why": "This lightweight branching model enables parallel development and experimentation.",
        "tags": ["git", "branches", "version-control"],
    },
    {
        "category": "Python",
        "title": "Python Generators",
        "body": "Generators produce values lazily using iteration rather than constructing the entire result in memory at once.",
        "why": "Lazy evaluation can significantly reduce memory usage when processing large or streaming datasets.",
        "tags": ["python", "generators", "programming"],
    },
    {
        "category": "Cybersecurity",
        "title": "Hash Functions",
        "body": "A cryptographic hash function maps arbitrary input data to a fixed-size digest and is designed to make finding collisions or reversing the input computationally difficult.",
        "why": "Cryptographic hashes are fundamental to integrity verification, password storage systems, and many security protocols.",
        "tags": ["cybersecurity", "cryptography", "hashing"],
    },
    {
        "category": "Artificial Intelligence",
        "title": "Gradient Descent",
        "body": "Gradient descent iteratively adjusts model parameters in the direction that decreases an objective function.",
        "why": "It is one of the foundational optimization techniques behind the training of many machine-learning models.",
        "tags": ["AI", "machine-learning", "optimization"],
    },
]


def select_topic(date: str):
    seed = int(hashlib.sha256(date.encode()).hexdigest(), 16)
    rng = random.Random(seed)
    return rng.choice(TOPICS)


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Prevent duplicate entries if the workflow runs more than once today.
    existing_log = LOG_FILE.read_text(encoding="utf-8") if LOG_FILE.exists() else ""

    if f"## {today}" in existing_log:
        print(f"Entry for {today} already exists. Nothing to do.")
        return

    topic = select_topic(today)

    entry = f"""
## {today}

### {topic['category']} — {topic['title']}

{topic['body']}

**Why it matters:**  
{topic['why']}

**Tags:** {", ".join(f"`{tag}`" for tag in topic['tags'])}

---
"""

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Generated entry: {topic['title']}")


if __name__ == "__main__":
    main()