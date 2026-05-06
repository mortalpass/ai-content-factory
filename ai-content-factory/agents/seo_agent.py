from utils.llm import call_llm

def optimize_seo(content):
    prompt = f"""
请对以下内容进行SEO优化：

{content}
"""
    return call_llm(prompt)
