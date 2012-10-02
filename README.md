#About
This script gets all names of views available to LLDB and all subviews of views in "self". It then matches these to get view hiearchy that has user defined UIView names whenever possible. Then the script outputs the hierarchy in html. You click each subview to unfold its subviews, etc. Gray subviews are the ones that don't have children. Top most view in iOS app is always the last in generated list and so on.

#Usage
##viewgen.py
1) setup proper path in generateHTML()

##Xcode
- import the script (EX: command script import ~/Dropbox/python/viewgen.py)
- assign alias (EX: command script add -f viewgen.printviews pv)
- create breakpoint anywhere where self is in scope
- call script from debug panel ( (lldb) pv )
- reload script before you want to use it again within the same debug session otherwise the hierarchy gets duplicated ( (lldb) script reload(viewgen) )

##Web browser
5) reload Output.html