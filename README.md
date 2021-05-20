# Todo REST api

Django REST Freamework를 사용한 todo api<br><br>

## API 리스트

#### 할일

|Method|URL|Function|
|---|---|---|
|(GET)|todos/|할일 리스트 보기|
|(POST)|todos/|할일 생성하기|
|(GET)|todos/<int:todo_id>|할일 디테일 보기|
|(PATCH)|todos/<int:todo_id>|할일 수정하기|
|(PATCH)|todos/<int:todo_id>|할일 수정하기|
|(DELETE)|todos/<int:todo_id>|할일 삭제하기|

#### 댓글

|Method|URL|Function|
|---|---|---|
|(GET)|todos/<int:todo_id>/comments/|댓글 리스트 보기|
|(POST)|todos/<int:todo_id>/comments/|댓글 생성하기|
|(PATCH)|todos/<int:todo_id>/comments/<int:comment_id>|댓글 수정하기|
|(DELETE)|todos/<int:todo_id>/comments/<int:comment_id>|댓글 삭제하기|
