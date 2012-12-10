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
#import cpu_load
# module is threaded :)
#cpu_load.main()

# simple log facility
try:
    import logpyle
except OSError:
    user="default"
    import logpyle

# python imports
import sys

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

@route('/cpu_usage')
def cpu_usage():
    ip = request.environ.get('REMOTE_ADDR')
    cpu = open('/proc/loadavg','r')
    data = cpu.read()
    cpu.close()
    logpyle.logger(ip, " requested cpu usage info") 
    a = str(data[0:4]) 
    plot.demo()
    plotlink = "<a href=\"plot.jpeg\"> plot </a></br>"
    b = header + "<div class='container'>" + a.replace('\n','</br>').replace('\t','&emsp;')+ "</div>"+ plotlink  + foot
    return b

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
    return static_file('favicon.ico', root='/home/pi/raspberry_juice/')
@route('/plot.jpeg', method='GET')
def favicon():
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
