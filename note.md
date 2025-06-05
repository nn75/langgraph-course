🔄 LangGraph 是如何管理状态的？
LangGraph 使用了一种叫做 Runnable 的链式架构，结合 Python 的不可变状态更新策略来保证线程安全和可预测性。

它的核心机制是：

- 每次节点执行都会收到当前状态的一个副本（不是引用）
- 节点返回的是要更新的部分（如 {"messages": [...]}）
- LangGraph 使用 updater 函数（如 add_messages）合并新旧状态
- 更新后的状态被保存在内存中，供下一个节点使用



🛠️ 如果我想把状态持久化怎么办？
如果你想让状态跨请求保留，或者支持断点恢复，你需要自己实现或集成以下机制之一：

方法	描述
- 🔁 使用 config: RunnableConfig	LangGraph 支持通过 config 设置唯一标识符（如 session_id），你可以配合自定义存储使用
- 💾 写入数据库（如 Redis、PostgreSQL）	将 state["messages"] 序列化后保存，下次读取时还原
- 📁 文件系统存储	把状态序列化成 JSON 或 pickle 存储在本地文件中
- ⚙️ 自定义 Checkpointer	LangGraph 提供了 BaseCheckpointSaver 接口，允许你自定义状态持久化逻辑
