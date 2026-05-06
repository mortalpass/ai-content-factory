from utils.llm import call_llm

def review_content(content):
    prompt = f"""
请审核以下内容：

{content}
"""
    return call_llm(prompt)
