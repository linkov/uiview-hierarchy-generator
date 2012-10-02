#About
This script gets all names of views available to LLDB and all subviews of views in "self". It then matches these to get view hiearchy that has user defined UIView names whenever possible. Then the script outputs the hierarchy in html. You click each subview to unfold its subviews, etc. Gray subviews are the ones that don't have children.

#Usage
##viewgen.py
1) setup proper path in generateHTML()

##Xcode
- import the script (command script import ~/Dropbox/python/utils.py)
- assign alias (command script add -f utils.printviews pv)
- create breakpoint anywhere where self is in scope
- call script from debug panel ( (lldb) pv )

##Web browser
5) reload Output.html