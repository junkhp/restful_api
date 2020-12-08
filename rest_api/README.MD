# RESTfulなAPI

## できなかったこと
- URLの末尾のスラッシュをうまく扱えなかった．
- returnする情報を加工できなかった

### URLの末尾のスラッシュをうまく扱えなかった．
URLの末尾に「/」がないときに301(リダイレクト)が返されて正しい結果が返せなかった．

```python:rest_api/urls.py
router = routers.DefaultRouter(trailing_slash=False)
```
`trailing_slash`を`False`にすると末尾に`/`がないと正しく動作(逆に`/`があると301)