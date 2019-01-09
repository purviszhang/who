# who

## 快速开始

```python
from who import get_region
from who import validity_check

# 根据身份证前面2~6位号码，查询所在省市县地区
result = get_region(320)
print(result)

# 校验一个身份证号码是否是合法号码
id="440304199010104562"
result = validity_check(id)
print(result)
```

