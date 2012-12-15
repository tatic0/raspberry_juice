#!/usr/bin/env python
# main.py

from bottle import route, run, error, request, static_file
import bottle

# bottle imports
import html_end, html_begin
header = html_begin.main()
foot = html_end.main()

# cpu plot imports
import plot

# simple log facility
try:
    import logpyle
except OSError:
    user="default"
    import logpyle

# python imports
import sys, os, fnmatch

bottle.debug(True)

# main landing site
@route('/')
@route('/index.html')
@route('/index.php')
@route('/home')
def index():
    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " requested index.{php,html}")
    a = header + "<div class='container'><p>Welcome to raspberry pi monitor!</p></div>" + foot
    return a

# some nice functions
@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    logpyle.logger(ip, " resquested its IP") 
    a = "<div class='container'> Your IP is: %s </div>" % ip
    a = header + a + foot
    return a

@route('/disk_usage')
def disk_usage():
    import df
    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " requested disk usage info") 
    a = df.fsinfo() 
    b = header + "<div class='container'>" + a.replace('\n','</br>').replace('\t','&emsp;')+ "</div>" + foot
    return b

#datafiles = []
#plotlinks = []
@route('/cpu_usage')
def cpu_usage():
    datafiles = []
    plotlinks = []

    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " requested cpu_usage") 
    cpu = open('/proc/loadavg','r')
    data = cpu.read()
    cpu.close()
    logpyle.logger(ip, " requested cpu usage info") 
    a = str(data[0:4]) 
    if float(a) > 1:
      a = 1
    width = 300 # 100%
    cpuu = (float(a) * 100) * 3 # 100% = 300 p
    r1w=(cpuu/2)
    r1w_round = round(r1w)
    r2w = 300 - r1w 
    print(r1w, r1w_round, r2w, cpuu)
  
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <rect id="rect1" x="0" y="0" width="%d" height="20" style="fill:rgb(254,0,0);stroke-width:1;stroke:rgb(0,0,0)" />
    <rect id="rect2" x="%d" y="0" width="%d" height="20" style="fill:rgb(0,255,0);stroke-width:1;stroke:rgb(0,0,0)" />
    </svg>
    </br></br> """ %(r1w,r1w_round,r2w)
    for i in os.listdir('/home/pi/raspberry_juice/'):
      if fnmatch.fnmatch(i, "*.data"):
        datafiles.append(i)    
    for each in datafiles:
      plotlink = "<a href=\"%s\"> %s </a>" %(each,each)
      print(plotlink)
      plotlinks.append(plotlink)
    
    b = header + "<div class='container'>" + a.replace('\n','</br>').replace('\t','&emsp;')+ "</br>"+ str(plotlinks) + svg + "</div>" + foot
    return b

@route('/<name>.data')
def makegraph(name):
    plot.plot(name)
    a = "<div class=\"container\"><a href=%s.jpg>%s.jpg</a></div>" %(name,name)
    a = header + a + foot
    return a
@route('/<name>.jpg', methog='GET')
def plottedgraph(name):
    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " cpu usage plotfile requested") 
    sfile = "%s.jpg"%name
    return static_file(sfile, root='/home/pi/raspberry_juice/')
    #a = "<div class=\"container\"><img src=\"/%s.jpg\"></div>" %name
    #a = header + a + foot
    #return a 
@route('/css/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pi/raspberry_juice/css') 
@route('/img/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pi/raspberry_juice/img') 
@route('/js/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pi/raspberry_juice/js') 
@route('/favicon.ico', method='GET')
def favicon():
    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " requested favicon") 
    return static_file('favicon.ico', root='/home/pi/raspberry_juice/')
@route('/plot.jpeg', method='GET')
def testplot():
    ip = request.environ.get('REMOTE_ADDR')
    logpyle.logger(ip, " requested plot.jpeg") 
    return static_file('plot.jpeg', root='/home/pi/raspberry_juice/')



# some errors
@error(404)
def error404(error):
    ip = request.environ.get('REMOTE_ADDR')
    url = request.url
    #maybe logged due to favico GET
    logpyle.logger(ip,url,"error 404") 
    a = header + 'Shop is closed, sorry' + foot
    return a

run(host='0.0.0.0', port=8080, reloader=True)
