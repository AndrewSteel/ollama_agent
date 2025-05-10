"""Constants for the Ollama Agent integration."""

DOMAIN = "ollama_agent"

CONF_MODEL = "model"
CONF_PROMPT = "prompt"

CONF_KEEP_ALIVE = "keep_alive"
DEFAULT_KEEP_ALIVE = -1  # seconds. -1 = indefinite, 0 = never

KEEP_ALIVE_FOREVER = -1
DEFAULT_TIMEOUT = 5.0  # seconds

CONF_NUM_CTX = "num_ctx"
DEFAULT_NUM_CTX = 8192
MIN_NUM_CTX = 2048
MAX_NUM_CTX = 131072

CONF_MAX_HISTORY = "max_history"
DEFAULT_MAX_HISTORY = 20

MAX_HISTORY_SECONDS = 60 * 60  # 1 hour

MODEL_NAMES = [  # https://ollama.com/library (tools models only)
	"athene-v2",
	"aya-expanse",
	"cogito",
	"command-a",
	"command-r",
	"command-r-plus",
	"command-r7b",
	"command-r7b-arabic",
	"firefunction-v2",
	"granite3-dense",
	"granite3-moe",
	"granite3.1-dense",
	"granite3.1-moe",
	"granite3.2",
	"granite3.2-vision",
	"granite3.3",
	"hermes3",
	"llama3.1",
	"llama3.2",
	"llama3.3",
	"llama3-groq-tool-use",
	"llama4",
	"mistral",
	"mistral-large",
	"mistral-nemo",
	"mistral-small",
	"mistral-small3.1",
	"mixtral",
	"nemotron-mini",
	"nemotron",
	"phi4-mini",
	"qwen2",
	"qwen2.5",
	"qwen2.5-coder",
	"qwen3",
	"qwq",
	"smollm2",
]
DEFAULT_MODEL = "llama3.2:latest"
