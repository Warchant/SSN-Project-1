Android Forensics Toolkit - AFT

https://forums.hak5.org/index.php?/topic/14965-android-forensics/

aft.sh is a sample script which one can use from the ADB (Android Debug Bridge) 
shell or other terminal emulator app to perform a logical dump.

You can modify the script and build in more intelligent functions after the logical dumping of /data.
You may need Busybox for this.

You can put the busybox binary under the /data/local folder and install it with 
./busybox --install -s /system/xbin

Check the Install BusyBox on Rooted Android Phone Gadgets DNA.htm document.
