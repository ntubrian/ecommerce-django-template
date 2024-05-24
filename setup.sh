#!/bin/bash

# 加載環境變量
source .env

# 停止并删除现有容器
docker-compose down

# 删除数据库卷
docker volume rm docker-files_postgres_data

# 啟動 Docker Compose
docker-compose -f docker-files/docker-compose.yml up --build -d

# 等待服務啟動
echo "等待服務啟動..."
sleep 10

# 進入 Django 容器
echo "進入 Django 容器並執行遷移..."
docker-compose -f docker-files/docker-compose.yml exec backend bash -c "
  poetry run python manage.py makemigrations &&
  poetry run python manage.py migrate
"

# echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')\" | poetry run python manage.py shell

# 運行 seed.py 腳本插入初始數據
echo "運行 seed.py 腳本插入初始數據..."
docker-compose -f docker-files/docker-compose.yml exec backend bash -c "
  poetry run python seed.py
"

echo "設置完成！您現在可以訪問 http://localhost:8000/admin/ 來登錄 Django Admin。"
