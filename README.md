# AlgoSolver 🤖💻

AlgoSolver is an interactive web application built with Streamlit and Microsoft Autogen that uses a team of AI agents to solve Data Structures and Algorithms (DSA) problems. Users can input a DSA problem, and the AI agents will collaboratively plan, write, execute, and explain the solution in real-time.

## Features

-   **Interactive Web UI:** A simple and clean user interface built with Streamlit.
-   **Multi-Agent System:** Utilizes a `ProblemSolverAgent` and a `CodeExecutorAgent` working together in a group chat.
-   **Secure Code Execution:** All generated code is safely executed inside a sandboxed Docker container.
-   **Real-time Streaming:** Watch the conversation between the AI agents as they solve the problem live.
-   **Solution Saving:** Automatically generates a `solution.py` file with the final correct code.

## Tech Stack

-   **Backend Framework:** Python
-   **AI Agent Framework:** Microsoft Autogen
-   **Web UI Framework:** Streamlit
-   **Large Language Model (LLM):** Google Gemini (via API)
-   **Containerization:** Docker
-   **Environment Management:** `venv`, `python-dotenv`

## How It Works

The application orchestrates a conversation between two specialized AI agents to deliver a complete solution.

1.  **User Input:** The user enters a DSA problem through the Streamlit web interface.
2.  **Problem Solver Agent:** This agent receives the task. Its job is to:
    -   Create a logical plan to solve the problem.
    -   Write the Python code, including function definitions and example calls to demonstrate its functionality.
3.  **Code Executor Agent:** This agent receives the Python code. It:
    -   Executes the code securely inside a Docker container.
    -   Returns the output (or any errors) back to the group chat.
4.  **Verification and Finalization:** The Problem Solver Agent receives the execution result.
    -   It verifies that the code ran correctly and explains the output.
    -   As a final step, it generates a new script to save the verified solution into a `solution.py` file and instructs the Code Executor to run it.
5.  **Streaming to UI:** The entire conversation is streamed to the user's web browser in real-time, showing the step-by-step process.
## Screenshots

Here are a few screenshots showcasing the AlgoSolver application in action.
<img width="1919" height="1031" alt="Screenshot 2025-08-05 010443" src="https://github.com/user-attachments/assets/a76aef69-45ba-46d6-bc6d-29ccd8fdd58c" />
<img width="1919" height="643" alt="Screenshot 2025-08-05 010510" src="https://github.com/user-attachments/assets/6b658fd4-5650-404e-9ac0-d3f9a3abb4e5" />
<img width="1919" height="1022" alt="Screenshot 2025-08-05 010526" src="https://github.com/user-attachments/assets/48e83a5e-eddc-4f42-9010-4e65344784a3" />
<img width="1919" height="928" alt="Screenshot 2025-08-05 010542" src="https://github.com/user-attachments/assets/5d7b34b2-4995-48e2-9000-9248e86a0238" />
<img width="1919" height="1028" alt="Screenshot 2025-08-05 010553" src="https://github.com/user-attachments/assets/97564a6c-30eb-41fa-bfd1-9c575dedc8a5" />




