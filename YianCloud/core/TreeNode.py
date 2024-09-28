from pydantic import BaseModel, Field
from typing import List, Optional


class TreeNode(BaseModel):
    value: str  # 节点的值
    children: List[Optional["TreeNode"]] = Field(default_factory=list)  # 子节点列表

    class Config:
        # 允许递归引用自身
        arbitrary_types_allowed = True


child3 = TreeNode(value="子节点 3")
child1 = TreeNode(value="子节点 1", children=[child3])
child2 = TreeNode(value="子节点 2")
root = TreeNode(value="根节点", children=[child1, child2])

print(root.model_dump_json(indent=2))
