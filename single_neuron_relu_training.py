import numpy as np

# 1 neuron, 3 pixels
inputs = np.array([0.0, 1.0, 0.0])  # image of digit "1" (middle pixel bright)
weights = np.random.uniform(-1, 1, 3)  # random weights
bias = 0.9  # high bias to ensure neuron can activate

# output close to 1
target = 1.0

learning_rate = 0.1

for epoch in range(10):
    output = np.dot(inputs, weights) + bias
    activated = max(0, output)  # ReLU

    loss = (activated - target) ** 2  # squared error loss

    # calculate gradient – how to change weights and bias
    grad_output = 2 * (activated - target)
    grad = grad_output if output > 0 else 0  # ReLU gives zero when output < 0

    # Update weights and bias
    weights -= learning_rate * grad * inputs
    bias -= learning_rate * grad

    print(f"Epoch {epoch+1}: Output={activated:.2f}, Loss={loss:.2f}, Weights={weights}, Bias={bias:.2f}")

print("After training: weights and bias adjusted, neuron predicts better!")