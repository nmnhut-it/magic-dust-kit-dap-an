@echo off
setlocal EnableDelayedExpansion
title Magic Dust - chep dap an
cd /d "%~dp0"

echo(
echo   ==========================================
echo     CHEP DAP AN VAO BO DO NGHE
echo   ==========================================
echo(

rem Bo do nghe nam o dau? Thu: keo tha vao file nay -> %1. Khong co thi do
rem mot vai cho quen thuoc quanh day.
set "KIT="
if not "%~1"=="" if exist "%~1\student\spells.py" set "KIT=%~1"
if not defined KIT if exist "..\magic-dust-kit\student\spells.py" set "KIT=..\magic-dust-kit"
if not defined KIT if exist "..\student\spells.py" set "KIT=.."
if not defined KIT if exist "%USERPROFILE%\Downloads\magic-dust-kit\student\spells.py" set "KIT=%USERPROFILE%\Downloads\magic-dust-kit"
if not defined KIT if exist "%USERPROFILE%\Desktop\magic-dust-kit\student\spells.py" set "KIT=%USERPROFILE%\Desktop\magic-dust-kit"

if not defined KIT (
  echo   Khong tim thay bo do nghe.
  echo(
  echo   Cach lam: keo THU MUC magic-dust-kit tha thang vao file
  echo   CHEP-VAO.bat nay, hoac dat hai thu muc canh nhau roi chay lai.
  echo(
  pause
  goto :eof
)

echo   Tim thay bo do nghe o: %KIT%
echo(

rem Giu lai bai cu, phong khi hoc sinh muon xem lai minh da viet gi.
if not exist "%KIT%\student\bai-cua-toi" mkdir "%KIT%\student\bai-cua-toi"
copy /y "%KIT%\student\spells.py" "%KIT%\student\bai-cua-toi\" >nul 2>&1
copy /y "%KIT%\student\image_spells.py" "%KIT%\student\bai-cua-toi\" >nul 2>&1

copy /y "student\spells.py" "%KIT%\student\spells.py" >nul
copy /y "student\image_spells.py" "%KIT%\student\image_spells.py" >nul

echo   Xong. Da chep 2 file dap an vao %KIT%\student\
echo   Bai cu cua ban duoc cat o  %KIT%\student\bai-cua-toi\
echo(
echo   Gio bam dup CHAY.bat trong bo do nghe, doi dong "Python san sang",
echo   roi bam phim T - phai thay ba dong dau tick (flip, blur, blend).
echo(
pause
