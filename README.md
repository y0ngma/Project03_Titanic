# Project03_Titanic
My first time to try Kaggle 입문용


## 캐글 명령어
- 다음은 `pip install kaggle` 이후에 사용할 수 있다
```py
kaggle competitions {list, files, download, submit, submissions, leaderboard}
kaggle datasets {list, files, download, create, version, init}
kaggle kernels {list, init, push, pull, output, status}
kaggle config {view, set, unset}

### 예시 ###
# download
kaggle competitions download -c titanic
# submit 하기
kaggle competitions submit -c titanic -f mysubmission.csv -m "Hello world. This is my first kaggle!"
# submission 확인
kaggle competitons submissions titanic
```