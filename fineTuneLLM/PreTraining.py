#  Pre-Training (Unsupervised Learning or Self-Supervised Learning): Pre-training is the initial phase of training a language model on a large corpus of text data in an unsupervised manner. The model learns to predict the next word or token in a sequence, capturing the statistical patterns and relationships present in the training data. This phase helps the model acquire general language understanding and knowledge, which can be leveraged for downstream tasks.

#  Source of data for Pre-Training:
    # Documentation
    # Research Papers
    # Common Crawl Dataset
    # Wikipedia
    # BooksCorpus

# Objective of Pre-Training: Next-Token Prediction: The primary objective of pre-training is to predict the next word or token in a given sequence of text. The model learns to capture the contextual information and dependencies between words, enabling it to generate coherent and contextually relevant text.

# Result: Base model is obtained from Llamma, Deep seek, Mistral Gemini.... etc
# After this stage model develops Knowledge and grammar understanding, but it is not yet specialized for specific tasks. The model can be used as a foundation for further fine-tuning and adaptation to various downstream applications. 

# Normal Fine Tuning (Domain Adaptation): After pre-training, the model can be fine-tuned on a smaller, task-specific dataset to adapt it to a particular domain or application. This process involves updating the model's parameters based on the labeled data, allowing it to learn task-specific patterns and improve its performance on the target task.
# dataset: plain text
# Usecases: Domain-specific language understanding, Sentiment analysis, Named entity recognition, Text classification, Question answering, Machine translation, Summarization, Chatbots and conversational agents, Information retrieval, Content generation.
# Goal: The goal of normal fine-tuning is to adapt the pretrained model to a specific domain or task, improving its performance and accuracy on the target application. By leveraging the knowledge acquired during pre-training, the model can effectively learn task-specific patterns and make more informed predictions or generate relevant outputs.
# output style:Produces text continuations that are coherent and contextually relevant to the input prompt- Not necessarily aligned with human preferences or values.
# Meaning: The model is trained to generate text that is contextually appropriate and coherent, but it may not always align with human preferences or values. It focuses on producing text that is grammatically correct and contextually relevant, rather than explicitly considering ethical or moral considerations.

# Instruction Fine Tuning (Alignment with Human Preferences): Instruction fine-tuning is a specialized form of fine-tuning that focuses on aligning the model's behavior with human preferences and values. 

# Dataset: Follows instrction + response format
# Usecases: Chatbots and conversational agents, Virtual assistants, Customer support systems, Content moderation, Personalized recommendations, Ethical AI applications, Human-AI collaboration, Interactive storytelling, Educational applications, Healthcare and medical applications.
# Goal: The goal of instruction fine-tuning is to improve the model's ability to understand and follow instructions provided by users. By training the model on datasets that contain explicit instructions and corresponding responses, it learns to generate outputs that align with human expectations and preferences. This helps enhance the user experience and ensures that the model behaves in a manner consistent with ethical guidelines and societal norms.
# output style: Produces text continuations that are aligned with human preferences and values, following the instructions provided in the input prompt.

# Combo Strategy: In practice, a combination of normal fine-tuning and instruction fine-tuning can be employed to achieve both domain adaptation and alignment with human preferences. This approach allows the model to leverage the benefits of both techniques, resulting in improved performance on specific tasks while also ensuring that the generated outputs align with human expectations and values. By carefully curating the training datasets and incorporating feedback from human evaluators, the model can be fine-tuned to strike a balance between domain-specific knowledge and ethical considerations, leading to more reliable and user-friendly language models.