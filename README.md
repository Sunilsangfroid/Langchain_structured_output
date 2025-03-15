# LangChain Structured Output

This repository demonstrates different approaches to obtain structured output from language models using LangChain. It includes examples with TypedDict, Pydantic models, and JSON Schema for both OpenAI and Google Gemini models.

## Overview

Structured output allows you to get predictable, schema-compliant responses from language models rather than free-form text. This makes it easier to integrate LLMs with databases, APIs, and other systems requiring structured data.

## Installation

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Examples

### 1. TypedDict with OpenAI (Recommended)

Use `with_structured_typeddict.py` to extract structured data using TypedDict with OpenAI models:

```bash
python with_structured_typeddict.py
```

Key features:
- Uses Annotated TypedDict for field descriptions
- Compatible with OpenAI models
- Supports Literal types to restrict field values
- Can extract complex structures from reviews

### 2. Pydantic Models with Google Gemini

Use `with_structured_output_pydantic.py` to get structured output from Google Gemini models:

```bash
python with_structured_output_pydantic.py
```

Key features:
- Uses Pydantic BaseModel with Field descriptions
- Works with Google Gemini models
- Provides runtime validation
- Supports optional fields and default values

### 3. JSON Schema with Google Gemini

Use `with_structured_output_json.py` to work with JSON schema definitions:

```bash
python with_structured_output_json.py
```

Key features:
- Uses raw JSON schema format
- Language-agnostic schema definition
- Works with Google Gemini models
- Supports advanced schema validation

## Model Compatibility

| Schema Type | OpenAI | Google Gemini | Notes |
|-------------|--------|---------------|-------|
| TypedDict   | ✅     | ❌            | TypedDict doesn't work with Google models due to inspection limitations |
| Pydantic    | ✅     | ✅            | Works with both model types, recommended for cross-compatibility |
| JSON Schema | ✅     | ✅            | Most flexible but more verbose approach |

## Common Issues and Solutions

### TypedDict not working with Google Gemini

Error: `ValueError: no signature found for builtin type <class 'dict'>`

Solution: Use Pydantic models instead with Google Gemini models:

```python
from pydantic import BaseModel, Field

class Review(BaseModel):
    summary: str = Field(description="A brief summary")
    sentiment: Literal["positive", "negative", "neutral"]
```

### Missing Dependencies

If you encounter errors related to missing packages, install the specific package:

```bash
pip install pydantic email-validator
```

## Additional Resources

- `notes.md`: Comprehensive notes on structured output approaches
- `typeddict_demo.py`: Basic usage of TypedDict
- `pydantic_demo.py`: Basic usage of Pydantic models
- `test.py`: Simple test of structured output with Gemini models

## License

This project is open source and available under the MIT License.