@echo off
title GitHub Auto Backup System
echo ==================================================
echo         🚀 GitHub Auto Backup System
echo ==================================================
echo.

:: Git 사용자 정보 자동 세팅 (최초 실행 에러 방지)
git config --global user.email "kimhyejin0122@example.com"
git config --global user.name "kimhyejin0122-hash"

git init
git branch -M main
git remote add origin https://github.com/kimhyejin0122-hash/Inventory_control.git
git remote set-url origin https://github.com/kimhyejin0122-hash/Inventory_control.git

git add .
git commit -m "Auto Backup %date% %time%"
git push -u origin main

echo.
echo ==================================================
echo       Backup process finished. 
echo       Please check the message above for success/fail.
echo ==================================================
echo.
pause
