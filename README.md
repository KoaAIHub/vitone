# Vitone

Vitone là thư viện dùng cho chuẩn hoá câu trong tiếng Việt

## Install
```bash
pip install vitone
```


## Usage
```python
>>> import vitone
>>> vitone.clean_tone('thị trừơng chứng khóan')
'thị trường chứng khoán'
>>> vitone.remove_tone('việc làm')
'viec lam'
```