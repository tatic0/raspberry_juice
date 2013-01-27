#!/bin/python
# html_begin.py

def main():
    a= """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Raspberry pi monitor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>

    </head>
  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="home">Raspberry juice</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="home">Home</a></li>
              <li><a href="my_ip">my ip</a></li>
              <li><a href="disk_usage">disk usage</a></li>
              <li><a href="cpu_usage">cpu usage</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div id="title" class="container">

      <h1>Raspberry monitor</h1>
      <p> raspberry monitoring site </p>

    </div> <!-- /container -->

    """
    return a
