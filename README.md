\# Local LLM Lab



My hands-on journey into local LLM engineering through practical experiments, measurements, and progressively more advanced AI applications.



\## Experiment 01: Local LLM Text Rewriter



A Python application that connects to a locally hosted Humanizer-12B language model through the llama.cpp HTTP API.



The application accepts text, sends a prompt to the local model, and displays the generated response.



\### Architecture



GGUF Model → llama.cpp → HTTP API → Python Application → Generated Response



\### Technologies



\- Python

\- llama.cpp

\- GGUF

\- Q4\_K\_M quantization

\- HTTP API

\- JSON



\### Model and Hardware



| Component | Configuration |

|---|---|

| Model | Humanizer-12B |

| Model format | GGUF |

| Quantization | Q4\_K\_M |

| GPU | NVIDIA RTX 3050, 6 GB VRAM |

| System RAM | 24 GB |

| Inference server | llama.cpp |

| Application | Python |



\### How It Works



1\. The llama.cpp server loads the quantized GGUF model.

2\. The server exposes a local HTTP endpoint.

3\. The Python application sends a prompt to the endpoint.

4\. The server generates a response using the model.

5\. Python receives and displays the generated text.



\### Run Locally



\*\*Prerequisites\*\*



\- Python

\- llama.cpp with `llama-server`

\- A compatible GGUF model file



\*\*1. Obtain the model\*\*



Obtain the model from its original publisher and review its license. Place the GGUF file in the project directory.



The model weights are not included in this repository.



\*\*2. Start the inference server\*\*



```powershell

llama-server -m ".\\humanizer-12b-Q4\_K\_M.gguf" -c 2048 -np 1 -ngl 20 --host 127.0.0.1 --port 8080

