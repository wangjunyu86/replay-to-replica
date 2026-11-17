# Replay to Replica

把你有权观察的软件演示、操作录像或真实使用流程，转化成可以独立实现和检查的行为规格。

这个 Codex Skill 的重点不是复制源代码、品牌或受保护素材，而是提取用户真正能观察到的：

- 操作步骤
- 输入与输出
- 状态变化
- 数据保存方式
- 错误与恢复路径
- 权限与角色规则
- 可执行验收场景
- 原产品与新实现之间的行为差异

## 适合解决什么问题

- 看完一个软件演示后整理成产品行为规格
- 分析现有 App 或网站的用户流程
- 为独立实现的软件生成开发交接包
- 把录屏转成可执行验收场景
- 对原流程和新实现进行回放对比
- 生成行为一致性报告，而不是凭“看起来差不多”验收

## 安装

```bash
git clone https://github.com/wangjunyu86/replay-to-replica.git ~/.codex/skills/replay-to-replica
```

重新启动 Codex，或让 Codex 重新扫描本地 Skills。

## 使用示例

```text
Use $replay-to-replica to turn this authorized app demonstration into a behavior specification and implementation handoff.
```

```text
调用 replay-to-replica，观察我演示的工作流程，把它整理成独立实现方案和验收用例。
```

## 三种结果

1. **Behavior pack only**：只生成行为规格和验收场景。
2. **Implementation handoff**：再加入数据契约、状态模型和开发任务。
3. **Verified replica**：独立实现后，重新回放相同任务并生成一致性报告。

初始化工作包：

```bash
python3 scripts/init_replica_pack.py ./replica-pack \
  --product "Observed Product" \
  --replica "New Product"
```

比较结构化事件轨迹：

```bash
python3 scripts/compare_traces.py original.json replica.json \
  --output parity-report.md
```

## 边界

仅用于经过授权的观察与独立实现。不要绕过登录、付费、加密、频率限制或其他技术控制，也不要复制源代码、反编译代码、商标、专有文案、受保护素材、密钥或私人数据。

## License

MIT
