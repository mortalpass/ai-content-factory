from utils.llm import call_llm

def generate_topics(niche="AI创业", n=10):
    prompt = f"""
你是爆款选题专家，请为{niche}生成{n}个适合小红书/抖音的爆款选题
"""
    result = call_llm(prompt)
    return result.split("\n")
