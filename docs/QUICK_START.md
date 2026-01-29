# Quick Start Guide

This guide will help you get started with the Digital Circuit Analysis tool in just a few minutes.

## Installation

### Option 1: Quick Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/muzammil5539/digital-circuit-analysis.git
cd digital-circuit-analysis

# Install dependencies
pip install -r requirements.txt

# Run the analyzer on example circuits
python src/main.py
```

### Option 2: Install as Package

```bash
# Clone and install as a package
git clone https://github.com/muzammil5539/digital-circuit-analysis.git
cd digital-circuit-analysis
pip install -e .

# Run the analyzer
circuit-analyze
```

## Your First Circuit Analysis

### Step 1: Create a Circuit File

Create a file named `my_circuit.txt`:

```
# My first circuit
INPUT in1
INPUT in2

ADD add1 in1 in2
MUL mul1 add1 in2

OUTPUT out1 mul1
```

### Step 2: Analyze the Circuit

```python
from src.circuit_analyzer import CircuitAnalyzer

# Load and analyze the circuit
analyzer = CircuitAnalyzer('my_circuit.txt')
critical_path, total_delay = analyzer.find_critical_path()

# Print results
print(f"Critical Path: {' -> '.join(critical_path)}")
print(f"Total Delay: {total_delay:.2f} time units")

# Generate visualization
analyzer.visualize_circuit(critical_path)
```

### Step 3: View the Results

Check the `output/` directory for the generated circuit visualization!

## Understanding the Output

### Console Output

The analyzer prints three sections:

1. **All Components**: List of all gates/components with their delays
2. **Critical Path**: The longest delay path through the circuit
3. **Path Components**: Details of components on the critical path

### Visualization

The generated PNG file shows:
- **Blue nodes**: Circuit components
- **Blue edges**: Connections with delay labels
- **Red edges**: Critical path (highlighted)

## Circuit File Format

### Basic Structure

```
# Comments start with #

INPUT <node_id>           # Define inputs

<GATE> <node_id> <input1> <input2> ...   # Define gates

OUTPUT <node_id> <source_node>    # Define outputs
```

### Supported Gates

| Gate | Delay | Description |
|------|-------|-------------|
| ADD  | 1.0 tu | Adder |
| MUL  | 1.0 tu | Multiplier |
| REG  | 0.2 tu | Register |
| MUX  | 1.0 tu | Multiplexer |

### Example: Sequential Circuit

```
# Sequential adder-multiplier
INPUT x[n]

ADD add1 x[n]
MUL mul1 add1
REG reg1 mul1      # Register creates feedback
ADD add2 reg1

OUTPUT y[n] add2
```

## Common Use Cases

### Finding Maximum Clock Frequency

The critical path delay determines the minimum clock period:

```
Minimum Clock Period = Critical Path Delay
Maximum Frequency = 1 / Critical Path Delay
```

Example: If critical path = 5.2 tu, max frequency = 1/5.2 ≈ 0.192 units⁻¹

### Comparing Circuit Designs

Analyze multiple designs and compare their critical paths:

```python
designs = ['design1.txt', 'design2.txt', 'design3.txt']
results = {}

for design in designs:
    analyzer = CircuitAnalyzer(design)
    path, delay = analyzer.find_critical_path()
    results[design] = delay

# Find the fastest design
fastest = min(results, key=results.get)
print(f"Fastest design: {fastest} with delay {results[fastest]}")
```

### Optimization Hints

If your critical path has many operations, consider:
1. **Pipeline insertion**: Add registers to break long paths
2. **Parallel structures**: Distribute operations across multiple paths
3. **Gate optimization**: Replace slow gates with faster alternatives

## Troubleshooting

### File Not Found Error

```
Exception: File my_circuit.txt not found.
```

**Solution**: Make sure the file path is correct. Use absolute paths or paths relative to your working directory.

### Empty Circuit Graph

```
Exception: Circuit graph is empty
```

**Solution**: Check your circuit file format. Ensure it has at least one gate and proper syntax.

### Visualization Not Generated

**Solution**: Ensure the `output/` directory exists or the script has permissions to create it.

## Next Steps

- Explore the example circuits in `examples/` directory
- Read the full documentation in [README.md](../README.md)
- Check out [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute
- Modify gate delays in `circuit_analyzer.py` for custom timing models

## Getting Help

- Open an issue on [GitHub Issues](https://github.com/muzammil5539/digital-circuit-analysis/issues)
- Check existing issues for similar problems
- Provide your circuit file and error messages when reporting bugs

---

Happy analyzing! 🚀
