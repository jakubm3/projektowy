import numpy as np

# simple hidden layer simulation with dynamic weights and clear messages
# changing the weights, biases, or input patterns helps understanding how the network's 'preferences' change

# input patterns (three pixels image)
input_A = np.array([1, 0, 0])  # first pixel is active
input_B = np.array([0, 1, 1])  # second and third pixels are active

# weights determine which pixels each neuron looks at and how strongly it reacts
weights_hidden = np.array([
    [1, 0, 0],   # neuron 1
    [0, 1, 1]    # neuron 2
])
bias_hidden = np.array([0, 0])  # bias set to 0

def relu(x):
    """ReLU activation function: returns x if x > 0, else 0"""
    return np.maximum(0, x)

def hidden_layer_activation(input_vector):
    """Calculates activation for each neuron in the hidden layer"""
    return relu(np.dot(weights_hidden, input_vector) + bias_hidden)

def interpret_activations(input_pattern, activations, pattern_label):
    print(f"\nInput pattern {pattern_label}: {input_pattern}")
    for idx, (weight, act) in enumerate(zip(weights_hidden, activations)):
        # what each neuron does
        features = []
        for i, w in enumerate(weight):
            if w > 0:
                features.append(f"+{w}*pixel{i+1}")
            elif w < 0:
                features.append(f"{w}*pixel{i+1}")
        description = " + ".join(features) if features else "Ignores all pixels"
        print(f"  Neuron {idx+1} looks at: {description}")
        print(f"    Activation: {act}")
        if act > 0:
            print(f"    → Neuron {idx+1} detected its pattern in this input!")
        else:
            print(f"    → Neuron {idx+1} did NOT detect anything interesting in this input.")

# simulation for both inputs
activation_A = hidden_layer_activation(input_A)
activation_B = hidden_layer_activation(input_B)

print("=== HIDDEN LAYER SIMULATION (WITH ANY WEIGHTS YOU CHOOSE) ===")
interpret_activations(input_A, activation_A, "A")
interpret_activations(input_B, activation_B, "B")

# network output: sum of hidden layer activations
output_A = np.sum(activation_A)
output_B = np.sum(activation_B)
print("\n--- Network output (sum of hidden activations) ---")
print(f"Pattern A: sum of activations = {output_A}")
print(f"Pattern B: sum of activations = {output_B}")

if output_A > output_B:
    print(">>> The network reacts more strongly to pattern A with the current weights.")
elif output_B > output_A:
    print(">>> The network reacts more strongly to pattern B with the current weights.")
else:
    print(">>> The network reacts equally to both patterns.")
