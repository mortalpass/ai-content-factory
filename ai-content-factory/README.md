# 🚀 AI Content Factory

一个可扩展的多 Agent 内容生产流水线系统。

## ✨ 特性

- 🧠 多 Agent 协同（选题 / 写作 / SEO / 审核）
- ⚙️ 自动化流水线
- 📈 支持规模化生产（300+ / 天）
- 🔁 可持续运行
- 🧩 模块化设计，易扩展

## 🏗 架构

Topic Agent → Writer Agent → SEO Agent → Review Agent

## 📦 安装

```bash
pip install -r requirements.txt
```

## 🔑 配置

设置环境变量：

```bash
export OPENAI_API_KEY=your_key
```

## ▶️ 运行

```bash
python main.py
```

## 📊 输出

生成内容会保存在：

```
/outputs/*.json
```

## 🚀 进阶方向

- 并发执行（ThreadPool / Async）
- 接入 Redis / Celery
- Web 控制台
- 爆款内容学习系统

---

> Build for scale. Run forever. Automate everything.
