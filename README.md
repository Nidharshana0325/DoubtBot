# QueryBot: Academic Query Answering System

## About

**QueryBot** is an AI-driven query answering system designed to provide accurate, context-aware responses to academic questions. It has been built by fine-tuning DeepSeek, a state-of-the-art language model, to specifically cater to academic topics. Whether you're a student, researcher, or educator, QueryBot helps you quickly find answers to a wide range of academic questions, offering detailed explanations and insights.

![image](https://github.com/user-attachments/assets/d158ce0e-a988-40ed-9f6e-ef7e02b6dafc)

### Key Features:
- **Context-Aware**: Understands and provides responses based on the context of your query.
- **Subject-Specific**: Fine-tuned for academic questions across various domains, including Computer Science, Natural Language Processing, Mathematics, and more.
- **Interactive**: Continuously learns and adapts to improve the accuracy and depth of its responses.

## Topics Covered
QueryBot can answer questions in a variety of academic fields, including but not limited to:

- **Computer Vision**: Image formation, histogram theory, convolution filtering, object detection, and more.
- **Natural Language Processing (NLP)**: Morphology, phonology, DFA construction, syntax, and language parsing.
- **Data Structures & Algorithms**: Sorting, searching, dynamic programming, trees, graphs, etc.
- **Physics & Chemistry**: Numerical problem-solving, equations, and theory.
- **Mathematics**: Calculus, linear algebra, probability, and other branches.
- **Energy Harvesting**: Techniques for wearable devices, including harvesting from temperature gradients and motion.
- **Machine Learning**: Basics of models, training, and optimization.

## Installation

To run QueryBot locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Nidharshana0325/DoubtBot.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the bot:
    ```bash
    python querybot.py
    ```

## Usage

After installation, simply start the bot, input an academic question, and QueryBot will provide a response based on its fine-tuned knowledge base. You can interact with it through a simple terminal interface or integrate it into a web application for broader access.

Example:
```python
querybot.ask("What is the principle of convolution in image processing?")
