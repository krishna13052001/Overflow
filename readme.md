# 🌟 Flipkart Overflow 🌟

## About the Creator

Hi, I'm **Sathya Krishna**, a backend developer at Aviatrix with experience in Golang, Python, MongoDB, and AWS. I created this project as part of an interview exercise for Flipkart. I have a keen interest in contributing to open-source projects and building innovative solutions in multi-cloud environments.

## Overview

**Flipkart Overflow** is a question-answer platform designed for developers, inspired by platforms like Stack Overflow. This platform enables users to ask tech-related questions and receive insightful answers from the community. The project is a simulation exercise with a focus on code functionality, in-memory data structures, and concurrency handling.

## 🚀 Features

### User Management
- **Signup** for new users with profile details (name, profession, etc.).
- **Login and logout** functionality (only one user can be logged in at a time).

### Subscription Management
- Users can **subscribe/unsubscribe** from topics (e.g., 'Java', 'Python').

### Content Filtering
- Users can **filter their feeds** based on subscribed topics.
- Users can view detailed information about a **single question and its responses**.

### Question and Answer
- Users can **ask questions** associated with one or more topics.
- Users can **answer questions** if they are subscribed to the relevant topic(s).
- Only logged-in users can ask and answer questions, but **any user can view questions**.

### Bonus Features
- Users can **upvote questions/answers** if they are subscribed to the relevant topic(s).
- Responses are sorted based on the **number of votes**.

## 🛠️ Implementation Notes

- Use **in-memory data structures** for data management.
- No UI is required for this application.
- A **driver class** will demonstrate the execution of commands and test cases.
- Prioritize **code compilation, execution, and completion**.
- Ensure the code is **functionally correct** and handles **concurrent requests** appropriately.
- Code should be **modular, readable, and easy to test**.
- Implement **proper error handling**.

## 🎯 Expectations

- **Working and Demonstrable Code**: Ensure that the code is functional and demonstrable.
- **Modular and Readable Code**: Code should be well-structured and maintainable.
- **Concurrency Handling**: Properly manage concurrent requests.
- **Separation of Concerns**: Address different functionalities in separate modules.
- **Extensibility**: Easily accommodate new requirements with minimal changes.
- **Testability**: Code should be easily testable.
- **Error Handling**: Implement proper error handling mechanisms.

## 🧪 Test Cases

The following test cases provide a basic understanding of the feature requirements:

```java
// User Signup
user_signup('Sachin', 'Developer');

// Topic Subscription
subscribe('java', 'hadoop', 'jdk');

// Asking Questions
add_questions("What are new open source jdks?", topic=["java", "jdk"]);
add_questions("Does Hadoop work on JDK 11?", topic=["hadoop", "jdk"]);

// Showing Feeds
show_feed();
show_feed(filter=['java']); // Shows only the first question
show_feed(filter=['jdk']); // Shows both questions
show_feed(answered=true); // Shows no question as no one has answered

// User Logout
logout();
```
## 🤝 Contribution

This project is open for contributions! If you have ideas for improvements or additional features, feel free to submit a pull request or open an issue. Your contributions are highly appreciated and will help enhance the platform.