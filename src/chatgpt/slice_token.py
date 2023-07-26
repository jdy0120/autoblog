from transformers import GPT2Tokenizer

def truncate_text(text: str, max_tokens=4000):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokens = tokenizer.encode(text)

    # 입력된 텍스트가 max_tokens보다 많을 경우 잘라냄
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]

    # 잘라낸 토큰들을 다시 문자열로 변환
    truncated_text = tokenizer.decode(tokens)

    return truncated_text