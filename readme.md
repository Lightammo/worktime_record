# ReadMe
打卡工具
自用时间模块，记录上下班时间，简单实现

## 1. 外部组件
fastapi

## 2. 功能
记录当前时间戳，轻量级json文件格式保存
### 接口
1. create_user 创建用户
2. record_worktime 记录时间
3. count_worktime 计算工时

## 3. 使用
### 启动 
```
# terminal
uvicorn main:app --reload
```

### 查看接口文档
```
# browser server 
localhost/docs
```

## 4. Next
后续添加环境变量用于控制启动服务端口
添加新的接口