# Tips

## 1. 快速搭建web服务器

```python
# python2
# python -m SimpleHTTPServer 8888
# python3
python3 -m http.server 8888
```

## 2. pydoc快速构建API文档

```python
python -m pydoc demo
# -w write 写入html文件
python -m pydoc -w demo
# 运行server查看python所有API
python -m pydoc -p 5200

```

## 3. 快速进入 pdb 调试模式

```python
python -m pdb demo.py
```

## 4. 快速美化 JSON 字符串

```python
echo '{"name": "MING"}' | python -m json.tool
```

## 5. 快速打印包的搜索路径

```python
python -m site
```

## 6. 用于快速计算程序执行时长

```python
python3 -m timeit '"-".join(map(str, range(100)))'
```
