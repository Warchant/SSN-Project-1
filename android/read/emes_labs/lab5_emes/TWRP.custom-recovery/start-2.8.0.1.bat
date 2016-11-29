REM http://stackoverflow.com/questions/5034076/what-does-dp0-mean-and-how-does-it-work
cd /d %~dp0
C:\android-sdk-windows\tools\emulator -avd TWRP -ramdisk twrp-2.8.0.1-twrp.img -kernel goldfish_2.6_kernel
pause