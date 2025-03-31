Intelligent LLM Agent for Automated Human Activity Simulation with CUE System

Project Overview

This project aims to develop an intelligent Large Language Model (LLM) agent that automates the simulation of complex human activities within the Cluster User Emulator (CUE) system. The agent leverages prompt engineering to dynamically generate and execute program code, utilizing both static and dynamic function calls through the CUE API. The goal is to improve efficiency, adaptability, and scalability for tasks such as debugging, system administration, and behavioral simulations.

Features

Human Activity Simulation: Automates emulation of human activities (e.g., debugging, file management, system interactions) with context-aware workflows.

Dynamic Code Generation: Automatically generates and executes program code based on task requirements and CUE API calls.

Seamless CUE Integration: Uses both static and dynamic API functions to configure and execute tasks.

Prompt Engineering: Employs structured prompt sets to guide the LLM in task-specific code and action generation.

Feedback and Optimization: Iterative feedback loops improve task accuracy and adaptability.

Technologies Used

Python for core development.

LangChain for LLM integration and prompt engineering.

CUE System API for task automation.

GitHub Actions for CI/CD integration.

Installation

Clone the repository:

git clone https://github.com/yourusername/intelligent-llm-agent.git
cd intelligent-llm-agent

Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Usage

To start the LLM agent, run the following command:

python main.py

Example Usage

To simulate a C program debugging task:

Place the C code in the input/ folder.

Run the script with the following command:

python main.py --task debug --input input/sample.c

Check the logs/ folder for the output and error logs.

Project Structure

intelligent-llm-agent/
├── input/          # Input files and data
├── logs/           # Execution logs and feedback data
├── src/            # Source code for the LLM agent
│   ├── SeverAPP.py  # Main server application script
│   ├── Cue_system.py # CUE system integration and task handling
│   ├── serverapp.css # CSS for the server application HTML
│   └── serverapp.html # Frontend HTML for the server application
├── prompts/        # Structured prompt templates
├── tests/          # Unit and integration tests
├── docs/           # Project documentation and support files
│   ├── Actiondetail.txt # Details of actions supported
│   └── Environment.txt # System environment configurations
├── README.md       # Project documentation
└── requirements.txt # Python dependencies

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

License

This project is licensed under the MIT License. See LICENSE for more information.

Acknowledgements

Special thanks to the open-source contributors of the CUE system and LangChain.

Inspired by innovative prompt engineering techniques.

Contact

For any questions or suggestions, feel free to reach out at
iankwacg00@gmail.com
