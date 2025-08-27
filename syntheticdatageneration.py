from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from colorama import Fore 

import json
from typing import List 
from pydantic import BaseModel
from litellm import completion
from generated_prompt import prompt_template