/*
IMPORTANT NOTE about TembooAccount.h

TembooAccount.h contains your Temboo account information and must be included
alongside your sketch. To do so, make a new tab in Energia, call it TembooAccount.h,
and copy this content into it. 
*/

#define TEMBOO_ACCOUNT "geevegeorge"  // Your Temboo account name 
#define TEMBOO_APP_KEY_NAME "myFirstApp"  // Your Temboo app name
#define TEMBOO_APP_KEY "TrmzEaglWvzazKMdb4rgrCwr5Ga64OhT"  // Your Temboo app key

#define WIFI_SSID "bsnl"
#define WPA_PASSWORD "gaussthebaws"

/* 
The same TembooAccount.h file settings can be used for all Temboo sketches.

Keeping your account information in a separate file means you can share the 
main .ino file without worrying that you forgot to delete your credentials.
*/
