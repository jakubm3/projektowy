# 🧠 Neural Network Simulations — Simple Python Demos

Welcome!  
This repository contains two easy-to-understand Python simulations that helped me grasp the **basic concepts of Machine Learning (ML)** and how neural networks work under the hood.  
They are perfect for beginners, educational projects, or anyone curious about how neural networks "think"!

---

## 📁 Files Included

### 1️⃣ `single_neuron_relu_training.py`

**What does it show?**

- Simulates training a single neuron (with ReLU activation) on a simple "image" input.
- Demonstrates how the bias helps the neuron "wake up" and start learning.
- Lets you observe how weights and bias change over epochs to minimize loss and make the neuron predict the target value.

**Why is it useful?**
- This experiment helped me understand why some neurons in neural networks can be "dead" (not learning) and how bias initialization affects learning.
- By adjusting parameters, I could see how gradient descent works step by step.

---

### 2️⃣ `hidden_layer_simulation_dynamic_weights.py`

**What does it show?**

- Simulates a hidden layer with two neurons processing small input patterns (like 3-pixel images).
- You can freely change the weights and biases to see how each neuron reacts to different inputs.
- The script prints clear, friendly messages explaining how each neuron "sees" the input and what features it detects.

**Why is it useful?**
- This simulation made it much easier for me to understand how hidden layers extract features and how changing weights influences what a neural network "notices."
- It gave me hands-on intuition for how neural networks build up their understanding of data.

---

## 🚀 How to Run

1. Make sure you have Python 3.x installed.
2. Download or clone this repository.
3. Run the script you want to explore:
   ```bash
   python single_neuron_relu_training.py
   # or
   python hidden_layer_simulation_dynamic_weights.py
   ```

4. Read the console output and try changing weights, biases, or input data.  
   Every run helps you understand how neural networks learn and react!

---

## ✨ Why Are These Simulations Useful?

- **See learning in action:** Get a hands-on feel for training and neuron activation.
- **Understand "dead neurons":** Learn why some neurons don't learn with ReLU and how bias can fix it.
- **Explore hidden layers:** Discover how different neurons specialize in different input features.
- **Build intuition for ML:** These simple experiments helped me build intuition for the math behind machine learning and neural networks.

---

## 👩‍💻 Try It Yourself!

- Tweak the code! Change values, add inputs, or modify the learning rate.
- Use these scripts in your own neural network learning journey or share them with friends.

---

Enjoy learning neural networks the fun and simple way!  
If you have ideas for more simulations, feel free to contribute or open an issue.
