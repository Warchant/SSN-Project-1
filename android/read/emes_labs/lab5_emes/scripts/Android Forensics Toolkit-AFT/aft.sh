clear
cd /
echo ---------------------------------------
echo "--- Android Forensics Toolkit - AFT ---"
echo ---------------------------------------
#
echo ---------------------------------------
echo ----- Data dumper ----
mkdir /sdcard/AFT/
mkdir /sdcard/AFT/datadump/
cd /
cp -r /data/ /sdcard/AFT/datadump/
echo "data dump finished..."
#
#
echo ---------------------------------------
echo "--------- Credential Recovery ---------"
echo ---------------------------------------
#
#
cd /
if [ -f /data/data/com.ebuddy.android/shared_prefs/ebuddy/com.ebuddy.android_preferences.xml ];
then
echo ---------------------------------------
echo "eBuddy Mobile"
echo ---------------------------------------
cd /data/data/com.ebuddy.android/shared_prefs/
grep -n ebuddy com.ebuddy.android_preferences.xml
grep -n password com.ebuddy.android_preferences.xml
else echo "ebuddy not installed..."
fi
#
#
cd /
if [ -f /data/data/com.himsn/shared_prefs/root.xml ];
then
echo ---------------------------------------
echo "HI MSN"
echo ---------------------------------------
cd data/data/com.himsn/shared_prefs/
grep -n a1 root.xml
grep -n l1 root.xml
else
echo Hi Msn not installed...
fi
#
#
cd /
if [ -f /data/data/com.hiaim/shared_prefs/root.xml ];
then
echo ---------------------------------------
echo "HI AIM"
echo ---------------------------------------
cd /
cd /data/data/com.hiaim/shared_prefs/
grep -n a1 root.xml
grep -n l1 root.xml
else
echo Hi Aim not installed...
fi
#
#
cd /
if [ -f /data/data/com.hiyahoo/shared_prefs/root.xml ];
then
echo ---------------------------------------
echo "HI Yahoo"
echo ---------------------------------------
cd /
cd /data/data/com.hiyahoo/shared_prefs/
grep -n a1 root.xml
grep -n l1 root.xml
else
echo Hi Yahoo not installed...
fi
#
#
echo ---------------------------------------
echo ---------- Browser Credentials --------
echo ---------------------------------------
cd /
if [ -f /data/data/com.mgeek.android.DolphinBrowser/databases/webview.db ];
then
echo "---- Dolphin Browser Credentials ----"
cd /
cd /data/data/com.mgeek.android.DolphinBrowser/databases/
sqlite3 webview.db 'select * from password'
echo ---------------------------------------
else echo "Dolphin Browser not installed..." 
fi
echo ---------------------------------------
echo finito.. Visit jakej.co.uk for updates!
echo ---------------------------------------
