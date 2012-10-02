#!/usr/bin/python
 
import lldb
import time
import markup
import os

namesDictionary = {}

page = markup.page()
page.init( title="View Hierarchy", css=( 'style.css',),script={'jquery.js':'javascript','main.js':'javascript'}, header="--///--", footer="--///--" )

def generateHTML():
    filename = os.path.dirname(os.path.abspath(__file__))+"/Output.html"
    outputfile = open(filename, "w+")
    outputfile.write(str(page))
    outputfile.close()
    print "generated "+filename


def buildViewHierarchy(viewNode,depth):
    viewNodeSubviewsCount = lldb.frame.EvaluateExpression('(int)[[%s subviews] count]' % (viewNode) ).GetValueAsUnsigned(0)
    for k in range(0,viewNodeSubviewsCount):
        view = lldb.frame.EvaluateExpression("(UIView*)[[%s subviews] objectAtIndex:%i]" % (viewNode,k)).GetValue()
        viewSubviewsCount =  lldb.frame.EvaluateExpression('(int)[[%s subviews] count]' % (view)).GetValueAsUnsigned(0)
        viewType = lldb.frame.EvaluateExpression("(id)[%s class]" % (view)).GetObjectDescription()
        default = 'NoName'
        viewName = namesDictionary.get(view,default)
        itm = viewName+" || "+str(viewType)
        page.li(itm,class_="viewitem")
        if viewSubviewsCount > 0:
            page.ul()
            buildViewHierarchy(view,depth+1)
            page.ul.close()

 
def collectKnownViewNames(mainNode,subNodesCount,nm):
    for x in range(0,subNodesCount):
        node = mainNode.GetChildAtIndex(x)
        
        if nm is "-":
            type_test = '(BOOL)[self->%s isKindOfClass:(id)[UIView class]]' % (node.GetName())
        else:
            type_test = '(BOOL)[%s->%s isKindOfClass:(id)[UIView class]]' % (mainNode.GetName(),node.GetName())

        test = lldb.frame.EvaluateExpression(type_test).GetValueAsUnsigned(0)
        if test is 1:
            namesDictionary[node.GetValue()] = node.GetName()
            #print nm+node.GetName()+" || "+ str(node.GetValue())
            collectKnownViewNames(node,node.GetNumChildren(),nm+"-")
 
def printviews(debugger, command_line, result, dict):
    fn = lldb.frame.GetFunctionName()
    print "preparing hierarchy in "+fn
    viewCount = lldb.frame.EvaluateExpression('(int)[[self.view subviews] count]').GetValue()
    viewNode = lldb.frame.EvaluateExpression("self.view").GetValue()
    viewNodeType = lldb.frame.EvaluateExpression("(id)[self class]").GetObjectDescription()
    page.h2(str(viewNodeType)+" view hierarchy")

    mainNode = lldb.frame.GetValueForVariablePath("*self")
    subNodesCount = lldb.frame.GetValueForVariablePath("*self").GetNumChildren();
    collectKnownViewNames(mainNode,subNodesCount,"-")
    #time.sleep(6)
    page.ul()
    buildViewHierarchy(viewNode,0)
    page.ul.close()
    #time.sleep(3)
    generateHTML()

